---
name: "rar-cowork-cookbook-teams-update-contract-suppliers-for-services"
description: "Drafts a Teams channel post on contract suppliers for services status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_contract_suppliers_for_services", "rar_sha256": "71d6de08d6a594efe8d5d86af08620ddc6a49c7e2a35aca9ee18853d790bc714", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_contract_suppliers_for_services_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-contract-suppliers-for-services:b91c9116baef967191df92bac589026de5e1438e0f341a3d928b5436a12d6ac3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_contract_suppliers_for_services`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_contract_suppliers_for_services_agent.py` is
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

Contract suppliers for services Teams Channel Update — Drafts a Teams channel post on contract suppliers for services status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-contract-suppliers-for-services
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_contract_suppliers_for_services_agent.py` and embedded as the fenced Python below (sha256 71d6de08d6a594ef…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_contract_suppliers_for_services_agent.py` first:

```bash
python3 teams_update_contract_suppliers_for_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_contract_suppliers_for_services_agent.py   # or on stdin
python3 teams_update_contract_suppliers_for_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Contract suppliers for services Teams Channel Update — Drafts a Teams channel post on contract suppliers for services status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-contract-suppliers-for-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_contract_suppliers_for_services',
    "version": '2.0.0',
    "display_name": 'Contract suppliers for services Teams Channel Update',
    "description": 'Drafts a Teams channel post on contract suppliers for services status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-contract-suppliers-for-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-contract-suppliers-for-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '02b5f64d501879b9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/contract-suppliers-for-services'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-contract-suppliers-for-services', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateContractSuppliersForServices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateContractSuppliersForServices'
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
    print(TeamsUpdateContractSuppliersForServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
