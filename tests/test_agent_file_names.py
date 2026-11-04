"""Agent files say what they are: a factory is `<what>_factory_agent.py`, never a bare `factory_agent.py`.
(Kody, 2026-11-04.) Two packs installed into ONE Brainstem share one agents/ folder; a bare generic name is how a
Neighborhood factory and a Copilot Studio factory overwrote each other. Old bare files stay served as aliases."""
import json
from pathlib import Path

BARE = {"factory_agent.py"}


def test_no_pack_installs_a_bare_generic_agent_name():
    for p in sorted(Path("stacks").glob("*/pack.json")):
        files = json.loads(p.read_text()).get("files") or {}
        assert not BARE & set(files), f"{p.parent.name} installs {sorted(BARE & set(files))}; name it <what>_factory_agent.py"
