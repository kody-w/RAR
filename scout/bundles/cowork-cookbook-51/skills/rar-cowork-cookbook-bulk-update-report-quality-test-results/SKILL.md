---
name: "rar-cowork-cookbook-bulk-update-report-quality-test-results"
description: "Applies a bulk field update across report quality test results records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_report_quality_test_results", "rar_sha256": "b6d1a4fa1ca01df0ccc4ea4d745e65afefeac468e44874171538e33bc9fd08c3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_report_quality_test_results`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_report_quality_test_results_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_report_quality_test_results_agent.py` and embedded as the fenced Python below (sha256 b6d1a4fa1ca01df0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_report_quality_test_results_agent.py` first:

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
    "version": '2.0.1',
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
