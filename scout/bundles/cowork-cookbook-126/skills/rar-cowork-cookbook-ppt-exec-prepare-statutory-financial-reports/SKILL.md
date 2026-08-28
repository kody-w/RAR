---
name: "rar-cowork-cookbook-ppt-exec-prepare-statutory-financial-reports"
description: "Generates an executive-ready PowerPoint deck on prepare statutory financial reports status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_prepare_statutory_financial_reports", "rar_sha256": "15b01caf79b6abbcdf2201629d07886f08a534904fe8caff2fa270965c766677", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_prepare_statutory_financial_reports`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_prepare_statutory_financial_reports_agent.py` and in the RCI capsule.

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
