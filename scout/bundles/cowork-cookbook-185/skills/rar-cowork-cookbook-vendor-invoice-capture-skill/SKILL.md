---
name: "rar-cowork-cookbook-vendor-invoice-capture-skill"
description: "The packaged Cowork skill that powers the vendor-invoice intake recipe \u2014 runs the PDF extraction, USMF vendor match, and pending invoice creation as a single reusable skill, with a 97/100 quality scorecard from the Cowork skill quality tool."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/vendor_invoice_capture_skill", "rar_sha256": "726bfc1e7f14bb64da0ac946394374d25418bdf169715a0ca0ac269ce3bd3410", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "vendor_invoice_capture_skill_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/vendor-invoice-capture-skill:e9b6fc1f12867b61c6974bcd790acdea20ff60e9b51871761e899eac83d63219", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/vendor_invoice_capture_skill`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `vendor_invoice_capture_skill_agent.py` is
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
