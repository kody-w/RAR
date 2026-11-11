# Write a layer

A layer changes how the **unchanged grail** serves every user: providers, transport,
storage or loading. A use-case tool belongs in an agent, not a layer. Authors and
AIs use this contract with [rapp/1 `protocols/rapp-layer/1`](https://github.com/kody-w/rapp-1/tree/main/protocols/rapp-layer/1).
The protocol wins if this guide and the protocol disagree.
That subordinate profile is currently **proposed, not a signed registry adoption**;
the accepted parent rapp/1 remains authoritative.

## Authoring contract

Ship one Python file with a descriptive module docstring, literal module-level
`PROVEN_GRAIL`, `TOUCHES` and/or `WRAPS` collections, and synchronous `apply()`.
The supervisor AST-parses those declarations **before importing** the file, calls
`apply()` before executing the verified grail bytes, and never edits `brainstem.py`.
Keep imports side-effect-free; install hooks in `apply()`.

**Wrap, never replace:** keep the function already installed at a hook and call
through for inputs your layer does not own. Preserve arguments, return values,
streaming, errors and existing behavior. Never discard an earlier wrapper or
rewrite the kernel. A failed layer must not strand the owner without plain grail.

- `TOUCHES` claims exclusive hook names (for example `requests.post`). The first
  occupant in the supervisor's ordered shape wins; a conflicting later layer is
  skipped and logged, never silently last-wins.
- `WRAPS` declares composable hooks: call through to the implementation already
  installed there. A wrapper may follow an earlier occupant, but a later
  exclusive `TOUCHES` cannot replace that chain. The supervisor reserves both
  sets after applying each part. Pack `point` is the coarse shape slot, not a
  substitute for the file's hook declarations.
- `PROVEN_GRAIL` contains full sha256 hashes of **engine file bytes actually
  tested**, not a version guess. The supervisor skips an unproven engine with
  an explicit log message. Do not remove or add proof to make an installer pass.
  Add an engine only after a real `/chat` **and** `/chat/stream` have run through
  the layer on that exact engine; check the layer's effect, tools, complete
  streaming output and ordinary fallback behavior. Record the version and
  evidence beside the hash in the file, then regenerate.

## Gate, fallback and zero-gap handover

The supervisor tries the proposed shape in a lab: `GET /health` plus a real
`POST /chat` with a nonempty reply. Health is liveness, not behavioral proof.
Before GitHub sign-in, an explicit **Not authenticated** response permits a
health-only gate; it is not evidence that a layer is proven. Sign in and run
real plain and streamed chats before declaring a new engine proven.

Only a passing shape is eligible to go live. A failed live shape falls back to
plain grail; repeated failures can roll back to the prior passing shape. Never
disable that safety net to ship a layer. During zero-gap handover the replacement
must bind and pass before the old process drains in-flight replies, including
streams through their last chunk. **Never break the conversation.** A failed
replacement must leave the working process serving the owner.

## Add, check and remove

In chat: `update my Brainstem with @kody-w/senses_and_pages` (replace the id with
the desired part). Or add the pack's seeded parts:

```bash
curl -fsSL https://kody-w.github.io/grail-layers/add.sh | bash -s -- grail-layers
```

Check `GET http://localhost:7071/api/ticket` when the ticket-page pack is
installed. Also inspect the supervisor's actual boot line:
`[grail-layers] grail <sha>; applied: [...]; skipped: ...`. Match the installed
file's label, check why anything was skipped, and run real `/chat` and
`/chat/stream`. A ticket or health response alone does not establish proof.

Remove the pack with its reversible packs command (shared/user files are kept):

```bash
curl -fsSL https://kody-w.github.io/grail-layers/add.sh | bash -s -- --remove grail-layers
```

This removes a ledger-tracked pack, not a part added individually through chat.
For an individual part, ask to remove its publisher-scoped id or undo that shape
change. Legacy untracked installs may refuse pack removal: inspect the message;
do not delete user files. Published alias files and URLs remain available.

## One source of truth

After editing a layer or pack selection, run:

```bash
python3 tools/sync_layers.py --write
python3 tools/sync_layers.py --check
python3 build_registry.py
```

The synchronizer never imports a layer. It stamps AST-identical comment tickets,
then hashes the **final ticketed bytes**. It derives `install.parts[].sha256`,
`proven_grail`, `touches`, `wraps` and `what` from each layer file, refreshes the
pack's file hashes/sizes and existing legacy proof aliases, and generates
JavaScript-free `a/@publisher/part/index.html` and `agent.md` tickets and the
table below. Existing `layers`, `default_enabled`, ids, locators, status and
published paths are retained. Historical layer filenames also keep their tickets.

`kernel.sha256` remains the historical base pin for older clients;
`kernel.proven` is the **intersection of the seeded layer files'**
`PROVEN_GRAIL` sets (empty if no layers are seeded). It describes compatibility
of the seeded layers, not a new engine download or proof of a replacement kernel.
A `kind: kernel` part with no layer declarations retains its own metadata and
is not treated as an `apply()` layer. Never hand-edit generated facts; CI runs
`--check` before building/publishing the registry.

## Current parts

<!-- BEGIN GENERATED LAYER FACTS -->

Generated from `stacks/*/pack.json` identities/points and each part file's declarations. Versions come from comments beside the declared engine SHA, not from a guessed kernel pin.

| Part / source | Pack | Kind / point | Seeded | Status | Proven engines (sha256 prefix / version) |
|---|---|---|---|---|---|
| [@kody-w/providers](stacks/grail-layers/providers_1_1.py) | grail-layers | layer / provider | yes | current | 35618683ebc3 (v0.6.17), bd55a7f0bcf5 (v0.6.16) |
| [@kody-w/responses_models](stacks/grail-layers/responses_models.py) | grail-layers | layer / provider | no | alias of @kody-w/providers | 35618683ebc3 (v0.6.17), bd55a7f0bcf5 (v0.6.16) |
| [@kody-w/journal_tap](stacks/grail-layers/journal_tap.py) | grail-layers | layer / transport | yes | current | 35618683ebc3 (v0.6.17), bd55a7f0bcf5 (v0.6.16) |
| [@kody-w/local_models](stacks/grail-layers/local_models.py) | grail-layers | layer / provider | no | alias of @kody-w/providers | 35618683ebc3 (v0.6.17), bd55a7f0bcf5 (v0.6.16) |
| [@kody-w/lispy_brainstem](stacks/grail-layers/lispy_brainstem.py) | grail-layers | kernel / kernel | no | current | Not a layer; no PROVEN_GRAIL declaration |
| [@kody-w/senses_and_pages](stacks/grail-layers/senses_and_pages.py) | grail-layers | layer / agents | yes | current | 35618683ebc3 (v0.6.17), bd55a7f0bcf5 (v0.6.16) |
| [@kody-w/own_ai](stacks/grail-layers/own_ai.py) | grail-layers | layer / provider | no | staging | 84d86c3b29e1 (v0.6.17), bd55a7f0bcf5 (v0.6.16) |

<!-- END GENERATED LAYER FACTS -->
