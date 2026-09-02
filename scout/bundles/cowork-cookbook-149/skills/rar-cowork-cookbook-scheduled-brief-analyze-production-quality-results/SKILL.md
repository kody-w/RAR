---
name: "rar-cowork-cookbook-scheduled-brief-analyze-production-quality-results"
description: "Schedulable morning-brief email summarizing analyze production quality results for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_production_quality_results", "rar_sha256": "009261234c9fc4e705872ff0206e1e1e86bdfb180409f663dfcca93b4a1fa4c0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_analyze_production_quality_results_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-analyze-production-quality-results:eaf3c0af5c8e58f86a55ed9ea24e32f380d3aa3d6833d8ae9f2a6965104db6f9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_analyze_production_quality_results`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_analyze_production_quality_results_agent.py` is
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
