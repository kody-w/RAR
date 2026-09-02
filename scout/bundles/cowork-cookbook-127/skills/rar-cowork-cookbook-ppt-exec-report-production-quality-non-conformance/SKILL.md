---
name: "rar-cowork-cookbook-ppt-exec-report-production-quality-non-conformance"
description: "Generates an executive-ready PowerPoint deck on report production quality non-conformance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_report_production_quality_non_conformance", "rar_sha256": "b926c0be09901c9ab225192ee9293f70a255b10660f69cdfdb0923dba8e3bdcc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_report_production_quality_non_conformance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-report-production-quality-non-conformance:3c666d5ebad17643c2030eab5ffde3f8fb48ca5dc80b3d475a07f78b6582d038", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_report_production_quality_non_conformance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_report_production_quality_non_conformance_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_report_production_quality_non_conformance_agent.py` and embedded as the fenced Python below (sha256 b926c0be09901c9a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_report_production_quality_non_conformance_agent.py` first:

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
    "version": '2.0.0',
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
