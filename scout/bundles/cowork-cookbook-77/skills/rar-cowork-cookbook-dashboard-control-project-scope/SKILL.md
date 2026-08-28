---
name: "rar-cowork-cookbook-dashboard-control-project-scope"
description: "Produces a self-contained interactive HTML dashboard for control project scope - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_control_project_scope", "rar_sha256": "673400957126293f672c367d23fc63c4c01746596dfb7226c9838c275756eca8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_control_project_scope`. The original RAPP
agent is preserved byte-for-byte in `dashboard_control_project_scope_agent.py` and in the RCI capsule.

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

Control project scope Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for control project scope - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-control-project-scope
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_control_project_scope_agent.py` and embedded as the fenced Python below (sha256 673400957126293f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_control_project_scope_agent.py` first:

```bash
python3 dashboard_control_project_scope_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_control_project_scope_agent.py   # or on stdin
python3 dashboard_control_project_scope_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Control project scope Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for control project scope - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-control-project-scope
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_control_project_scope',
    "version": '2.0.1',
    "display_name": 'Control project scope Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for control project scope - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-control-project-scope',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-control-project-scope',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f03f84e22a57e1ea',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/control-project-scope'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/dashboard-control-project-scope', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardControlProjectScope(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardControlProjectScope'
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
    print(DashboardControlProjectScope().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
