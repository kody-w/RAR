---
name: "rar-cowork-cookbook-adaptive-card-analyze-production-costs"
description: "Produces a reusable Adaptive Card JSON snapshot of analyze production costs status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_production_costs", "rar_sha256": "52912eac50178da0ec983a91d7def47caed89e52fd5fbc0fd8d425c48a1a2a82", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_analyze_production_costs`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_analyze_production_costs_agent.py` and in the RCI capsule.

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

Analyze production costs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of analyze production costs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-production-costs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_analyze_production_costs_agent.py` and embedded as the fenced Python below (sha256 52912eac50178da0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_analyze_production_costs_agent.py` first:

```bash
python3 adaptive_card_analyze_production_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_analyze_production_costs_agent.py   # or on stdin
python3 adaptive_card_analyze_production_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze production costs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of analyze production costs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-production-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_analyze_production_costs',
    "version": '2.0.0',
    "display_name": 'Analyze production costs Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of analyze production costs status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-analyze-production-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-analyze-production-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ed9ebef808b9d724',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/analyze-production-costs'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/adaptive-card-analyze-production-costs', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardAnalyzeProductionCosts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAnalyzeProductionCosts'
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
    print(AdaptiveCardAnalyzeProductionCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
