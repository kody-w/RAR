---
name: "rar-cowork-cookbook-demo-data-invoice-project-transactions"
description: "Generates and creates realistic demo records for invoice project transactions in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_invoice_project_transactions", "rar_sha256": "112a1b8c482bb24eecf0d9529e7aa5ad049b3a4a1e75a31033be9f938cdfab26", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_invoice_project_transactions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-invoice-project-transactions:3b7e8d6e50c471f6d32dcb42a9878d7de3df302f1c60a0b8085100c1fe4e7072", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_invoice_project_transactions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_invoice_project_transactions_agent.py` is
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

Invoice project transactions Demo Data Generator — Generates and creates realistic demo records for invoice project transactions in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-invoice-project-transactions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_invoice_project_transactions_agent.py` and embedded as the fenced Python below (sha256 112a1b8c482bb24e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_invoice_project_transactions_agent.py` first:

```bash
python3 demo_data_invoice_project_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_invoice_project_transactions_agent.py   # or on stdin
python3 demo_data_invoice_project_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Invoice project transactions Demo Data Generator — Generates and creates realistic demo records for invoice project transactions in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-invoice-project-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_invoice_project_transactions',
    "version": '2.0.0',
    "display_name": 'Invoice project transactions Demo Data Generator',
    "description": 'Generates and creates realistic demo records for invoice project transactions in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-invoice-project-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-invoice-project-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f0a7a73815b45440',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/invoice-project-transactions'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/demo-data-invoice-project-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataInvoiceProjectTransactions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataInvoiceProjectTransactions'
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
    print(DemoDataInvoiceProjectTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
