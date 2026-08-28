---
name: "rar-cowork-cookbook-configure-maintain-fixed-assets"
description: "Applies a bulk configuration change to maintain fixed assets from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_maintain_fixed_assets", "rar_sha256": "0d8437ae559813180707a2271e5316d0cfa2b49185907e0b6e887729d32e2a7a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_maintain_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 0d8437ae55981318…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_maintain_fixed_assets_agent.py` first:

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
    "version": '2.0.0',
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
