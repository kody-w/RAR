---
name: "rar-cowork-cookbook-bulk-update-analyze-production-quality-results"
description: "Applies a bulk field update across analyze production quality results records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_production_quality_results", "rar_sha256": "599cadbbf5c0c276333df9813e39b7ed9a3d650325291f02843c52b55ff6f187", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_analyze_production_quality_results`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_analyze_production_quality_results_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_production_quality_results_agent.py` and embedded as the fenced Python below (sha256 599cadbbf5c0c276…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_production_quality_results_agent.py` first:

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
    "version": '2.0.1',
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
