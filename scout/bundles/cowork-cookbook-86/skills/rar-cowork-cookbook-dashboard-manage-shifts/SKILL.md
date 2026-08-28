---
name: "rar-cowork-cookbook-dashboard-manage-shifts"
description: "Produces a self-contained interactive HTML dashboard for manage shifts - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_shifts", "rar_sha256": "e183dff2d7e9f1aed337cea4222ff927f613aed589595d72df9f0eacaa309a85", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_shifts`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_shifts_agent.py` and in the RCI capsule.

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

Manage shifts Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage shifts - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-shifts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_shifts_agent.py` and embedded as the fenced Python below (sha256 e183dff2d7e9f1ae…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_shifts_agent.py` first:

```bash
python3 dashboard_manage_shifts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_shifts_agent.py   # or on stdin
python3 dashboard_manage_shifts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage shifts Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage shifts - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-shifts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_shifts',
    "version": '2.0.1',
    "display_name": 'Manage shifts Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage shifts - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-manage-shifts',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-shifts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a4f4f36d4a6b2d74',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/manage-shifts'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-manage-shifts', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardManageShifts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageShifts'
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
    print(DashboardManageShifts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
