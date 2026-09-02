---
name: "rar-cowork-cookbook-adaptive-card-plan-service-contractor-work"
description: "Produces a reusable Adaptive Card JSON snapshot of plan service contractor work status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_service_contractor_work", "rar_sha256": "3a88dcde032e78736992e9dacae4421a3d353e98c85ce97e3dd3771e39c0fa30", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_plan_service_contractor_work_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-plan-service-contractor-work:02292d5ddf5a6ffb683d7b69211b11555d15a01db0d8b28c7b8a2da138aad5e0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_plan_service_contractor_work`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_plan_service_contractor_work_agent.py` is
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
