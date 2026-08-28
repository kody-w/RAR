---
name: "rar-cowork-cookbook-configure-manage-open-purchases"
description: "Applies a bulk configuration change to manage open purchases from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_open_purchases", "rar_sha256": "ac9aaf5f717bd6b24ba1973050f89ea9112f9b00e1e4a5911d932077b2890929", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_open_purchases`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_open_purchases_agent.py` and in the RCI capsule.

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

Manage open purchases Configuration Bulk Setup — Applies a bulk configuration change to manage open purchases from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-open-purchases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_open_purchases_agent.py` and embedded as the fenced Python below (sha256 ac9aaf5f717bd6b2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_open_purchases_agent.py` first:

```bash
python3 configure_manage_open_purchases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_open_purchases_agent.py   # or on stdin
python3 configure_manage_open_purchases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage open purchases Configuration Bulk Setup — Applies a bulk configuration change to manage open purchases from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-open-purchases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_open_purchases',
    "version": '2.0.1',
    "display_name": 'Manage open purchases Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage open purchases from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-manage-open-purchases',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-open-purchases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e07eb8ed54ccbdff',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/manage-open-purchases'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-manage-open-purchases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureManageOpenPurchases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageOpenPurchases'
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
    print(ConfigureManageOpenPurchases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
