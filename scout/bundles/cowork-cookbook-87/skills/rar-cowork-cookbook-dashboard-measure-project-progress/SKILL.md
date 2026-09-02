---
name: "rar-cowork-cookbook-dashboard-measure-project-progress"
description: "Produces a self-contained interactive HTML dashboard for measure project progress - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_measure_project_progress", "rar_sha256": "2cf32ea64fd0f645f24e83f7e418f957cebd497d2ec823ff29a2747c463dfa4d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_measure_project_progress_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-measure-project-progress:2c9cefc3c33715e21f418d8e3b5abe0df983bc6f357d0b9e47de12dbb9cbe834", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_measure_project_progress`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_measure_project_progress_agent.py` is
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

Measure project progress Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for measure project progress - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-measure-project-progress
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_measure_project_progress_agent.py` and embedded as the fenced Python below (sha256 2cf32ea64fd0f645…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_measure_project_progress_agent.py` first:

```bash
python3 dashboard_measure_project_progress_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_measure_project_progress_agent.py   # or on stdin
python3 dashboard_measure_project_progress_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure project progress Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for measure project progress - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-measure-project-progress
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_measure_project_progress',
    "version": '2.0.0',
    "display_name": 'Measure project progress Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for measure project progress - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-measure-project-progress',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-measure-project-progress',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '39e3b7a34749d2e0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/measure-project-progress'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/dashboard-measure-project-progress', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardMeasureProjectProgress(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMeasureProjectProgress'
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
    print(DashboardMeasureProjectProgress().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
