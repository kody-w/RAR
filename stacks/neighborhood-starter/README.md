# Neighborhood Starter Stack

The canonical starter pack for planting your own RAPP neighborhood. Two files:

| File | Purpose |
|---|---|
| `factory_agent.py` | Drops into your local brainstem `agents/` directory. Plants new neighborhoods from the template. |
| `neighborhood-starter.egg` | The template content (10 agents + dashboard rapplication + constitution + skill + specs + onboarding HTML). |

## How to use

1. Get a brainstem running locally (one-time):
   ```bash
   curl -fsSL https://kody-w.github.io/RAPP/installer/install.sh | bash
   ```

2. Drop `factory_agent.py` into your brainstem's `agents/` directory.

3. In your brainstem chat:
   ```
   NeighborhoodFactory mode=local owner=alice name=my-team display="Alice's Team" dry_run=False
   ```

That's it. You have a brand-new neighborhood at `~/brainstem-workspace/my-team/` with the full workflow.

## Modes

The factory supports four modes, comma-separated to combine:

| Mode | Where it lives | Use case |
|---|---|---|
| `local` | `~/brainstem-workspace/<name>/` only | Solo, on-device, no remote |
| `private` | Above + `gh repo create --private` + push | Team with sensitive work |
| `public` | Above + `gh repo create --public` + push | Open community |
| `egg` | `~/brainstem-eggs/<name>-<ts>.egg` | Sneakernet to anyone |

Combinations work: `mode=local,egg` produces both a workspace AND a portable .egg in one shot.

## What's in the template

```
agents/                          ← 10 single-file agents, sha256-pinned
  egg_hatcher_agent.py           (ONE bootstrap, all modes — egg, repo, pack, status)
  engagement_factory_agent.py    (end-to-end engagement starter)
  dashboard_render_agent.py      (rapplication renderer)
  ses_workspace_init_agent.py    (per-handle workspace mint)
  project_pinger_agent.py        (cross-team + personal portfolio)
  twin_agent.py                  (parameterized twin)
  outcome_framer_agent.py        (why-first gate)
  intake_agent.py                (capture raw ideas)
  outcome_validator_agent.py     (validate before close)
  pm_agent.py                    (sprints + status reports)
rapplications/dashboard/         ← deterministic HTML dashboard
specs/                           ← agent contract / neighborhood protocol / rar index
ses/                             ← per-operator front doors land here
CONSTITUTION.md                  ← 8 articles governing the neighborhood
SKILL.md                         ← feed to your LLM to drive setup
SETUP.md                         ← all 3 setup modes documented
QUICK_START.md                   ← terse 1-pager
README.md, onboarding.html       ← entry points
rappid.json, neighborhood.json, members.json, soul.md, .gitignore  ← templated
rar/index.json                   ← sha256 manifest
```

## Sneakernet portability

This pack obeys the kernel sneakernet portability invariant: the receiver does drag-drop + one chat. No shell commands, no follow-up configuration. Per `pages/docs/rapplication-sdk.md` (Sneakernet portability invariant section).

After a planting, the resulting neighborhood inherits the same property: pack it as a .egg, sneakernet to anyone, they hatch it with `EggHatcher from_egg=<path>` — done.

## See also

- Kernel constitution: https://github.com/kody-w/RAPP/blob/main/CONSTITUTION.md
- Rapplication SDK + sneakernet rule: https://github.com/kody-w/RAPP/blob/main/pages/docs/rapplication-sdk.md
- Stack metadata: `pack.json`
