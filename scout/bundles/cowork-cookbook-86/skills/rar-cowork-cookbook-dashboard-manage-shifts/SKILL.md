---
name: "rar-cowork-cookbook-dashboard-manage-shifts"
description: "Produces a self-contained interactive HTML dashboard for manage shifts - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_shifts", "rar_sha256": "4905a0020e026dcbe4f24a42d96a9c402999ed9dfc9e58522134f6414728c580", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_shifts_agent.py` and embedded as the fenced Python below (sha256 4905a0020e026dcb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_shifts_agent.py` first:

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
    "version": '2.0.0',
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
