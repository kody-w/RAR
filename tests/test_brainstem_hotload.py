"""Focused regressions for RAR files that previously failed Brainstem hot-load."""

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parent.parent

CASES = [
    ("agents/@discreetRappers/powerpoint_generator_agent.py", ["pptx"]),
    ("agents/@discreetRappers/rapp_pipeline_agent.py", ["azure", "openai"]),
    ("agents/@discreetRappers/sharepoint_contract_analysis_agent.py", ["azure", "openai"]),
    ("agents/@kody-w/ecosystem-grail-stack/launch_to_public_agent.py", ["graft_neighborhood_agent"]),
]


CHILD = r'''
import importlib.abc
import importlib.util
import json
import re
import sys
import types

path = sys.argv[1]
blocked = set(json.loads(sys.argv[2]))

class BlockedImports(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".")[0] in blocked:
            raise ModuleNotFoundError(f"blocked optional dependency: {fullname}")
        return None

sys.meta_path.insert(0, BlockedImports())

class BasicAgent:
    def __init__(self, name=None, metadata=None):
        if name is not None:
            self.name = name
        if metadata is not None:
            self.metadata = metadata

    def to_tool(self):
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.metadata.get("description", ""),
                "parameters": self.metadata.get(
                    "parameters", {"type": "object", "properties": {}}
                ),
            },
        }

class Storage:
    def set_memory_context(self, *args, **kwargs): return True
    def read_json(self, *args, **kwargs): return {}
    def write_json(self, *args, **kwargs): return True
    def read_file(self, *args, **kwargs): return None
    def write_file(self, *args, **kwargs): return True
    def list_files(self, *args, **kwargs): return []
    def file_exists(self, *args, **kwargs): return False

agents = types.ModuleType("agents")
agents.__path__ = []
basic = types.ModuleType("agents.basic_agent")
basic.BasicAgent = BasicAgent
agents.basic_agent = basic
sys.modules["agents"] = agents
sys.modules["agents.basic_agent"] = basic

utils = types.ModuleType("utils")
utils.__path__ = []
storage_factory = types.ModuleType("utils.storage_factory")
storage_factory.get_storage_manager = Storage
utils.storage_factory = storage_factory
sys.modules["utils"] = utils
sys.modules["utils.storage_factory"] = storage_factory

spec = importlib.util.spec_from_file_location("flattened_agent", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

loaded = []
for attr in dir(module):
    cls = getattr(module, attr)
    if not (
        isinstance(cls, type)
        and cls.__module__ == module.__name__
        and hasattr(cls, "perform")
        and cls.__name__ != "BasicAgent"
        and not cls.__name__.startswith("_")
    ):
        continue
    instance = cls()
    assert re.fullmatch(r"[A-Za-z0-9_-]+", instance.name), instance.name
    metadata_name = instance.metadata.get("name", instance.name)
    assert metadata_name == instance.name, (metadata_name, instance.name)
    json.dumps(instance.to_tool())
    loaded.append(instance.name)

assert loaded, "no agent class loaded"
print(json.dumps(loaded))
'''


@pytest.mark.parametrize("relative_path,blocked", CASES)
def test_flattened_agent_loads_without_optional_dependencies(
    tmp_path, relative_path, blocked
):
    source = REPO_ROOT / relative_path
    flattened = tmp_path / source.name
    shutil.copyfile(source, flattened)
    result = subprocess.run(
        [sys.executable, "-c", CHILD, str(flattened), json.dumps(blocked)],
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert result.returncode == 0, (
        f"{relative_path} failed flattened hot-load\n"
        f"stdout: {result.stdout}\nstderr: {result.stderr}"
    )