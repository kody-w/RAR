---
name: "rar-cowork-cookbook-dashboard-build-a-quality-plan-for-a-product"
description: "Produces a self-contained interactive HTML dashboard for build a quality plan for a product - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_build_a_quality_plan_for_a_product", "rar_sha256": "84872fd2a5ca2fe8c17a05e3592cb7a470540aaec55fa9f8980b4b1d85b798b5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_build_a_quality_plan_for_a_product_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-build-a-quality-plan-for-a-product:9953e5663dc5659a372d82c24acb743ec523fbf91b93ede780a59e777c44a15a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_build_a_quality_plan_for_a_product`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_build_a_quality_plan_for_a_product_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_build_a_quality_plan_for_a_product_agent.py` and embedded as the fenced Python below (sha256 84872fd2a5ca2fe8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_build_a_quality_plan_for_a_product_agent.py` first:

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
    "version": '2.0.0',
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
