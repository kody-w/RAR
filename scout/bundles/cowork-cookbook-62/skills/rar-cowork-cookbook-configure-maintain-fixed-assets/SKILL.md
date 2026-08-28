---
name: "rar-cowork-cookbook-configure-maintain-fixed-assets"
description: "Applies a bulk configuration change to maintain fixed assets from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_maintain_fixed_assets", "rar_sha256": "9221daf44d8716ed732d7259e432a5648280cc5acc701653ca34d462af634045", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_maintain_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `configure_maintain_fixed_assets_agent.py` and in the RCI capsule.

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

Maintain fixed assets Configuration Bulk Setup — Applies a bulk configuration change to maintain fixed assets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-maintain-fixed-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_maintain_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 9221daf44d8716ed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_maintain_fixed_assets_agent.py` first:

```bash
python3 configure_maintain_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_maintain_fixed_assets_agent.py   # or on stdin
python3 configure_maintain_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain fixed assets Configuration Bulk Setup — Applies a bulk configuration change to maintain fixed assets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-maintain-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_maintain_fixed_assets',
    "version": '2.0.1',
    "display_name": 'Maintain fixed assets Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to maintain fixed assets from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-maintain-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-maintain-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7b96abe3654e63ee',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/maintain-fixed-assets'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-maintain-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureMaintainFixedAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureMaintainFixedAssets'
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
    print(ConfigureMaintainFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
