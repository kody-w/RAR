---
name: "rar-cowork-cookbook-scheduled-brief-develop-long-range-plan"
description: "Schedulable morning-brief email summarizing develop long-range plan for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_long_range_plan", "rar_sha256": "4bdfcc4e6cce452593d4e76cea53afcd60812783526748092ede881cf928e093", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_long_range_plan_agent.py` and embedded as the fenced Python below (sha256 4bdfcc4e6cce4525…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_long_range_plan_agent.py` first:

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
    "version": '2.0.0',
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
