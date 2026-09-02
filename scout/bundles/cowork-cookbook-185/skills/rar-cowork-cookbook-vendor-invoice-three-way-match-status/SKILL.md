---
name: "rar-cowork-cookbook-vendor-invoice-three-way-match-status"
description: "Builds a status report of vendor invoices and their three-way-match state against POs and goods receipts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_invoice_three_way_match_status", "rar_sha256": "2cb439fbe5cf5c566dd0199b043e5dc1e50150e650ac8fcff1cfb39ca93f18d4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "vendor_invoice_three_way_match_status_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/vendor-invoice-three-way-match-status:04e6116bcde9ba9f26ec6606c9c1caacf0b1cc2e48805b255e7d0a9f279a3b7e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/vendor_invoice_three_way_match_status`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `vendor_invoice_three_way_match_status_agent.py` is
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

Vendor Invoice Three-Way Match Status Report — Builds a status report of vendor invoices and their three-way-match state against POs and goods receipts.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/vendor-invoice-three-way-match-status
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vendor_invoice_three_way_match_status_agent.py` and embedded as the fenced Python below (sha256 2cb439fbe5cf5c56…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vendor_invoice_three_way_match_status_agent.py` first:

```bash
python3 vendor_invoice_three_way_match_status_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vendor_invoice_three_way_match_status_agent.py   # or on stdin
python3 vendor_invoice_three_way_match_status_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Vendor Invoice Three-Way Match Status Report — Builds a status report of vendor invoices and their three-way-match state against POs and goods receipts.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/vendor-invoice-three-way-match-status
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/vendor_invoice_three_way_match_status',
    "version": '2.0.0',
    "display_name": 'Vendor Invoice Three-Way Match Status Report',
    "description": 'Builds a status report of vendor invoices and their three-way-match state against POs and goods receipts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'vendor-invoice-three-way-match-status',
        "upstream_url": 'https://coworkcookbook.com/recipes/vendor-invoice-three-way-match-status',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8a903f9e2efd4ea5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/vendor-invoice-three-way-match-status', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'vendor-invoice-query', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.286, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class VendorInvoiceThreeWayMatchStatus(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'VendorInvoiceThreeWayMatchStatus'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(VendorInvoiceThreeWayMatchStatus().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
