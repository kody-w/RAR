---
name: "rar-cowork-cookbook-vendor-invoice-validation"
description: "Validates open vendor invoices against posting rules and emails the AP team a fix-list."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_invoice_validation", "rar_sha256": "9d0ea5ca2757e5d92794def6683b99b9ff22417d1fcc435c724cad192d02eb2b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
