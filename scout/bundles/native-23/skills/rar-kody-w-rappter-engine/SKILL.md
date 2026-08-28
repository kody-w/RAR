---
name: "rar-kody-w-rappter-engine"
description: "Provides a base class for rules-as-data content engines \u2014 subclass it, override tick(), and run it as a CLI or brainstem tool."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rappter_engine_agent", "rar_sha256": "5679d82a2ea53a7dc8ae3b9c78e932ed83d068947f07d53be3af7582e32f7fd9", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["engine", "framework", "content", "automation", "rules-as-data", "heartbeat"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rappter_engine_agent.py` and embedded as the fenced Python below (sha256 5679d82a2ea53a7d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rappter_engine_agent.py` first:

```bash
python3 rappter_engine_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rappter_engine_agent.py   # or on stdin
python3 rappter_engine_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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

<!-- rci-capsule:v1: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 -->
