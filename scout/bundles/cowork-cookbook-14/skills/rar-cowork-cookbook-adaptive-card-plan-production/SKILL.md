---
name: "rar-cowork-cookbook-adaptive-card-plan-production"
description: "Produces a reusable Adaptive Card JSON snapshot of plan production status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_production", "rar_sha256": "c7cb69a5f7d29012bb8a9f71246a2f5a7775cdfc93415f6bd6faf3cb25cb86d6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_plan_production_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-plan-production:cbdce09490752053fb0915f2987307b721cb9cc2156861c0b5e0a7577dce770c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_plan_production`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_plan_production_agent.py` is
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

Plan production Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of plan production status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-production
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_plan_production_agent.py` and embedded as the fenced Python below (sha256 c7cb69a5f7d29012…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_plan_production_agent.py` first:

```bash
python3 adaptive_card_plan_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_plan_production_agent.py   # or on stdin
python3 adaptive_card_plan_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan production Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of plan production status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_plan_production',
    "version": '2.0.0',
    "display_name": 'Plan production Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of plan production status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-plan-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-plan-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b604d47ba6c87be3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-production'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/adaptive-card-plan-production', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardPlanProduction(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardPlanProduction'
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
    print(AdaptiveCardPlanProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
