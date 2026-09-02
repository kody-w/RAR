---
name: "rar-kody-w-rappter-engine"
description: "Provides a base class for rules-as-data content engines \u2014 subclass it, override tick(), and run it as a CLI or brainstem tool."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rappter_engine_agent", "rar_sha256": "5679d82a2ea53a7dc8ae3b9c78e932ed83d068947f07d53be3af7582e32f7fd9", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "rappter_engine_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/rappter-engine:37b3cf26f5461923ebb97b445120852963c38500a7d1e5af2a4be8c92ce117e2", "kind": "skill"}, "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["engine", "framework", "content", "automation", "rules-as-data", "heartbeat"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/rappter_engine_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `rappter_engine_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
