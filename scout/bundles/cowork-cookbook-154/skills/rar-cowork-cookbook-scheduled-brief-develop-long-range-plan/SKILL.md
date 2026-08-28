---
name: "rar-cowork-cookbook-scheduled-brief-develop-long-range-plan"
description: "Schedulable morning-brief email summarizing develop long-range plan for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_long_range_plan", "rar_sha256": "a56a2b756ac7890753a477dd1f267fca3e7f90626da90f28cc6bc3ef8423bee1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_develop_long_range_plan`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_develop_long_range_plan_agent.py` and in the RCI capsule.

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

Develop long-range plan Scheduled Email Brief — Schedulable morning-brief email summarizing develop long-range plan for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-long-range-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_long_range_plan_agent.py` and embedded as the fenced Python below (sha256 a56a2b756ac78907…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_long_range_plan_agent.py` first:

```bash
python3 scheduled_brief_develop_long_range_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_long_range_plan_agent.py   # or on stdin
python3 scheduled_brief_develop_long_range_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop long-range plan Scheduled Email Brief — Schedulable morning-brief email summarizing develop long-range plan for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-long-range-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_develop_long_range_plan',
    "version": '2.0.1',
    "display_name": 'Develop long-range plan Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing develop long-range plan for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-develop-long-range-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-develop-long-range-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1e5ed0185cc1fabf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-long-range-plan'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-develop-long-range-plan', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefDevelopLongRangePlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopLongRangePlan'
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
    print(ScheduledBriefDevelopLongRangePlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
