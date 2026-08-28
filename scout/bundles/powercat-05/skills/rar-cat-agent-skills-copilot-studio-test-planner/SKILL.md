---
name: "rar-cat-agent-skills-copilot-studio-test-planner"
description: "Reads an exported Copilot Studio agent and generates a graded, runnable test suite (happy-path, paraphrase, disambiguation, negative, knowledge-grounding, multilingual, and safety cases) plus a regression set, ready to run in the free Copilot Studio test panel."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_test_planner", "rar_sha256": "3cfc5e42ce1e3f436c2129fd6b933475640c6476a63b042d5d0d6ac22e817bd2", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Elliot Margot", "tags": ["qa", "eval", "regression", "agent"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/copilot_studio_test_planner`. The original RAPP
agent is preserved byte-for-byte in `copilot_studio_test_planner_agent.py` and in the RCI capsule.

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

Copilot Studio Test Planner — Reads an exported Copilot Studio agent and generates a graded, runnable test suite (happy-path, paraphrase, disambiguation, negative, knowledge-grounding, multilingual, and safety cases) plus a regression set, ready to run in the free Copilot Studio test panel.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-test-planner
  Upstream author: Elliot Margot
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "What to apply this capability to.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_test_planner_agent.py` and embedded as the fenced Python below (sha256 3cfc5e42ce1e3f43…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_test_planner_agent.py` first:

```bash
python3 copilot_studio_test_planner_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_test_planner_agent.py   # or on stdin
python3 copilot_studio_test_planner_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Copilot Studio Test Planner — Reads an exported Copilot Studio agent and generates a graded, runnable test suite (happy-path, paraphrase, disambiguation, negative, knowledge-grounding, multilingual, and safety cases) plus a regression set, ready to run in the free Copilot Studio test panel.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-test-planner
  Upstream author: Elliot Margot
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/copilot_studio_test_planner',
    "version": '2.0.0',
    "display_name": 'Copilot Studio Test Planner',
    "description": 'Reads an exported Copilot Studio agent and generates a graded, runnable test suite (happy-path, paraphrase, disambiguation, negative, knowledge-grounding, multilingual, and safety cases) plus a regression set, ready to run in the free Copilot Studio test panel.',
    "author": 'Elliot Margot',
    "tags": ['qa', 'eval', 'regression', 'agent'],
    "category": 'general',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'copilot-studio-test-planner',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#copilot-studio-test-planner',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'ddaf3694d8c2a432',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'general', 'checks': ['The outcome is independently verifiable.', 'Assumptions are written down.', 'The result was checked against the original goal.'], 'confidence': 0.0, 'deliverable': 'A completed pass with the goal, the method, the result, and the assumptions it rests on.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'What to apply this capability to.'}, 'refined_by': 'rules', 'signals': [], 'steps': ['State the goal as an outcome someone else could verify without you.', 'List what you have and what is missing before starting.', 'Do the smallest version end to end, so unknowns surface while they are cheap.', 'Check the result against the goal as stated, not against what turned out to be convenient.', 'Record what would have to be true for this to be wrong.'], 'subject_label': 'task', 'verb': 'Run'}


class CopilotStudioTestPlanner(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CopilotStudioTestPlanner'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to apply this capability to.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(CopilotStudioTestPlanner().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
