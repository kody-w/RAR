---
name: "rar-cowork-cookbook-dashboard-plan-logistics-and-distribution"
description: "Produces a self-contained interactive HTML dashboard for plan logistics and distribution - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_plan_logistics_and_distribution", "rar_sha256": "c78deeed5e0b13d665847404803d971521deeeb5d6f7dc40bce5864b1c7f760c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_plan_logistics_and_distribution_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-plan-logistics-and-distribution:166e3e84c490ce59cdbe8c44f61132299058377d24ee6db424b661b4195f25c5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_plan_logistics_and_distribution`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_plan_logistics_and_distribution_agent.py` is
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

Plan logistics and distribution Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for plan logistics and distribution - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-plan-logistics-and-distribution
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_plan_logistics_and_distribution_agent.py` and embedded as the fenced Python below (sha256 c78deeed5e0b13d6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_plan_logistics_and_distribution_agent.py` first:

```bash
python3 dashboard_plan_logistics_and_distribution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_plan_logistics_and_distribution_agent.py   # or on stdin
python3 dashboard_plan_logistics_and_distribution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan logistics and distribution Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for plan logistics and distribution - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-plan-logistics-and-distribution
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_plan_logistics_and_distribution',
    "version": '2.0.0',
    "display_name": 'Plan logistics and distribution Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for plan logistics and distribution - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-plan-logistics-and-distribution',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-plan-logistics-and-distribution',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '33f2c6d250e964d7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-logistics-and-distribution'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-plan-logistics-and-distribution', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardPlanLogisticsAndDistribution(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardPlanLogisticsAndDistribution'
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
    print(DashboardPlanLogisticsAndDistribution().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
