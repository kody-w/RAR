---
name: "rar-cowork-cookbook-scheduled-brief-conduct-competitive-analysis"
description: "Schedulable morning-brief email summarizing conduct competitive analysis for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_conduct_competitive_analysis", "rar_sha256": "a1d796d255edb706c13b4eca2bdd09971cfd9ec0c5b35001a1a39c51f1beb663", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_conduct_competitive_analysis_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-conduct-competitive-analysis:315ba171eb329fa1e31e1b7bfdb66e98d97aa4bd81e0e598f2c07a44afca1bdf", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_conduct_competitive_analysis`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_conduct_competitive_analysis_agent.py` is
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

Conduct competitive analysis Scheduled Email Brief — Schedulable morning-brief email summarizing conduct competitive analysis for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-conduct-competitive-analysis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_conduct_competitive_analysis_agent.py` and embedded as the fenced Python below (sha256 a1d796d255edb706…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_conduct_competitive_analysis_agent.py` first:

```bash
python3 scheduled_brief_conduct_competitive_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_conduct_competitive_analysis_agent.py   # or on stdin
python3 scheduled_brief_conduct_competitive_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct competitive analysis Scheduled Email Brief — Schedulable morning-brief email summarizing conduct competitive analysis for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-conduct-competitive-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_conduct_competitive_analysis',
    "version": '2.0.0',
    "display_name": 'Conduct competitive analysis Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing conduct competitive analysis for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-conduct-competitive-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-conduct-competitive-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '233da0d910dba42d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/conduct-competitive-analysis'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/scheduled-brief-conduct-competitive-analysis', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefConductCompetitiveAnalysis(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefConductCompetitiveAnalysis'
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
    print(ScheduledBriefConductCompetitiveAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
