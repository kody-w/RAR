---
name: "rar-cowork-cookbook-bulk-update-define-service-risk-management-strategy"
description: "Applies a bulk field update across define service risk management strategy records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_service_risk_management_strategy", "rar_sha256": "d9752a61c9d1e2ecf76c1e65e1e1ad44858b82ee70926ae142b17f0be867bc28", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_define_service_risk_management_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-define-service-risk-management-strategy:07f053af8c4572dc9be546a9e536503195d564124249b354c4167fdab89c7010", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_define_service_risk_management_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_define_service_risk_management_strategy_agent.py` is
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

Define service risk management strategy Bulk Field Update — Applies a bulk field update across define service risk management strategy records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-service-risk-management-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_service_risk_management_strategy_agent.py` and embedded as the fenced Python below (sha256 d9752a61c9d1e2ec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_service_risk_management_strategy_agent.py` first:

```bash
python3 bulk_update_define_service_risk_management_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_service_risk_management_strategy_agent.py   # or on stdin
python3 bulk_update_define_service_risk_management_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service risk management strategy Bulk Field Update — Applies a bulk field update across define service risk management strategy records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-service-risk-management-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_service_risk_management_strategy',
    "version": '2.0.0',
    "display_name": 'Define service risk management strategy Bulk Field Update',
    "description": 'Applies a bulk field update across define service risk management strategy records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-service-risk-management-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-service-risk-management-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a36d38c696b35ab9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/define-service-risk-management-strategy'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-define-service-risk-management-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDefineServiceRiskManagementStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineServiceRiskManagementStrategy'
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
    print(BulkUpdateDefineServiceRiskManagementStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
