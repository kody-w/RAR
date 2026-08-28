---
name: "rar-cowork-cookbook-dashboard-manage-trade-allowances"
description: "Produces a self-contained interactive HTML dashboard for manage trade allowances - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_trade_allowances", "rar_sha256": "ca903dd16f4654050cc171942f05719c407d11ed1d0dd8c27808c771d817721b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_trade_allowances_agent.py` and embedded as the fenced Python below (sha256 ca903dd16f465405…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_trade_allowances_agent.py` first:

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
    "version": '2.0.0',
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
