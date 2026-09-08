---
name: "rar-cat-agent-skills-copilot-studio-test-planner"
description: "Reads an exported Copilot Studio agent and generates a graded, runnable test suite (happy-path, paraphrase, disambiguation, negative, knowledge-grounding, multilingual, and safety cases) plus a regression set, ready to run in the free Copilot Studio test panel."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_test_planner", "rar_sha256": "b844fedd3d1befa33932d43c296c9fc3ede7185c6a805ccd59b5dd0ce70a20c6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Elliot Margot", "tags": ["qa", "eval", "regression", "agent"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_test_planner_agent.py` and embedded as the fenced Python below (sha256 b844fedd3d1befa3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_test_planner_agent.py` first:

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
    "version": '3.0.2',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
