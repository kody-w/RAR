---
name: "rar-cowork-cookbook-dashboard-manage-supplier-pricing"
description: "Produces a self-contained interactive HTML dashboard for manage supplier pricing - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_supplier_pricing", "rar_sha256": "110398a02599326812a8cf258dae4bc9364c9c681115e8d7d1dc7ef12492e449", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_supplier_pricing_agent.py` and embedded as the fenced Python below (sha256 110398a025993268…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_supplier_pricing_agent.py` first:

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
    "version": '2.0.1',
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
