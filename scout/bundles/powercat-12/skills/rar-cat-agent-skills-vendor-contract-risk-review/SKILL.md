---
name: "rar-cat-agent-skills-vendor-contract-risk-review"
description: "First-pass review of a vendor contract or SOW for the clauses that commonly cause problems (auto-renewal, liability caps, termination, IP ownership), flagged by risk level to prepare for legal review, not replace it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/vendor_contract_risk_review", "rar_sha256": "a1eaff0f2d79f7143b9cd5cd11d58b9144cd6537ce0f81ec7f204ad55c256818", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Tim Karlsson", "tags": ["contracts", "legal", "procurement", "risk", "vendor_management", "review"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/vendor_contract_risk_review`. The original RAPP
agent is preserved byte-for-byte in `vendor_contract_risk_review_agent.py` and in the RCI capsule.

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

Vendor Contract Risk Review — First-pass review of a vendor contract or SOW for the clauses that commonly cause problems (auto-renewal, liability caps, termination, IP ownership), flagged by risk level to prepare for legal review, not replace it.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#vendor-contract-risk-review
  Upstream author: Tim Karlsson
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vendor_contract_risk_review_agent.py` and embedded as the fenced Python below (sha256 a1eaff0f2d79f714…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vendor_contract_risk_review_agent.py` first:

```bash
python3 vendor_contract_risk_review_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vendor_contract_risk_review_agent.py   # or on stdin
python3 vendor_contract_risk_review_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Vendor Contract Risk Review — First-pass review of a vendor contract or SOW for the clauses that commonly cause problems (auto-renewal, liability caps, termination, IP ownership), flagged by risk level to prepare for legal review, not replace it.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#vendor-contract-risk-review
  Upstream author: Tim Karlsson
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/vendor_contract_risk_review',
    "version": '3.0.2',
    "display_name": 'Vendor Contract Risk Review',
    "description": 'First-pass review of a vendor contract or SOW for the clauses that commonly cause problems (auto-renewal, liability caps, termination, IP ownership), flagged by risk level to prepare for legal review, not replace it.',
    "author": 'Tim Karlsson',
    "tags": ['contracts', 'legal', 'procurement', 'risk', 'vendor_management', 'review'],
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
        "upstream_slug": 'vendor-contract-risk-review',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#vendor-contract-risk-review',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'b809a298c80e1782',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 1.0, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:review', 'tag:risk', 'word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class VendorContractRiskReview(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'VendorContractRiskReview'
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
    print(VendorContractRiskReview().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
