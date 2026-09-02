---
name: "rar-cowork-cookbook-adaptive-card-develop-a-business-continuity-plan"
description: "Produces a reusable Adaptive Card JSON snapshot of develop a business continuity plan status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_a_business_continuity_plan", "rar_sha256": "d2ebc9f7b35ec0591ca1ca06a720093d6116f954eab03996b0b8450dcb9e38db", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_develop_a_business_continuity_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-develop-a-business-continuity-plan:d7ac853ba31060f34476bc039e1bf5e21116bf0994ad1134ae2f67304d0cc950", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_develop_a_business_continuity_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_develop_a_business_continuity_plan_agent.py` is
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

Develop a business continuity plan Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop a business continuity plan status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-a-business-continuity-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_develop_a_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 d2ebc9f7b35ec059…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_develop_a_business_continuity_plan_agent.py` first:

```bash
python3 adaptive_card_develop_a_business_continuity_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_develop_a_business_continuity_plan_agent.py   # or on stdin
python3 adaptive_card_develop_a_business_continuity_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop a business continuity plan Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of develop a business continuity plan status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-develop-a-business-continuity-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_develop_a_business_continuity_plan',
    "version": '2.0.0',
    "display_name": 'Develop a business continuity plan Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of develop a business continuity plan status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-develop-a-business-continuity-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-develop-a-business-continuity-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4d2399e203219a3f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/develop-a-business-continuity-plan'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-develop-a-business-continuity-plan', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardDevelopABusinessContinuityPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDevelopABusinessContinuityPlan'
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
    print(AdaptiveCardDevelopABusinessContinuityPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
