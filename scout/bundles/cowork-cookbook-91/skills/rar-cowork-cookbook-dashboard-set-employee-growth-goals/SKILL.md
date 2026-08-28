---
name: "rar-cowork-cookbook-dashboard-set-employee-growth-goals"
description: "Produces a self-contained interactive HTML dashboard for set employee growth goals - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_set_employee_growth_goals", "rar_sha256": "3830df1a6c11e9423c128cb46842c521452504cfe16b3c65d56514654f381ad8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_set_employee_growth_goals`. The original RAPP
agent is preserved byte-for-byte in `dashboard_set_employee_growth_goals_agent.py` and in the RCI capsule.

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

Set employee growth goals Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for set employee growth goals - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-set-employee-growth-goals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_set_employee_growth_goals_agent.py` and embedded as the fenced Python below (sha256 3830df1a6c11e942…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_set_employee_growth_goals_agent.py` first:

```bash
python3 dashboard_set_employee_growth_goals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_set_employee_growth_goals_agent.py   # or on stdin
python3 dashboard_set_employee_growth_goals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set employee growth goals Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for set employee growth goals - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-set-employee-growth-goals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_set_employee_growth_goals',
    "version": '2.0.0',
    "display_name": 'Set employee growth goals Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for set employee growth goals - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-set-employee-growth-goals',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-set-employee-growth-goals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '13c80fc5bd768cdb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/set-employee-growth-goals'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-set-employee-growth-goals', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardSetEmployeeGrowthGoals(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardSetEmployeeGrowthGoals'
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
    print(DashboardSetEmployeeGrowthGoals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
