---
name: "rar-cowork-cookbook-teams-update-develop-product-strategy"
description: "Drafts a Teams channel post on develop product strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_product_strategy", "rar_sha256": "8bed2a049098be94730399218d327c4fa4d7923844f5f9eb3d5b809b5c783c82", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_develop_product_strategy`. The original RAPP
agent is preserved byte-for-byte in `teams_update_develop_product_strategy_agent.py` and in the RCI capsule.

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

Develop product strategy Teams Channel Update — Drafts a Teams channel post on develop product strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-product-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_product_strategy_agent.py` and embedded as the fenced Python below (sha256 8bed2a049098be94…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_product_strategy_agent.py` first:

```bash
python3 teams_update_develop_product_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_product_strategy_agent.py   # or on stdin
python3 teams_update_develop_product_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product strategy Teams Channel Update — Drafts a Teams channel post on develop product strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-product-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_product_strategy',
    "version": '2.0.1',
    "display_name": 'Develop product strategy Teams Channel Update',
    "description": 'Drafts a Teams channel post on develop product strategy status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-develop-product-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-product-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2462aa0d27b90da1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-product-strategy'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-develop-product-strategy', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateDevelopProductStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopProductStrategy'
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
    print(TeamsUpdateDevelopProductStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
