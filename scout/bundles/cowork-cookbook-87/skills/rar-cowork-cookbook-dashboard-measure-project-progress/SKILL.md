---
name: "rar-cowork-cookbook-dashboard-measure-project-progress"
description: "Produces a self-contained interactive HTML dashboard for measure project progress - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_measure_project_progress", "rar_sha256": "e5e681eb6167fc50b7027b008a1639ea35ebe3a111fc32a7385fc9d50830bd17", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_measure_project_progress_agent.py` and embedded as the fenced Python below (sha256 e5e681eb6167fc50…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_measure_project_progress_agent.py` first:

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
    "version": '2.0.1',
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
