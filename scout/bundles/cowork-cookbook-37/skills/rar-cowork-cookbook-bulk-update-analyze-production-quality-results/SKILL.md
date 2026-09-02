---
name: "rar-cowork-cookbook-bulk-update-analyze-production-quality-results"
description: "Applies a bulk field update across analyze production quality results records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_production_quality_results", "rar_sha256": "3697538499196f7b27af7666ba7033a96732ab0f793bc670e0525a4476f9d0c5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_analyze_production_quality_results_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-analyze-production-quality-results:60d8f8390f6b9c701c0b07fcb03b26ff05a590619b3e04c73b70128854336841", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_analyze_production_quality_results`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_analyze_production_quality_results_agent.py` is
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

Analyze production quality results Bulk Field Update — Applies a bulk field update across analyze production quality results records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-production-quality-results
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_production_quality_results_agent.py` and embedded as the fenced Python below (sha256 3697538499196f7b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_production_quality_results_agent.py` first:

```bash
python3 bulk_update_analyze_production_quality_results_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_production_quality_results_agent.py   # or on stdin
python3 bulk_update_analyze_production_quality_results_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze production quality results Bulk Field Update — Applies a bulk field update across analyze production quality results records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-production-quality-results
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_production_quality_results',
    "version": '2.0.0',
    "display_name": 'Analyze production quality results Bulk Field Update',
    "description": 'Applies a bulk field update across analyze production quality results records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-analyze-production-quality-results',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-production-quality-results',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '07d3aaa9f1ad24c1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/analyze-production-quality-results'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/bulk-update-analyze-production-quality-results', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateAnalyzeProductionQualityResults(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeProductionQualityResults'
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
    print(BulkUpdateAnalyzeProductionQualityResults().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
