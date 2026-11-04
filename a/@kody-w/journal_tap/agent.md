# @kody-w/journal_tap - RAPP layer ticket

## What it changes

Layer: journal_tap — every completed chat turn is recorded in the owner's journal, by default.

Simon Willison's `llm` lesson: the log people keep a tool for is the one that is on by default and searchable
later. The Brainstem Journal (a sidecar on :7074) already keeps that record, but only for turns routed through
its proxy; the chat page talks to the kernel on :7071 directly, so the record stayed nearly empty.

This layer wraps, inside the Brainstem process only, the registration of the kernel's two chat routes:
  POST /chat         -> after the kernel answers (200, JSON), the turn is posted to <journal>/journal/record
  POST /chat/stream  -> the event stream is passed through untouched; when its "done" event has gone by, the
                        same record is posted
The post runs on a daemon thread with a short timeout; the answer to the person is never delayed or changed.
No journal running, journal refusing, bad network: nothing happens and the kernel is unaffected.
The owner pauses it with a file (`<journal store>/paused`; the JournalRecall agent toggles it in chat).

Env: JOURNAL_URL (default http://127.0.0.1:7074), JOURNAL_STORE (default ~/.brainstem/journal).

Pack: grail-layers
Kind: layer
Point: transport
Status: current
TOUCHES (exclusive): flask.Flask.add_url_rule
WRAPS (composable): None
Proven engines: 35618683ebc3 (v0.6.17), bd55a7f0bcf5 (v0.6.16)

## Add, check, remove

Add in chat: update my Brainstem with @kody-w/journal_tap
Or add the pack (its seeded parts): curl -fsSL https://kody-w.github.io/grail-layers/add.sh | bash -s -- grail-layers
Check: GET http://localhost:7071/api/ticket (when the ticket-page pack is installed);
  confirm this file's label is in the supervisor log: [grail-layers] grail <sha>; applied: [...]; skipped: ...
  Label: journal_tap. Health alone is not proof; test /chat and /chat/stream.
Remove the pack (keeps shared/user files): curl -fsSL https://kody-w.github.io/grail-layers/add.sh | bash -s -- --remove grail-layers
  For a part added individually in chat, ask to remove its id or undo that shape change.
Rules: https://kody-w.github.io/RAR/LAYERS.md ; rapp/1 protocols/rapp-layer/1: https://github.com/kody-w/rapp-1/tree/main/protocols/rapp-layer/1

A pack command installs only its seeded parts; it does not select an unseeded alias. Use the publisher-scoped chat id for an individual part. Only load code you trust.

Raw file: https://kody-w.github.io/RAR/stacks/grail-layers/journal_tap.py
Page: https://kody-w.github.io/RAR/a/@kody-w/journal_tap/
Plain text for AIs: https://kody-w.github.io/RAR/a/@kody-w/journal_tap/agent.md

Full PROVEN_GRAIL sha256 values:
- 35618683ebc3d1c2bfaff47f60182fd756f3a8de53c53dd907ec1099d631930a
- bd55a7f0bcf5efd3f7966ca39bb146da3c25fda9a0b1ce5ba587919d3c3775f4
