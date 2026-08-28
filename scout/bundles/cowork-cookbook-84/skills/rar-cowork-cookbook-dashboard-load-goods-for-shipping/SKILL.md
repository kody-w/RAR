---
name: "rar-cowork-cookbook-dashboard-load-goods-for-shipping"
description: "Produces a self-contained interactive HTML dashboard for load goods for shipping - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_load_goods_for_shipping", "rar_sha256": "270cfacaf2d3858102037456de84aad4234f78b6c45ed6b71ff604413afa2356", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_load_goods_for_shipping`. The original RAPP
agent is preserved byte-for-byte in `dashboard_load_goods_for_shipping_agent.py` and in the RCI capsule.

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

Load goods for shipping Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for load goods for shipping - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-load-goods-for-shipping
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_load_goods_for_shipping_agent.py` and embedded as the fenced Python below (sha256 270cfacaf2d38581…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_load_goods_for_shipping_agent.py` first:

```bash
python3 dashboard_load_goods_for_shipping_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_load_goods_for_shipping_agent.py   # or on stdin
python3 dashboard_load_goods_for_shipping_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Load goods for shipping Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for load goods for shipping - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-load-goods-for-shipping
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_load_goods_for_shipping',
    "version": '2.0.1',
    "display_name": 'Load goods for shipping Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for load goods for shipping - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-load-goods-for-shipping',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-load-goods-for-shipping',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a99dc89a7942ed30',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/load-goods-for-shipping'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/dashboard-load-goods-for-shipping', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardLoadGoodsForShipping(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardLoadGoodsForShipping'
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
    print(DashboardLoadGoodsForShipping().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
