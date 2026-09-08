---
name: "rar-cat-agent-skills-business-os"
description: "A practical operating system for Copilot Studio that gives agents a consistent way to clarify outcomes, choose the right approach, solve problems, make decisions, plan projects, improve processes, handle incidents, and turn repeatable work into reusable skills. Unlike a standard Copilot experience that relies mainly on the prompt and available context, Business OS adds a structured way of working\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/business_os", "rar_sha256": "6482b513441d7a7adb56c67fbd6733482e86851f16e151ff3d9f112c8e661bac", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Matthew James Davis", "tags": ["business", "decision_making", "problem_solving", "project_planning", "process_improvement", "governance", "skill_generation"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/business_os`. The original RAPP
agent is preserved byte-for-byte in `business_os_agent.py` and in the RCI capsule.

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

Business OS — A practical operating system for Copilot Studio that gives agents a consistent way to clarify outcomes, choose the right approach, solve problems, make decisions, plan projects, improve processes, handle incidents, and turn repeatable work into reusable skills. Unlike a standard Copilot experience that relies mainly on the prompt and available context, Business OS adds a structured way of working…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#business-os
  Upstream author: Matthew James Davis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `business_os_agent.py` and embedded as the fenced Python below (sha256 6482b513441d7a7a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `business_os_agent.py` first:

```bash
python3 business_os_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 business_os_agent.py   # or on stdin
python3 business_os_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Business OS — A practical operating system for Copilot Studio that gives agents a consistent way to clarify outcomes, choose the right approach, solve problems, make decisions, plan projects, improve processes, handle incidents, and turn repeatable work into reusable skills. Unlike a standard Copilot experience that relies mainly on the prompt and available context, Business OS adds a structured way of working…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#business-os
  Upstream author: Matthew James Davis
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/business_os',
    "version": '3.0.2',
    "display_name": 'Business OS',
    "description": 'A practical operating system for Copilot Studio that gives agents a consistent way to clarify outcomes, choose the right approach, solve problems, make decisions, plan projects, improve processes, handle incidents, and turn repeatable work into reusable skills. Unlike a standard Copilot experience that relies mainly on the prompt and available context, Business OS adds a structured way of working…',
    "author": 'Matthew James Davis',
    "tags": ['business', 'decision_making', 'problem_solving', 'project_planning', 'process_improvement', 'governance', 'skill_generation'],
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
        "upstream_slug": 'business-os',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#business-os',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '0f102cac2f8ea262',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.333, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:governance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class BusinessOs(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BusinessOs'
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
    print(BusinessOs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
