---
name: "rar-cowork-cookbook-configure-classify-assets"
description: "Applies a bulk configuration change to classify assets from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_classify_assets", "rar_sha256": "dd194b98f6766caa01d70bf8fd051d3ea8f6e805b05d015095b8c8d7c729358c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_classify_assets`. The original RAPP
agent is preserved byte-for-byte in `configure_classify_assets_agent.py` and in the RCI capsule.

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

Classify assets Configuration Bulk Setup — Applies a bulk configuration change to classify assets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-classify-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_classify_assets_agent.py` and embedded as the fenced Python below (sha256 dd194b98f6766caa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_classify_assets_agent.py` first:

```bash
python3 configure_classify_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_classify_assets_agent.py   # or on stdin
python3 configure_classify_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Classify assets Configuration Bulk Setup — Applies a bulk configuration change to classify assets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-classify-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_classify_assets',
    "version": '2.0.1',
    "display_name": 'Classify assets Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to classify assets from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-classify-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-classify-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f58aba90b73692aa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/classify-assets'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-classify-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureClassifyAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureClassifyAssets'
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
    print(ConfigureClassifyAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
