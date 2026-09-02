---
name: "rar-cowork-cookbook-bulk-update-track-supplier-certifications-and-compliance"
description: "Applies a bulk field update across track supplier certifications and compliance records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_track_supplier_certifications_and_compliance", "rar_sha256": "b81be689017dae1de65e0bc25a0664fa5aaa6665fa7e3d4d619e99bd1ebe7dcf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_track_supplier_certifications_and_compliance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-track-supplier-certifications-and-compliance:9e82dddddeb8ef5375f4a36a32f5947483d1a8c30fe254ada1ca16093c93a086", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_track_supplier_certifications_and_compliance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_track_supplier_certifications_and_compliance_agent.py` is
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
