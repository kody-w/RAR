---
name: "rar-cat-agent-skills-copilot-studio-agent-test"
description: "Test a Copilot Studio agent against your own Q&A set and get a graded pass/fail report \u2014 no browser automation."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_studio_agent_test", "rar_sha256": "571bdedba33c20a1913db0d63202aba452b953bb1a6bfe1bb09559c9fb986c64", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Matteo Pagani", "tags": ["copilot_studio", "testing", "evaluation", "quality", "agents", "power_platform"]}
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
