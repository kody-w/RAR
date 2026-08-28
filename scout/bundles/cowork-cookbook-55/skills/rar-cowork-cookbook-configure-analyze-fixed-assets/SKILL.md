---
name: "rar-cowork-cookbook-configure-analyze-fixed-assets"
description: "Applies a bulk configuration change to analyze fixed assets from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_fixed_assets", "rar_sha256": "a4f2ea3fad377bae207d435d4c59634577e5d08cfd5c49f20eb739e6bb0de4ce", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 a4f2ea3fad377bae…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_fixed_assets_agent.py` first:

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
    "version": '2.0.0',
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
