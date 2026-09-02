---
name: "rar-cowork-cookbook-scheduled-brief-contract-suppliers-for-services"
description: "Schedulable morning-brief email summarizing contract suppliers for services for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_contract_suppliers_for_services", "rar_sha256": "5d8f59cd8ae1216222cb4dfa0ea7befc63db8fee9b207c5bb3484d5e813a24d3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_contract_suppliers_for_services_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-contract-suppliers-for-services:8c577e6bc949a1a70549e51f04e37a590dc69a43fd572e975c7f0fb31b3f7266", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_contract_suppliers_for_services`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_contract_suppliers_for_services_agent.py` is
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
