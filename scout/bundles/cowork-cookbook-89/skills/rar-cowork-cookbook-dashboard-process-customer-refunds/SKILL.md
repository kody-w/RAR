---
name: "rar-cowork-cookbook-dashboard-process-customer-refunds"
description: "Produces a self-contained interactive HTML dashboard for process customer refunds - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_process_customer_refunds", "rar_sha256": "28145e748496ffa179148ce63881ede7fadeffaf463c14e5abffc987beebfac4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_process_customer_refunds`. The original RAPP
agent is preserved byte-for-byte in `dashboard_process_customer_refunds_agent.py` and in the RCI capsule.

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

Process customer refunds Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for process customer refunds - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-process-customer-refunds
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_process_customer_refunds_agent.py` and embedded as the fenced Python below (sha256 28145e748496ffa1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_process_customer_refunds_agent.py` first:

```bash
python3 dashboard_process_customer_refunds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_process_customer_refunds_agent.py   # or on stdin
python3 dashboard_process_customer_refunds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer refunds Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for process customer refunds - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-process-customer-refunds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_process_customer_refunds',
    "version": '2.0.1',
    "display_name": 'Process customer refunds Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for process customer refunds - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-process-customer-refunds',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-process-customer-refunds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '78f9eb434a061b19',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-refunds'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-process-customer-refunds', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardProcessCustomerRefunds(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardProcessCustomerRefunds'
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
    print(DashboardProcessCustomerRefunds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
