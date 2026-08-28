---
name: "rar-cowork-cookbook-dashboard-budget-asset-leases"
description: "Produces a self-contained interactive HTML dashboard for budget asset leases - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_budget_asset_leases", "rar_sha256": "6c9c28ecf82a20d8045ed2224d6e5bf2063c8ad0b1b03a856c7732b28ef1514a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_budget_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `dashboard_budget_asset_leases_agent.py` and in the RCI capsule.

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

Budget asset leases Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for budget asset leases - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-budget-asset-leases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_budget_asset_leases_agent.py` and embedded as the fenced Python below (sha256 6c9c28ecf82a20d8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_budget_asset_leases_agent.py` first:

```bash
python3 dashboard_budget_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_budget_asset_leases_agent.py   # or on stdin
python3 dashboard_budget_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Budget asset leases Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for budget asset leases - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-budget-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_budget_asset_leases',
    "version": '2.0.1',
    "display_name": 'Budget asset leases Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for budget asset leases - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'dashboard-budget-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-budget-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1ec2568471d4eb3e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/budget-asset-leases'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/dashboard-budget-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardBudgetAssetLeases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardBudgetAssetLeases'
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
    print(DashboardBudgetAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
