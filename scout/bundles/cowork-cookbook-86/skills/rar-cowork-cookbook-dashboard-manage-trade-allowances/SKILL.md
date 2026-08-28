---
name: "rar-cowork-cookbook-dashboard-manage-trade-allowances"
description: "Produces a self-contained interactive HTML dashboard for manage trade allowances - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_trade_allowances", "rar_sha256": "5f01422196c12b6fbcab00ecd12c05e8f4c1f6bfbfb7f47595369f0e2001ddb2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_trade_allowances`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_trade_allowances_agent.py` and in the RCI capsule.

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

Manage trade allowances Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage trade allowances - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-trade-allowances
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_trade_allowances_agent.py` and embedded as the fenced Python below (sha256 5f01422196c12b6f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_trade_allowances_agent.py` first:

```bash
python3 dashboard_manage_trade_allowances_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_trade_allowances_agent.py   # or on stdin
python3 dashboard_manage_trade_allowances_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage trade allowances Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage trade allowances - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-trade-allowances
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_trade_allowances',
    "version": '2.0.1',
    "display_name": 'Manage trade allowances Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage trade allowances - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-trade-allowances',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-trade-allowances',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd90c20093bf37e38',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/manage-trade-allowances'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-manage-trade-allowances', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardManageTradeAllowances(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageTradeAllowances'
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
    print(DashboardManageTradeAllowances().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
