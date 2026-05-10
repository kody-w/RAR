# Microsoft 365 Team Starter (RAR stack)

Drop-in pack for Microsoft Solution Engineers. Plant your own MS-themed RAPP neighborhood under YOUR GitHub handle in one chat.

## Two files

| File | Purpose |
|---|---|
| `factory_agent.py` | Drop into your local brainstem `agents/`. Plants new MS-themed neighborhoods. |
| `microsoft-365-team.egg` | The template content — 11 agents including WorkIQ + MS-stack Twin. |

## How to use (one chat)

```
NeighborhoodFactory mode=public owner=YOURHANDLE name=my-ms-team display_name="My MS Team" dry_run=False
```

Modes: `local` / `private` / `public` / `egg` (combinable: `local,egg` etc).

## What you get

- 11 agents: workflow gate set (Intake / OutcomeFramer / Pm / OutcomeValidator / EngagementFactory) + WorkIQ for M365 data + MS-stack Twin with field patterns + EggHatcher for sneakernet + DashboardRender + ProjectPinger + SesWorkspaceInit
- Per-operator workspace at `~/.brainstem/workbenches/<your-slug>/<handle>/customers/`
- PII enforcement: `.gitignore` excludes `.brainstem/`; no customer data ever in repo by default
- Use the canonical example at https://github.com/kody-w/microsoft-365-team as a template via "Use this template" in the GitHub UI

See `pack.json` for sha256 manifest. See https://github.com/kody-w/RAPP/blob/main/CONSTITUTION.md for the kernel constitution this neighborhood inherits from.
