CREATE TABLE IF NOT EXISTS agent_interactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    trigger_type TEXT NOT NULL,
    input_text TEXT,
    output_text TEXT,
    status TEXT DEFAULT 'completed',
    error_message TEXT,
    metadata JSON
);

CREATE TABLE IF NOT EXISTS agent_memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    summary TEXT NOT NULL,
    source_interaction_ids TEXT
);

CREATE TABLE IF NOT EXISTS cron_jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    name TEXT NOT NULL UNIQUE,
    cron_expression TEXT NOT NULL,
    timezone TEXT DEFAULT 'Asia/Seoul',
    enabled INTEGER DEFAULT 1,
    last_run_at TIMESTAMP,
    next_run_at TIMESTAMP
);

-- Persistent knowledge-base document registry.
-- This stores structured metadata for files under knowledge-base/ and URL ingests.
CREATE TABLE IF NOT EXISTS kb_documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    -- One of: file_upload, url_ingest, kb_seed
    source_type TEXT NOT NULL,
    -- Absolute path on disk (for files we store locally). May be NULL for future remote-only sources.
    path TEXT,
    -- Original URL (for url_ingest). NULL for local uploads.
    url TEXT,
    -- Stable content hash to dedupe ingests.
    content_sha256 TEXT,
    title TEXT,
    tags TEXT, -- JSON array string
    language TEXT,
    scope TEXT,
    last_updated TEXT,
    metadata JSON,
    UNIQUE(path),
    UNIQUE(url)
);

-- Persistent list of “Resource Center URLs” used for OpenRouter web search.
CREATE TABLE IF NOT EXISTS rc_urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    url TEXT NOT NULL UNIQUE,
    title TEXT,
    tags TEXT, -- JSON array string
    scope TEXT,
    enabled INTEGER DEFAULT 1
);

-- Lightweight key/value settings used by UI-configurable prompt profile.
CREATE TABLE IF NOT EXISTS app_settings (
    key TEXT PRIMARY KEY,
    value TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- User feedback that drives self-evolution memory.
CREATE TABLE IF NOT EXISTS agent_feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    interaction_id INTEGER,
    verdict TEXT NOT NULL, -- correct | incorrect | useful | noisy
    note TEXT,
    correction TEXT,
    metadata JSON
);
