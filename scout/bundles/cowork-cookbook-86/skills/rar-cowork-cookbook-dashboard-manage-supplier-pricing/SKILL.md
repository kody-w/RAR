---
name: "rar-cowork-cookbook-dashboard-manage-supplier-pricing"
description: "Produces a self-contained interactive HTML dashboard for manage supplier pricing - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_supplier_pricing", "rar_sha256": "604f551d1bea7a83933e7ac5313975f2f0674144109afb6571f31146cc92925c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_supplier_pricing`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_supplier_pricing_agent.py` and in the RCI capsule.

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

Manage supplier pricing Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage supplier pricing - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-supplier-pricing
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_supplier_pricing_agent.py` and embedded as the fenced Python below (sha256 604f551d1bea7a83…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_supplier_pricing_agent.py` first:

```bash
python3 dashboard_manage_supplier_pricing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_supplier_pricing_agent.py   # or on stdin
python3 dashboard_manage_supplier_pricing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage supplier pricing Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for manage supplier pricing - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-supplier-pricing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_supplier_pricing',
    "version": '2.0.0',
    "display_name": 'Manage supplier pricing Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for manage supplier pricing - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-supplier-pricing',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-supplier-pricing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '444cd4d293bdf6f4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/manage-supplier-pricing'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-manage-supplier-pricing', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardManageSupplierPricing(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageSupplierPricing'
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
    print(DashboardManageSupplierPricing().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
