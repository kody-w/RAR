# Thoughtbox

Local-first reflection journal — append, list, search, tag, export, import. Durable local storage, portable JSON blob you control.

By default entries persist in `thoughtbox/entries.json` under `BRAINSTEM_DATA_DIR` (or `.brainstem_data` beside the installed `agents/` directory). Writes are atomic and flushed to disk; entries survive agent reloads and process restarts. Paired `_context` callbacks `workspace_read` and `workspace_write` still select workspace storage. Read/write failures return `ok: false` without switching to volatile memory or acknowledging an unsaved entry.

Moved here from the RAPP Store (now an alias of RAR); the original page keeps working: https://kody-w.github.io/RAPP_Store/#thoughtbox
