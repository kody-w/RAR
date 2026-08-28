---
name: "rar-cowork-cookbook-configure-manage-procurement-spend"
description: "Applies a bulk configuration change to manage procurement spend from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_procurement_spend", "rar_sha256": "c19dd090588ccc350054cf6d794ee1ba633e9d646d0e18a39b5106619da0b2f1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_procurement_spend`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_procurement_spend_agent.py` and in the RCI capsule.

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

Manage procurement spend Configuration Bulk Setup — Applies a bulk configuration change to manage procurement spend from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-procurement-spend
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_procurement_spend_agent.py` and embedded as the fenced Python below (sha256 c19dd090588ccc35…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_procurement_spend_agent.py` first:

```bash
python3 configure_manage_procurement_spend_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_procurement_spend_agent.py   # or on stdin
python3 configure_manage_procurement_spend_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage procurement spend Configuration Bulk Setup — Applies a bulk configuration change to manage procurement spend from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-procurement-spend
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_procurement_spend',
    "version": '2.0.0',
    "display_name": 'Manage procurement spend Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage procurement spend from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-procurement-spend',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-procurement-spend',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '526c93515deb5e55',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/manage-procurement-spend'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-manage-procurement-spend', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureManageProcurementSpend(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageProcurementSpend'
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
    print(ConfigureManageProcurementSpend().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
