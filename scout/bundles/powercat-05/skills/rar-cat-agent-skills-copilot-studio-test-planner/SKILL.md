---
name: "rar-cat-agent-skills-copilot-studio-test-planner"
description: "Reads an exported Copilot Studio agent and generates a graded, runnable test suite (happy-path, paraphrase, disambiguation, negative, knowledge-grounding, multilingual, and safety cases) plus a regression set, ready to run in the free Copilot Studio test panel."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_test_planner", "rar_sha256": "3cfc5e42ce1e3f436c2129fd6b933475640c6476a63b042d5d0d6ac22e817bd2", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "copilot_studio_test_planner_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/copilot-studio-test-planner:8df6eb21fc5bf82b5a4d981f8ef3caf1113de2d3c965c89df14696d3ba8979e2", "kind": "skill"}, "version": "2.0.0", "author": "Elliot Margot", "tags": ["qa", "eval", "regression", "agent"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/copilot_studio_test_planner`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `copilot_studio_test_planner_agent.py` is
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
