---
name: "rar-cowork-cookbook-teams-update-react-to-supply-chain-signals"
description: "Drafts a Teams channel post on react to supply chain signals status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_react_to_supply_chain_signals", "rar_sha256": "b13be839dd72913b3a915864c88dc0083d374ab511ef13bae485a9f97855122e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_react_to_supply_chain_signals_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-react-to-supply-chain-signals:ec5b7bbd945b44d3a2783864bea1f16fcbcd5797b6de6b56ddc2b40d4107f86f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_react_to_supply_chain_signals`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_react_to_supply_chain_signals_agent.py` is
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
