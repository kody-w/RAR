---
name: "rar-cowork-cookbook-configure-depreciate-assets"
description: "Applies a bulk configuration change to depreciate assets from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_depreciate_assets", "rar_sha256": "dd1b33b2e78c4face81ee7d52e79a715047696b426ac385db63e6da90e74f79a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_depreciate_assets`. The original RAPP
agent is preserved byte-for-byte in `configure_depreciate_assets_agent.py` and in the RCI capsule.

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

Depreciate assets Configuration Bulk Setup — Applies a bulk configuration change to depreciate assets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-depreciate-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_depreciate_assets_agent.py` and embedded as the fenced Python below (sha256 dd1b33b2e78c4fac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_depreciate_assets_agent.py` first:

```bash
python3 configure_depreciate_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_depreciate_assets_agent.py   # or on stdin
python3 configure_depreciate_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Depreciate assets Configuration Bulk Setup — Applies a bulk configuration change to depreciate assets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-depreciate-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_depreciate_assets',
    "version": '2.0.1',
    "display_name": 'Depreciate assets Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to depreciate assets from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-depreciate-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-depreciate-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a0357dd999ee742d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/depreciate-assets'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-depreciate-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDepreciateAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDepreciateAssets'
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
    print(ConfigureDepreciateAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
