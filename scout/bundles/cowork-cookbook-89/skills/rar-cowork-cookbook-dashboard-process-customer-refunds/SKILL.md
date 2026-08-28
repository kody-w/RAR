---
name: "rar-cowork-cookbook-dashboard-process-customer-refunds"
description: "Produces a self-contained interactive HTML dashboard for process customer refunds - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_process_customer_refunds", "rar_sha256": "1605ecd4bbfcc389bd4edde4953e4b4ac4368893e7a032227f64d78f31986b3f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_process_customer_refunds_agent.py` and embedded as the fenced Python below (sha256 1605ecd4bbfcc389…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_process_customer_refunds_agent.py` first:

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
    "version": '2.0.0',
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
