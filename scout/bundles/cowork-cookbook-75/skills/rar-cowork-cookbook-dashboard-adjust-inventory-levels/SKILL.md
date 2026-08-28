---
name: "rar-cowork-cookbook-dashboard-adjust-inventory-levels"
description: "Produces a self-contained interactive HTML dashboard for adjust inventory levels - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_adjust_inventory_levels", "rar_sha256": "6bebaad56adb787aeea31983d73ef0132b32756a6af8daa2af48bf32ba095173", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_adjust_inventory_levels`. The original RAPP
agent is preserved byte-for-byte in `dashboard_adjust_inventory_levels_agent.py` and in the RCI capsule.

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

Adjust inventory levels Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for adjust inventory levels - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-adjust-inventory-levels
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_adjust_inventory_levels_agent.py` and embedded as the fenced Python below (sha256 6bebaad56adb787a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_adjust_inventory_levels_agent.py` first:

```bash
python3 dashboard_adjust_inventory_levels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_adjust_inventory_levels_agent.py   # or on stdin
python3 dashboard_adjust_inventory_levels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Adjust inventory levels Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for adjust inventory levels - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-adjust-inventory-levels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_adjust_inventory_levels',
    "version": '2.0.0',
    "display_name": 'Adjust inventory levels Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for adjust inventory levels - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-adjust-inventory-levels',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-adjust-inventory-levels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a0d677d76519f6d8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/adjust-inventory-levels'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/dashboard-adjust-inventory-levels', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardAdjustInventoryLevels(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardAdjustInventoryLevels'
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
    print(DashboardAdjustInventoryLevels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
