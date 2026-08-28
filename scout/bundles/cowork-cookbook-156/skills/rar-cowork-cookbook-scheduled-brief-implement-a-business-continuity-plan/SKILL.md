---
name: "rar-cowork-cookbook-scheduled-brief-implement-a-business-continuity-plan"
description: "Schedulable morning-brief email summarizing implement a business continuity plan for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_implement_a_business_continuity_plan", "rar_sha256": "5c7a05dc6ad9995bcc9692270964d367901b443a28ec9bb8379ff0ba17671f5a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_implement_a_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 5c7a05dc6ad9995b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_implement_a_business_continuity_plan_agent.py` first:

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
    "version": '2.0.0',
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
