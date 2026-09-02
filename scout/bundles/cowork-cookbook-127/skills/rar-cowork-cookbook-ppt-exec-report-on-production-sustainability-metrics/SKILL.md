---
name: "rar-cowork-cookbook-ppt-exec-report-on-production-sustainability-metrics"
description: "Generates an executive-ready PowerPoint deck on report on production sustainability metrics status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_report_on_production_sustainability_metrics", "rar_sha256": "f6374ee44b2f55cbe8e123b7362db780d6dee72a869a5a69911ff6fae7a939a8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_report_on_production_sustainability_metrics_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-report-on-production-sustainability-metrics:53e2eb753407ffa746325d15bcebbbeda2413c7285a74228be8db167f362031c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_report_on_production_sustainability_metrics`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_report_on_production_sustainability_metrics_agent.py` is
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

Report on production sustainability metrics Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on report on production sustainability metrics status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-report-on-production-sustainability-metrics
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_report_on_production_sustainability_metrics_agent.py` and embedded as the fenced Python below (sha256 f6374ee44b2f55cb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_report_on_production_sustainability_metrics_agent.py` first:

```bash
python3 ppt_exec_report_on_production_sustainability_metrics_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_report_on_production_sustainability_metrics_agent.py   # or on stdin
python3 ppt_exec_report_on_production_sustainability_metrics_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report on production sustainability metrics Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on report on production sustainability metrics status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-report-on-production-sustainability-metrics
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_report_on_production_sustainability_metrics',
    "version": '2.0.0',
    "display_name": 'Report on production sustainability metrics Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on report on production sustainability metrics status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-report-on-production-sustainability-metrics',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-report-on-production-sustainability-metrics',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3a70e689ee5fb6f6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/report-on-production-sustainability-metrics'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/ppt-exec-report-on-production-sustainability-metrics', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecReportOnProductionSustainabilityMetrics(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecReportOnProductionSustainabilityMetrics'
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
    print(PptExecReportOnProductionSustainabilityMetrics().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
