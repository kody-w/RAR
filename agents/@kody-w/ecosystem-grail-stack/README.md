# ecosystem-grail-stack

The operator's daily-driver toolkit for keeping the RAPP ecosystem
grail-compliant + extensible. Four single-file agents that compose:

| Agent | Purpose |
|---|---|
| `bond_rhythm_agent.py` | The Bond Pulse heartbeat — local↔global drift detection. Suggests Launch / Graft / RarLoader actions; never auto-executes. Schema: `rapp-rhythm-pulse/1.0`. |
| `launch_to_public_agent.py` | LOCAL→GLOBAL push — snapshots local brainstem state, plants/grafts to a target public repo with the bond technique. Schema: `rapp-launch-result/1.0`. |
| `chain_composer_agent.py` | Compose multi-primitive chain plans from natural-language operator prompts. Reads the canonical RAPP toolbox and returns `rapp-chain-plan/1.0` envelopes + executable bash scripts. Operator-mediated. |
| `plant_seed_agent.py` | Create fresh public planted seeds (neighborhoods OR twins), grail-complete from minute one. Each planting includes the full front-door grail (rappid + soul + holocard + holo.svg + holo-qr + specs/). Schema: `rapp-plant-seed-result/1.0`. |

## How they compose

```
operator prompt (e.g. "weekly heartbeat self-portrait")
  ↓
chain_composer.perform(user_prompt=...) — returns multi-step plan
  ↓
plan may include:
  - bond_rhythm.perform()       — pulse + classify drift
  - plant_seed.perform()        — create new neighborhoods/twins
  - launch_to_public.perform()  — push local → public
  ↓
operator reviews + runs the executable script
```

## Identity

Each agent has its canonical schema declared in its docstring. All
operator-mediated by design (default `dry_run=True` for anything that
affects global state). Per ANTIPATTERNS §9.

Parent project: [kody-w/RAPP](https://github.com/kody-w/RAPP).
Discussed in detail: vault note `2026-05-09 — Bond Pulse — the on-going beat for the full organism.md`.
