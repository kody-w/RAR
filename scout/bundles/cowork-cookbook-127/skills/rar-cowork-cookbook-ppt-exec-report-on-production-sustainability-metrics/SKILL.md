---
name: "rar-cowork-cookbook-ppt-exec-report-on-production-sustainability-metrics"
description: "Generates an executive-ready PowerPoint deck on report on production sustainability metrics status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_report_on_production_sustainability_metrics", "rar_sha256": "197336379652fa9ce812664c2ecf4841b1b8c147931b43968575c4070eb9a1f4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_report_on_production_sustainability_metrics_agent.py` and embedded as the fenced Python below (sha256 197336379652fa9c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_report_on_production_sustainability_metrics_agent.py` first:

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
    "version": '2.0.1',
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
