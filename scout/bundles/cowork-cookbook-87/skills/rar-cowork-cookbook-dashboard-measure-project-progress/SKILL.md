---
name: "rar-cowork-cookbook-dashboard-measure-project-progress"
description: "Produces a self-contained interactive HTML dashboard for measure project progress - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_measure_project_progress", "rar_sha256": "2cf32ea64fd0f645f24e83f7e418f957cebd497d2ec823ff29a2747c463dfa4d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_measure_project_progress`. The original RAPP
agent is preserved byte-for-byte in `dashboard_measure_project_progress_agent.py` and in the RCI capsule.

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
