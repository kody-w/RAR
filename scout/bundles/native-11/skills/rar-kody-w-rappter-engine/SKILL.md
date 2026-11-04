---
name: "rar-kody-w-rappter-engine"
description: "Provides a base class for rules-as-data content engines \u2014 subclass it, override tick(), and run it as a CLI or brainstem tool."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rappter_engine_agent", "rar_sha256": "4d532a0027f1424511d571af7f1c8e31d2fb73cfc00b10320d119e94dc00422e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["engine", "framework", "content", "automation", "rules-as-data", "heartbeat"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/6166ZebyJLvv6Kp+XDbI9sSm0Cec895gACBECCB2Np93Oz7Inbo5//9pVRVdve9PfPpVZ2yITMyMjKWX0Sc5I8Xp+/iqnn58nKq/HllJLkfBn3QvHx88YPWa5K6S6oSTCtNNSRgaOWsXKcNVl7utO0qrJpV0+dB+8lpP/lO56y8quyCslsFZZSUgPxrD28hdNX27uuKpPu4qoagaQCzVZd42S8fPq6c0gdsSjC5ch470CK/ApzdxknKtguKVVdV+WcgUzA5RQ22e/ny628fXxLw/PLlj5cnZyDj1anrLmiY59aAOnfKCAzXMzhiCd7roAECF2DID8LV29svbZCHH1f/9V/Z6DRR++HL13L19vP15fFLOW3ikRE41CevKmqnS9w8+LH6w1MH1A9JY6cBx24/v679yasCC5yHLlf/XL3u9DkKul++vvyY+PryEez4qnU3+Pry4efiGCgoD5oWrP3j5+iriEBv3x56/PryZfU4yudvVf3tffDj31G7fdN2/0b+HP03eiDjt7ZzuuAv9D9G/40+T9ru29Mj/rLg5/C/rfh54D/Rvw/+ifr7v6kDaONdMU9d/tDknzSXhKuy6t7pvvx18ybo+qZchV9fbmVWVmP500pfVn/8eP7+eUUOTpI7wO5g/B8fV//4nFZJ+cuP3bNgbn/58OH7nw3+xvyN5pc373r5DtwWeErTew/WD6/9z/9cnROvqdoq7FaqV/XdIxa6pAi+ll9LLU5A0LSrLg4ASxA47dP9XunqpkqDJ6NVFa5+/z8ZiOFP46Z5jYNvrzH4zXn47u+fVxpgUTUJGHPy1ZVUlK/lc+rBvm6CNmiGwF+5cxd8Aj796fGwSsrV73/H7nM9//4MW0DwEO1K8yvPqVtg4s8PsY04KN+E9JxyFUyB1wN2eeWBvcPk4QjgOG2VDwAFHkdssyTPV37SgPNUzfwOCV8ezH7//XeAOfHX8jWSkdUrMLWbh9++i7P69AkcIsyTKO6+loEXV6t//PH9H6v/u/rfVj2ZP/ZQHuD0qmQgoaDK0goYrC8AGdD/I7Yd/6nkP76/qRKwKYETApMkYRK8Ls6TMgv8d72qR/ITjO1WbgD0CXRZ1FXTJWUEcO7zig9XP+QFmz6mHtAXV2238oM6KP2g9GbA1QHH+aHJhzO3wCvbcP646tvguevvP4DymwfIf1+daeUJmeCfJ64+iMDiqkyA+n9Y/XUcMGn+0f5EsM8r6eFmq9oBdo8b522P0Hm1CwC79+WAubMqg/Fr+QDi4KGqZ7y8qgcQAc14byb99LA5SA5FAQzbvu/9pAEw4q+0ygGbN1/L9s2fneZhCu+RKuZV1Ce+U3rBf7+5VBtXfe4/9QckfXB6s4L/ZpWnD76lg9VrPlg9Ifw9H1GPc70e5IHfbg8S38Myjxz2yW+SAbjvv6SyJ0/1PY/9Jdd8BBYLH3vMVd+srjeRUR+J7MHs77Pd1xJQAmwA3g+iA+TgqqyKqm//Zc+n9Vdj1WTtz8T4iIzHy9fyh80+vWWdB0K9nuopLPNU3hur90B9UwpQbTs/M9YvdlWtjoHTdG7ggOzMeA9h5je1AQTmgUiN82qW9/OSnuMHP4ne2daBnzhvg4/MmOfV2D4DHASv0wGKp3eAeH/VfTB1D86vwdOCUwALFo4Xg+VA8rZ6KPQJIE8DPbXWrB5A/fNQRVICZHm1zj//ubrcePq0UjXyqq3++c/H4AOMw6YqVn+HY29B+Vdzvq96tfR5fh395S80f64TGInjJeabRJ4ZkJO+vpzf9fLnfPDqFX+TwOvqNRv/y8Tr5Bg88QxMYx//bh4YsM5BBD3T7a9fX44BUPnrcf94Le2+P5T0B/Ch3P/+H19ffvsXNt//mmJ/vjxKpKfHvtZHr+l+5XXTh3/NogDzv5VOAWYfj+CIzzReg7XfXsUP/CeTz08VfPjr6g64wPsSgBH5Lw3w76r4DPA78YJfHhx//csxf/vwKsVf2TzF+9wGHRDb6fNHYZWARe2jqPr1tw+fgekAov7yB2A1189a409iP/hPTyU//v/+4W+rhF9BmcC94xWw1oP01y+77W8g6//2rjhQbnx7Mv32DXgfYPztWwFi9Ns3wPwn1x8e9eEzgKtfPjxWy+/VRvsk/LR6L+G+vLrYWwKtgNO/YwOYfE2TrwKCdAoO3v5c/azovvx5dQEIEgDVz7VvlD9quSfl9ZWX1zfNn2DoOf8AnUdefF32s6J7rFPjalw5IIE3QZQ8gPyJxI8q8En8Xs69nuXw9vYM+rcdnqUEwAFQQzhukicdyKiPCh74AEgJL1/KPs8/vjw0+zd1/iNVFQEYaR/dACiKgC6fDB69QQVqqcfDX9sZqS9cgILVq4+3b0kA6GtVVP6D58NNAB3IckEE2iFQtv2oB/+d21uG+UkBOpWyB43Grz/KczD0wybg+YfWn4d8V+WPrssNQKC+ywCqRZCaXr4DGZrg3oN86j84/9ztJ2nlPurBh7SPcHltdv54AbpxHrnoTTtvJSMgb5zmU/vIqBvo8/YhodO8wiKY+9+KyTdSANigvAG0qI8hsLPdwngIoTCKQZCP4ZATglePCBDIh0MXR7zQ225daIvAWx+C9sEe9cEACsMPJbQA2b3g26NCSB7bP5IeOPWnrgn+NA2G/De5XwV5KOVH7fo435v4f7y4OxRQHtGWJ19/6M1a93BEdNWjuFnugTXZthgJAVNLSGtaNxPLHdjWeyS7T7yX2rgRWyeysjI9OZCTRRsBeR/wDo2OizUEzFrFa3RTkCylmq4umFzi5Vm2lRRtu1c0Yj30nIkIm8FtzDUZyguByrAE5d0yGun6bmN5lM1LeTjixyw5BcSdD9pGjPCjbYz3/sDPdt+mU2ncWGWBXKih58pwIksJ78N+vuFFQ+m9s1hR7tFFGybxPURj6ZbPRIvaeunbCDeNA07cujMr8oWolLa/zI1cOCl2iWYKMXHezK+T3tIHOTyXxAlVXIFHcVzCSnHG4QMiJ73p4/tIMWzO6GCRD5sIPWSnm5W7ZrI+9mJ8VNScUUJ8QOAN4nPWZglaV82izsgPOs8XGBZryFXDT62XOlbCd6mTrMnxBttN5CCopjY2MTRnukPuSDJxJ4rxbHxxcn9Pt8Z5o/V42t7OwXHrt42fK95h2t8ZVy+56H47+PyAk3iQVRd6gNKDnyIUO9sVHS2SrOQPhR8ns+vwvdagmWV0wdWdLTsylB0Ho4bIUnO4IzgIb9zSZ/Mr1UGHSS1Fe8yOgh/1IzvsOvtcdY3U+/R47D0Vt25ncdxRojBcBicYKhoSzfSqaOyeauxx3+NJ1m/VO9IqHHu96slsdJqfmXHCIUON1Kf+JG543UgFKxkDx7RVFqVweH/ge7+oDfHSG7kiYeZJpdcah2O+rw68nKJK2GoXa7HYtmop7YQyAkz1vHKEjmOENz6lcUHPputwgzeBjZsyFjgWGmSy6ZBFIW3WRD/gzO3sbYGGlX6Alds87+W2EPlt00uU0R491B8N6SrwndWPEN5ZZuJjIqihQtp0lWzAKKnUXGG9UZYdQR59pjkfHGWg73MuyGXHK1saiG5etTM0x5a4mdpkJ3o52l+d7nCmkrH2+7mPj7xYWEOKrkfJROrCuhHFWdejYIjl3EvJjFEA+OpYpshp0dvcbX9qbaHHq30++9jsUampkPYQ2Ekk0H3emPhAn9UavWvyeGygG7lWZfkmpYGzQ7nMuKMe1dcXr6QvWCWhSVNxEc0xkk009ZlNhZlNLhYpcKSIuog8no1K8arkekzvvSvc7WOSQAMNd4yHHI7SDTk5Z22Nhch1Xm/sKTCptXpzU7Pa76lEu9fz0tTmoR2KpOFq5FDcXNnNytOmPPtzQlvWui4JRZO2QRnvj/XoZTG3HIcrNxzOk6bSjNsi6UIdYYIyo8RLlf6GdMvsHpqDv98A5NjQJo3MHGOJ+G5NdNN8O6E+ciCs5bRroVN/CURaVwCuohYWHvqh2OF1oVjiUeUjUxEQZFRber1g4m6Jq2KTa2LJ+KzCB+aa4riYRGhKU6X6PBLCFY0PWj5yIIG07E2EeXseRnERAz8+J/0SKwNPnCsHOSQXJo0IVRQuBFVlaQ1Q32ztjqKCEoKlaCKLhArqcL3R7+PtiOtpEnQRrpyF0MH8cgq6XHdp0LgFXESwFDXnZzoWgoO5XiQIw61dUblnPkFjm7VY95zseEwUq4qIK5/TW+HSRfLmdDAD3CfThsoolpc8IeBvknRwtBpRSA4XAjrNl4Koj0Y38Sefaq1ak5XGvuh4vofQQ79erurOVVu+bmZJZa9coG53Y64HACiOyO6ArD3l2OdskxdOlEJCSdpxsBC1RY0RKdQDTaO7U5ZvVder2Rvsmm0kQioCR9Rpg6JxtBg+xQ9o37bLujoXd96c7shd2WxSYrM9ErF8U8x4CY6NoEWYnEJoSFYHMgyuuhokPVpK456/bG6ls7/FFaNv3XUChbG9I+hO2SbFSK+nsxGZQlRmcRFOaOLSp+lkA7jGy1LdmQkaKIfuso25LXEyBONg84d8pJUQIpaLhtKUkQWgbeT0w1Vx0DtlHNpdQ5BC2+N1Y/aSJE4oiivXcstT1gERcNdYFtwJSwgZ0M35dEQCa4z70h7HErORYBETmj2vWdq0r9h9dlTxeufW1ASRG4EuGRzPchMLJ0ipITxzGOVcsJdRlxCcqDKNScdIx/qrSwjtwpTjuF16DIlOBEW5RHeaDPg4nJQd5V2GEJ+XEye4FY0QV6Ev+Xm2+XYZTDwZ1vNyJs1Rn/YXpeSunVJ5ZXG1uWqzjtDSv4a3ktbvl4rdbvzMDZkNFQsE1a8HxRs2KkJQJzY3bFKxZg1ykuvULhpZDO1SmgYjbfBFAabbRBv15lsnyS5zqGlTBYX7nkKmCGYYm7vuuNzcInsyJq61jEw9CjJGaTMgfTT3+8yxd6qmeU8m+SjCz3mkqO2FV0JJdvZpd4oM5kRJRzqPiEAeFjvY8ddDlS7QvHE3672m7OvNssYCDovKJSPK49HBlhO2IKSZeSi6hEVVjOQeoMPGE6D6Euk+S0+c2sXkdB5uqkVvHBuuuztKgbx8jATmfkuPcx9otc6GLMny2N3KeQ+Nt7Q118nZgfANzt2l056sxlukFop3EXM0vO52UrqjYvOYclh5OfbjdVSvPTzG83DD6AGV9SutiqRelVLFMTWJ3KhaGuIyymPzfBon7xZaEmZYDCrfbcEEpdAoNFFh5JAcURsdeBuc4uoip77AVItJs1e23jg7I9QF5BrnzHhQUbu6qz5TaJHLO25xu958jD9veY42HJ88T6NDCktGMjxiRMzNIAq7bPgtTamopMfMbXO5dJQjsTv9oER+cG971JbzSIBkxjmcW7m11d1FkYeSQurSL3y+YcjkytmRv6FkDfh1XNadmNEDPR3zhpXLo3ZRGN7LrtLe4vZc3A+NH6v1blvb4aBlO1m8y0tE9MisLCca305E6xtkAS1JR6aaVaIHnV7LaYVozHngFdgjtqZwb043YNlOjWVbpaDeJTljxkN/uCD7Jh9Rqcc6eBSczCFoF3U6bifDKNs3l3Xnn3AXYlOWFuxI314h444fLqfdfoNVOVckuyPd6aq60MtssVUqn+AsTUA10ChJkR9tqOd2u7LVJUUitxDW2qOGS8JUWyp9yhZGnK1byFPSuCME0uW6wyA6SY/xQhp7WSnYELPRtMiRHa6JcEi5efjdMwl5d4JN7nJPmGN4TwM77znYONYUrEjnWlIdU6IO8+2yMMYwXudE6X1BVSUY2kqR2/GYrJFMmnW+D+BdlM0dN4TQXKN2g53SG8skAaa5Dk6hW0xqh60cEJWacZJRF67ArvUu50u1gyy8lwzzlIfjZuBzS79Wcr6O5AXeBSeP8E7xFAn6YeuRMHXarafGjdtsRzOCS1HCBkWac0gRmyKCwxpzZWSEvRL8meF4Pe5RmpnnqVOdcJEoqkuuZU97bbKGTQH2uUa8s4S9OQXCXRwRarnqxOgGp23JrPeB7R5GdkrmAV8j3T7cXDfAE6MHqkjLGQ62hDTHRUtsODmmQ0ecPKEQc5OjEC6v4rFwIU71FlozCu8c3Gvx7DI+3J+lfn26x4oejCNM5GtVyDhL9S8Jp5NSx3Yzlx9QriR4iQv2BXNLBEYOllO/O/p7+ChK8jrzzymc5HHABufLICRDuxP2XbwBJtxceD6f2g2TtZA4kl21m29mzEB5SEy7GkEg+LyvlGZwOdcGwH660JNgElKJVXxSgLaF1WVEv9/XIwSlTUpVjYBbR9+uSFRSF5xhPVsYKLbaGJpGJhnIhDNB8i02SWeZHMlByUHRz9/Z5ty18CWZJSvqLnNsSoc1sfblIdfZLMSRkLlNtkD4F+e6uWLrAzVl65qOWi1zeLecz36+zY+GHEt3hxGo21262sUo+oF6I/l9qpp9eTDkVNQq3rO6cXs5oi5xiCZ9LSEqPDt8i7L6hchEZum1JbXQjKKPGEMEpuxbEQdxiBF0GVVzXsU22Z5U+UMtUtDJoMKr2YyW2ArmbneTy/PlXI1Jc9nQrnTK92vGUUQnKh3B1BnsAu0PrnM+lgey8YOcjGu8r8chZEu3KMhYuZhwtVsfyn6It4zOJrh41g2UUjbOpNcdZ0n0HRWpfLQXIT6kh6u4gX2X3584g/aotTG5Amln11S0G/EEUvNWnOh4y+7NoFhPe0iM6/tZFzOqvBHpbm+gW1u7s+miH80ik9cjGd/kpp9lfN5FRWnh7j5J3D6uIJyPWJQnw3sZUfcJiXSuxmWFqtzLppxxy+i52FTr8bpjTyC6pm1/2KPIUSYKbGJ8Pr4zA5uW0/GIB5i81HjQ8YuZrW9oo6TRkSV7izkdL1xzZGB8svGai5mKPKZXikPkdM/NvLwPByFvLL1G5/B4tedKv7Oolmg9n5QDj+W2ueHgxrFLlPe607mbzwium5QMUk6yUVptP9akVqwp4crRRUpvUX8vxAwiNojutzJoUhEGFzj5sLHGSoemRkxshz0ctqap+DYu7Q6NP9nlaVlSVgzpjBE2gUzLoC8E4SEIFgHjEp5yTImpvmVsRCadT+6uIncsdfP6o3ChliN0biyX6o11OCcyyh6M3UmbjMLQhLN40pj9eKYtdDdaCakrbVYY/ok7H4ZLW49zOW1iOphE3D2vg3tiQx0HMSIGMUxhKwV8VeFzcrZGsez0edulVVyese3cZr2x74V6t+uNsQAa88bZ5CZTXk6uBFhre0PEfRcuzcBvRWUs00GcMeqsNRQFtXVcNs5wPhXmcX/R9KHXKB3XMAs6hvMFyzYcCmaFoCCG3iRz3u2m1IvWNeX7eWv2RWOavBTIcD3WGmsvCYNDWX42NaZome5oXKirdjSpwW9pdDuNCbm58xgtDnSt0CayK7Msv0GztguD+0n27TUjl+x171uWNw9BhDKHCy+3vs5GJ/KQYc60qZJ2XfI3bUc05b27krucsW9mdzxJzVU1jcnubK0lYBM+SjBylXUMXRNC39lCLUh6hE6z4NmuCkvcekN4coCVNgRnU3WZySl1HWqkguZyENmTYnoqjjKQ1WkK5x0pB0vPcNR7CuIz6402hJcNm+J+0nbA3lSB+QZoMvCJgE5Xuj97B4JGDmKuVNvtTiFVfWO16QRfYAzb7GPTdfFWEM3anB2OZUT1dpXWfZwmW+geke5e5TXxZgRTt4N1rNiJJlViTZ529zxVi/borzkpHggOl52x0WLD25/lyWYjx+8rQlcXsWl3yQ302M5lOdKGTuln3XRn1pPhpUYXFlIulTDQRZkirrqe7LvrKfA1RALv0sNF3nBmRUDKdNsfZetYjidlxhZymaDw4A4mRzqbLKcobAblDSpqtA+l56aBdfcYGXFxOTF+ayS12WnCyTvcci9wBFE+39U6Xu+wLD62HLdkUozEPnyq7nFtGEXm8nO2hHFzRs39BVnLhM/XJ61DNIqxT+4yNHqMg+F4sw1yb1ra+xrdUjdrHBk8ZFkbHehN17IwQ3OCwao6XraX7kRFkhVezgRnnY8TUxF8vzVu5tGspXwGMJaTR11sHekQNnBLOC4ZVbWpyvw2mwzyNiPNXa3kHcODWo3wvJYBZU425sAqDS1U4tDhhzvibOdMMAjW2dYtURtRVvDXKxtRrZzfjlBlOpOtpHfuYA5yKtHM+hQrh2ncm+utIlZz2cWdz1SgUGDjO+wcT+PW2BZ5xwXV7VycNGCvVLrwd74kQIMM+Sxv83ArRicWvZUBh1Cw7LhiKfPB+UDOriXCJ0ZYK6k+uNn+AtpQ6HZbH4UbqqIHnN1covAGeUvPAQhQjwLreo6h78JbcVn3HqhXRmy3IOu5A3G0CdvSqouwE7oO80M0lZH9pq8kdYeWCaoo9jIcr8OE943CGlRUQf3dD01j9G76TG65/QAKrEt2pbniYI1XUNeZh/jCXOdLys6+ocp1KeFQgq1P1+mal5jZwRxmlewlR49nKGgyr9yNB+hUTLdUpRq7x2o+vxV2fsOuI6jsBIP2JbjKlOLaFT2sg8IZSS7ubstkjYmJNk1nUW0oCOSOd2o5lOjdV0hKifJkb/ZNoLdNHu/OZtogold4ATN4F6NMz9yid7d4pAmoBc0W1G+7Od2Puw0hJDNo97jr2tB2rnw7tjWBbkUOOy0mTKO0wrNI7pBYRS7t2jz1EzRgxo2nK34SMmVDCpskJsN2i/vSdJu60luHyH6GB+qEbtbuDSKpGw3JtqXPvUE0O91UDhqLOJ5Ahydtfbh7VSAwDrJEusWGdXGIKKtOy7YEnbTYjjYJuqhrf0u27WZX7DSVxP2q9vdTYrcpFTtT4EdJl6GWIWnSltilvOTJzgZu7+M8XKP1AUKqqLkWueuQ66vv2Ig9oTgK2pZi7RSKG+HeUvpeJCvt1U6TzAxEXLOXVtXsvtc1djuAMvo01mFhYRDZBg4DbdtRP3ddme1dKxijfEYG7sz5aIGtw7bYSF09NoQ/922s5EM2yPYhiXc7vrLkrZczXZvLiKRzor4/3fc2heE+RQjHtFaIkDNaPCxryjtz57Tbagyui3u3RSRBbuiasNQSXmzolhplNd/XCiWb6KgZlMmLzAl0oQzCcoyHhVaX4npSpD2OqCBVYWLoOyTeFLkOGoljRTUlXokc6AF0mszFYo6sfFtvU1A3X2phHyBONC8BTNzCNRyTO2J31bicg3ussjN4wRrrClk7Wo8tLd3t7pc4B+XIdWlu6yvYMceRWyiOg404s1vloJF1Zjzt033JgSR9QufszkCZ3+xde+BEDVjKGNwk2jqX2YDulgLVXa4M/PnYZLG6beKiNofwJkB9j6RQ6Kfsja7pJjs0fF4cG4qHLT4nZqlGG70z8Mf3C+jmoGkikneOsRzgNSJhN8Q/3oc7yVrkRYP2AlZeXN88jaJJbjykr3sH2qRweRfueFd7u150i+C+MGvznHJ566lmea29mRmIPXIpeKsesztf0aDdc8I9MasoiaklSB8qIhSpicikdgorzWAzm4YFyImwNTGLcUkcLnN6RtuU2UzN9UCQWduYFyaDPcZIM6GAw3HtrzFZmZEIOy+KcN2Q3RApklsec+5QVeq+GhoSsqCKEH2IOG4SqnVj01ouGM+J01KrZ+Z+FW8zfcgGGrQt53IhOXWTeQO77QbbazU5Is2G9jl/G9fxcJDXlK2nGdJ0owexFHvYQ8NuUQmmi7ADiLHpCCNlIeW5kaRuEAJU2ovBXj6BJCVOdZk0WpAj+qAWs79vjEHzZQU+Dvsw3LOQkC+dQQsBrbmiwS6u6J16tljf+mMaMYJxF5u+oQfYyDsrttY92ep+UKE5Ui7+cB020oQi6zZmDl1SEg+4PDBbVmDVWqPdwtZLhcjNkhQQON9CQSC6zMLsAzQqoAmrfFJyPFTfxkHQ5nq+qbv+rPkXmQoVmLw1+Fo+GcTcX0MAijy+8dTMZwUVKXYHm51ud4fwYHqwvD1pGdTtFCJxwosgstt1suwz4WYmrTm2LkqTXV/fE5jHs6vg5qJnbQOJQxrM2TtJAWXEpu3JG9uEN9bvjuUwtMX6MKx1j244qSRa2ib31Ya4EIwrbp22vw3UoNpKdDscvYretU4enfG7PZ3XprR1kb6fNsqZ3hFINNLqEgyu0CYiK1mGu5HWWNthOMYR3p27AWCDLl4czbXqC5caqc85hduycXeVe9lpRn2CU9zEMJ3ad4sakeTLx5fHV1Fvl9r/w1d2j7vP/2/XrK+3pdUA9iy94Hk9HTj+l+deX/4nAX77+NJ4Cdj+9Y64zfvo7Qr29Yb409vCT8H7ffzrh0Xfnt8yTd375X3nRI/vdl9+kIWPW/vHPS94fvvuCTw9wKR4v0X/y7fF4D1+/0zpIdXzY8jnPTaQ7DP08v3/Ad7qq7POLAAA -->
