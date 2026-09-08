---
name: "rar-cat-agent-skills-copilot-studio-agent-test"
description: "Test a Copilot Studio agent against your own Q&A set and get a graded pass/fail report \u2014 no browser automation."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_agent_test", "rar_sha256": "571bdedba33c20a1913db0d63202aba452b953bb1a6bfe1bb09559c9fb986c64", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Matteo Pagani", "tags": ["copilot_studio", "testing", "evaluation", "quality", "agents", "power_platform"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/copilot_studio_agent_test`. The original RAPP
agent is preserved byte-for-byte in `copilot_studio_agent_test_agent.py` and in the RCI capsule.

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

Copilot Studio Agent Test — Test a Copilot Studio agent against your own Q&A set and get a graded pass/fail report — no browser automation.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-agent-test
  Upstream author: Matteo Pagani
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
      "type": "string"
    },
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_studio_agent_test_agent.py` and embedded as the fenced Python below (sha256 571bdedba33c20a1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_studio_agent_test_agent.py` first:

```bash
python3 copilot_studio_agent_test_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_studio_agent_test_agent.py   # or on stdin
python3 copilot_studio_agent_test_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Copilot Studio Agent Test — Test a Copilot Studio agent against your own Q&A set and get a graded pass/fail report — no browser automation.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-studio-agent-test
  Upstream author: Matteo Pagani
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/copilot_studio_agent_test',
    "version": '3.0.2',
    "display_name": 'Copilot Studio Agent Test',
    "description": 'Test a Copilot Studio agent against your own Q&A set and get a graded pass/fail report — no browser automation.',
    "author": 'Matteo Pagani',
    "tags": ['copilot_studio', 'testing', 'evaluation', 'quality', 'agents', 'power_platform'],
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
        "upstream_slug": 'copilot-studio-agent-test',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#copilot-studio-agent-test',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'ac86f61bb9663d51',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:quality', 'tag:testing', 'word:against'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class CopilotStudioAgentTest(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CopilotStudioAgentTest'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(CopilotStudioAgentTest().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
