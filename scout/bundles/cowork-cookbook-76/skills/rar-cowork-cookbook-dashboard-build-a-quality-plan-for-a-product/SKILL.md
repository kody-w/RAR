---
name: "rar-cowork-cookbook-dashboard-build-a-quality-plan-for-a-product"
description: "Produces a self-contained interactive HTML dashboard for build a quality plan for a product - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_build_a_quality_plan_for_a_product", "rar_sha256": "f4097a386754a4949b26d1c99939cb24aa4f152ad85987df32d2a13046efa7f9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_build_a_quality_plan_for_a_product`. The original RAPP
agent is preserved byte-for-byte in `dashboard_build_a_quality_plan_for_a_product_agent.py` and in the RCI capsule.

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

Build a quality plan for a product Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for build a quality plan for a product - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-build-a-quality-plan-for-a-product
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_build_a_quality_plan_for_a_product_agent.py` and embedded as the fenced Python below (sha256 f4097a386754a494…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_build_a_quality_plan_for_a_product_agent.py` first:

```bash
python3 dashboard_build_a_quality_plan_for_a_product_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_build_a_quality_plan_for_a_product_agent.py   # or on stdin
python3 dashboard_build_a_quality_plan_for_a_product_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Build a quality plan for a product Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for build a quality plan for a product - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-build-a-quality-plan-for-a-product
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_build_a_quality_plan_for_a_product',
    "version": '2.0.1',
    "display_name": 'Build a quality plan for a product Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for build a quality plan for a product - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-build-a-quality-plan-for-a-product',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-build-a-quality-plan-for-a-product',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '13d2c876382ffa10',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/build-a-quality-plan-for-a-product'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/dashboard-build-a-quality-plan-for-a-product', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardBuildAQualityPlanForAProduct(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardBuildAQualityPlanForAProduct'
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
    print(DashboardBuildAQualityPlanForAProduct().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
