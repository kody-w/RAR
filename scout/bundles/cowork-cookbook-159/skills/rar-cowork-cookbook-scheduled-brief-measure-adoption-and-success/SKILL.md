---
name: "rar-cowork-cookbook-scheduled-brief-measure-adoption-and-success"
description: "Schedulable morning-brief email summarizing measure adoption and success for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_measure_adoption_and_success", "rar_sha256": "054b03a54c45e1bb68c7b8dab878edbdd2a50e00e373e4a0afd581bc7c5520ab", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_measure_adoption_and_success`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_measure_adoption_and_success_agent.py` and in the RCI capsule.

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

Measure adoption and success Scheduled Email Brief — Schedulable morning-brief email summarizing measure adoption and success for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-measure-adoption-and-success
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_measure_adoption_and_success_agent.py` and embedded as the fenced Python below (sha256 054b03a54c45e1bb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_measure_adoption_and_success_agent.py` first:

```bash
python3 scheduled_brief_measure_adoption_and_success_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_measure_adoption_and_success_agent.py   # or on stdin
python3 scheduled_brief_measure_adoption_and_success_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure adoption and success Scheduled Email Brief — Schedulable morning-brief email summarizing measure adoption and success for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-measure-adoption-and-success
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_measure_adoption_and_success',
    "version": '2.0.1',
    "display_name": 'Measure adoption and success Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing measure adoption and success for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-measure-adoption-and-success',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-measure-adoption-and-success',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'acfb59770760788f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/measure-adoption-and-success'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-measure-adoption-and-success', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefMeasureAdoptionAndSuccess(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMeasureAdoptionAndSuccess'
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
    print(ScheduledBriefMeasureAdoptionAndSuccess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
