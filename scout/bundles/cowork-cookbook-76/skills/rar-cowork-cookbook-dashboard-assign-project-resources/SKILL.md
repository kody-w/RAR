---
name: "rar-cowork-cookbook-dashboard-assign-project-resources"
description: "Produces a self-contained interactive HTML dashboard for assign project resources - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_assign_project_resources", "rar_sha256": "030716f609c613d63f5510e2544b5498669856befa96846123fffe158fb711c3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_assign_project_resources`. The original RAPP
agent is preserved byte-for-byte in `dashboard_assign_project_resources_agent.py` and in the RCI capsule.

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

Assign project resources Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for assign project resources - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-assign-project-resources
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_assign_project_resources_agent.py` and embedded as the fenced Python below (sha256 030716f609c613d6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_assign_project_resources_agent.py` first:

```bash
python3 dashboard_assign_project_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_assign_project_resources_agent.py   # or on stdin
python3 dashboard_assign_project_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assign project resources Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for assign project resources - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-assign-project-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_assign_project_resources',
    "version": '2.0.0',
    "display_name": 'Assign project resources Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for assign project resources - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-assign-project-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-assign-project-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7a42b638f485b14e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/assign-project-resources'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/dashboard-assign-project-resources', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardAssignProjectResources(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardAssignProjectResources'
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
    print(DashboardAssignProjectResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
