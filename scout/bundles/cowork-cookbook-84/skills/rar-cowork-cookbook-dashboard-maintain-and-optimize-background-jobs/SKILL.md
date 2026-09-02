---
name: "rar-cowork-cookbook-dashboard-maintain-and-optimize-background-jobs"
description: "Produces a self-contained interactive HTML dashboard for maintain and optimize background jobs - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_maintain_and_optimize_background_jobs", "rar_sha256": "2d492788f73b5b66139dfb9b319c20eb1b20d66a96cabc470bffa42681256947", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_maintain_and_optimize_background_jobs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-maintain-and-optimize-background-jobs:cee37b01e858e5045697a90c3eca2611e00ca7ab3eed24420dc385064ea84e5c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_maintain_and_optimize_background_jobs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_maintain_and_optimize_background_jobs_agent.py` is
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

Maintain and optimize background jobs Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for maintain and optimize background jobs - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-maintain-and-optimize-background-jobs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_maintain_and_optimize_background_jobs_agent.py` and embedded as the fenced Python below (sha256 2d492788f73b5b66…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_maintain_and_optimize_background_jobs_agent.py` first:

```bash
python3 dashboard_maintain_and_optimize_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_maintain_and_optimize_background_jobs_agent.py   # or on stdin
python3 dashboard_maintain_and_optimize_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain and optimize background jobs Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for maintain and optimize background jobs - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-maintain-and-optimize-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_maintain_and_optimize_background_jobs',
    "version": '2.0.0',
    "display_name": 'Maintain and optimize background jobs Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for maintain and optimize background jobs - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-maintain-and-optimize-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-maintain-and-optimize-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '19ac1a455aa9b38e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/maintain-and-optimize-background-jobs'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-maintain-and-optimize-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardMaintainAndOptimizeBackgroundJobs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMaintainAndOptimizeBackgroundJobs'
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
    print(DashboardMaintainAndOptimizeBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
