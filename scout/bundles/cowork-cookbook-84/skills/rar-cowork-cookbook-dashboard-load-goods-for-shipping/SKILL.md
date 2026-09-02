---
name: "rar-cowork-cookbook-dashboard-load-goods-for-shipping"
description: "Produces a self-contained interactive HTML dashboard for load goods for shipping - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_load_goods_for_shipping", "rar_sha256": "4eede99ca6ba017d782c5b7ed68f42a5c39db6d4766f8916efa4eef9b8125e53", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_load_goods_for_shipping_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-load-goods-for-shipping:4fd41575436ac387c9f8544385f8810cfa34be7a8f3c7a240214045cc0eb4796", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_load_goods_for_shipping`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_load_goods_for_shipping_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_load_goods_for_shipping_agent.py` and embedded as the fenced Python below (sha256 4eede99ca6ba017d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_load_goods_for_shipping_agent.py` first:

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
    "version": '2.0.0',
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
