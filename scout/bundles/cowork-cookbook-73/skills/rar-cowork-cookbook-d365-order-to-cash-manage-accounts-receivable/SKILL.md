---
name: "rar-cowork-cookbook-d365-order-to-cash-manage-accounts-receivable"
description: "A Dynamics 365 F&SCM expert scoped to the Manage accounts receivable area (a level-2 subdomain of Order to cash) - covers 13 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_order_to_cash_manage_accounts_receivable", "rar_sha256": "414b1ea1463981b85da652cdb533e5d23a1862d5e59818879500c44d4d96ae77", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_order_to_cash_manage_accounts_receivable_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-order-to-cash-manage-accounts-receivable:5ad3d9667441e03e784f06ba01c11eae54e027d7888817c84993e0eaef336c47", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_order_to_cash_manage_accounts_receivable`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_order_to_cash_manage_accounts_receivable_agent.py` is
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
