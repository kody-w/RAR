---
name: "rar-cowork-cookbook-scheduled-brief-perform-a-skill-gap-analysis"
description: "Schedulable morning-brief email summarizing perform a skill gap analysis for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_perform_a_skill_gap_analysis", "rar_sha256": "19afce86f56dda5f93ebd162c5d4f009278094586a0fb4fd91c0a6e480e12970", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_perform_a_skill_gap_analysis`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_perform_a_skill_gap_analysis_agent.py` and in the RCI capsule.

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
