---
name: "rar-cowork-cookbook-ppt-exec-correct-supplier-payments"
description: "Generates an executive-ready PowerPoint deck on correct supplier payments status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_correct_supplier_payments", "rar_sha256": "83c33726f3f832415c827ee7f8fbf3c621060b896c1bf97a1724f508301169df", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_correct_supplier_payments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-correct-supplier-payments:76b3705965d150abb390654ff8d14989da889b690105bbcec7ea625ea2dc2608", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_correct_supplier_payments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_correct_supplier_payments_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_correct_supplier_payments_agent.py` and embedded as the fenced Python below (sha256 83c33726f3f83241…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_correct_supplier_payments_agent.py` first:

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
    "version": '2.0.0',
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
