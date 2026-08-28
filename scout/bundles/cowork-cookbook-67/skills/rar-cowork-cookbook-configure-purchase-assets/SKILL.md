---
name: "rar-cowork-cookbook-configure-purchase-assets"
description: "Applies a bulk configuration change to purchase assets from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_purchase_assets", "rar_sha256": "0f3aa73594f6822cb5e218162287497896c41f6a9638d72ed2fc13462f7af9e8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_purchase_assets`. The original RAPP
agent is preserved byte-for-byte in `configure_purchase_assets_agent.py` and in the RCI capsule.

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

Purchase assets Configuration Bulk Setup — Applies a bulk configuration change to purchase assets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-purchase-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_purchase_assets_agent.py` and embedded as the fenced Python below (sha256 0f3aa73594f6822c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_purchase_assets_agent.py` first:

```bash
python3 configure_purchase_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_purchase_assets_agent.py   # or on stdin
python3 configure_purchase_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Purchase assets Configuration Bulk Setup — Applies a bulk configuration change to purchase assets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-purchase-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_purchase_assets',
    "version": '2.0.1',
    "display_name": 'Purchase assets Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to purchase assets from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-purchase-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-purchase-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0238913c360410d4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/purchase-assets'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-purchase-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigurePurchaseAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePurchaseAssets'
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
    print(ConfigurePurchaseAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
