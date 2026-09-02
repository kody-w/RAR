---
name: "rar-cowork-cookbook-scheduled-brief-react-to-supply-chain-signals"
description: "Schedulable morning-brief email summarizing react to supply chain signals for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_react_to_supply_chain_signals", "rar_sha256": "b8bc4a5a1ea0e00044be8d3befd4fae5a151ca019a1a2680e76ca1f8dfe81311", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_react_to_supply_chain_signals_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-react-to-supply-chain-signals:a3cca049c72960eb7dcfa7b29718873df9b7c99af0f6efaedfe1763ba9740218", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_react_to_supply_chain_signals`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_react_to_supply_chain_signals_agent.py` is
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
