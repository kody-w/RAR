---
name: "rar-cowork-cookbook-d365-order-to-cash-manage-accounts-receivable"
description: "A Dynamics 365 F&SCM expert scoped to the Manage accounts receivable area (a level-2 subdomain of Order to cash) - covers 13 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_order_to_cash_manage_accounts_receivable", "rar_sha256": "414b1ea1463981b85da652cdb533e5d23a1862d5e59818879500c44d4d96ae77", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_order_to_cash_manage_accounts_receivable_agent.py` and embedded as the fenced Python below (sha256 414b1ea1463981b8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_order_to_cash_manage_accounts_receivable_agent.py` first:

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
    "version": '2.0.0',
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
