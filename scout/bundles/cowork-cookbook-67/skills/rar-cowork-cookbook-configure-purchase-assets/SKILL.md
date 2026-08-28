---
name: "rar-cowork-cookbook-configure-purchase-assets"
description: "Applies a bulk configuration change to purchase assets from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_purchase_assets", "rar_sha256": "5d1e1ec783be94e49c4613a21679b7bc49db282a1935545a46f3593ec5710de0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_purchase_assets_agent.py` and embedded as the fenced Python below (sha256 5d1e1ec783be94e4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_purchase_assets_agent.py` first:

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
    "version": '2.0.0',
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
