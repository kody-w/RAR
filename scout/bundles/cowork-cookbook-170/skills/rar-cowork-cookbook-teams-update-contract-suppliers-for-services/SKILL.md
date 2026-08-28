---
name: "rar-cowork-cookbook-teams-update-contract-suppliers-for-services"
description: "Drafts a Teams channel post on contract suppliers for services status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_contract_suppliers_for_services", "rar_sha256": "dda9ef273b1d424601d83c09af83ff182a4a8b03a39e2074367bba8079a48b59", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_contract_suppliers_for_services`. The original RAPP
agent is preserved byte-for-byte in `teams_update_contract_suppliers_for_services_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_contract_suppliers_for_services_agent.py` and embedded as the fenced Python below (sha256 dda9ef273b1d4246…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_contract_suppliers_for_services_agent.py` first:

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
    "version": '2.0.1',
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
