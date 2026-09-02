---
name: "rar-cowork-cookbook-dashboard-measure-business-performance"
description: "Produces a self-contained interactive HTML dashboard for measure business performance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_measure_business_performance", "rar_sha256": "33ea5c3cce6f7b00516ecfb9ec3d8eae5a32b8df6bdc16e74cbb2cda373c4442", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_measure_business_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-measure-business-performance:d656660e1e7058514b9e60da09435fbb1ead97398e754f5299b051b7c2f1ef38", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_measure_business_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_measure_business_performance_agent.py` is
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

Measure business performance Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for measure business performance - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-measure-business-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_measure_business_performance_agent.py` and embedded as the fenced Python below (sha256 33ea5c3cce6f7b00…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_measure_business_performance_agent.py` first:

```bash
python3 dashboard_measure_business_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_measure_business_performance_agent.py   # or on stdin
python3 dashboard_measure_business_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure business performance Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for measure business performance - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-measure-business-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_measure_business_performance',
    "version": '2.0.0',
    "display_name": 'Measure business performance Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for measure business performance - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-measure-business-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-measure-business-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '91048919d59346b6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/measure-business-performance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-measure-business-performance', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardMeasureBusinessPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMeasureBusinessPerformance'
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
    print(DashboardMeasureBusinessPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
