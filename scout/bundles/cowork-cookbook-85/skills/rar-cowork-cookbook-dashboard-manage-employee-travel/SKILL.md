---
name: "rar-cowork-cookbook-dashboard-manage-employee-travel"
description: "Produces a self-contained interactive HTML dashboard for manage employee travel - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_employee_travel", "rar_sha256": "5798a7a93adce56aec1fdf1a432dac86e8d143e07847e0bb7213dea75f1e4066", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_employee_travel`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_employee_travel_agent.py` and in the RCI capsule.

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

Manage employee travel Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage employee travel - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-employee-travel
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_employee_travel_agent.py` and embedded as the fenced Python below (sha256 5798a7a93adce56a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_employee_travel_agent.py` first:

```bash
python3 dashboard_manage_employee_travel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_employee_travel_agent.py   # or on stdin
python3 dashboard_manage_employee_travel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage employee travel Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage employee travel - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-employee-travel
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_employee_travel',
    "version": '2.0.0',
    "display_name": 'Manage employee travel Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage employee travel - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-manage-employee-travel',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-employee-travel',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7507fb0f7d51f09c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/manage-employee-travel'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-manage-employee-travel', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardManageEmployeeTravel(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageEmployeeTravel'
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
    print(DashboardManageEmployeeTravel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
