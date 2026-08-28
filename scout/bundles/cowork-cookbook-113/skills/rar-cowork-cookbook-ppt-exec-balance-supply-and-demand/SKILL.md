---
name: "rar-cowork-cookbook-ppt-exec-balance-supply-and-demand"
description: "Generates an executive-ready PowerPoint deck on balance supply and demand status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_balance_supply_and_demand", "rar_sha256": "3ddd978ed7314df5ef98577c3a31918212069cedf426ed74354141da1405d666", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_balance_supply_and_demand_agent.py` and embedded as the fenced Python below (sha256 3ddd978ed7314df5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_balance_supply_and_demand_agent.py` first:

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
    "version": '2.0.1',
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
