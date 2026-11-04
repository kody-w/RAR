# @kody-w/providers - RAPP layer ticket

## What it changes

Layer: providers — every model the unchanged grail can reach, in one provider part.

Kody's ruling (2026-11-03): one occupant per shape point, so the two provider behaviours live in ONE part:
  1. responses_models: models that only speak the Responses API (gpt-6.1-sol, gpt-6-luna) on GitHub Copilot
     become usable; /chat/completions calls for them are translated to /responses and back.
  2. local_models: models running on this machine (Ollama, OLLAMA_URL default http://127.0.0.1:11434) join the
     model list as ollama/<name> and answer chat with tools, no Copilot needed for them.
`@kody-w/responses_models` and `@kody-w/local_models` are ALIASES of this part: their files stay published and
unchanged, new shapes use this one. Privacy-policy and local-dispatch errors refuse; they never fall back to cloud.
  3. private mode (1.1): topics the owner marked private (<layers home>/private-topics.json, managed in chat by the
     PrivateMode agent) never leave this machine. A chat whose user messages mention one is answered by a local
     Ollama model whatever model is picked; with no local model running it is refused, never sent to the cloud.
     Matching is case-insensitive substring matching, not semantic classification. An absent policy leaves ordinary
     routing unchanged; an unreadable, corrupt or invalid policy refuses chat until repaired.

Pack: grail-layers
Kind: layer
Point: provider
Status: current
TOUCHES (exclusive): requests.get, requests.post
WRAPS (composable): None
Proven engines: 35618683ebc3 (v0.6.17), bd55a7f0bcf5 (v0.6.16)

## Add, check, remove

Add in chat: update my Brainstem with @kody-w/providers
Or add the pack (its seeded parts): curl -fsSL https://kody-w.github.io/grail-layers/add.sh | bash -s -- grail-layers
Check: GET http://localhost:7071/api/ticket (when the ticket-page pack is installed);
  confirm this file's label is in the supervisor log: [grail-layers] grail <sha>; applied: [...]; skipped: ...
  Label: providers_1_1. Health alone is not proof; test /chat and /chat/stream.
Remove the pack (keeps shared/user files): curl -fsSL https://kody-w.github.io/grail-layers/add.sh | bash -s -- --remove grail-layers
  For a part added individually in chat, ask to remove its id or undo that shape change.
Rules: https://kody-w.github.io/RAR/LAYERS.md ; rapp/1 protocols/rapp-layer/1: https://github.com/kody-w/rapp-1/tree/main/protocols/rapp-layer/1

A pack command installs only its seeded parts; it does not select an unseeded alias. Use the publisher-scoped chat id for an individual part. Only load code you trust.

Raw file: https://kody-w.github.io/RAR/stacks/grail-layers/providers_1_1.py
Page: https://kody-w.github.io/RAR/a/@kody-w/providers/
Plain text for AIs: https://kody-w.github.io/RAR/a/@kody-w/providers/agent.md

Full PROVEN_GRAIL sha256 values:
- 35618683ebc3d1c2bfaff47f60182fd756f3a8de53c53dd907ec1099d631930a
- bd55a7f0bcf5efd3f7966ca39bb146da3c25fda9a0b1ce5ba587919d3c3775f4
