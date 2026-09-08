---
name: "rar-cat-agent-skills-vendor-contract-risk-review"
description: "First-pass review of a vendor contract or SOW for the clauses that commonly cause problems (auto-renewal, liability caps, termination, IP ownership), flagged by risk level to prepare for legal review, not replace it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/vendor_contract_risk_review", "rar_sha256": "a1eaff0f2d79f7143b9cd5cd11d58b9144cd6537ce0f81ec7f204ad55c256818", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Tim Karlsson", "tags": ["contracts", "legal", "procurement", "risk", "vendor_management", "review"]}
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
