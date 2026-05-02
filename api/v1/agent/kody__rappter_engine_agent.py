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
    "name": "@kody/rappter_engine_agent",
    "version": "1.0.0",
    "display_name": "RappterEngine",
    "description": "Base agent for building data-driven content engines. Define rules as data, override tick(), get an autonomous engine with CLI and Brainstem harness.",
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
