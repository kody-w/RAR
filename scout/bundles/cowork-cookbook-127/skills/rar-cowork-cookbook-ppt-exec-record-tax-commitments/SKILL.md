---
name: "rar-cowork-cookbook-ppt-exec-record-tax-commitments"
description: "Generates an executive-ready PowerPoint deck on record tax commitments status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_record_tax_commitments", "rar_sha256": "c957a56801c699ec4a7a2140a729dde90e8b564722f041c71fca8ccaec96f116", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_record_tax_commitments`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_record_tax_commitments_agent.py` and in the RCI capsule.

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

Record tax commitments Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on record tax commitments status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-record-tax-commitments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_record_tax_commitments_agent.py` and embedded as the fenced Python below (sha256 c957a56801c699ec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_record_tax_commitments_agent.py` first:

```bash
python3 ppt_exec_record_tax_commitments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_record_tax_commitments_agent.py   # or on stdin
python3 ppt_exec_record_tax_commitments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record tax commitments Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on record tax commitments status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-record-tax-commitments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_record_tax_commitments',
    "version": '2.0.1',
    "display_name": 'Record tax commitments Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on record tax commitments status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-record-tax-commitments',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-record-tax-commitments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f5ee99bbf19dcffa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/record-tax-commitments'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-record-tax-commitments', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecRecordTaxCommitments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecRecordTaxCommitments'
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
    print(PptExecRecordTaxCommitments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
