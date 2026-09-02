---
name: "rar-cowork-cookbook-ppt-exec-process-supplier-invoices"
description: "Generates an executive-ready PowerPoint deck on process supplier invoices status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_process_supplier_invoices", "rar_sha256": "103753f92f061b68f87b4cd3c12fa2c371177acefd11a7a54d720407351b23d1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_process_supplier_invoices_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-process-supplier-invoices:8cab86fa2bde212ddd13a53e3ce4d36415ba1231374cc44b61860f490349c49d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_process_supplier_invoices`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_process_supplier_invoices_agent.py` is
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
