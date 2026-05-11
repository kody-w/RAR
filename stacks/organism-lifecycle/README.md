# Organism Lifecycle (RAR stack)

Two agents that turn a vanilla brainstem into a full organism host. Both were kernel-shipped through 2026-05-10; relocated to RAR so the base install stays minimal and operators opt in when they're ready.

## Two files

| File | Purpose |
|---|---|
| `agents/@rapp/twin_agent.py` | Full digital-twin lifecycle in one drop-in agent — `Twin(action="summon"|"hatch"|"boot"|"stop"|"list"|"inspect"|...)`. Birth twins from a soul template, hatch `.egg` cartridges into local twins, boot them as their own brainstems on their own ports. |
| `agents/@rapp/egg_hatcher_agent.py` | Universal `.egg` cartridge router — `HatchEgg(egg_path=...)`. Reads any `.egg` from a local path or URL, introspects `manifest.schema`/`type`, and routes by kind: organism / rapplication / session / neighborhood / estate. Refuses on unknown kinds — never a destructive fallback. |

## How to install (sneakernet)

Copy both files into your brainstem's `agents/` directory and restart:

```bash
cp ~/Documents/GitHub/RAR/agents/@rapp/twin_agent.py ~/brainstem/agents/
cp ~/Documents/GitHub/RAR/agents/@rapp/egg_hatcher_agent.py ~/brainstem/agents/
```

The LLM picks up `Twin(...)` and `HatchEgg(...)` as tools on the next `/chat` request.

## Why it left the kernel

The base brainstem doesn't need to host sub-twins or hatch eggs on day one — those are capabilities a user grows into. Keeping them kernel-shipped paid a discovery + maintenance cost for every install regardless of whether the operator used them.

See `pack.json` for the sha256 manifest. See [`kody-w/RAPP/blob/main/CLAUDE.md`](https://github.com/kody-w/RAPP/blob/main/CLAUDE.md) for the slimmer kernel-shipped agent list.
