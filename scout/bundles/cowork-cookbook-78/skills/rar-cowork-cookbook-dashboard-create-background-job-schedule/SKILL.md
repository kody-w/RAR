---
name: "rar-cowork-cookbook-dashboard-create-background-job-schedule"
description: "Produces a self-contained interactive HTML dashboard for create background job schedule - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_background_job_schedule", "rar_sha256": "d5cb51ed72f3ce09143e4ed91146d07183dd23d4e571f4666d105313cd1920d1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_create_background_job_schedule`. The original RAPP
agent is preserved byte-for-byte in `dashboard_create_background_job_schedule_agent.py` and in the RCI capsule.

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

Create background job schedule Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for create background job schedule - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-background-job-schedule
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_create_background_job_schedule_agent.py` and embedded as the fenced Python below (sha256 d5cb51ed72f3ce09…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_create_background_job_schedule_agent.py` first:

```bash
python3 dashboard_create_background_job_schedule_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_create_background_job_schedule_agent.py   # or on stdin
python3 dashboard_create_background_job_schedule_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create background job schedule Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for create background job schedule - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-background-job-schedule
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_create_background_job_schedule',
    "version": '2.0.0',
    "display_name": 'Create background job schedule Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for create background job schedule - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-create-background-job-schedule',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-create-background-job-schedule',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '45863b4ef31448fb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/create-background-job-schedule'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-create-background-job-schedule', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardCreateBackgroundJobSchedule(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCreateBackgroundJobSchedule'
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
    print(DashboardCreateBackgroundJobSchedule().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
