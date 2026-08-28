---
name: "rar-cowork-cookbook-scheduled-brief-conduct-competitive-analysis"
description: "Schedulable morning-brief email summarizing conduct competitive analysis for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_conduct_competitive_analysis", "rar_sha256": "7b363ab650609652b60cc78760c6f00b39acd72e5fe6546f9f565b22c10cbce0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_conduct_competitive_analysis_agent.py` and embedded as the fenced Python below (sha256 7b363ab650609652…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_conduct_competitive_analysis_agent.py` first:

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
    "version": '2.0.1',
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
