---
name: "rar-cowork-cookbook-teams-update-establish-sales-commission-and-incentive-structures"
description: "Drafts a Teams channel post on establish sales commission and incentive structures status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_establish_sales_commission_and_incentive_structures", "rar_sha256": "ff2bbaf9292c43a6ad54fb99ac07dab2118e94e574fa8d56432956bd5faa3a11", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_establish_sales_commission_and_incentive_structures_agent.py` and embedded as the fenced Python below (sha256 ff2bbaf9292c43a6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_establish_sales_commission_and_incentive_structures_agent.py` first:

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
    "version": '2.0.0',
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
