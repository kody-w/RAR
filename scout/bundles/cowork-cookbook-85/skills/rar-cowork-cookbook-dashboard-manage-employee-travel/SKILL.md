---
name: "rar-cowork-cookbook-dashboard-manage-employee-travel"
description: "Produces a self-contained interactive HTML dashboard for manage employee travel - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_employee_travel", "rar_sha256": "a781f0a1112652265f1f11abdfef14a4d6ed821644d2def1ec7ff0fbef2a586a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_employee_travel_agent.py` and embedded as the fenced Python below (sha256 a781f0a111265226…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_employee_travel_agent.py` first:

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
    "version": '2.0.1',
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
