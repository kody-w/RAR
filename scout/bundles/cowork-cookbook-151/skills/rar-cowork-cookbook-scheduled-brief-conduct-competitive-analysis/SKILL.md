---
name: "rar-cowork-cookbook-scheduled-brief-conduct-competitive-analysis"
description: "Schedulable morning-brief email summarizing conduct competitive analysis for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_conduct_competitive_analysis", "rar_sha256": "a1d796d255edb706c13b4eca2bdd09971cfd9ec0c5b35001a1a39c51f1beb663", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_conduct_competitive_analysis`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_conduct_competitive_analysis_agent.py` and in the RCI capsule.

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
