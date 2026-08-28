---
name: "rar-cowork-cookbook-scheduled-brief-analyze-production-quality-results"
description: "Schedulable morning-brief email summarizing analyze production quality results for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_production_quality_results", "rar_sha256": "8bd5d10cf6c477739c4df4294e17fc02d5cad0d77d1f5bb85a345c70c14c4aaf", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_production_quality_results_agent.py` and embedded as the fenced Python below (sha256 8bd5d10cf6c47773…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_production_quality_results_agent.py` first:

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
    "version": '2.0.1',
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
