---
name: "rar-cowork-cookbook-teams-update-react-to-supply-chain-signals"
description: "Drafts a Teams channel post on react to supply chain signals status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_react_to_supply_chain_signals", "rar_sha256": "b13be839dd72913b3a915864c88dc0083d374ab511ef13bae485a9f97855122e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_react_to_supply_chain_signals_agent.py` and embedded as the fenced Python below (sha256 b13be839dd72913b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_react_to_supply_chain_signals_agent.py` first:

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
    "version": '2.0.0',
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
