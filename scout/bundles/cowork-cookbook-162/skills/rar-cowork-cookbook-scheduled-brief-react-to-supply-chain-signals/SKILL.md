---
name: "rar-cowork-cookbook-scheduled-brief-react-to-supply-chain-signals"
description: "Schedulable morning-brief email summarizing react to supply chain signals for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_react_to_supply_chain_signals", "rar_sha256": "c458fda554b1de6ca8d97f2f1d3a30e7d148384c032a59aa9061a580f8eb0176", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_react_to_supply_chain_signals_agent.py` and embedded as the fenced Python below (sha256 c458fda554b1de6c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_react_to_supply_chain_signals_agent.py` first:

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
    "version": '2.0.1',
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
