---
name: "rar-kody-w-rappter-engine"
description: "Provides a base class for rules-as-data content engines \u2014 subclass it, override tick(), and run it as a CLI or brainstem tool."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rappter_engine_agent", "rar_sha256": "4d532a0027f1424511d571af7f1c8e31d2fb73cfc00b10320d119e94dc00422e", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["engine", "framework", "content", "automation", "rules-as-data", "heartbeat"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/rappter_engine_agent`. The original RAPP
agent is preserved byte-for-byte in `rappter_engine_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Rappter Engine Agent — Base agent for building data-driven content engines.

Subclass RappterEngine, define your RULES as data, override tick(), and
you have an autonomous content engine that works as a CLI and as a
Brainstem-harnessable agent.

Every engine in the Rappter ecosystem (Zoo Heartbeat, Economy Engine,
Interaction Engine, Academy Engine, Rappterpedia Engine) follows this
pattern. This agent extracts the shared machinery so you can build
your own engine in minutes.

== QUICK START ==

    from rappter_engine_agent import RappterEngine

    class MyEngine(RappterEngine):
        ENGINE_NAME = "My Engine"
        RULES = {
            "post": {
                "weight": 5,
                "templates": ["Hello from {author} in {world}!"],
            },
        }

        def tick(self, state, ctx):
            rule_name, rule = self.pick_weighted(self.RULES)
            text = self.fill(random.choice(rule["templates"]), ctx)
            state.setdefault("items", []).append({"type": rule_name, "text": text})
            return [f"Generated: {text[:60]}"]

    if __name__ == "__main__":
        MyEngine().run()

Operations:
  - run_tick:     Execute one engine tick and return results
  - run_burst:    Execute multiple ticks
  - get_state:    Return current engine state as JSON
  - list_rules:   Show all registered rules
  - describe:     Describe the engine and its capabilities

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "count": {
      "description": "Number of ticks for burst mode",
      "type": "integer"
    },
    "operation": {
      "description": "Engine operation",
      "enum": [
        "run_tick",
        "run_burst",
        "get_state",
        "list_rules",
        "describe"
      ],
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rappter_engine_agent.py` and embedded as the fenced Python below (sha256 4d532a0027f14245…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rappter_engine_agent.py` first:

```bash
python3 rappter_engine_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rappter_engine_agent.py   # or on stdin
python3 rappter_engine_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/rappter_engine_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/rappter_engine_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/rappter_engine_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Rappter Engine Agent — Base agent for building data-driven content engines.

Subclass RappterEngine, define your RULES as data, override tick(), and
you have an autonomous content engine that works as a CLI and as a
Brainstem-harnessable agent.

Every engine in the Rappter ecosystem (Zoo Heartbeat, Economy Engine,
Interaction Engine, Academy Engine, Rappterpedia Engine) follows this
pattern. This agent extracts the shared machinery so you can build
your own engine in minutes.

== QUICK START ==

    from rappter_engine_agent import RappterEngine

    class MyEngine(RappterEngine):
        ENGINE_NAME = "My Engine"
        RULES = {
            "post": {
                "weight": 5,
                "templates": ["Hello from {author} in {world}!"],
            },
        }

        def tick(self, state, ctx):
            rule_name, rule = self.pick_weighted(self.RULES)
            text = self.fill(random.choice(rule["templates"]), ctx)
            state.setdefault("items", []).append({"type": rule_name, "text": text})
            return [f"Generated: {text[:60]}"]

    if __name__ == "__main__":
        MyEngine().run()

Operations:
  - run_tick:     Execute one engine tick and return results
  - run_burst:    Execute multiple ticks
  - get_state:    Return current engine state as JSON
  - list_rules:   Show all registered rules
  - describe:     Describe the engine and its capabilities
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/rappter_engine_agent",
    "version": "1.0.1",
    "display_name": "RappterEngine",
    "description": "Provides a base class for rules-as-data content engines \u2014 subclass it, override tick(), and run it as a CLI or brainstem tool.",
    "author": "Kody Wildfeuer",
    "tags": ["engine", "framework", "content", "automation", "rules-as-data", "heartbeat"],
    "category": "devtools",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════

import json
import random
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# RAPPTER ENGINE — the base class
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class RappterEngine(BasicAgent):
    """
    Base class for all Rappter content engines.

    Subclass this and override:
      - ENGINE_NAME: str — display name for your engine
      - RULES: dict — your rules-as-data (weighted rule sets)
      - STATE_FILE: Path — where to persist state (default: engine_state.json)
      - tick(state, ctx) -> list[str] — one generation cycle, returns log lines

    Optional overrides:
      - build_context(state) -> dict — build template context for this tick
      - on_start(state) — called before first tick
      - on_finish(state, all_results) — called after all ticks
      - export(state) -> dict — custom export format
    """

    # ── Override these in your subclass ──────────────────
    ENGINE_NAME = "Rappter Engine"
    RULES = {}  # Your rules-as-data dicts
    STATE_FILE = Path("engine_state.json")
    COMMIT_PATHS = ["."]  # Paths to git add
    GIT_DIR = Path(".")   # Repo root for git operations

    def __init__(self):
        self.name = __manifest__["display_name"]
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "description": "Engine operation",
                        "enum": ["run_tick", "run_burst", "get_state",
                                 "list_rules", "describe"],
                    },
                    "count": {
                        "type": "integer",
                        "description": "Number of ticks for burst mode",
                    },
                },
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)
        self._state = None

    # ── Core Utilities (shared by all engines) ───────────

    @staticmethod
    def now_iso():
        """Current UTC timestamp in ISO format."""
        return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    @staticmethod
    def uid():
        """Generate a short unique ID."""
        return (
            datetime.now(timezone.utc).strftime("%s")
            + "-"
            + f"{random.randint(1000,9999)}"
        )

    @staticmethod
    def pick_weighted(rules):
        """
        Weighted random selection from a rules dict.
        Each rule must have a 'weight' key.
        Returns (rule_name, rule_dict).
        """
        names = list(rules.keys())
        if not names:
            return None, {}
        weights = [rules[n].get("weight", 1) for n in names]
        chosen = random.choices(names, weights=weights, k=1)[0]
        return chosen, rules[chosen]

    @staticmethod
    def fill(template, ctx):
        """
        Fill a template string with context variables.
        Missing keys are left as-is (no crash).
        """
        try:
            return template.format(**ctx)
        except (KeyError, IndexError):
            return template

    @staticmethod
    def load_json(path):
        """Load a JSON file, return empty dict if missing."""
        path = Path(path)
        if not path.exists():
            return {}
        with open(path) as f:
            return json.load(f)

    @staticmethod
    def save_json(path, data):
        """Save data to a JSON file with pretty-printing."""
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

    def pick_from_pool(self, pool, used_key, state):
        """
        Pick an item from a pool, preferring unused items.
        Tracks used items in state[used_key].
        """
        used = state.get(used_key, [])
        unused = [x for x in pool if x not in used]
        if not unused:
            unused = pool  # Wrap around
        choice = random.choice(unused)
        state.setdefault(used_key, []).append(choice)
        return choice

    def fill_from_rule(self, rule, key, ctx):
        """
        Pick a random template from rule[key] and fill it with context.
        """
        templates = rule.get(key, [])
        if not templates:
            return ""
        return self.fill(random.choice(templates), ctx)

    # ── State Management ─────────────────────────────────

    def init_state(self):
        """Load or initialize engine state."""
        if self.STATE_FILE.exists():
            return self.load_json(self.STATE_FILE)
        return {"tick_count": 0, "created": self.now_iso()}

    def save_state(self, state):
        """Persist engine state to disk."""
        self.save_json(self.STATE_FILE, state)

    # ── Lifecycle Hooks (override in subclass) ───────────

    def build_context(self, state):
        """
        Build template context dict for this tick.
        Override to add domain-specific variables.
        """
        return {"tick": state.get("tick_count", 0)}

    def on_start(self, state):
        """Called before the first tick. Override for setup."""
        pass

    def on_finish(self, state, all_results):
        """Called after all ticks. Override for cleanup/export."""
        pass

    def tick(self, state, ctx):
        """
        Execute one generation cycle.
        MUST be overridden by subclass.

        Args:
            state: Mutable state dict (persisted between ticks)
            ctx: Template context dict from build_context()

        Returns:
            list[str]: Log lines describing what was generated
        """
        raise NotImplementedError("Subclass must implement tick()")

    def export(self, state):
        """
        Export engine state for web consumption.
        Override for custom export format.
        """
        return {
            "engine": self.ENGINE_NAME,
            "version": "1.0",
            "exported": self.now_iso(),
            "tick_count": state.get("tick_count", 0),
            "state": state,
        }

    # ── Execution ────────────────────────────────────────

    def run_ticks(self, count=1, dry_run=False):
        """
        Execute one or more ticks.
        Returns (state, all_results).
        """
        state = self.init_state()
        self.on_start(state)
        all_results = []

        for _ in range(count):
            state["tick_count"] = state.get("tick_count", 0) + 1
            ctx = self.build_context(state)
            results = self.tick(state, ctx)
            all_results.extend(results)

        self.on_finish(state, all_results)

        if not dry_run:
            self.save_state(state)

        return state, all_results

    def git_commit(self, results, no_push=False):
        """Commit state changes and optionally push."""
        msg = (
            f"{self.ENGINE_NAME} heartbeat: +{len(results)} items\n\n"
            + "\n".join(results[:50])  # Cap commit message length
        )
        for path in self.COMMIT_PATHS:
            subprocess.run(["git", "add", str(path)], cwd=str(self.GIT_DIR))
        subprocess.run(["git", "commit", "-m", msg], cwd=str(self.GIT_DIR))
        if not no_push:
            subprocess.run(["git", "push"], cwd=str(self.GIT_DIR))

    # ── CLI ──────────────────────────────────────────────

    def run(self, args=None):
        """
        Run the engine from CLI.

        Flags:
          --dry-run    Don't persist state or commit
          --no-push    Persist state but skip git push
          --burst N    Run N ticks (default 1)
          --seed       Alias for --burst 10
          --export     Write export JSON after running
        """
        if args is None:
            args = sys.argv[1:]

        dry_run = "--dry-run" in args
        no_push = "--no-push" in args or dry_run
        do_export = "--export" in args

        burst = 1
        if "--seed" in args:
            burst = 10
        for i, arg in enumerate(args):
            if arg == "--burst" and i + 1 < len(args):
                burst = int(args[i + 1])

        print(f"{'=' * 60}")
        print(f"  {self.ENGINE_NAME}")
        print(f"  {'DRY RUN' if dry_run else 'LIVE'} | burst={burst}")
        print(f"{'=' * 60}")

        state, results = self.run_ticks(count=burst, dry_run=dry_run)

        for r in results:
            print(f"  {r}")

        print(f"\n{'=' * 60}")
        print(f"  Generated: {len(results)} items across {burst} ticks")
        print(f"{'=' * 60}")

        if do_export and not dry_run:
            export_data = self.export(state)
            export_path = self.STATE_FILE.parent / f"{self.STATE_FILE.stem}_export.json"
            self.save_json(export_path, export_data)
            print(f"\n  Exported to {export_path}")

        if not dry_run and not no_push:
            print("\n  Committing...")
            self.git_commit(results, no_push=no_push)
            print("  Done!")
        elif not dry_run and no_push:
            print("\n  State saved (--no-push: skipping git)")

        return state, results

    # ── Agent Harness (perform interface) ────────────────

    def perform(self, **kwargs):
        """BasicAgent-compatible perform() for Brainstem harness."""
        operation = kwargs.get("operation", "describe")
        handlers = {
            "run_tick": self._op_run_tick,
            "run_burst": self._op_run_burst,
            "get_state": self._op_get_state,
            "list_rules": self._op_list_rules,
            "describe": self._op_describe,
        }
        handler = handlers.get(operation)
        if not handler:
            return f"Unknown operation: {operation}. Available: {', '.join(handlers.keys())}"
        return handler(kwargs)

    def _op_run_tick(self, params):
        state, results = self.run_ticks(count=1, dry_run=True)
        return f"Tick {state.get('tick_count', 0)} complete:\n\n" + "\n".join(results)

    def _op_run_burst(self, params):
        count = int(params.get("count", 5))
        state, results = self.run_ticks(count=count, dry_run=True)
        return (
            f"Burst complete: {count} ticks, {len(results)} items generated.\n\n"
            + "\n".join(results[:30])
        )

    def _op_get_state(self, params):
        state = self.init_state()
        return json.dumps(state, indent=2)

    def _op_list_rules(self, params):
        if not self.RULES:
            return "No rules defined. Override RULES in your subclass."
        lines = []
        for name, rule in self.RULES.items():
            weight = rule.get("weight", 1)
            template_count = len(rule.get("templates", []))
            lines.append(f"  {name} (weight={weight}, {template_count} templates)")
        return f"{self.ENGINE_NAME} Rules:\n\n" + "\n".join(lines)

    def _op_describe(self, params):
        return (
            f"{self.ENGINE_NAME}\n"
            f"{'=' * len(self.ENGINE_NAME)}\n\n"
            f"A data-driven content engine built on the Rappter Engine SDK.\n\n"
            f"Rules: {len(self.RULES)}\n"
            f"State file: {self.STATE_FILE}\n\n"
            f"Available operations:\n"
            f"  - run_tick: Execute one generation tick\n"
            f"  - run_burst: Execute multiple ticks (pass count=N)\n"
            f"  - get_state: Return current engine state\n"
            f"  - list_rules: Show all registered rules\n"
            f"  - describe: This message\n\n"
            f"CLI usage:\n"
            f"  python {Path(__file__).name}                 # Single tick\n"
            f"  python {Path(__file__).name} --burst 10      # 10 ticks\n"
            f"  python {Path(__file__).name} --dry-run       # No persistence\n"
            f"  python {Path(__file__).name} --seed          # 10 ticks (alias)\n"
            f"  python {Path(__file__).name} --export        # Write export JSON\n"
        )


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXAMPLE: Minimal engine (also serves as a test)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class ExampleEngine(RappterEngine):
    """
    Minimal example engine for testing and demonstration.
    Generates 'hello world' style content from rules.
    """
    ENGINE_NAME = "Example Engine"
    STATE_FILE = Path("/tmp/example_engine_state.json")
    RULES = {
        "greeting": {
            "weight": 5,
            "templates": [
                "Hello from tick {tick}!",
                "Engine says hi at tick {tick}.",
                "Greetings, world. This is tick {tick}.",
            ],
        },
        "observation": {
            "weight": 3,
            "templates": [
                "Tick {tick}: Everything is running smoothly.",
                "Tick {tick}: The engine hums along.",
                "Tick {tick}: Another cycle, another frame.",
            ],
        },
        "fact": {
            "weight": 2,
            "templates": [
                "Did you know? Rules are data, not code.",
                "Fun fact: Adding new behaviors = adding a dict entry.",
                "The Rappter Engine SDK powers all content engines.",
            ],
        },
    }

    def tick(self, state, ctx):
        results = []
        for _ in range(random.randint(1, 3)):
            rule_name, rule = self.pick_weighted(self.RULES)
            text = self.fill_from_rule(rule, "templates", ctx)
            state.setdefault("items", []).append({
                "type": rule_name, "text": text, "tick": ctx["tick"],
            })
            results.append(f"[{rule_name}] {text}")
        return results


# ── Standalone execution ─────────────────────────────
if __name__ == "__main__":
    engine = ExampleEngine()
    print(engine.perform(operation="describe"))
    print()
    print(engine.perform(operation="run_tick"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/616abObyJbtX1Gf/nDLLdsSk0DuuBEPECAQAiQQU7nCxTwPYoZ6/u8vpXOOXXVvdX96drgKZe7cuXMPa+0M+OPF6bu4al6+vJwqf14ZSe6HQR80Lx9f/KD1mqTukqoE00pTDQkYWjkr12mDlZc7bbsKq2bV9HnQfnLaT77TOSuvKrug7FZBGSUlEP/aw1sIXbW9+7oi6T6uqiFoGqBs1SVe9suHjyun9IGaEkyunMcOtMivgGa3cZKy7YJi1VVV/hnYFExOUYPtXr78+tvHlwQ8v3z54+WpGdh4deq6CxrmuTWQzp0yAsP1DI5Ygt910ACDCzDkB+Hq7dcvbZCHH1f/9V/Z6DRR++HL13L19ufry+Mv5bSJR0bgUJ+8qqidLnHz4MfqD08fUD8sjZ0GHLv9/Lr2p64KLHAevlz9c/W60+co6H75+vJj4uvLR7Djq9fd4OvLh5+LY+CgPGhasPaPn6OvJgK/fXv48evLl9XjKJ+/VfW398GPfyft9k3b/Zv4c/Tf5IGN39rO6YK/yP8Y/Tf5PGm7b8+M+MuCn8P/tuLngf8k/z74J+nv/+YO4I13xzx9+cOTf/JcEq7KqnuX+/LXzZug65tyFX59uZVZWY3lzyh9Wf3x4/n75xU5OEnugLiD8X98XP3jc1ol5S8/ds+Cuf3lw4fvfw74m/I3mV/esuvlO0hbkClN7z1UP7L2P/9zdU68pmqrsFupXtV3j1rokiL4Wn4ttTgBRdOuujgAKkHhtM/0e5WrmyoNnopWVbj6/f9koIY/jZvmtQ6+vdbgN+eRu79/XmlARdUkYMzJV1dSUb6Wz6mH+roJ2qAZAn/lzl3wCeT0p8fDKilXv/+dus/1/PuzbIHAw7Qrza88p25BiD8/zDbioHwz0nPKVTAFXg/U5ZUH9g6TRyKA47RVPgAUeByxzZI8X/lJA85TNfM7JHx5KPv9998B5sRfy9dKRlavwNRuHnn7bs7q0ydwiDBPorj7WgZeXK3+8cf3f6z+7+p/W/VU/thDeYDTq5OBhYIqSysQsL4AYsD/j9p2/KeT//j+5kqgpgRJCEKShEnwujhPyizw3/2qHslPMLZbuQHwJ/BlUVdNl5QRwLnPKz5c/bAXbPqYekBfXLXdyg/qoPSD0puBVgcc54cnH8ncgqxsw/njqm+D566//wDKbx4Q/311ppUnZIL/PHH1IQQWV2UC3P8j6q/jQEnzj/Yngn1eSY80W9UOiHvcOG97hM5rXADYvS8Hyp1VGYxfywcQBw9XPevl1T1ACHjGewvpp0fMATkUBQhs+773UwbAiL/SKgds3nwt27d8dppHKLwHVcyrqE98p/SC/35LqTau+tx/+g9Y+tD0FgX/LSrPHHyjg9UrH6yeEP7OR9TjXK8HeeC32wPie0TmwWGf/CYZQPr+C5U9darvPPYXrvkIIhY+9pirvlldbyKjPojsoezv2e5rCSQBNoDsB9UBOLgqq6Lq23/Z8xn91Vg1WfuTGB+V8fjxtfwRs09vrPNAqNdTPY1lns57U/VeqG9OAa5t5ydj/WJX1eoYOE3nBg5gZ8Z7GDO/uQ0gMA9MapzXsLyfl/QcP/gp9K62DvzEeRt8MGOeV2P7LHBQvE4HJJ7ZAer91ffB1D00vxZPC04BIlg4XgyWA8vb6uHQJ4A8A/T0WrN6APXPQxVJCZDlNTr//OfqcuPp00rVyKu2+uc/H4MPMA6bqlj9HY69FeVfw/m+6jXS5/l19Je/yPy5T2AkjpeYbxJ5ZgAnfX05v/vlz3zwmhV/Q+B19crG/zLxOjkGTzwD09jHv5sHAaxzUEFPuv3168sxAC5/Pe4fr63d94eT/gA5lPvf/+Pry2//oub7Xyn2549Hi/TM2Nf+6JXuV143ffhXFgWY/610CjD7eARHfNJ4DdZ+ezU/8J9KPj9d8OGvqzuQAu9LAEbkvzQgv6viM8DvxAt+eWj89S/H/O3DqxV/VfM073MbdMBsp88fjVUCFrWPpurX3z58BqEDiPrLH0DVXD97jT+Z/dA/PZ38+P/3D3/bJfwK2gTuHa9AtB6iv37ZbX8DrP/bu+NAu/HtqfTbN5B9QPG3bwWo0W/fgPKfWn9k1IfPAK5++fBYLb93G+1T8NPqvYX78ppibwRagaR/xwYw+UqTrwYCOgUHb3+ufnZ0X/68ugACCYDq59o3yR+93FPy+qrL65vmTzD0nH+AzoMXX5f97Oge69S4GlcOIPAmiJIHkD+R+NEFPoXf27nXsxzefj2L/m2HZysBcAD0EI6b5EkHGPXRwYMcAJTw8qXs8/zjy8Ozf9PnP6iqCMBI+7gNgKYI+PKp4HE3qEAv9Xj463VG6gsXoGD1muPtGwkAf62Kyn/ofKQJkAMsF0TgOgTath/94L9re2OYnxLgplL24KLx64/2HAz9iAl4/uH15yHfXfnj1uUGoFDfbQDdIqCml+/Ahia494BP/Yfmn7v9FK3cRz/4sPZRLq+XnT9egG+cBxe9eeetZQTijdN8ah+MuoE+bx8WOs0rLIK5/62ZfBMFgA3aGyCL+hgCO9stjIcQCqMYBPkYDjkh+OkRAQL5cOjiiBd6260LbRF460PQPtijPhhAYfjhhBYguxd8e3QIyWN719uG0G4PEWEQ7F0YRnZbItiGyH6Hh84uQODAJ7ZA3c+lWVL6b2d6NfLhsB997ePsb0f748XdoUDyiLY8+fqH3qx1D0dEVz2Km+UeWJNti5EQMLWEtKZ1M7HcgW29R7L7xHupjRuxdSIrK9OTAzlZtBGQ9wHv0Oi4WEPArFW8RjcFyVKq6eqCySVenmVbSdG2e0Uj1kPPmYiwGdzGXJOhvBCoDEtQ3i2jka7vNpZH2byUhyN+zJJTQNz5oG3ECD/axnjvD/xs9206lcaNVRbIhRp6rgwnspTwPuznG140lN47ixXlHl20YRLfQzSWbvlMtKitl76NcNM44MStO7MiX4hKafvL3MiFk2KXaKYQE+fN/DrpLX2Qw3NJnFDFFXgUxyWsFGccPiBy0ps+vo8Uw+aMDhb5sInQQ3a6WblrJutjL8ZHRc0ZJcQHBN4gPmdtlqB11SzqjPyg83yBYbGGXDX81HqpYyV8lzrJmhxvsN1EDoJqamMTQ3OmO+SOJBN3ohjPxhcn9/d0a5w3Wo+n7e0cHLd+2/i54h2m/Z1x9ZKL7reDzw84iQdZdaEHKD34KUKxs13R0SLJSv5w+HEyuw7faw2aWUYXXN3ZsiND2XEwaogsNYc7goPwxi19Nr9SHXSY1FK0x+wo+FE/ssOus89V10i9T4/H3lNx63YWxx0lCsNlcIKhoiHRTK+Kxu6pxh73PZ5k/Va9I63CsdernsxGp/mZGSccMtRIfepP4obXjVSwkjFwTFtlUQqH9we+94vaEC+9kSsSZp5Ueq1xOOb76sDLKaqErXaxFottq5bSTigjwFTPK0foOEZ441MaF/Rsug43eBPYuCljgWOhQSabDlkU0mZN9APO3M7eFnhY6QdYuc3zXm4Lkd82vUQZ7dFD/dGQrgLfWf0I4Z1lJj4mgv4qpE1XyQaMkkrNFdYbZdkR5NFnmvPBUQb6PueCXHa8sqWB6eZVO0NzbImbqU12opej/dXpDmcqGWu/n/v4yIuFNaToepRMpC6sG1GcdT0KhljOvZTMGAUAs45lipwWvc3d9qfWFnq82uezj80elZoKaQ+BnUQC3eeNiQ/0Wa3RuyaPxwa6kWtVlm9SGjg7lMuMO+pRfX3xSvqCVRKaNBUX0Rwj2URTn9lUmNnkYpECR4qoi8jj2agUr0qux/Teu8LdPiYJNNBwx3jI4SjdkJNz1tZYiFzn9caeApNaqzc3Nav9nkq0ez0vTW0e2qFIGq5GDsXNld2sPG3Ksz8ntGWt65JQNGkblPH+WI9eFnPLcbhyw+E8aSrNuC2SLtQRJigzSrxU6W9It8zuoTn4+w1Ajg1t0sjMMZaI79ZEN823E+ojB8JaTrsWOvWXQKR1BWAuamHhoR+KHV4XiiUeVT4yFQFBRrWl1wsm7pa4Kja5JpaMzyp8YK4pjotJhKY0VarPIyFc0fig5SMHyKVlbyLM2/MwiosY+PE56ZdYGXjiXDnIIbkwaUSoonAhqCpLa8AIZmt3FBWUECxFE1kkVFCH641+H29HXE+ToItw5SyEDuaXU9DlukuDS13ARQRLUXN+pmMhOJjrRYIw3NoVlXvmEzS2WYt1z8mOx0Sxqoi48jm9FS5dJG9OBzPAfTJtqIxieckTAv4mSQdHqxGF5HAhoNN8KYj6aHQTf/Kp1qo1WWnsi47newg99Ovlqu5cteXrZpZU9soF6nY35noAgOKI7A7I2lOOfc42eeFEKSSUpB0HC1Fb1BiRQj3QNLo7ZflWdb2avcGu2UYipCJwRJ02KBpHi+FT/ID2bbusq3Nx583pjtyVzSYlNtsjEcs3xYyX4NgIWoTJKYSGZHUgw+Cqq0HSo6U07vnL5lY6+1tcMfrWXSdQGNs7gu6UbVKM9Ho6G5EpRGUWF+GEJi59mk42gGu8LNWdmaCBcugu25jbEidDMA42f8hHWgkhYrloKE0ZWQCulJx+uCoOeqeMQ7trCFJoe7xuzF6SxAlFceVabnnKOiAC7hrLgjthCSEDujmfjkhgjXFf2uNYYjYSLGJCs+c1S5v2FbvPjipe79yamiByI9Alg+NZbmLhBCk1hGcOo5wL9jLqEoITVaYx6RjpWH91CaFdmHIct0uPIdGJoCiX6E6TAR+Hk7KjvMsQ4vNy4gS3ohHiKvQlP8823y6DiSfDel7OpDnq0/6ilNy1UyqvLK42V23WEVr61/BW0vr9UrHbjZ+5IbOhYoGg+vWgeMNGRQjqxOaGTSrWrEFOcp3aRSOLoV1K02CkDb4oIHSbaKPefOsk2WUONW2qoHDfU8gUwQxjc9cdl5tbZE/GxLWWkalHAWOUNgPoo7nfZ469UzXNezLJRxF+ziNFbS+8Ekqys0+7U2QwJ0o60nlEBPKw2MGOvx6qdIHmjbtZ7zVlX2+WNRZwWFQuGVEejw62nLAFIc3MQ9ElLKpiJPcAHTaeANWXSPdZeuLULian83BTLXrj2HDd3VEK8PIxEpj7LT3OfaDVOhuyJMtjdyvnPTTe0tZcJ2cHwjc4d5dOe7Iab5FaKN5FzNHwuttJ6Y6KzWPKYeXl2I/XUb328BjPww2jB1TWr7QqknpVShXH1CRyo2ppiMsoj83zaZy8W2hJmGExqHy3BRO0QqPQRIWRQ3JEbXSQbXCKq4uc+gJTLSbNXtl64+yMUBeQa5wz40FF7equ+kyhRS7vuMXtevMx/rzlOdpwfPI8jQ4pLBnJ8IgRMTeDKOyy4bc0paKSHjO3zeXSUY7E7vSDEvnBve1RW84jAZIZ53Bu5dZWdxdFHkoKqUu/8PmGIZMrZ0f+hpI1kNdxWXdiRg/0dMwbVi6P2kVheC+7SnuL23NxPzR+rNa7bW2Hg5btZPEuLxHRI7OynGh8OxGtb5AFtCQdmWpWiR50ei2nFaIx54FXYI/YmsK9Od1AZDs1lm2VgnqX5IwZD/3hguybfESlHuvgUXAyh6Bd1Om4nQyjbN9c1p1/wl2ITVlasCN9e4WMO364nHb7DVblXJHsjnSnq+pCL7PFVql8grM0Ad1AoyRFfrShntvtylaXFIncQlhrjxouCVNtqfQpWxhxtm4hT0njjhBIl+sOg+gkPcYLaexlpWBDzEbTIkd2uCbCIeXm4XfPJOTdCTa5yz1hjuE9Dey852DjWFOwIp1rSXVMiTrMt8vCGMN4nROl9wVVlWBoK0Vux2OyRjJp1vk+gHdRNnfcEEJzjdoNdkpvLJMEmOY6OIVuMakdtnJAVGrGSUZduAK71rucL9UOsvBeMsxTHo6bgc8t/VrJ+TqSF3gXnDzCO8VTJOiHrUfC1Gm3nho3brMdzQguRQkbFGnOIUVsiggOa8yVkRH2SvDPDMfrcY/SzDxPneqEi0RRXXIte9prkzVsCrDPNeKdJezNKRDu4ohQy1UnRjc4bUtmvQ9s9zCyUzIP+Brp9uHmugGZGD1QRVrOcLAlpDkuWmLDyTEdOuLkCYWYmxyFcHkVj4ULcaq30JpReOfgXotnl/Hh/iz169M9VvRgHGEiX6tCxlmqf0k4nZQ6tpu5/IByJcFLXLAvmFsiMHKwnPrd0d/DR1GS15l/TuEkjwM2OF8GIRnanbDv4g0I4ebC8/nUbpishcSR7KrdfDNjBspDYtrVCALB532lNIPLuTYA9tOFngSTkEqs4pMCXFtYXUb0+309QlDapFTVCLh19O2KRCV1wRnWs4WBYquNoWlkkgEmnAmSb7FJOsvkSA5KDpp+/s42566FL8ksWVF3mWNTOqyJtS8Puc5mIY6EzG2yBcK/ONfNFVsfqClb13TUapnDu+V89vNtfjTkWLo7jEDd7tLVLkbRD9Qbye9T1ezLgyGnolbxntWN28sRdYlDNOlrCVHh2eFblNUvRCYyS68tqYVmFH3EGCIwZd+KOIhDjKDLqJrzKrbJ9qTKH2qRgk4GFV7NZrTEVjB3u5tcni/nakyay4Z2pVO+XzOOIjpR6QimzmAXaH9wnfOxPJCNH+RkXON9PQ4hW7pFQcbKxYSr3fpQ9kO8ZXQ2wcWzbqCUsnEmve44S6LvqEjlo70I8SE9XMUN7Lv8/sQZtEetjckVSDu7pqLdiCdAzVtxouMtuzeDYj3tITGu72ddzKjyRqS7vYFube3Opot+NItMXo9kfJObfpbxeRcVpYW7+yRx+7iCcD5iUZ4M72VE3Sck0rkalxWqci+bcsYto+diU63H6449geqatv1hjyJHmSiwifH5+M4MbFpOxyMeYPJS40HHL2a2vqGNkkZHluwt5nS8cM2RgfHJxmsuZirymF4pDpHTPTfz8j4chLyx9Bqdw+PVniv9zqJaovV8Ug48ltvmhoMbxy5R3utO524+I7huUjKgnGSjtNp+rEmtWFPClaOLlN6i/l6IGURsEN1vZXBJRRhc4OTDxhorHZoaMbEd9nDYmqbi27i0OzT+ZJenZUlZMaQzRtgEMi2DeyEoD0GwCBiX8JRjSkz1LWMjMul8cncVuWOpm9cfhQu1HKFzY7lUb6zDOZFR9mDsTtpkFIYmnMWTxuzHM22hu9FKSF1ps8LwT9z5MFzaepzLaRPTwSTi7nkd3BMb6jiIETGIYQpbKeCrCp+TszWKZafP2y6t4vKMbec26419L9S7XW+MBfCYN84mN5nycnIloFrbGyLuu3BpBn4rKmOZDuKMUWetoSioreOycYbzqTCP+4umD71G6biGWdAxnC9YtuFQMCsEBTH0JpnzbjelXrSuKd/PW7MvGtPkpUCG67HWWHtJGBzK8rOpMUXLdEfjQl21o0kNfkuj22lMyM2dx2hxoGuFNpFdmWX5DZq1XRjcT7Jvrxm5ZK9737K8eQgilDlceLn1dTY6kYcMc6ZNlbTrkr9pO6Ip792V3OWMfTO740lqrqppTHZnay0Bm/BRgpGrrGPomhD6zhZqQdIjdJoFz3ZVWOLWG8KTA6y0ITibqstMTqnrUCMVNJeDyJ4U01NxlIGsTlM470g5WHqGo95TEJ9Zb7QhvGzYFPeTtgPxpgrMN8AlA58I6HSl+7N3IGjkIOZKtd3uFFLVN1abTvAFxrDNPjZdF28F0azN2eFYRlRvV2ndx2myhe4R6e5VXhNvRjB1O1jHip1oUiXW5Gl3z1O1aI/+mpPigeBw2RkbLTa8/VmebDZy/L4idHURm3aX3MAd27ksR9rQKf2sm+7MejK81OjCQsqlEga6KFPEVdeTfXc9Bb6GSOBderjIG86sCEiZbvujbB3L8aTM2EIuExQe3MHkSGeT5RSFzaC9QUWN9qH03DSw7h4jIy4uJ8ZvjaQ2O004eYdb7gWOIMrnu1rH6x2WxceW45ZMipHYh0/VPa4No8hcfs6WMG7OqLm/IGuZ8Pn6pHWIRjH2yV2GRo9xMBxvtkHuTUt7X6Nb6maNI4OHLGujA73pWhZmaE4wWFXHy/bSnahIssLLmeCs83FiKoLvt8bNPJq1lM8AxnLyqIutIx3CBm4JxyWjqjZVmd9mk0HeZqS5q5W8Y3jQqxGe1zKgzcnGHESloYVKHDr8cEec7ZwJBsE627olaiPKCv56ZSOqlfPbEapMZ7KV9M4dzEFOJZpZn2LlMI17c71VxGouu7jzmQo0Cmx8h53jadwa2yLvuKC6nYuTBuKVShf+zpcEuCBDPsvbPNyK0YlFb2XAIRQsO65YynxwPpCza4nwiRHWSqoPbra/gGsodLutj8INVdEDzm4uUXiDvKXnAASoR4F1PcfQd+GtuKx7D/QrI7ZbkPXcgTrahG1p1UXYCV2H+SGaysh+01eSukPLBFUUexmO12HC+0ZhDSqqoP7uh6Yxejd9JrfcfgAN1iW70lxxsMYr6OvMQ3xhrvMlZWffUOW6lHAowdan63TNS8zsYA6zSvaSo8czFDSZV+7GA3QqpluqUo3dYzWf3wo7v2HXEXR2gkH7ElxlSnHtih7WQeOMJBd3t2WyxsREm6azqDYUBHLHO7UcSvTuKySlRHmyN/sm0Nsmj3dnM20Q0Su8gBm8i1GmZ27Ru1s80gTUgssW1G+7Od2Puw0hJDO47nHXtaHtXPl2bGsC3YocdlpMmEZphWeR3CGxilzatXnqJ2jAjBtPV/wkZMqGFDZJTIbtFvel6TZ1pbcOkf0MD9QJ3azdG0RSNxqSbUufe4NodrqpHDQWcTyBDk/a+nD3qkBgHGSJdIsN6+IQUVadlm0JbtJiO9okuEVd+1uybTe7YqepJO5Xtb+fErtNqdiZAj9Kugy1DEmTtsQu5SVPdjZwex/n4RqtDxBSRc21yF2HXF99x0bsCcVRcG0p1k6huBHuLaXvRbLSXu00ycxAxDV7aVXN7ntdY7cDaKNPYx0WFgaRbeAw0LYd9XPXldnetYIxymdk4M6cjxbYOmyLjdTVY0P4c9/GSj5kg2wfkni34ytL3no507W5jEg6J+r7031vUxjuU4RwTGuFCDmjxcOyprwzd067rcbgurh3W0QS5IauCUst4cWGbqlRVvN9rVCyiY6aQZm8yJzALZRBWI7xsNDqUlxPirTHERVQFSaGvkPiTZHr4CJxrKimxCuRA3cAnSZzsZgjK9/W2xT0zZda2AeIE81LABO3cA3H5I7YXTUu5+Aeq+wMXrDGukLWjtZjS0t3u/slzkE7cl2a2/oKdsxx5BaK42AjzuxWObjIOjOe9um+5ABJn9A5uzNQ5jd71x44UQORMgY3ibbOZTagu6VAdZcrA38+Nlmsbpu4qM0hvAlQ3yMpFPope6NruskODZ8Xx4biYYvPiVmq0UbvDPzxbQO6OWiaiOSdYywHeI1I2A3xj/fhTrIWedGgvYCVF9c3T6NokhsP6evegTYpXN6FO97V3q4X3SK4L8zaPKdc3nqqWV5rb2YGYo9cCt6qx+zOVzS47jnhnphVlMTUEtCHighFaiIyqZ3CSjPYzKZhAXIibE3MYlwSh8ucntE2ZTZTcz0QZNY25oXJYI8x0kwo4HBc+2tMVmYkws6LIlw3ZDdEiuSWx5w7VJW6r4aGhCyoIkQfIo6bhGrd2LSWC8Zz4rTU6pm5X8XbTB+ygQbXlnO5kJy6ybyB3XaD7bWaHJFmQ/ucv43reDjIa8rW0wxputGDWIo97KFht6gE00XYAdTYdISRspDy3EhSNwgBKu3FYC+fAEmJU10mjRbkiD6oxezvG2PQfFmBj8M+DPcsJORLZ9BCQGuuaLCLK3qnni3Wt/6YRoxg3MWmb+gBNvLOiq11T7a6H1RojpSLP1yHjTShyLqNmUOXlMQDLg/MlhVYtdZot7D1UiFysyQFBM63UBCILrMw+wCNCmjCKp+UHA/Vt3EQtLmeb+quP2v+RaZCBSZvDb6WTwYx99cQgCKPbzw181lBRYrdwWan290hPJgeLG9PWgZ1O4VInPAiqOx2nSz7TLiZSWuOrYvSZNfX9wTm8ewquLnoWdtA4pAGc/ZOUkAZsWl78sY24Y31u2M5DG2xPgxr3aMbTiqJlrbJfbUhLgTjilun7W8DNai2Et0OR6+id62TR2f8bk/ntSltXaTvp41ypncEEo20ugSDK7SJyEqW4W6kNdZ2GI5xhHfnbgDYoIsXR3Ot+sKlRupzTuG2bNxd5V52mlGf4BQ3MUyn9t2iRiT58vHl8cXU2wvv/+ELvMe7z/9vr2Bf35ZWA9iz9ILnq+vA8b889/ryPxnw28eXxkvA9q/vj9u8j95ewb6+Pf70tvBT8P6u/vWjo2/P75ym7v3FfudEj296X36IhY83+o8Pn8Dz2zdR4OkBJsX7G/a/fHcMfsfvnzA9rHp+KPl8xw0s+wy9fP9/SMbfEeosAAA= -->
