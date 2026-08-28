---
name: "rar-cowork-cookbook-teams-update-establish-sales-commission-and-incentive-structures"
description: "Drafts a Teams channel post on establish sales commission and incentive structures status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_establish_sales_commission_and_incentive_structures", "rar_sha256": "2713dd3120185dc2a91f01093bb271b17e07ab18439c128cf7d5bb026089b16b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_establish_sales_commission_and_incentive_structures`. The original RAPP
agent is preserved byte-for-byte in `teams_update_establish_sales_commission_and_incentive_structures_agent.py` and in the RCI capsule.

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

Establish sales commission and incentive structures Teams Channel Update — Drafts a Teams channel post on establish sales commission and incentive structures status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-establish-sales-commission-and-incentive-structures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_establish_sales_commission_and_incentive_structures_agent.py` and embedded as the fenced Python below (sha256 2713dd3120185dc2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_establish_sales_commission_and_incentive_structures_agent.py` first:

```bash
python3 teams_update_establish_sales_commission_and_incentive_structures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_establish_sales_commission_and_incentive_structures_agent.py   # or on stdin
python3 teams_update_establish_sales_commission_and_incentive_structures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish sales commission and incentive structures Teams Channel Update — Drafts a Teams channel post on establish sales commission and incentive structures status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-establish-sales-commission-and-incentive-structures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_establish_sales_commission_and_incentive_structures',
    "version": '2.0.1',
    "display_name": 'Establish sales commission and incentive structures Teams Channel Update',
    "description": 'Drafts a Teams channel post on establish sales commission and incentive structures status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-establish-sales-commission-and-incentive-structures',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-establish-sales-commission-and-incentive-structures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5dbf7bb0eb2fab64',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/establish-sales-commission-and-incentive-structures'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/teams-update-establish-sales-commission-and-incentive-structures', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateEstablishSalesCommissionAndIncentiveStructures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateEstablishSalesCommissionAndIncentiveStructures'
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
    print(TeamsUpdateEstablishSalesCommissionAndIncentiveStructures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
