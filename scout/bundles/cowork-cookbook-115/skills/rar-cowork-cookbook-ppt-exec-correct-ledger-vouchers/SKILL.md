---
name: "rar-cowork-cookbook-ppt-exec-correct-ledger-vouchers"
description: "Generates an executive-ready PowerPoint deck on correct ledger vouchers status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_correct_ledger_vouchers", "rar_sha256": "3ff6d15731062f1545dbb58ac98d6eaa47d63cd7bb385023de087ee27abe0876", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_correct_ledger_vouchers`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_correct_ledger_vouchers_agent.py` and in the RCI capsule.

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

Correct ledger vouchers Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on correct ledger vouchers status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-correct-ledger-vouchers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_correct_ledger_vouchers_agent.py` and embedded as the fenced Python below (sha256 3ff6d15731062f15…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_correct_ledger_vouchers_agent.py` first:

```bash
python3 ppt_exec_correct_ledger_vouchers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_correct_ledger_vouchers_agent.py   # or on stdin
python3 ppt_exec_correct_ledger_vouchers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct ledger vouchers Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on correct ledger vouchers status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-correct-ledger-vouchers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_correct_ledger_vouchers',
    "version": '2.0.1',
    "display_name": 'Correct ledger vouchers Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on correct ledger vouchers status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-correct-ledger-vouchers',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-correct-ledger-vouchers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9ba2e888808402be',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/correct-ledger-vouchers'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-correct-ledger-vouchers', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecCorrectLedgerVouchers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecCorrectLedgerVouchers'
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
    print(PptExecCorrectLedgerVouchers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
