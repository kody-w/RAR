# Brain

Four agents that make a Brainstem sense itself, plus a skill that lets any AI be the host.

| Agent | Brain part | What it does |
|---|---|---|
| HebbianSynapse | synapses | Notes which agents fire together (names and times only) and shows the strongest connections. |
| ReflexArc | reflexes | Suggests "after A, also run B" from repeated sequences; arms one only when you ask. |
| PainReceptor | pain | Shows which agents keep failing, with the error type, so you know what to fix. |
| BrainstemImpact | interoception | Compares the lines of code you committed before and after installing the Brainstem. |

**In a Brainstem:** drop the four `*_agent.py` files into `agents/`.
**In any other AI:** give it `SKILL.md` and `run.py`; it lists the agents and fires them itself.

Everything stays on your machine: `~/.brainstem/synapses.jsonl` and `~/.brainstem/reflexes.json`.
Delete them to forget. Delete the agent files and restart to remove the brain.
