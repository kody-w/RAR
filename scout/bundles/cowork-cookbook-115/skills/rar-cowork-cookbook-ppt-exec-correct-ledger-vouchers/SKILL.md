---
name: "rar-cowork-cookbook-ppt-exec-correct-ledger-vouchers"
description: "Generates an executive-ready PowerPoint deck on correct ledger vouchers status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_correct_ledger_vouchers", "rar_sha256": "be94a1be018994376252cd7743f3692ed62d0148f7c6e68d8fbf41bd860c5237", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_correct_ledger_vouchers_agent.py` and embedded as the fenced Python below (sha256 be94a1be01899437…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_correct_ledger_vouchers_agent.py` first:

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
    "version": '2.0.0',
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
