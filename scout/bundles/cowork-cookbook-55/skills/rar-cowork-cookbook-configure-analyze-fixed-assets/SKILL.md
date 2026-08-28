---
name: "rar-cowork-cookbook-configure-analyze-fixed-assets"
description: "Applies a bulk configuration change to analyze fixed assets from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_fixed_assets", "rar_sha256": "a6f18dee895674c92d965366db36564e914c082b65df58680da2b6f5fd931098", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_fixed_assets_agent.py` and in the RCI capsule.

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

Analyze fixed assets Configuration Bulk Setup — Applies a bulk configuration change to analyze fixed assets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-fixed-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 a6f18dee895674c9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_fixed_assets_agent.py` first:

```bash
python3 configure_analyze_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_fixed_assets_agent.py   # or on stdin
python3 configure_analyze_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze fixed assets Configuration Bulk Setup — Applies a bulk configuration change to analyze fixed assets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_fixed_assets',
    "version": '2.0.1',
    "display_name": 'Analyze fixed assets Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze fixed assets from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-analyze-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '87e9348e7a9140a9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-fixed-assets'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-analyze-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureAnalyzeFixedAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeFixedAssets'
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
    print(ConfigureAnalyzeFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
