---
name: "rar-cowork-cookbook-configure-reconcile-freight"
description: "Applies a bulk configuration change to reconcile freight from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reconcile_freight", "rar_sha256": "ce9ecc23dc53c6ee7d488ad94f742aeee8401958ca049cfe597ba165c071498a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_reconcile_freight_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-reconcile-freight:98e3e02afeea73fccc708baf6cccdc1e03f10c74391101424f505826468b1650", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_reconcile_freight`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_reconcile_freight_agent.py` is
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
