# RAPP — the one page for any AI (read this, then you can participate)

RAPP lets a person run their own AI on their own computer, a **Brainstem**, and extend it with single-file
**agents**. It is driven entirely by chat. You (an outside AI) can build for it, install into it, talk to it and
publish to it. This page is the summary; where it and a linked spec disagree, the spec wins.

## 1. The five things to know
1. **The kernel (the grail) never changes.** `brainstem.py` from github.com/kody-w/rapp-installer is pinned by
   sha256. Everything else is built on top: an agent, a layer, or a sidecar. Never patch the kernel.
2. **The wire is one endpoint.** `POST /chat` with JSON `{"user_input": "...", "session_id"?: "...",
   "conversation_history"?: [...]}` returns `{"response", "agent_logs", "session_id", ...}`; ignore members you do
   not know; a bad request is HTTP 400 `{"error"}`. `GET /health` is liveness only. Default port 7071.
   **New capability is a new agent behind /chat, never a new REST route.** (rapp/1 §8)
3. **An agent is one Python file** named `*_agent.py` (factories: `*_factory_agent.py`) in the Brainstem's
   `agents/` folder. It subclasses `BasicAgent` (`from agents.basic_agent import BasicAgent`), sets `self.name`
   (the tool name) and `self.metadata` (an OpenAI function schema), and implements `perform(**kwargs) -> str`.
   Optional `system_context() -> str|None` adds a line to every prompt. Carry a `__manifest__` dict
   (`schema: rapp-agent/1.0`, `name: @publisher/slug`, version, display_name, description). Agents reload on every
   request; no restart.
4. **Everything is content-addressed.** Files are pinned by sha256; the same bytes install once; published bytes
   never change (a fix is a new version). Identities are rappids (rapp/1 §6), never derived from names.
5. **Nothing is deleted.** Old names get a status (current, alias of X, retiring on a date, tombstone) and every URL
   that ever worked keeps working.

## 2. The parts you can ship (all in RAR, the one store: https://kody-w.github.io/RAR/)
| Part | File | Goes to | What it does |
|---|---|---|---|
| agent | `*_agent.py` | `agents/` | a tool the AI can call; the only way to add capability |
| layer | `grail-layer/1` Python with `apply()` | applied in memory by the supervisor | serves every user (providers, journal); declares `TOUCHES` (exclusive) or `WRAPS` (composable) and `PROVEN_GRAIL` shas |
| sense | `*_sense.py` (`name, delimiter, response_key, system_prompt`) | `~/.brainstem/senses/` | one extra field beside each plain `/chat` reply (headline, tl;dr) |
| page | `*_page.py` (`name, handle(method, path, body)`) | `~/.brainstem/pages/` | a local page at `/api/<name>/`; a convenience with no RAPP semantics. `organ` is an alias of page |
| pack | `stacks/<name>/pack.json` (`rapp-rar-stack/1.2`) | the cart | a list of the parts above, sha-pinned, with optional `includes` (other packs). A starter or distro is a pack |
| egg | rapp/1 §9 ZIP (`organism`, `rapplication`, ...) | anywhere | a pack plus your data: a whole Brainstem you can move or hatch |

## 3. Installing (what the person runs, or you run for them)
```bash
curl -fsSL https://kody-w.github.io/grail-layers/install.sh | bash        # the grail, then layers over it
curl -fsSL https://kody-w.github.io/grail-layers/add.sh | bash -s -- starter-personal @rapp/twin_agent   # packs and store agents, one cart
```
The installer resolves the cart as a sorted set (any order gives the same plan), checks every sha before
touching anything, boots the layers in a lab and sends a real `/chat` before going live, never overwrites (same
tool name = upgrade with a kept copy; different bytes under a taken name = a scoped name), and undoes in one step.
`--plan-json` shows the plan and changes nothing; `--skip <file>` leaves a card out.

Easy mode (you do it all for the person): load the RAPP skill https://kody-w.github.io/grail-layers/skills/rar-easy-mode/SKILL.md
(GitHub Copilot Chat in Agent mode is the default host; any AI that can run commands works; a Brainstem can run it as
`rar_easy_mode_agent.py` beside it). The person only says "Show me RAR" or "Give me <names> ... and test it for me".
## 4. Lifecycle (ALM) rules you must follow
Status: PROPOSAL (`rapp-alm/1`, https://github.com/kody-w/rapp-1/pull/59, not yet accepted). Follow it, but where it
differs from the accepted rapp/1 spec, the accepted spec wins; re-read this page before relying on it.
Author → publish (immutable version + shas) → verify (RAR CI, receipts) → cart → plan → gate → install →
upgrade → undo → alias → tombstone (only after measured zero use). Ids are publisher-scoped from the first publish
(`@you/part`). A pack only adds; it never edits the kernel or another publisher's part. A use case is an agent,
never a layer. Full rules and the lessons behind them: https://kody-w.github.io/grail-layers/ALM.md (proposed as
`rapp-alm/1`: https://github.com/kody-w/rapp-1/pull/59).

## 5. Data surfaces
Every catalog, registry or site follows **rapp-static-api/1.1** (https://github.com/kody-w/rapp-static-apis):
one hand-written input, one idempotent build, a schema-tagged `registry.json`, `api/v<major>/*.json`,
append-only `versions/`, `llms.txt`. Browsers never call api.github.com and never defeat the cache.

## 6. How to participate
- **Talk to a Brainstem:** `POST http://127.0.0.1:7071/chat` (local only unless the owner enables LAN).
- **Build an agent:** copy https://kody-w.github.io/RAR/template_agent.py, keep it one file, stdlib first, never
  hold secrets, reply in plain words, never raise from `perform`.
- **Publish:** submit to RAR (https://kody-w.github.io/RAR/submit.html or an issue on github.com/kody-w/RAR);
  CI checks names, shas and receipts. A red check is the system working: fix it, never bypass it.
- **Change the protocol:** only through a pull request to github.com/kody-w/rapp-1, accepted by the owner.
  Proposals say they are proposals; nothing is registered until ratified.
- **Never:** edit the grail, add a sibling REST route as capability, put secrets or keys in any repo, invent a new
  file format or noun without naming the existing one it maps to, or silently overwrite anything.

## 7. Source of truth (verify, do not trust this page)
rapp/1 spec: https://kody-w.github.io/rapp-1/SPEC.md · rapp/1 for AIs: https://kody-w.github.io/rapp-1/llms.txt ·
reference code: https://kody-w.github.io/rapp-1/rapp.py · conformance: https://kody-w.github.io/rapp-1/conformance/vectors.json ·
grail layers: https://kody-w.github.io/grail-layers/llms.txt · the store: https://kody-w.github.io/RAR/distros.html
