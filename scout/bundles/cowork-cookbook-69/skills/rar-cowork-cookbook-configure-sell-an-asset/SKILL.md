---
name: "rar-cowork-cookbook-configure-sell-an-asset"
description: "Applies a bulk configuration change to sell an asset from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_sell_an_asset", "rar_sha256": "951b4212998018e0edd3e28a8a250a833dc07ad930b8dd94da283d0c75190f0f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_sell_an_asset`. The original RAPP
agent is preserved byte-for-byte in `configure_sell_an_asset_agent.py` and in the RCI capsule.

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

Sell an asset Configuration Bulk Setup — Applies a bulk configuration change to sell an asset from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-sell-an-asset
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_sell_an_asset_agent.py` and embedded as the fenced Python below (sha256 951b4212998018e0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_sell_an_asset_agent.py` first:

```bash
python3 configure_sell_an_asset_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_sell_an_asset_agent.py   # or on stdin
python3 configure_sell_an_asset_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Sell an asset Configuration Bulk Setup — Applies a bulk configuration change to sell an asset from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-sell-an-asset
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_sell_an_asset',
    "version": '2.0.1',
    "display_name": 'Sell an asset Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to sell an asset from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-sell-an-asset',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-sell-an-asset',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '295f978d3b1573cf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/sell-an-asset'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-sell-an-asset', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureSellAnAsset(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureSellAnAsset'
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
    print(ConfigureSellAnAsset().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
