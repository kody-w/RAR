---
name: "rar-cowork-cookbook-dashboard-manage-compensation-changes"
description: "Produces a self-contained interactive HTML dashboard for manage compensation changes - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_compensation_changes", "rar_sha256": "f06c0c0d91d8f64a101c3a07a1c185149d7128412100ce47b6f55aa51ea73f12", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_compensation_changes`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_compensation_changes_agent.py` and in the RCI capsule.

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

Manage compensation changes Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage compensation changes - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-compensation-changes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_compensation_changes_agent.py` and embedded as the fenced Python below (sha256 f06c0c0d91d8f64a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_compensation_changes_agent.py` first:

```bash
python3 dashboard_manage_compensation_changes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_compensation_changes_agent.py   # or on stdin
python3 dashboard_manage_compensation_changes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage compensation changes Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage compensation changes - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-compensation-changes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_compensation_changes',
    "version": '2.0.1',
    "display_name": 'Manage compensation changes Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage compensation changes - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-compensation-changes',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-compensation-changes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7a4d07e15229c459',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/manage-compensation-changes'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-manage-compensation-changes', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardManageCompensationChanges(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageCompensationChanges'
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
    print(DashboardManageCompensationChanges().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
