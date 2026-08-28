---
name: "rar-cowork-cookbook-configure-classify-assets"
description: "Applies a bulk configuration change to classify assets from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_classify_assets", "rar_sha256": "62c20996af6f25a3cfcf6cf82fe56dbfd709f2cfabf9354747a4dd2befe4f8d0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_classify_assets_agent.py` and embedded as the fenced Python below (sha256 62c20996af6f25a3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_classify_assets_agent.py` first:

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
    "version": '2.0.0',
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
