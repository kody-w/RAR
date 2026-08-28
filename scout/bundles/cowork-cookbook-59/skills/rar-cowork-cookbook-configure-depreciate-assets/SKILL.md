---
name: "rar-cowork-cookbook-configure-depreciate-assets"
description: "Applies a bulk configuration change to depreciate assets from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_depreciate_assets", "rar_sha256": "23eba458705bdabe144d5143f483f1501264411a198d273462a285af20f1f185", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_depreciate_assets_agent.py` and embedded as the fenced Python below (sha256 23eba458705bdabe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_depreciate_assets_agent.py` first:

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
    "version": '2.0.0',
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
