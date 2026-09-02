---
name: "rar-cowork-cookbook-scheduled-brief-perform-a-skill-gap-analysis"
description: "Schedulable morning-brief email summarizing perform a skill gap analysis for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_perform_a_skill_gap_analysis", "rar_sha256": "19afce86f56dda5f93ebd162c5d4f009278094586a0fb4fd91c0a6e480e12970", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_perform_a_skill_gap_analysis_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-perform-a-skill-gap-analysis:f2ef4298a351f3bf66baf9014090aea946e7f69a2edc6c5586ca48f3b7b3c7c1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_perform_a_skill_gap_analysis`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_perform_a_skill_gap_analysis_agent.py` is
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

Perform a skill gap analysis Scheduled Email Brief — Schedulable morning-brief email summarizing perform a skill gap analysis for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-perform-a-skill-gap-analysis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_perform_a_skill_gap_analysis_agent.py` and embedded as the fenced Python below (sha256 19afce86f56dda5f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_perform_a_skill_gap_analysis_agent.py` first:

```bash
python3 scheduled_brief_perform_a_skill_gap_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_perform_a_skill_gap_analysis_agent.py   # or on stdin
python3 scheduled_brief_perform_a_skill_gap_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform a skill gap analysis Scheduled Email Brief — Schedulable morning-brief email summarizing perform a skill gap analysis for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-perform-a-skill-gap-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_perform_a_skill_gap_analysis',
    "version": '2.0.0',
    "display_name": 'Perform a skill gap analysis Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing perform a skill gap analysis for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-perform-a-skill-gap-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-perform-a-skill-gap-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '528bfd0679ce49da',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/perform-a-skill-gap-analysis'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-perform-a-skill-gap-analysis', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefPerformASkillGapAnalysis(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPerformASkillGapAnalysis'
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
    print(ScheduledBriefPerformASkillGapAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
