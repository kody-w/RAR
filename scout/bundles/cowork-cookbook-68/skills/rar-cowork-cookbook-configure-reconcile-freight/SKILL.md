---
name: "rar-cowork-cookbook-configure-reconcile-freight"
description: "Applies a bulk configuration change to reconcile freight from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reconcile_freight", "rar_sha256": "ce9ecc23dc53c6ee7d488ad94f742aeee8401958ca049cfe597ba165c071498a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_reconcile_freight`. The original RAPP
agent is preserved byte-for-byte in `configure_reconcile_freight_agent.py` and in the RCI capsule.

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

Reconcile freight Configuration Bulk Setup — Applies a bulk configuration change to reconcile freight from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-reconcile-freight
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_reconcile_freight_agent.py` and embedded as the fenced Python below (sha256 ce9ecc23dc53c6ee…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_reconcile_freight_agent.py` first:

```bash
python3 configure_reconcile_freight_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_reconcile_freight_agent.py   # or on stdin
python3 configure_reconcile_freight_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reconcile freight Configuration Bulk Setup — Applies a bulk configuration change to reconcile freight from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-reconcile-freight
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_reconcile_freight',
    "version": '2.0.0',
    "display_name": 'Reconcile freight Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to reconcile freight from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-reconcile-freight',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-reconcile-freight',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7117e3309270a7e6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/reconcile-freight'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-reconcile-freight', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureReconcileFreight(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReconcileFreight'
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
    print(ConfigureReconcileFreight().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
