---
name: "rar-cowork-cookbook-ppt-exec-correct-supplier-payments"
description: "Generates an executive-ready PowerPoint deck on correct supplier payments status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_correct_supplier_payments", "rar_sha256": "c405b266dcacf862919c33cafd0ecf2f832f184f4b2942baa7572ea57a3ab4b6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_correct_supplier_payments`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_correct_supplier_payments_agent.py` and in the RCI capsule.

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

Correct supplier payments Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on correct supplier payments status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-correct-supplier-payments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_correct_supplier_payments_agent.py` and embedded as the fenced Python below (sha256 c405b266dcacf862…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_correct_supplier_payments_agent.py` first:

```bash
python3 ppt_exec_correct_supplier_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_correct_supplier_payments_agent.py   # or on stdin
python3 ppt_exec_correct_supplier_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct supplier payments Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on correct supplier payments status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-correct-supplier-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_correct_supplier_payments',
    "version": '2.0.1',
    "display_name": 'Correct supplier payments Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on correct supplier payments status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-correct-supplier-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-correct-supplier-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f15e0532d898b6e2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/correct-supplier-payments'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/ppt-exec-correct-supplier-payments', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecCorrectSupplierPayments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecCorrectSupplierPayments'
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
    print(PptExecCorrectSupplierPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
