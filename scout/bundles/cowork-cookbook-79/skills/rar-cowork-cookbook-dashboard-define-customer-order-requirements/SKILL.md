---
name: "rar-cowork-cookbook-dashboard-define-customer-order-requirements"
description: "Produces a self-contained interactive HTML dashboard for define customer order requirements - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_customer_order_requirements", "rar_sha256": "33347d6b28ccb3c296b07b399f1eb9901b79d1fabb924470a842cd0bb52fed4f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_customer_order_requirements`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_customer_order_requirements_agent.py` and in the RCI capsule.

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

Define customer order requirements Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define customer order requirements - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-customer-order-requirements
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_customer_order_requirements_agent.py` and embedded as the fenced Python below (sha256 33347d6b28ccb3c2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_customer_order_requirements_agent.py` first:

```bash
python3 dashboard_define_customer_order_requirements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_customer_order_requirements_agent.py   # or on stdin
python3 dashboard_define_customer_order_requirements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define customer order requirements Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define customer order requirements - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-customer-order-requirements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_customer_order_requirements',
    "version": '2.0.0',
    "display_name": 'Define customer order requirements Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for define customer order requirements - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-define-customer-order-requirements',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-customer-order-requirements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fcd89656acf904c0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/define-customer-order-requirements'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/dashboard-define-customer-order-requirements', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardDefineCustomerOrderRequirements(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineCustomerOrderRequirements'
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
    print(DashboardDefineCustomerOrderRequirements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
