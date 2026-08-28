---
name: "rar-cowork-cookbook-dashboard-budget-asset-leases"
description: "Produces a self-contained interactive HTML dashboard for budget asset leases - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_budget_asset_leases", "rar_sha256": "bb671a0e8750aaed17ef224393aab35c2938fe6c76512d62373809484c63f9f6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_budget_asset_leases_agent.py` and embedded as the fenced Python below (sha256 bb671a0e8750aaed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_budget_asset_leases_agent.py` first:

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
    "version": '2.0.0',
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
