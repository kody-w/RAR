# @kody-w/own_ai - RAPP layer ticket

## What it changes

Layer: own_ai — the unchanged grail thinks with the AI already on this device, with no sign-in.

The kernel knows one provider: the endpoint it is handed by its sign-in exchange, which speaks the OpenAI
chat-completions wire. When BRAINSTEM_AI names a command that runs the person's own AI for one message
(for example `claude -p`), this layer answers that exchange itself and sends every chat-completions call
to that command instead. The kernel file is untouched: soul, agents, memory, tool calls, /chat and the
web page all work as they do on any Brainstem. BRAINSTEM_AI unset: this layer does nothing.

Status: staging. Not seeded: the person turns it on. Proven on a Mac with one AI so far.

Env: BRAINSTEM_AI   the one-message command; the prompt is added as its last argument
     BRAINSTEM_AI_STDIN=1   send the prompt on standard input instead (for long conversations)

Pack: grail-layers
Kind: layer
Point: provider
Status: staging
TOUCHES (exclusive): None
WRAPS (composable): requests.get, requests.post
Proven engines: 84d86c3b29e1 (v0.6.17), bd55a7f0bcf5 (v0.6.16)

## Add, check, remove

Add in chat: update my Brainstem with @kody-w/own_ai
Or add the pack (its seeded parts): curl -fsSL https://kody-w.github.io/grail-layers/add.sh | bash -s -- grail-layers
Check: GET http://localhost:7071/api/ticket (when the ticket-page pack is installed);
  confirm this file's label is in the supervisor log: [grail-layers] grail <sha>; applied: [...]; skipped: ...
  Label: own_ai. Health alone is not proof; test /chat and /chat/stream.
Remove the pack (keeps shared/user files): curl -fsSL https://kody-w.github.io/grail-layers/add.sh | bash -s -- --remove grail-layers
  For a part added individually in chat, ask to remove its id or undo that shape change.
Rules: https://kody-w.github.io/RAR/LAYERS.md ; rapp/1 protocols/rapp-layer/1: https://github.com/kody-w/rapp-1/tree/main/protocols/rapp-layer/1

A pack command installs only its seeded parts; it does not select an unseeded alias. Use the publisher-scoped chat id for an individual part. Only load code you trust.

Raw file: https://kody-w.github.io/RAR/stacks/grail-layers/own_ai.py
Page: https://kody-w.github.io/RAR/a/@kody-w/own_ai/
Plain text for AIs: https://kody-w.github.io/RAR/a/@kody-w/own_ai/agent.md

Full PROVEN_GRAIL sha256 values:
- 84d86c3b29e111a2c1d1c68b67230e057261f7fc8a191dfefc0e3b26d6fcc99c
- bd55a7f0bcf5efd3f7966ca39bb146da3c25fda9a0b1ce5ba587919d3c3775f4
