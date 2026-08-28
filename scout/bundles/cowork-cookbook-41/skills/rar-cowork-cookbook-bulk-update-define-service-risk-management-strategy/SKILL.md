---
name: "rar-cowork-cookbook-bulk-update-define-service-risk-management-strategy"
description: "Applies a bulk field update across define service risk management strategy records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_service_risk_management_strategy", "rar_sha256": "71c018abb2efab48e793d030c7827748b92bde117716773743304ec8a2a1baba", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_service_risk_management_strategy_agent.py` and embedded as the fenced Python below (sha256 71c018abb2efab48…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_service_risk_management_strategy_agent.py` first:

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
    "version": '2.0.1',
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
