---
name: "rar-cowork-cookbook-teams-update-develop-product-strategy"
description: "Drafts a Teams channel post on develop product strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_product_strategy", "rar_sha256": "f2c9dc4b56ce02e16d5a6a946d78d02cda2a859cf9832f55a33e1a8bb5287d08", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_product_strategy_agent.py` and embedded as the fenced Python below (sha256 f2c9dc4b56ce02e1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_product_strategy_agent.py` first:

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
    "version": '2.0.0',
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
