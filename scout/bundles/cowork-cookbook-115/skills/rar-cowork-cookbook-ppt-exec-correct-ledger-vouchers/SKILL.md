---
name: "rar-cowork-cookbook-ppt-exec-correct-ledger-vouchers"
description: "Generates an executive-ready PowerPoint deck on correct ledger vouchers status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_correct_ledger_vouchers", "rar_sha256": "be94a1be018994376252cd7743f3692ed62d0148f7c6e68d8fbf41bd860c5237", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_correct_ledger_vouchers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-correct-ledger-vouchers:0363efbabf864acc20e4aaba7682ead1422894b026a0b353efdd0d12e477a69f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_correct_ledger_vouchers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_correct_ledger_vouchers_agent.py` is
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
