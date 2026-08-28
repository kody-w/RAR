---
name: "rar-cowork-cookbook-teams-update-process-customer-prepayments"
description: "Drafts a Teams channel post on process customer prepayments status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_process_customer_prepayments", "rar_sha256": "e391319fb958affbf2db055a33b55773fe6b90f4f5557a74e221ee0930fa9cf0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_process_customer_prepayments`. The original RAPP
agent is preserved byte-for-byte in `teams_update_process_customer_prepayments_agent.py` and in the RCI capsule.

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

Process customer prepayments Teams Channel Update — Drafts a Teams channel post on process customer prepayments status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-customer-prepayments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_process_customer_prepayments_agent.py` and embedded as the fenced Python below (sha256 e391319fb958affb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_process_customer_prepayments_agent.py` first:

```bash
python3 teams_update_process_customer_prepayments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_process_customer_prepayments_agent.py   # or on stdin
python3 teams_update_process_customer_prepayments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer prepayments Teams Channel Update — Drafts a Teams channel post on process customer prepayments status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-customer-prepayments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_process_customer_prepayments',
    "version": '2.0.0',
    "display_name": 'Process customer prepayments Teams Channel Update',
    "description": 'Drafts a Teams channel post on process customer prepayments status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-process-customer-prepayments',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-process-customer-prepayments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '45b62e8e59e1516b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-prepayments'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-process-customer-prepayments', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class TeamsUpdateProcessCustomerPrepayments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateProcessCustomerPrepayments'
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
    print(TeamsUpdateProcessCustomerPrepayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
