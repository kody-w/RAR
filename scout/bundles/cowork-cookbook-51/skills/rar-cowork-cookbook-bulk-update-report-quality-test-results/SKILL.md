---
name: "rar-cowork-cookbook-bulk-update-report-quality-test-results"
description: "Applies a bulk field update across report quality test results records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_report_quality_test_results", "rar_sha256": "727a8bd9a6e192773a59b20341481dcae5159caa5fdeedcc30063e26495c7931", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_report_quality_test_results_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-report-quality-test-results:3f4bf1aeb5ed33649b7ae61e2f6432664b423a4b09ab9afa6bcfa63bbc5ee97d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_report_quality_test_results`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_report_quality_test_results_agent.py` is
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

Report quality test results Bulk Field Update — Applies a bulk field update across report quality test results records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-report-quality-test-results
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_report_quality_test_results_agent.py` and embedded as the fenced Python below (sha256 727a8bd9a6e19277…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_report_quality_test_results_agent.py` first:

```bash
python3 bulk_update_report_quality_test_results_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_report_quality_test_results_agent.py   # or on stdin
python3 bulk_update_report_quality_test_results_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report quality test results Bulk Field Update — Applies a bulk field update across report quality test results records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-report-quality-test-results
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_report_quality_test_results',
    "version": '2.0.0',
    "display_name": 'Report quality test results Bulk Field Update',
    "description": 'Applies a bulk field update across report quality test results records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-report-quality-test-results',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-report-quality-test-results',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b48eb9a79109a726',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/report-quality-test-results'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/bulk-update-report-quality-test-results', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateReportQualityTestResults(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReportQualityTestResults'
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
    print(BulkUpdateReportQualityTestResults().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
