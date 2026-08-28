---
name: "rar-cowork-cookbook-scheduled-brief-perform-a-skill-gap-analysis"
description: "Schedulable morning-brief email summarizing perform a skill gap analysis for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_perform_a_skill_gap_analysis", "rar_sha256": "6c768919d10d63018dcf5343b43b6614aa5a086b045678489900f43e49e8f1d5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_perform_a_skill_gap_analysis_agent.py` and embedded as the fenced Python below (sha256 6c768919d10d6301…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_perform_a_skill_gap_analysis_agent.py` first:

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
    "version": '2.0.1',
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
