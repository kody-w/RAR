---
name: "rar-cat-agent-skills-vendor-contract-risk-review"
description: "First-pass review of a vendor contract or SOW for the clauses that commonly cause problems (auto-renewal, liability caps, termination, IP ownership), flagged by risk level to prepare for legal review, not replace it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/vendor_contract_risk_review", "rar_sha256": "b83fe34b7b87dcbf87a736131abad982e5fe477b0823a4204428b09fb1750590", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Tim Karlsson", "tags": ["contracts", "legal", "procurement", "risk", "vendor_management", "review"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vendor_contract_risk_review_agent.py` and embedded as the fenced Python below (sha256 b83fe34b7b87dcbf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vendor_contract_risk_review_agent.py` first:

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
    "version": '2.0.0',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
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
    print(VendorContractRiskReview().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
