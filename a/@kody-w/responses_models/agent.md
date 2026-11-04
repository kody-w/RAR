# @kody-w/responses_models - RAPP layer ticket

## What it changes

Layer: responses_models — lets the unchanged grail use models that only speak the Responses API
(for example gpt-6-astra and gpt-6.1-sol on GitHub Copilot).

The grail filters those models out of /models because it only calls /chat/completions. This layer
wraps the `requests` functions the grail calls, inside the Brainstem process only:
  GET  <endpoint>/models            -> keeps Responses-only models in the list (remembers which)
  POST <endpoint>/chat/completions  -> for those models: calls <endpoint>/responses and returns the
                                       answer in chat-completions shape; a streaming request gets a
                                       clean refusal so the grail falls back to its non-stream path.
Everything else passes straight through. Any error inside the layer -> the grail's original call.

Pack: grail-layers
Kind: layer
Point: provider
Status: alias of @kody-w/providers
TOUCHES (exclusive): requests.get, requests.post
WRAPS (composable): None
Proven engines: 35618683ebc3 (v0.6.17), bd55a7f0bcf5 (v0.6.16)

## Add, check, remove

Add in chat: update my Brainstem with @kody-w/responses_models
Or add the pack (its seeded parts): curl -fsSL https://kody-w.github.io/grail-layers/add.sh | bash -s -- grail-layers
Check: GET http://localhost:7071/api/ticket (when the ticket-page pack is installed);
  confirm this file's label is in the supervisor log: [grail-layers] grail <sha>; applied: [...]; skipped: ...
  Label: responses_models. Health alone is not proof; test /chat and /chat/stream.
Remove the pack (keeps shared/user files): curl -fsSL https://kody-w.github.io/grail-layers/add.sh | bash -s -- --remove grail-layers
  For a part added individually in chat, ask to remove its id or undo that shape change.
Rules: https://kody-w.github.io/RAR/LAYERS.md ; rapp/1 protocols/rapp-layer/1: https://github.com/kody-w/rapp-1/tree/main/protocols/rapp-layer/1

A pack command installs only its seeded parts; it does not select an unseeded alias. Use the publisher-scoped chat id for an individual part. Only load code you trust.

Raw file: https://kody-w.github.io/RAR/stacks/grail-layers/responses_models.py
Page: https://kody-w.github.io/RAR/a/@kody-w/responses_models/
Plain text for AIs: https://kody-w.github.io/RAR/a/@kody-w/responses_models/agent.md

Full PROVEN_GRAIL sha256 values:
- 35618683ebc3d1c2bfaff47f60182fd756f3a8de53c53dd907ec1099d631930a
- bd55a7f0bcf5efd3f7966ca39bb146da3c25fda9a0b1ce5ba587919d3c3775f4
