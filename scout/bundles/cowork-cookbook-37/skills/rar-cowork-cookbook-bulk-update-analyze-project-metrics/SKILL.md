---
name: "rar-cowork-cookbook-bulk-update-analyze-project-metrics"
description: "Applies a bulk field update across analyze project metrics records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_project_metrics", "rar_sha256": "923965ce01e57b014f96c75c81306cad7d43e0db50587dfe9ea62bbe5353adb5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_analyze_project_metrics`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_analyze_project_metrics_agent.py` and in the RCI capsule.

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
