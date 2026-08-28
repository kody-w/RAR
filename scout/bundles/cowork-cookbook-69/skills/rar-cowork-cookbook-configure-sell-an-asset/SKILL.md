---
name: "rar-cowork-cookbook-configure-sell-an-asset"
description: "Applies a bulk configuration change to sell an asset from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_sell_an_asset", "rar_sha256": "7c8d0dbeed3b307f3a87a370d1050447e7a35f04f729e6ee0772c2887f258439", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_sell_an_asset_agent.py` and embedded as the fenced Python below (sha256 7c8d0dbeed3b307f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_sell_an_asset_agent.py` first:

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
    "version": '2.0.0',
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
