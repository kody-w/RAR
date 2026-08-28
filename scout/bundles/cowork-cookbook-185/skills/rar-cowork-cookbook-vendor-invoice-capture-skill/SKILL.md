---
name: "rar-cowork-cookbook-vendor-invoice-capture-skill"
description: "The packaged Cowork skill that powers the vendor-invoice intake recipe \u2014 runs the PDF extraction, USMF vendor match, and pending invoice creation as a single reusable skill, with a 97/100 quality scorecard from the Cowork skill quality tool."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_invoice_capture_skill", "rar_sha256": "726bfc1e7f14bb64da0ac946394374d25418bdf169715a0ca0ac269ce3bd3410", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `vendor_invoice_capture_skill_agent.py` and embedded as the fenced Python below (sha256 726bfc1e7f14bb64…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `vendor_invoice_capture_skill_agent.py` first:

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
    "version": '2.0.0',
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
