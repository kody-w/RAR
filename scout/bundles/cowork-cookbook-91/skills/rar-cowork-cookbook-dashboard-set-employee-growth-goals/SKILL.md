---
name: "rar-cowork-cookbook-dashboard-set-employee-growth-goals"
description: "Produces a self-contained interactive HTML dashboard for set employee growth goals - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_set_employee_growth_goals", "rar_sha256": "ddb272ba719db448a6ecc9db6f6ee4784c06983a749b2a44bdff16e8cefd62c5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_set_employee_growth_goals_agent.py` and embedded as the fenced Python below (sha256 ddb272ba719db448…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_set_employee_growth_goals_agent.py` first:

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
    "version": '2.0.1',
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
