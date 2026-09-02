---
name: "rar-cowork-cookbook-vendor-invoice-validation"
description: "Validates open vendor invoices against posting rules and emails the AP team a fix-list."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_invoice_validation", "rar_sha256": "9d0ea5ca2757e5d92794def6683b99b9ff22417d1fcc435c724cad192d02eb2b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "vendor_invoice_validation_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/vendor-invoice-validation:e2361b08f950d50be2a53859f387de2b5717d1c46f01b298be3a2541f977d9b1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/vendor_invoice_validation`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `vendor_invoice_validation_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vendor_invoice_validation_agent.py` and embedded as the fenced Python below (sha256 9d0ea5ca2757e5d9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vendor_invoice_validation_agent.py` first:

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
    "version": '2.0.0',
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
