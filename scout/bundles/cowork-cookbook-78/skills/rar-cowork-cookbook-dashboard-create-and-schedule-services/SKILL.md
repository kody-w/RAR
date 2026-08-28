---
name: "rar-cowork-cookbook-dashboard-create-and-schedule-services"
description: "Produces a self-contained interactive HTML dashboard for create and schedule services - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_and_schedule_services", "rar_sha256": "f54e4f23cab4430e2353528cbbffc04be2d79b231173ee1500171aae2559abad", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_create_and_schedule_services`. The original RAPP
agent is preserved byte-for-byte in `dashboard_create_and_schedule_services_agent.py` and in the RCI capsule.

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

Create and schedule services Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for create and schedule services - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-and-schedule-services
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_create_and_schedule_services_agent.py` and embedded as the fenced Python below (sha256 f54e4f23cab4430e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_create_and_schedule_services_agent.py` first:

```bash
python3 dashboard_create_and_schedule_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_create_and_schedule_services_agent.py   # or on stdin
python3 dashboard_create_and_schedule_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create and schedule services Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for create and schedule services - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-and-schedule-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_create_and_schedule_services',
    "version": '2.0.0',
    "display_name": 'Create and schedule services Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for create and schedule services - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-create-and-schedule-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-create-and-schedule-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ecfb4cf4bdef7fb0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/create-and-schedule-services'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/dashboard-create-and-schedule-services', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'word:schedule'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardCreateAndScheduleServices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCreateAndScheduleServices'
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
    print(DashboardCreateAndScheduleServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
