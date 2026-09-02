---
name: "rar-cowork-cookbook-bulk-update-analyze-project-metrics"
description: "Applies a bulk field update across analyze project metrics records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_project_metrics", "rar_sha256": "923965ce01e57b014f96c75c81306cad7d43e0db50587dfe9ea62bbe5353adb5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_analyze_project_metrics_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-analyze-project-metrics:0e1d6281230bac9ba052a707f2873b7a5d717ddc74dc54b0c0b79da08178f748", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_analyze_project_metrics`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_analyze_project_metrics_agent.py` is
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

Analyze project metrics Bulk Field Update — Applies a bulk field update across analyze project metrics records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-project-metrics
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_project_metrics_agent.py` and embedded as the fenced Python below (sha256 923965ce01e57b01…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_project_metrics_agent.py` first:

```bash
python3 bulk_update_analyze_project_metrics_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_project_metrics_agent.py   # or on stdin
python3 bulk_update_analyze_project_metrics_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze project metrics Bulk Field Update — Applies a bulk field update across analyze project metrics records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-project-metrics
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_project_metrics',
    "version": '2.0.0',
    "display_name": 'Analyze project metrics Bulk Field Update',
    "description": 'Applies a bulk field update across analyze project metrics records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-analyze-project-metrics',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-project-metrics',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '37c75cf23ed92612',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/analyze-project-metrics'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/bulk-update-analyze-project-metrics', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateAnalyzeProjectMetrics(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeProjectMetrics'
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
    print(BulkUpdateAnalyzeProjectMetrics().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
