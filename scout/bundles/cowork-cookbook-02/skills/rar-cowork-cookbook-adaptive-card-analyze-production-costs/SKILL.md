---
name: "rar-cowork-cookbook-adaptive-card-analyze-production-costs"
description: "Produces a reusable Adaptive Card JSON snapshot of analyze production costs status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_production_costs", "rar_sha256": "2d88fd2960a17de2901ac502eca74585998ff3407140820edfc1ea965fe8d0e5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_analyze_production_costs_agent.py` and embedded as the fenced Python below (sha256 2d88fd2960a17de2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_analyze_production_costs_agent.py` first:

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
    "version": '2.0.1',
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
