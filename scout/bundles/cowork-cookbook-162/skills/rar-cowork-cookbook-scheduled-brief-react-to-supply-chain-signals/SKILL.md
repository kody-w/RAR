---
name: "rar-cowork-cookbook-scheduled-brief-react-to-supply-chain-signals"
description: "Schedulable morning-brief email summarizing react to supply chain signals for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_react_to_supply_chain_signals", "rar_sha256": "b8bc4a5a1ea0e00044be8d3befd4fae5a151ca019a1a2680e76ca1f8dfe81311", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_react_to_supply_chain_signals`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_react_to_supply_chain_signals_agent.py` and in the RCI capsule.

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

React to supply chain signals Scheduled Email Brief — Schedulable morning-brief email summarizing react to supply chain signals for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-react-to-supply-chain-signals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_react_to_supply_chain_signals_agent.py` and embedded as the fenced Python below (sha256 b8bc4a5a1ea0e000…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_react_to_supply_chain_signals_agent.py` first:

```bash
python3 scheduled_brief_react_to_supply_chain_signals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_react_to_supply_chain_signals_agent.py   # or on stdin
python3 scheduled_brief_react_to_supply_chain_signals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
React to supply chain signals Scheduled Email Brief — Schedulable morning-brief email summarizing react to supply chain signals for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-react-to-supply-chain-signals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_react_to_supply_chain_signals',
    "version": '2.0.0',
    "display_name": 'React to supply chain signals Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing react to supply chain signals for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-react-to-supply-chain-signals',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-react-to-supply-chain-signals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b7cd0f7a1798d6b8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/react-to-supply-chain-signals'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-react-to-supply-chain-signals', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefReactToSupplyChainSignals(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefReactToSupplyChainSignals'
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
    print(ScheduledBriefReactToSupplyChainSignals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
