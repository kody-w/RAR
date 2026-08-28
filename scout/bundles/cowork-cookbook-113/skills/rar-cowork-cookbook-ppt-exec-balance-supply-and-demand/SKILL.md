---
name: "rar-cowork-cookbook-ppt-exec-balance-supply-and-demand"
description: "Generates an executive-ready PowerPoint deck on balance supply and demand status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_balance_supply_and_demand", "rar_sha256": "55bbb3d00cb48d56dbeb627f3b81f780cc0f460c9f363faccf69bb461595ba7f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_balance_supply_and_demand`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_balance_supply_and_demand_agent.py` and in the RCI capsule.

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

Balance supply and demand Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on balance supply and demand status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-balance-supply-and-demand
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_balance_supply_and_demand_agent.py` and embedded as the fenced Python below (sha256 55bbb3d00cb48d56…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_balance_supply_and_demand_agent.py` first:

```bash
python3 ppt_exec_balance_supply_and_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_balance_supply_and_demand_agent.py   # or on stdin
python3 ppt_exec_balance_supply_and_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Balance supply and demand Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on balance supply and demand status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-balance-supply-and-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_balance_supply_and_demand',
    "version": '2.0.0',
    "display_name": 'Balance supply and demand Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on balance supply and demand status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-balance-supply-and-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-balance-supply-and-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '87985becffdb4ccd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/balance-supply-and-demand'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-balance-supply-and-demand', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecBalanceSupplyAndDemand(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecBalanceSupplyAndDemand'
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
    print(PptExecBalanceSupplyAndDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
