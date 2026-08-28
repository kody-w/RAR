---
name: "rar-cowork-cookbook-vendor-invoice-validation"
description: "Validates open vendor invoices against posting rules and emails the AP team a fix-list."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_invoice_validation", "rar_sha256": "30b66026ffe92f9bc12f310c642de6fc2ee93fe56f0a18c20335f89b39edcf74", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/vendor_invoice_validation`. The original RAPP
agent is preserved byte-for-byte in `vendor_invoice_validation_agent.py` and in the RCI capsule.

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

Vendor Invoice Pre-Posting Validation — Validates open vendor invoices against posting rules and emails the AP team a fix-list.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/vendor-invoice-validation
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vendor_invoice_validation_agent.py` and embedded as the fenced Python below (sha256 30b66026ffe92f9b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vendor_invoice_validation_agent.py` first:

```bash
python3 vendor_invoice_validation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vendor_invoice_validation_agent.py   # or on stdin
python3 vendor_invoice_validation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Vendor Invoice Pre-Posting Validation — Validates open vendor invoices against posting rules and emails the AP team a fix-list.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/vendor-invoice-validation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/vendor_invoice_validation',
    "version": '2.0.1',
    "display_name": 'Vendor Invoice Pre-Posting Validation',
    "description": 'Validates open vendor invoices against posting rules and emails the AP team a fix-list.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'vendor-invoice-validation',
        "upstream_url": 'https://coworkcookbook.com/recipes/vendor-invoice-validation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c4bcfea956c66609',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/vendor-invoice-validation', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.375, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class VendorInvoiceValidation(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'VendorInvoiceValidation'
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
    print(VendorInvoiceValidation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
