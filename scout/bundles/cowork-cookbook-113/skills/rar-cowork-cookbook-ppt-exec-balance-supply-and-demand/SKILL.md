---
name: "rar-cowork-cookbook-ppt-exec-balance-supply-and-demand"
description: "Generates an executive-ready PowerPoint deck on balance supply and demand status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_balance_supply_and_demand", "rar_sha256": "55bbb3d00cb48d56dbeb627f3b81f780cc0f460c9f363faccf69bb461595ba7f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_balance_supply_and_demand_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-balance-supply-and-demand:6083fb6641cb9c0cb44c988276ad6ccb068d749b74a29da866793b00943854b1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_balance_supply_and_demand`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_balance_supply_and_demand_agent.py` is
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
