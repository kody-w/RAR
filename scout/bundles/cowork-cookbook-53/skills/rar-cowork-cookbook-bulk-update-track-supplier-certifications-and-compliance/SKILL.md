---
name: "rar-cowork-cookbook-bulk-update-track-supplier-certifications-and-compliance"
description: "Applies a bulk field update across track supplier certifications and compliance records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_track_supplier_certifications_and_compliance", "rar_sha256": "6653cde5e2381f1867d10b6093c0965cb83fa941d516590405e98d0a87355841", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_track_supplier_certifications_and_compliance`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_track_supplier_certifications_and_compliance_agent.py` and in the RCI capsule.

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

Track supplier certifications and compliance Bulk Field Update — Applies a bulk field update across track supplier certifications and compliance records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-track-supplier-certifications-and-compliance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_track_supplier_certifications_and_compliance_agent.py` and embedded as the fenced Python below (sha256 6653cde5e2381f18…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_track_supplier_certifications_and_compliance_agent.py` first:

```bash
python3 bulk_update_track_supplier_certifications_and_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_track_supplier_certifications_and_compliance_agent.py   # or on stdin
python3 bulk_update_track_supplier_certifications_and_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track supplier certifications and compliance Bulk Field Update — Applies a bulk field update across track supplier certifications and compliance records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-track-supplier-certifications-and-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_track_supplier_certifications_and_compliance',
    "version": '2.0.1',
    "display_name": 'Track supplier certifications and compliance Bulk Field Update',
    "description": 'Applies a bulk field update across track supplier certifications and compliance records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'bulk-update-track-supplier-certifications-and-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-track-supplier-certifications-and-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ecba38519fd35bf0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/track-supplier-certifications-and-compliance'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/bulk-update-track-supplier-certifications-and-compliance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateTrackSupplierCertificationsAndCompliance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateTrackSupplierCertificationsAndCompliance'
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
    print(BulkUpdateTrackSupplierCertificationsAndCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
