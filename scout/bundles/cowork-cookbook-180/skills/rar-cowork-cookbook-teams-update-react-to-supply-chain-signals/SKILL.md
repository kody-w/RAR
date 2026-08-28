---
name: "rar-cowork-cookbook-teams-update-react-to-supply-chain-signals"
description: "Drafts a Teams channel post on react to supply chain signals status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_react_to_supply_chain_signals", "rar_sha256": "b9d2867c4094693833bc67bf13586a14133f42c0ef10532bd840d4476727c860", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_react_to_supply_chain_signals`. The original RAPP
agent is preserved byte-for-byte in `teams_update_react_to_supply_chain_signals_agent.py` and in the RCI capsule.

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

React to supply chain signals Teams Channel Update — Drafts a Teams channel post on react to supply chain signals status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-react-to-supply-chain-signals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_react_to_supply_chain_signals_agent.py` and embedded as the fenced Python below (sha256 b9d2867c40946938…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_react_to_supply_chain_signals_agent.py` first:

```bash
python3 teams_update_react_to_supply_chain_signals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_react_to_supply_chain_signals_agent.py   # or on stdin
python3 teams_update_react_to_supply_chain_signals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
React to supply chain signals Teams Channel Update — Drafts a Teams channel post on react to supply chain signals status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-react-to-supply-chain-signals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_react_to_supply_chain_signals',
    "version": '2.0.1',
    "display_name": 'React to supply chain signals Teams Channel Update',
    "description": 'Drafts a Teams channel post on react to supply chain signals status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-react-to-supply-chain-signals',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-react-to-supply-chain-signals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5d69728f126d5950',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/react-to-supply-chain-signals'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-react-to-supply-chain-signals', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateReactToSupplyChainSignals(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateReactToSupplyChainSignals'
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
    print(TeamsUpdateReactToSupplyChainSignals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
