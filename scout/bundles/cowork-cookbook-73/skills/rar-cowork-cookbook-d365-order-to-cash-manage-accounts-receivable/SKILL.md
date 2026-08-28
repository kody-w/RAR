---
name: "rar-cowork-cookbook-d365-order-to-cash-manage-accounts-receivable"
description: "A Dynamics 365 F&SCM expert scoped to the Manage accounts receivable area (a level-2 subdomain of Order to cash) - covers 13 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_order_to_cash_manage_accounts_receivable", "rar_sha256": "9cb38f40f46a87ff61a8827ea73851efc45d87b92a56b5f86d632a329d22841e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_order_to_cash_manage_accounts_receivable`. The original RAPP
agent is preserved byte-for-byte in `d365_order_to_cash_manage_accounts_receivable_agent.py` and in the RCI capsule.

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

D365 Manage accounts receivable Expert — A Dynamics 365 F&SCM expert scoped to the Manage accounts receivable area (a level-2 subdomain of Order to cash) - covers 13 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-order-to-cash-manage-accounts-receivable
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_order_to_cash_manage_accounts_receivable_agent.py` and embedded as the fenced Python below (sha256 9cb38f40f46a87ff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_order_to_cash_manage_accounts_receivable_agent.py` first:

```bash
python3 d365_order_to_cash_manage_accounts_receivable_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_order_to_cash_manage_accounts_receivable_agent.py   # or on stdin
python3 d365_order_to_cash_manage_accounts_receivable_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Manage accounts receivable Expert — A Dynamics 365 F&SCM expert scoped to the Manage accounts receivable area (a level-2 subdomain of Order to cash) - covers 13 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-order-to-cash-manage-accounts-receivable
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_order_to_cash_manage_accounts_receivable',
    "version": '2.0.1',
    "display_name": 'D365 Manage accounts receivable Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Manage accounts receivable area (a level-2 subdomain of Order to cash) - covers 13 L3 processes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-order-to-cash-manage-accounts-receivable',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-order-to-cash-manage-accounts-receivable',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '821f48174a759a3d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'order-to-cash/d365-order-to-cash-manage-accounts-receivable', 'uses_skills': {'custom': ['d365-order-to-cash-manage-accounts-receivable'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class D365OrderToCashManageAccountsReceivable(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365OrderToCashManageAccountsReceivable'
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
    print(D365OrderToCashManageAccountsReceivable().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
