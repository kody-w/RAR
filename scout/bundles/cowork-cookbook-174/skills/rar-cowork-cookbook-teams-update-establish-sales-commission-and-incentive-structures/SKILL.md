---
name: "rar-cowork-cookbook-teams-update-establish-sales-commission-and-incentive-structures"
description: "Drafts a Teams channel post on establish sales commission and incentive structures status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_establish_sales_commission_and_incentive_structures", "rar_sha256": "ff2bbaf9292c43a6ad54fb99ac07dab2118e94e574fa8d56432956bd5faa3a11", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_establish_sales_commission_and_incentive_structures_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-establish-sales-commission-and-incentive-structures:fa9388c825a0c74492f90dbd41825c0f0d39eb3ae21b4009db65eb288eae4da3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_establish_sales_commission_and_incentive_structures`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_establish_sales_commission_and_incentive_structures_agent.py` is
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
