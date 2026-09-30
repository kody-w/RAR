# DynamicWorkflow — sources

`agents/@kody-w/dynamic_workflow_agent.py` is the published single-file agent; this folder holds the parts it is
assembled from. Edit here, then rebuild — the assembled file must stay byte-identical to what `assemble.py` writes.

| file | what it is |
|---|---|
| `agent.src.py` | the agent (library, engine launcher, mount, Copilot extension install) with placeholders |
| `runner.mjs` | the engine: Copilot's workflow `ctx` on headless `copilot -p` subagents, journaled so runs survive crashes |
| `extension.mjs` | the Copilot CLI extension `install_copilot` writes: registers every saved workflow natively |
| `workflows/<name>.run.js` / `.meta.json` / `.version` | the built-in workflows (`adversarial-fleet`, `reflect`) |
| `sims/` | each built-in workflow run against a mock `ctx` with the documented semantics (no model calls) |
| `governor/` | watching runs from a governing session: `watch.py` (wakes on final outcomes, re-runs each proven unit's A/B), `gov_ab.py`, `fleet_status.sh` |

```sh
python3 scripts/dynamic_workflow/assemble.py                     # rebuild the agent
node scripts/dynamic_workflow/sims/sim_reflect.js scripts/dynamic_workflow/workflows/reflect.run.js
python3 -m pytest -q tests/test_dynamic_workflow_agent.py        # the engine, with a fake copilot
```

A built-in's library copy (`~/.rapp/workflows/library/<name>.json`) upgrades only when its `.version` rises.
