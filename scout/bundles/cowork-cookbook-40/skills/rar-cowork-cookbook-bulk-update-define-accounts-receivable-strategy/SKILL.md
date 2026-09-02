---
name: "rar-cowork-cookbook-bulk-update-define-accounts-receivable-strategy"
description: "Applies a bulk field update across define accounts receivable strategy records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_accounts_receivable_strategy", "rar_sha256": "a15e6b10e808c064db3d8eff8892b430465ae4871a61bc0cc05f45216c7b2474", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_define_accounts_receivable_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-define-accounts-receivable-strategy:937772ed7f9a2c55c87ed857a1b8adff2b0da2f22705f6256786610d8884341d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_define_accounts_receivable_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_define_accounts_receivable_strategy_agent.py` is
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

Define accounts receivable strategy Bulk Field Update — Applies a bulk field update across define accounts receivable strategy records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-accounts-receivable-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_accounts_receivable_strategy_agent.py` and embedded as the fenced Python below (sha256 a15e6b10e808c064…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_accounts_receivable_strategy_agent.py` first:

```bash
python3 bulk_update_define_accounts_receivable_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_accounts_receivable_strategy_agent.py   # or on stdin
python3 bulk_update_define_accounts_receivable_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define accounts receivable strategy Bulk Field Update — Applies a bulk field update across define accounts receivable strategy records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-accounts-receivable-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_accounts_receivable_strategy',
    "version": '2.0.0',
    "display_name": 'Define accounts receivable strategy Bulk Field Update',
    "description": 'Applies a bulk field update across define accounts receivable strategy records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-accounts-receivable-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-accounts-receivable-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c6f2abe196e1d0a3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-accounts-receivable-strategy'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-define-accounts-receivable-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateDefineAccountsReceivableStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineAccountsReceivableStrategy'
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
    print(BulkUpdateDefineAccountsReceivableStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
