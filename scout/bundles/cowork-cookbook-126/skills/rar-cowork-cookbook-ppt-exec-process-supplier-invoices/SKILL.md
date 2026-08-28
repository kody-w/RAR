---
name: "rar-cowork-cookbook-ppt-exec-process-supplier-invoices"
description: "Generates an executive-ready PowerPoint deck on process supplier invoices status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_process_supplier_invoices", "rar_sha256": "103753f92f061b68f87b4cd3c12fa2c371177acefd11a7a54d720407351b23d1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_process_supplier_invoices_agent.py` and embedded as the fenced Python below (sha256 103753f92f061b68…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_process_supplier_invoices_agent.py` first:

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
    "version": '2.0.0',
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
