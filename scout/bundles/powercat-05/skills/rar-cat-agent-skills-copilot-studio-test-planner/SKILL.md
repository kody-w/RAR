---
name: "rar-cat-agent-skills-copilot-studio-test-planner"
description: "Reads an exported Copilot Studio agent and generates a graded, runnable test suite (happy-path, paraphrase, disambiguation, negative, knowledge-grounding, multilingual, and safety cases) plus a regression set, ready to run in the free Copilot Studio test panel."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_test_planner", "rar_sha256": "b844fedd3d1befa33932d43c296c9fc3ede7185c6a805ccd59b5dd0ce70a20c6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Elliot Margot", "tags": ["qa", "eval", "regression", "agent"]}
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
