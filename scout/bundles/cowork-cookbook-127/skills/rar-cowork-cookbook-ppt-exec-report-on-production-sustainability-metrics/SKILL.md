---
name: "rar-cowork-cookbook-ppt-exec-report-on-production-sustainability-metrics"
description: "Generates an executive-ready PowerPoint deck on report on production sustainability metrics status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_report_on_production_sustainability_metrics", "rar_sha256": "f6374ee44b2f55cbe8e123b7362db780d6dee72a869a5a69911ff6fae7a939a8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_report_on_production_sustainability_metrics`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_report_on_production_sustainability_metrics_agent.py` and in the RCI capsule.

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
