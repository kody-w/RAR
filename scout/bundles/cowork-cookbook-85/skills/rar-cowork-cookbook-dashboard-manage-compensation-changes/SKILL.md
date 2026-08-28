---
name: "rar-cowork-cookbook-dashboard-manage-compensation-changes"
description: "Produces a self-contained interactive HTML dashboard for manage compensation changes - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_compensation_changes", "rar_sha256": "be782da82742ab7bc94402456db057f8e41f74443489b0dd94f918bb205b8421", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_compensation_changes_agent.py` and embedded as the fenced Python below (sha256 be782da82742ab7b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_compensation_changes_agent.py` first:

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
    "version": '2.0.0',
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
