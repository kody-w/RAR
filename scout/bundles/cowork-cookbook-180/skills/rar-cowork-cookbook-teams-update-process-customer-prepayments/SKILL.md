---
name: "rar-cowork-cookbook-teams-update-process-customer-prepayments"
description: "Drafts a Teams channel post on process customer prepayments status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_process_customer_prepayments", "rar_sha256": "727d27b1af1c1b9a394b1574fd415323d1611d5e0ecb0149ad2a500bf69ea9ae", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_process_customer_prepayments_agent.py` and embedded as the fenced Python below (sha256 727d27b1af1c1b9a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_process_customer_prepayments_agent.py` first:

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
    "version": '2.0.1',
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
