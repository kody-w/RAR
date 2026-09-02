---
name: "rar-cowork-cookbook-dashboard-create-background-job-schedule"
description: "Produces a self-contained interactive HTML dashboard for create background job schedule - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_background_job_schedule", "rar_sha256": "d5cb51ed72f3ce09143e4ed91146d07183dd23d4e571f4666d105313cd1920d1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_create_background_job_schedule_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-create-background-job-schedule:ae39a3ec3c6c9fcbf2938bafc8cd1f81d131ae81ae42fd1d2cf7d420728e084d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_create_background_job_schedule`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_create_background_job_schedule_agent.py` is
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
