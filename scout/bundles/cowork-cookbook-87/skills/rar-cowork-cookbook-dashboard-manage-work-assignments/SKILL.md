---
name: "rar-cowork-cookbook-dashboard-manage-work-assignments"
description: "Produces a self-contained interactive HTML dashboard for manage work assignments - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_work_assignments", "rar_sha256": "11b608c47718763c5258a2b7f1349bf08c06c21d5f7a436a58a5e3b40bf5a807", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_work_assignments_agent.py` and embedded as the fenced Python below (sha256 11b608c47718763c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_work_assignments_agent.py` first:

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
    "version": '2.0.0',
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
