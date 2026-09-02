---
name: "rar-cowork-cookbook-teams-update-report-production-output"
description: "Drafts a Teams channel post on report production output status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_report_production_output", "rar_sha256": "545edc14b684915efb9fb33c8b413e0bc583375d2a24b28d44204d716ab12d66", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_report_production_output_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-report-production-output:1cf8f6650595a519180ed1fe5061e094d8926ba48dab3115d92f4f4c4dbf00ce", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_report_production_output`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_report_production_output_agent.py` is
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

Report production output Teams Channel Update — Drafts a Teams channel post on report production output status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-report-production-output
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_report_production_output_agent.py` and embedded as the fenced Python below (sha256 545edc14b684915e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_report_production_output_agent.py` first:

```bash
python3 teams_update_report_production_output_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_report_production_output_agent.py   # or on stdin
python3 teams_update_report_production_output_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report production output Teams Channel Update — Drafts a Teams channel post on report production output status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-report-production-output
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_report_production_output',
    "version": '2.0.0',
    "display_name": 'Report production output Teams Channel Update',
    "description": 'Drafts a Teams channel post on report production output status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-report-production-output',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-report-production-output',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f11de26cf197494a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/report-production-output'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/teams-update-report-production-output', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateReportProductionOutput(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateReportProductionOutput'
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
    print(TeamsUpdateReportProductionOutput().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
