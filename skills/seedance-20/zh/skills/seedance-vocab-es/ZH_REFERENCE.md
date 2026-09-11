---
name: seedance-vocab-es
description: "This skill should be used when the user asks for Spanish Seedance 2.0 prompt wording, Spanish cinematic vocabulary, or translation of camera, lighting, action, VFX, audio, and production terms into Spanish."
license: MIT
metadata:
  version: "6.1.0"
  updated: "2026-06-22"
  parent: "seedance-20"
  author: "Iamemily2050 (@iamemily2050)"
  repository: "https://github.com/Emily2040/seedance-2.0"
  openclaw:
    emoji: "🎬"
    homepage: "https://github.com/Emily2040/seedance-2.0"
---

# seedance-vocab-es

当用户要求西班牙语提示词、双语交付，或要求把相机、光线、动作、视效、音频和制作约束做紧凑翻译时，使用西班牙语电影词汇。引用标签务必原样保留：`[Image1]`、`[Video1]`、`[Audio1]` 绝不能被翻译。

## 意图

西班牙语即使在技术性的执导中也自带韵律。为用西班牙语思考的用户提供既保有其音乐性、又保持相机精度的词汇——他们绝不应感到用自己的语言执导是一种降级。

## 使用规则

翻译制作含义，而非逐字对译英语。让提示词保持具体而简洁：主体、可见动作、相机、光线、声音和约束。

| 功能 | 西班牙语措辞 |
|---|---|
| Camera | `travelling de acercamiento`, `plano medio`, `primer plano`, `seguimiento lateral`, `cámara fija` |
| Lighting | `contraluz`, `luz suave de ventana`, `luz práctica cálida`, `sombra marcada`, `halo frío de luna` |
| Motion | `gira lentamente`, `cruza rápido el encuadre`, `avanza con estabilidad`, `las gotas se deslizan` |
| Audio | `sonido ambiente`, `diálogo claro`, `golpe metálico suave`, `sin música` |
| Constraints | `mantener el logotipo, la etiqueta y la forma sin cambios` |

## 紧凑范式

`[Image1] es la referencia; mantener identidad, color y forma sin cambios. Solo cambia [movimiento/luz/cámara]. Cámara: [un movimiento]. Sonido: [señal].`

## 去套话规则

当提示词依赖 `cinematográfico`、`épico`、`impresionante`、`mágico` 或 `de alta calidad` 时，加载 `../../../references/vocab/es.md` 中的套话陷阱表，把每个词分解为产生它的物理要素——movimiento de cámara、fuente de luz、material、sonido。

## 输出契约

返回西班牙语提示词措辞、有用时可选的英语注释，以及未改动的引用标签。
