---
name: "rar-cowork-cookbook-ppt-exec-report-production-quality-non-conformance"
description: "Generates an executive-ready PowerPoint deck on report production quality non-conformance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_report_production_quality_non_conformance", "rar_sha256": "d7e6b31b25d8f6b1a447c89176eaeaeea231d8d738b11ffce061ad6843b05e38", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_report_production_quality_non_conformance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_report_production_quality_non_conformance_agent.py` and in the RCI capsule.

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

Report production quality non-conformance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on report production quality non-conformance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-report-production-quality-non-conformance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_report_production_quality_non_conformance_agent.py` and embedded as the fenced Python below (sha256 d7e6b31b25d8f6b1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_report_production_quality_non_conformance_agent.py` first:

```bash
python3 ppt_exec_report_production_quality_non_conformance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_report_production_quality_non_conformance_agent.py   # or on stdin
python3 ppt_exec_report_production_quality_non_conformance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report production quality non-conformance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on report production quality non-conformance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-report-production-quality-non-conformance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_report_production_quality_non_conformance',
    "version": '2.0.1',
    "display_name": 'Report production quality non-conformance Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on report production quality non-conformance status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ppt-exec-report-production-quality-non-conformance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-report-production-quality-non-conformance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '467cef525f410442',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/report-production-quality-non-conformance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/ppt-exec-report-production-quality-non-conformance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecReportProductionQualityNonConformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecReportProductionQualityNonConformance'
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
    print(PptExecReportProductionQualityNonConformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
