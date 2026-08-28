---
name: "rar-cowork-cookbook-demo-data-invoice-project-transactions"
description: "Generates and creates realistic demo records for invoice project transactions in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_invoice_project_transactions", "rar_sha256": "a38625f428415fb771c0398768196331d7fd28c26ab356696726b016f5320625", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_invoice_project_transactions`. The original RAPP
agent is preserved byte-for-byte in `demo_data_invoice_project_transactions_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_invoice_project_transactions_agent.py` and embedded as the fenced Python below (sha256 a38625f428415fb7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_invoice_project_transactions_agent.py` first:

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
    "version": '2.0.1',
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
