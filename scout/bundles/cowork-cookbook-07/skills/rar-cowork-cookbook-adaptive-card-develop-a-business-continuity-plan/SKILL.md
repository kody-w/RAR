---
name: "rar-cowork-cookbook-adaptive-card-develop-a-business-continuity-plan"
description: "Produces a reusable Adaptive Card JSON snapshot of develop a business continuity plan status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_develop_a_business_continuity_plan", "rar_sha256": "d2ebc9f7b35ec0591ca1ca06a720093d6116f954eab03996b0b8450dcb9e38db", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_develop_a_business_continuity_plan`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_develop_a_business_continuity_plan_agent.py` and in the RCI capsule.

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
