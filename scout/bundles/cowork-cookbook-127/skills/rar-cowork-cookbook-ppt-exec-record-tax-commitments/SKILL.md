---
name: "rar-cowork-cookbook-ppt-exec-record-tax-commitments"
description: "Generates an executive-ready PowerPoint deck on record tax commitments status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_record_tax_commitments", "rar_sha256": "b14bba12dafe2c8fad1ae6978500c53bdadb59aa7773ce3e130e81357c185af4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_record_tax_commitments_agent.py` and embedded as the fenced Python below (sha256 b14bba12dafe2c8f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_record_tax_commitments_agent.py` first:

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
    "version": '2.0.0',
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
