---
name: "rar-cowork-cookbook-bulk-update-analyze-project-metrics"
description: "Applies a bulk field update across analyze project metrics records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_project_metrics", "rar_sha256": "32a1a9b87b3d849ec86ade4750a4c7e26f7c367867af846ea9441bbb6976c1e0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_project_metrics_agent.py` and embedded as the fenced Python below (sha256 32a1a9b87b3d849e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_project_metrics_agent.py` first:

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
    "version": '2.0.1',
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
