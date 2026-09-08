---
name: "rar-cat-agent-skills-business-os"
description: "A practical operating system for Copilot Studio that gives agents a consistent way to clarify outcomes, choose the right approach, solve problems, make decisions, plan projects, improve processes, handle incidents, and turn repeatable work into reusable skills. Unlike a standard Copilot experience that relies mainly on the prompt and available context, Business OS adds a structured way of working\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/business_os", "rar_sha256": "6482b513441d7a7adb56c67fbd6733482e86851f16e151ff3d9f112c8e661bac", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Matthew James Davis", "tags": ["business", "decision_making", "problem_solving", "project_planning", "process_improvement", "governance", "skill_generation"]}
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
