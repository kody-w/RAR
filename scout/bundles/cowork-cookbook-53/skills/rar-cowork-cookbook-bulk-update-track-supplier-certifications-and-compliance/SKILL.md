---
name: "rar-cowork-cookbook-bulk-update-track-supplier-certifications-and-compliance"
description: "Applies a bulk field update across track supplier certifications and compliance records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_track_supplier_certifications_and_compliance", "rar_sha256": "b81be689017dae1de65e0bc25a0664fa5aaa6665fa7e3d4d619e99bd1ebe7dcf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_track_supplier_certifications_and_compliance_agent.py` and embedded as the fenced Python below (sha256 b81be689017dae1d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_track_supplier_certifications_and_compliance_agent.py` first:

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
    "version": '2.0.0',
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
