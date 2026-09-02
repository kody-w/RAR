---
name: "rar-cowork-cookbook-dashboard-manage-trade-allowances"
description: "Produces a self-contained interactive HTML dashboard for manage trade allowances - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_trade_allowances", "rar_sha256": "ca903dd16f4654050cc171942f05719c407d11ed1d0dd8c27808c771d817721b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_manage_trade_allowances_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-manage-trade-allowances:2d55f5bea1551c9db9a5eaac52df072d617dea996443c4649f94d658de7a40fd", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_manage_trade_allowances`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_manage_trade_allowances_agent.py` is
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
