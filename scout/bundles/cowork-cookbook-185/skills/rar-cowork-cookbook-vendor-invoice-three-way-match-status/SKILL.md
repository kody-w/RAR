---
name: "rar-cowork-cookbook-vendor-invoice-three-way-match-status"
description: "Builds a status report of vendor invoices and their three-way-match state against POs and goods receipts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_invoice_three_way_match_status", "rar_sha256": "2cb439fbe5cf5c566dd0199b043e5dc1e50150e650ac8fcff1cfb39ca93f18d4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/vendor_invoice_three_way_match_status`. The original RAPP
agent is preserved byte-for-byte in `vendor_invoice_three_way_match_status_agent.py` and in the RCI capsule.

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
