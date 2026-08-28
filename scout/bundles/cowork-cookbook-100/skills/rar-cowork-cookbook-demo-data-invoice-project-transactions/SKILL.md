---
name: "rar-cowork-cookbook-demo-data-invoice-project-transactions"
description: "Generates and creates realistic demo records for invoice project transactions in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_invoice_project_transactions", "rar_sha256": "112a1b8c482bb24eecf0d9529e7aa5ad049b3a4a1e75a31033be9f938cdfab26", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
