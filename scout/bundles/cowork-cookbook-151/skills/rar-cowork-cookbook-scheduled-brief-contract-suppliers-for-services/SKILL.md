---
name: "rar-cowork-cookbook-scheduled-brief-contract-suppliers-for-services"
description: "Schedulable morning-brief email summarizing contract suppliers for services for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_contract_suppliers_for_services", "rar_sha256": "5d8f59cd8ae1216222cb4dfa0ea7befc63db8fee9b207c5bb3484d5e813a24d3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_contract_suppliers_for_services`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_contract_suppliers_for_services_agent.py` and in the RCI capsule.

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

Contract suppliers for services Scheduled Email Brief — Schedulable morning-brief email summarizing contract suppliers for services for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-contract-suppliers-for-services
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_contract_suppliers_for_services_agent.py` and embedded as the fenced Python below (sha256 5d8f59cd8ae12162…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_contract_suppliers_for_services_agent.py` first:

```bash
python3 scheduled_brief_contract_suppliers_for_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_contract_suppliers_for_services_agent.py   # or on stdin
python3 scheduled_brief_contract_suppliers_for_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Contract suppliers for services Scheduled Email Brief — Schedulable morning-brief email summarizing contract suppliers for services for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-contract-suppliers-for-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_contract_suppliers_for_services',
    "version": '2.0.0',
    "display_name": 'Contract suppliers for services Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing contract suppliers for services for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-contract-suppliers-for-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-contract-suppliers-for-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2735feb334a8748a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/contract-suppliers-for-services'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-contract-suppliers-for-services', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefContractSuppliersForServices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefContractSuppliersForServices'
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
    print(ScheduledBriefContractSuppliersForServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
