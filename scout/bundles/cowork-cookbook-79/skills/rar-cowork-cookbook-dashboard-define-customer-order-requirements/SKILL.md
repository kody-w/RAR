---
name: "rar-cowork-cookbook-dashboard-define-customer-order-requirements"
description: "Produces a self-contained interactive HTML dashboard for define customer order requirements - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_customer_order_requirements", "rar_sha256": "82601b5d749f1673b0636fcbc2ed2b39ecc3c162074c913c627dc0b63128cbdc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_customer_order_requirements_agent.py` and embedded as the fenced Python below (sha256 82601b5d749f1673…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_customer_order_requirements_agent.py` first:

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
    "version": '2.0.1',
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
