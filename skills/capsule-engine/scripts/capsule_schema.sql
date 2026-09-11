PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS meta (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL,
  updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS capsules (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  capsule_class TEXT NOT NULL CHECK (capsule_class IN ('pattern', 'synthesis', 'architecture', 'response')),
  knowledge_kind TEXT NOT NULL CHECK (knowledge_kind IN ('fact', 'rule', 'process', 'opinion', 'hypothesis')),
  status TEXT NOT NULL DEFAULT 'candidate' CHECK (status IN ('candidate', 'provisional', 'validated', 'active', 'deprecated', 'archived')),
  summary TEXT NOT NULL,
  what_worked TEXT NOT NULL,
  when_to_apply TEXT NOT NULL,
  why_it_works TEXT NOT NULL,
  failure_conditions TEXT NOT NULL,
  bound_scenarios TEXT NOT NULL DEFAULT '[]',
  tags TEXT NOT NULL DEFAULT '[]',
  source_refs TEXT NOT NULL DEFAULT '[]',
  target_skills TEXT NOT NULL DEFAULT '[]',
  supersedes TEXT REFERENCES capsules(id) ON DELETE SET NULL,
  evidence_confidence REAL NOT NULL DEFAULT 0.50 CHECK (evidence_confidence BETWEEN 0 AND 1),
  context_fit REAL NOT NULL DEFAULT 0.50 CHECK (context_fit BETWEEN 0 AND 1),
  utility_score REAL NOT NULL DEFAULT 0.50 CHECK (utility_score BETWEEN 0 AND 1),
  freshness REAL NOT NULL DEFAULT 1.00 CHECK (freshness BETWEEN 0 AND 1),
  stability REAL NOT NULL DEFAULT 0.50 CHECK (stability BETWEEN 0 AND 1),
  success_count INTEGER NOT NULL DEFAULT 0 CHECK (success_count >= 0),
  failure_count INTEGER NOT NULL DEFAULT 0 CHECK (failure_count >= 0),
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at TEXT NOT NULL DEFAULT (datetime('now')),
  last_applied_at TEXT
);

CREATE TABLE IF NOT EXISTS capsule_events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  capsule_id TEXT NOT NULL REFERENCES capsules(id) ON DELETE CASCADE,
  event_type TEXT NOT NULL CHECK (event_type IN (
    'capture', 'application_success', 'application_failure', 'application_neutral',
    'counterexample', 'promotion', 'activation', 'deprecation', 'archival',
    'synthesis', 'link'
  )),
  context_key TEXT NOT NULL DEFAULT '',
  context TEXT NOT NULL DEFAULT '',
  result TEXT NOT NULL DEFAULT '',
  source TEXT NOT NULL DEFAULT '',
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS capsule_links (
  from_capsule TEXT NOT NULL REFERENCES capsules(id) ON DELETE CASCADE,
  to_capsule TEXT NOT NULL REFERENCES capsules(id) ON DELETE CASCADE,
  relation TEXT NOT NULL CHECK (relation IN (
    'synergy', 'complement', 'conflict', 'tension', 'supersedes',
    'derived_from', 'feeds_skill'
  )),
  notes TEXT NOT NULL DEFAULT '',
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  PRIMARY KEY (from_capsule, to_capsule, relation)
);

CREATE TABLE IF NOT EXISTS capsule_spores (
  id TEXT PRIMARY KEY,
  kind TEXT NOT NULL CHECK (kind IN ('decision', 'gotcha', 'discovery', 'tradeoff', 'fix', 'hypothesis')),
  statement TEXT NOT NULL,
  context TEXT NOT NULL DEFAULT '',
  source TEXT NOT NULL DEFAULT '',
  status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'consumed', 'rejected')),
  evidence_confidence REAL NOT NULL DEFAULT 0.50 CHECK (evidence_confidence BETWEEN 0 AND 1),
  tags TEXT NOT NULL DEFAULT '[]',
  consumed_by TEXT REFERENCES capsules(id) ON DELETE SET NULL,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  consumed_at TEXT
);

CREATE INDEX IF NOT EXISTS idx_capsules_status ON capsules(status);
CREATE INDEX IF NOT EXISTS idx_capsules_class_kind ON capsules(capsule_class, knowledge_kind);
CREATE INDEX IF NOT EXISTS idx_capsule_events_capsule ON capsule_events(capsule_id, created_at);
CREATE INDEX IF NOT EXISTS idx_capsule_events_context ON capsule_events(context_key);
CREATE INDEX IF NOT EXISTS idx_capsule_spores_status ON capsule_spores(status);

INSERT OR REPLACE INTO meta(key, value, updated_at)
VALUES ('capsule_schema_version', '1', datetime('now'));
