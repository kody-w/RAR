---
name: "rar-cowork-cookbook-configure-plan-loads"
description: "Applies a bulk configuration change to plan loads from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_loads", "rar_sha256": "302e62cbe452c8a143701623a132f214a9f81c36713dd8321685bdbf46146a83", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_plan_loads`. The original RAPP
agent is preserved byte-for-byte in `configure_plan_loads_agent.py` and in the RCI capsule.

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

Plan loads Configuration Bulk Setup — Applies a bulk configuration change to plan loads from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-loads
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_loads_agent.py` and embedded as the fenced Python below (sha256 302e62cbe452c8a1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_loads_agent.py` first:

```bash
python3 configure_plan_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_loads_agent.py   # or on stdin
python3 configure_plan_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan loads Configuration Bulk Setup — Applies a bulk configuration change to plan loads from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_loads',
    "version": '2.0.0',
    "display_name": 'Plan loads Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to plan loads from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-plan-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '51bb804c681b8b23',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/plan-loads'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-plan-loads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigurePlanLoads(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanLoads'
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
    print(ConfigurePlanLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
