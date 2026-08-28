---
name: "rar-cowork-cookbook-scheduled-brief-analyze-production-quality-results"
description: "Schedulable morning-brief email summarizing analyze production quality results for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_production_quality_results", "rar_sha256": "009261234c9fc4e705872ff0206e1e1e86bdfb180409f663dfcca93b4a1fa4c0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_analyze_production_quality_results`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_analyze_production_quality_results_agent.py` and in the RCI capsule.

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

Analyze production quality results Scheduled Email Brief — Schedulable morning-brief email summarizing analyze production quality results for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-production-quality-results
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_production_quality_results_agent.py` and embedded as the fenced Python below (sha256 009261234c9fc4e7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_production_quality_results_agent.py` first:

```bash
python3 scheduled_brief_analyze_production_quality_results_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_analyze_production_quality_results_agent.py   # or on stdin
python3 scheduled_brief_analyze_production_quality_results_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze production quality results Scheduled Email Brief — Schedulable morning-brief email summarizing analyze production quality results for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-production-quality-results
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_analyze_production_quality_results',
    "version": '2.0.0',
    "display_name": 'Analyze production quality results Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing analyze production quality results for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-analyze-production-quality-results',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-analyze-production-quality-results',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b2f4f474305db194',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/analyze-production-quality-results'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/scheduled-brief-analyze-production-quality-results', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefAnalyzeProductionQualityResults(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAnalyzeProductionQualityResults'
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
    print(ScheduledBriefAnalyzeProductionQualityResults().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
