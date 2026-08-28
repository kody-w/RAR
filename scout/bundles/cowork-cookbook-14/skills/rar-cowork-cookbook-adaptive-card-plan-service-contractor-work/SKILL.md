---
name: "rar-cowork-cookbook-adaptive-card-plan-service-contractor-work"
description: "Produces a reusable Adaptive Card JSON snapshot of plan service contractor work status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_service_contractor_work", "rar_sha256": "3a88dcde032e78736992e9dacae4421a3d353e98c85ce97e3dd3771e39c0fa30", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_plan_service_contractor_work`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_plan_service_contractor_work_agent.py` and in the RCI capsule.

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

Plan service contractor work Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of plan service contractor work status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-service-contractor-work
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_plan_service_contractor_work_agent.py` and embedded as the fenced Python below (sha256 3a88dcde032e7873…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_plan_service_contractor_work_agent.py` first:

```bash
python3 adaptive_card_plan_service_contractor_work_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_plan_service_contractor_work_agent.py   # or on stdin
python3 adaptive_card_plan_service_contractor_work_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan service contractor work Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of plan service contractor work status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-service-contractor-work
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_plan_service_contractor_work',
    "version": '2.0.0',
    "display_name": 'Plan service contractor work Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of plan service contractor work status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-plan-service-contractor-work',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-plan-service-contractor-work',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b14d8887c3d5e81d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/plan-service-contractor-work'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/adaptive-card-plan-service-contractor-work', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardPlanServiceContractorWork(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardPlanServiceContractorWork'
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
    print(AdaptiveCardPlanServiceContractorWork().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
