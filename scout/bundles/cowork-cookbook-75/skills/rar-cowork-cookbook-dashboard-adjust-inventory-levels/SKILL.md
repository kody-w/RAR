---
name: "rar-cowork-cookbook-dashboard-adjust-inventory-levels"
description: "Produces a self-contained interactive HTML dashboard for adjust inventory levels - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_adjust_inventory_levels", "rar_sha256": "ab245beeb712838a6ac9e8a9c5b945e06af5ba23a6d1f08ca3dbe3253f9f8d80", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_adjust_inventory_levels_agent.py` and embedded as the fenced Python below (sha256 ab245beeb712838a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_adjust_inventory_levels_agent.py` first:

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
    "version": '2.0.1',
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
