---
name: "rar-cowork-cookbook-configure-analyze-fixed-assets"
description: "Applies a bulk configuration change to analyze fixed assets from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_fixed_assets", "rar_sha256": "a4f2ea3fad377bae207d435d4c59634577e5d08cfd5c49f20eb739e6bb0de4ce", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_analyze_fixed_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-analyze-fixed-assets:9de4d32ed35ba70c400af898faa24b400b31755f46fc4dbef8468671eb7be976", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_analyze_fixed_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_analyze_fixed_assets_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
