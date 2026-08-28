---
name: "rar-cowork-cookbook-bulk-update-define-service-risk-management-strategy"
description: "Applies a bulk field update across define service risk management strategy records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_service_risk_management_strategy", "rar_sha256": "d9752a61c9d1e2ecf76c1e65e1e1ad44858b82ee70926ae142b17f0be867bc28", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_service_risk_management_strategy`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_service_risk_management_strategy_agent.py` and in the RCI capsule.

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
