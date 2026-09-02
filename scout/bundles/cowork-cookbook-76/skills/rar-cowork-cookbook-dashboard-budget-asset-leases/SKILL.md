---
name: "rar-cowork-cookbook-dashboard-budget-asset-leases"
description: "Produces a self-contained interactive HTML dashboard for budget asset leases - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_budget_asset_leases", "rar_sha256": "bb671a0e8750aaed17ef224393aab35c2938fe6c76512d62373809484c63f9f6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_budget_asset_leases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-budget-asset-leases:59c109f868b8b129c5753183d99fe2031f00f49a5f98b2abb4abd36c3096bea8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_budget_asset_leases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_budget_asset_leases_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
