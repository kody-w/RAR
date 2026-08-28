---
name: "rar-cowork-cookbook-scheduled-brief-implement-a-business-continuity-plan"
description: "Schedulable morning-brief email summarizing implement a business continuity plan for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_implement_a_business_continuity_plan", "rar_sha256": "24836d4490563591333cbc80a8fe548da026aa52e96c51b388b9325351b26e39", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_implement_a_business_continuity_plan`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_implement_a_business_continuity_plan_agent.py` and in the RCI capsule.

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

Implement a business continuity plan Scheduled Email Brief — Schedulable morning-brief email summarizing implement a business continuity plan for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-implement-a-business-continuity-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_implement_a_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 24836d4490563591…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_implement_a_business_continuity_plan_agent.py` first:

```bash
python3 scheduled_brief_implement_a_business_continuity_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_implement_a_business_continuity_plan_agent.py   # or on stdin
python3 scheduled_brief_implement_a_business_continuity_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement a business continuity plan Scheduled Email Brief — Schedulable morning-brief email summarizing implement a business continuity plan for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-implement-a-business-continuity-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_implement_a_business_continuity_plan',
    "version": '2.0.1',
    "display_name": 'Implement a business continuity plan Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing implement a business continuity plan for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-implement-a-business-continuity-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-implement-a-business-continuity-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd90c5b1ac2025c6f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/implement-a-business-continuity-plan'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-implement-a-business-continuity-plan', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefImplementABusinessContinuityPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefImplementABusinessContinuityPlan'
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
    print(ScheduledBriefImplementABusinessContinuityPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
