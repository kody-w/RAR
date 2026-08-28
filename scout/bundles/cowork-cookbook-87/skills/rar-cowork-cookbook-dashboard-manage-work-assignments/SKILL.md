---
name: "rar-cowork-cookbook-dashboard-manage-work-assignments"
description: "Produces a self-contained interactive HTML dashboard for manage work assignments - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_work_assignments", "rar_sha256": "7177bb552e5800aaff021cfb3e820a146284fe466c2f7c95af4ccfbace988956", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_work_assignments`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_work_assignments_agent.py` and in the RCI capsule.

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

Manage work assignments Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage work assignments - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-work-assignments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_work_assignments_agent.py` and embedded as the fenced Python below (sha256 7177bb552e5800aa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_work_assignments_agent.py` first:

```bash
python3 dashboard_manage_work_assignments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_work_assignments_agent.py   # or on stdin
python3 dashboard_manage_work_assignments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage work assignments Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage work assignments - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-work-assignments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_work_assignments',
    "version": '2.0.1',
    "display_name": 'Manage work assignments Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage work assignments - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-work-assignments',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-work-assignments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4cee09e17b34d1a3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/manage-work-assignments'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/dashboard-manage-work-assignments', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardManageWorkAssignments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageWorkAssignments'
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
    print(DashboardManageWorkAssignments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
