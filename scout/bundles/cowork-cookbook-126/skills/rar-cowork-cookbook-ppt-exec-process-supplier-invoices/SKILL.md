---
name: "rar-cowork-cookbook-ppt-exec-process-supplier-invoices"
description: "Generates an executive-ready PowerPoint deck on process supplier invoices status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_process_supplier_invoices", "rar_sha256": "874d531fa280383dc2401ce84ed19b4e52d7ed310921b6884ef18cbb833ddb30", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_process_supplier_invoices`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_process_supplier_invoices_agent.py` and in the RCI capsule.

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

Process supplier invoices Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on process supplier invoices status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-process-supplier-invoices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_process_supplier_invoices_agent.py` and embedded as the fenced Python below (sha256 874d531fa280383d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_process_supplier_invoices_agent.py` first:

```bash
python3 ppt_exec_process_supplier_invoices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_process_supplier_invoices_agent.py   # or on stdin
python3 ppt_exec_process_supplier_invoices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process supplier invoices Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on process supplier invoices status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-process-supplier-invoices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_process_supplier_invoices',
    "version": '2.0.1',
    "display_name": 'Process supplier invoices Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on process supplier invoices status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-process-supplier-invoices',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-process-supplier-invoices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '40166d4d7365dd8d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/process-supplier-invoices'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/ppt-exec-process-supplier-invoices', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecProcessSupplierInvoices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecProcessSupplierInvoices'
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
    print(PptExecProcessSupplierInvoices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
