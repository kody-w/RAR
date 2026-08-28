---
name: "rar-cowork-cookbook-ppt-exec-prepare-statutory-financial-reports"
description: "Generates an executive-ready PowerPoint deck on prepare statutory financial reports status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_prepare_statutory_financial_reports", "rar_sha256": "97fdfa0e766ed5500e5e6327da291944bf87dfc7196213549dc132c57581bb2a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_prepare_statutory_financial_reports_agent.py` and embedded as the fenced Python below (sha256 97fdfa0e766ed550…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_prepare_statutory_financial_reports_agent.py` first:

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
    "version": '2.0.1',
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
