"""
无边框 Electron 窗口「到底能不能拖」的判据工具。

背景
────
`-webkit-app-region` 的最终判定发生在 **系统命中测试**（WM_NCHITTEST），
不在渲染进程里。所以：

    · CDP 的 Input.dispatchMouseEvent / elementFromPoint —— 直接进渲染进程，
      **绕过系统命中判定**，永远测不出「这一像素被当成标题栏」；
    · 只有向窗口发 WM_NCHITTEST 看返回码才是真判据：
          HTCAPTION(2)  → 系统认为是标题栏，按下即拖窗口
          HTCLIENT(1)   → 普通客户区，事件进渲染进程（按钮能点）
          HTNOWHERE(0)  → 该点不属于本窗口

这正是「按钮看着能点、实际点不动」这类问题的唯一验证手段。

用法
────
    python scripts/nchittest-probe.py                      # 默认一组探针点
    python scripts/nchittest-probe.py 600,8 600,20 60,20   # 指定客户端坐标
    python scripts/nchittest-probe.py --scan 600           # 扫 x=600 这一列，
                                                           # 找拖拽带的连续区间
    python scripts/nchittest-probe.py --restore            # 还原最小化的窗口再跑
    python scripts/nchittest-probe.py --list               # 只列可见顶层窗口

坐标是**客户端 CSS 像素**。dpr=1 的机器上与物理像素 1:1；若系统有缩放
（如 125%），传入的先乘 dpr 才是物理像素 —— 见文件末尾 DPI 说明。

两个踩过的坑
────────────
1. **别用「窗口尺寸 > N」筛候选窗口**。最小化的窗口 `GetWindowRect` 返回
   (-32000, -32000, -32000+160, -32000+28)，算出来只有 160x28，会被筛掉，
   然后程序 quietly 挑到别的进程的窗口（本机就挑中过 explorer.exe 的桌面），
   拿别人的窗口测半天。现在改用 `IsIconic` 判定并**优先**非最小化的窗口。
2. 最小化状态下 Chromium 仍会响应 WM_NCHITTEST（IsWindowVisible 对最小化窗口
   为真），结果一般仍有效 —— 但 `GetWindowRect` 不可信，客户端原点也对不上，
   所以**验收要在正常窗口上做**。窗口是最小化时会打警告。
"""
import ctypes
import sys
import time
from ctypes import wintypes

user32 = ctypes.WinDLL('user32', use_last_error=True)
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

WM_NCHITTEST = 0x0084
PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
SW_RESTORE = 9

HT = {
    0: 'HTNOWHERE',
    1: 'HTCLIENT',
    2: 'HTCAPTION',
    3: 'HTSYSMENU',
    4: 'HTGROWBOX',
    8: 'HTMINBUTTON',
    9: 'HTMAXBUTTON',
    10: 'HTLEFT',
    11: 'HTRIGHT',
    12: 'HTTOP',
    13: 'HTTOPLEFT',
    14: 'HTTOPRIGHT',
    15: 'HTBOTTOM',
    16: 'HTBOTTOMLEFT',
    17: 'HTBOTTOMRIGHT',
    20: 'HTCLOSE',
}

DEFAULT_POINTS = ['8,8', '60,8', '300,8', '600,20', '1000,20', '600,34', '600,46']


class RECT(ctypes.Structure):
    _fields_ = [('left', ctypes.c_long), ('top', ctypes.c_long),
                ('right', ctypes.c_long), ('bottom', ctypes.c_long)]


class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_long), ('y', ctypes.c_long)]


def _exe_name(pid):
    handle = kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
    if not handle:
        return ''
    try:
        buf = ctypes.create_unicode_buffer(1024)
        size = wintypes.DWORD(1024)
        if kernel32.QueryFullProcessImageNameW(handle, 0, buf, ctypes.byref(size)):
            return buf.value
        return ''
    finally:
        kernel32.CloseHandle(handle)


def find_windows():
    """可见的顶层窗口：[(hwnd, pid, exe 基名, rect, minimized)]，Z 序。"""
    found = []

    @ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
    def callback(hwnd, _lparam):
        if not user32.IsWindowVisible(hwnd):
            return True
        pid = wintypes.DWORD()
        user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
        name = _exe_name(pid.value)
        if not name:
            return True
        rect = RECT()
        user32.GetWindowRect(hwnd, ctypes.byref(rect))
        found.append((hwnd, pid.value, name.rsplit('\\', 1)[-1].lower(),
                      (rect.left, rect.top, rect.right - rect.left, rect.bottom - rect.top),
                      bool(user32.IsIconic(hwnd))))
        return True

    user32.EnumWindows(callback, 0)
    return found


def _pack(x, y):
    return ((y & 0xFFFF) << 16) | (x & 0xFFFF)


def hit_test(hwnd, screen_x, screen_y):
    result = user32.SendMessageW(hwnd, WM_NCHITTEST, 0, _pack(screen_x, screen_y))
    return ctypes.c_long(result).value


def pick_window():
    """优先 electron.exe 的非最小化窗口；找不到再退让。"""
    windows = find_windows()
    if not windows:
        print('没有可见的顶层窗口。')
        return None
    print('候选窗口（本进程相关优先，Z 序）：')
    for hwnd, pid, base, rect, mini in windows:
        print('   hwnd=0x%08X pid=%-7d %-18s %-22s %s'
              % (hwnd, pid, base, str(rect), '最小化' if mini else ''))

    def rank(win):
        _hwnd, _pid, base, rect, mini = win
        return (0 if 'electron' in base else 1, 1 if mini else 0, -(rect[2] * rect[3]))

    chosen = min(windows, key=rank)
    print('\n选中 hwnd=0x%08X (%s) 尺寸 %dx%d%s\n'
          % (chosen[0], chosen[2], chosen[3][2], chosen[3][3], '  ⚠️ 最小化中' if chosen[4] else ''))
    return chosen


def main(argv):
    if '--restore' in argv:
        windows = find_windows()
        targets = [w for w in windows if 'electron' in w[2] and w[4]] or \
                  [w for w in windows if 'electron' in w[2]]
        if not targets:
            print('没找到可还原的 electron 窗口。')
            return 1
        hwnd = targets[0][0]
        user32.ShowWindow(hwnd, SW_RESTORE)
        user32.SetForegroundWindow(hwnd)
        time.sleep(0.6)
        print('已还原 hwnd=0x%08X\n' % hwnd)
        argv = [a for a in argv if a != '--restore']

    if '--list' in argv:
        pick_window()
        return 0

    chosen = pick_window()
    if not chosen:
        return 1
    hwnd, _pid, _base, rect, minimized = chosen
    if minimized:
        print('⚠️ 该窗口处于最小化：GetWindowRect 返回 -32000 系坐标，客户端原点不可信。')
        print('   加 --restore 还原后再验收。下面的结果仅供参考。\n')

    origin = POINT(0, 0)
    user32.ClientToScreen(hwnd, ctypes.byref(origin))
    print('客户端原点（屏幕坐标）: (%d, %d)，窗口 rect=%s\n' % (origin.x, origin.y, rect))

    if '--scan' in argv:
        index = argv.index('--scan')
        column = int(argv[index + 1]) if len(argv) > index + 2 else 600
        print('扫描 x=%d 这一列，找拖拽带的连续区间（步长 1，0..160）：' % column)
        bands, start, prev = [], None, None
        for y in range(0, 161):
            name = HT.get(hit_test(hwnd, origin.x + column, origin.y + y), '?')
            if name == 'HTCAPTION':
                start = y if start is None else start
                prev = y
            elif start is not None:
                bands.append((start, prev))
                start = None
        if start is not None:
            bands.append((start, prev))
        if not bands:
            print('   ⚠️ 该列 0..160 内**没有任何** HTCAPTION —— 这页拖不动窗口。')
        for lo, hi in bands:
            print('   HTCAPTION: y = %d..%d  (共 %dpx)' % (lo, hi, hi - lo + 1))
        return 0

    points = [a for a in argv[1:] if ',' in a] or DEFAULT_POINTS
    print('%-12s %-16s %s' % ('客户端坐标', '屏幕坐标', 'WM_NCHITTEST'))
    print('-' * 56)
    for point in points:
        x, y = (int(v) for v in point.split(','))
        code = hit_test(hwnd, origin.x + x, origin.y + y)
        print('%-12s %-16s %s(%d)' % (point, '(%d, %d)' % (origin.x + x, origin.y + y),
                                      HT.get(code, '?'), code))
    return 0


if __name__ == '__main__':
    # DPI 说明：WM_NCHITTEST 的 lParam 用**物理像素**，而 CSS 布局用的是逻辑像素。
    # dpr=1 的机器上两者相同（本仓库的验收环境即是）。若系统缩放不是 100%，
    # 需要把客户端坐标乘上 dpr 再传进来，否则探针点会整体偏。
    sys.exit(main(sys.argv))
