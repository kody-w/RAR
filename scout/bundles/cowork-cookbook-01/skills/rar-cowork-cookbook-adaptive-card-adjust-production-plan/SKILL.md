---
name: "rar-cowork-cookbook-adaptive-card-adjust-production-plan"
description: "Produces a reusable Adaptive Card JSON snapshot of adjust production plan status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_adjust_production_plan", "rar_sha256": "a6b0d7069bc960382c3a44aabd738c078304f3524050f12453120f4fb8270f64", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_adjust_production_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-adjust-production-plan:613aac8db78a6ff80c171fd24f8bb57bf818a1feda3609048440355332725300", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_adjust_production_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_adjust_production_plan_agent.py` is
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

Adjust production plan Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of adjust production plan status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-adjust-production-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_adjust_production_plan_agent.py` and embedded as the fenced Python below (sha256 a6b0d7069bc96038…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_adjust_production_plan_agent.py` first:

```bash
python3 adaptive_card_adjust_production_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_adjust_production_plan_agent.py   # or on stdin
python3 adaptive_card_adjust_production_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Adjust production plan Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of adjust production plan status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-adjust-production-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_adjust_production_plan',
    "version": '2.0.0',
    "display_name": 'Adjust production plan Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of adjust production plan status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-adjust-production-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-adjust-production-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2754295b0dcf60aa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/adjust-production-plan'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/adaptive-card-adjust-production-plan', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardAdjustProductionPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAdjustProductionPlan'
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
    print(AdaptiveCardAdjustProductionPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
