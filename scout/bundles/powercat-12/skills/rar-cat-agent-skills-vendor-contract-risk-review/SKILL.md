---
name: "rar-cat-agent-skills-vendor-contract-risk-review"
description: "First-pass review of a vendor contract or SOW for the clauses that commonly cause problems (auto-renewal, liability caps, termination, IP ownership), flagged by risk level to prepare for legal review, not replace it."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/vendor_contract_risk_review", "rar_sha256": "b83fe34b7b87dcbf87a736131abad982e5fe477b0823a4204428b09fb1750590", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "vendor_contract_risk_review_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/vendor-contract-risk-review:753ee07346ea4397a415bd80a9745e3e6175bc45fdfbd895213995ac51a986be", "kind": "skill"}, "version": "2.0.0", "author": "Tim Karlsson", "tags": ["contracts", "legal", "procurement", "risk", "vendor_management", "review"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/vendor_contract_risk_review`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `vendor_contract_risk_review_agent.py` is
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
