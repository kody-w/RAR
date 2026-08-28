---
name: "rar-cowork-cookbook-vendor-invoice-capture-skill"
description: "The packaged Cowork skill that powers the vendor-invoice intake recipe \u2014 runs the PDF extraction, USMF vendor match, and pending invoice creation as a single reusable skill, with a 97/100 quality scorecard from the Cowork skill quality tool."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_invoice_capture_skill", "rar_sha256": "5368489e39f33703188b55f9dca3c4f951050c56d71f1a82f09449e1e15ab4c6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/vendor_invoice_capture_skill`. The original RAPP
agent is preserved byte-for-byte in `vendor_invoice_capture_skill_agent.py` and in the RCI capsule.

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

Vendor Invoice Capture Skill (packaged + scored) — The packaged Cowork skill that powers the vendor-invoice intake recipe — runs the PDF extraction, USMF vendor match, and pending invoice creation as a single reusable skill, with a 97/100 quality scorecard from the Cowork skill quality tool.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/vendor-invoice-capture-skill
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vendor_invoice_capture_skill_agent.py` and embedded as the fenced Python below (sha256 5368489e39f33703…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vendor_invoice_capture_skill_agent.py` first:

```bash
python3 vendor_invoice_capture_skill_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 vendor_invoice_capture_skill_agent.py   # or on stdin
python3 vendor_invoice_capture_skill_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Vendor Invoice Capture Skill (packaged + scored) — The packaged Cowork skill that powers the vendor-invoice intake recipe — runs the PDF extraction, USMF vendor match, and pending invoice creation as a single reusable skill, with a 97/100 quality scorecard from the Cowork skill quality tool.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/vendor-invoice-capture-skill
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/vendor_invoice_capture_skill',
    "version": '2.0.1',
    "display_name": 'Vendor Invoice Capture Skill (packaged + scored)',
    "description": 'The packaged Cowork skill that powers the vendor-invoice intake recipe — runs the PDF extraction, USMF vendor match, and pending invoice creation as a single reusable skill, with a 97/100 quality scorecard from the Cowork skill quality tool.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'vendor-invoice-capture-skill',
        "upstream_url": 'https://coworkcookbook.com/recipes/vendor-invoice-capture-skill',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fab025314d181057',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-05', 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/process-supplier-invoices'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'source-to-pay/vendor-invoice-capture-skill', 'uses_skills': {'custom': ['vendor-invoice-capture'], 'ootb': ['Email', 'PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_get_entity_metadata', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}, {'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class VendorInvoiceCaptureSkill(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'VendorInvoiceCaptureSkill'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(VendorInvoiceCaptureSkill().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
