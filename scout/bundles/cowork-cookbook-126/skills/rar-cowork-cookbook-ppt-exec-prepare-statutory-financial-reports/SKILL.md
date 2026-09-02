---
name: "rar-cowork-cookbook-ppt-exec-prepare-statutory-financial-reports"
description: "Generates an executive-ready PowerPoint deck on prepare statutory financial reports status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_prepare_statutory_financial_reports", "rar_sha256": "15b01caf79b6abbcdf2201629d07886f08a534904fe8caff2fa270965c766677", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_prepare_statutory_financial_reports_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-prepare-statutory-financial-reports:d5d5dc7ddb3455489921c6ac13bc9584848ad2a156e0fe3b760635473ee0b157", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_prepare_statutory_financial_reports`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_prepare_statutory_financial_reports_agent.py` is
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

Prepare statutory financial reports Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on prepare statutory financial reports status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-prepare-statutory-financial-reports
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_prepare_statutory_financial_reports_agent.py` and embedded as the fenced Python below (sha256 15b01caf79b6abbc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_prepare_statutory_financial_reports_agent.py` first:

```bash
python3 ppt_exec_prepare_statutory_financial_reports_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_prepare_statutory_financial_reports_agent.py   # or on stdin
python3 ppt_exec_prepare_statutory_financial_reports_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare statutory financial reports Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on prepare statutory financial reports status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-prepare-statutory-financial-reports
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_prepare_statutory_financial_reports',
    "version": '2.0.0',
    "display_name": 'Prepare statutory financial reports Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on prepare statutory financial reports status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-prepare-statutory-financial-reports',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-prepare-statutory-financial-reports',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '30b2acc436b82081',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/prepare-statutory-financial-reports'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-prepare-statutory-financial-reports', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecPrepareStatutoryFinancialReports(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPrepareStatutoryFinancialReports'
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
    print(PptExecPrepareStatutoryFinancialReports().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
