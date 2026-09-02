---
name: "rar-cowork-cookbook-dashboard-create-and-schedule-services"
description: "Produces a self-contained interactive HTML dashboard for create and schedule services - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_and_schedule_services", "rar_sha256": "f54e4f23cab4430e2353528cbbffc04be2d79b231173ee1500171aae2559abad", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_create_and_schedule_services_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-create-and-schedule-services:9aea6194c4d17d59e150961d6c7117cfbafaeb045e7d04e1ed3476356c494ab8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_create_and_schedule_services`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_create_and_schedule_services_agent.py` is
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
