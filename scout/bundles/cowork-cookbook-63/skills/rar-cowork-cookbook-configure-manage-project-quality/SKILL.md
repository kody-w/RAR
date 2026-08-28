---
name: "rar-cowork-cookbook-configure-manage-project-quality"
description: "Applies a bulk configuration change to manage project quality from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_project_quality", "rar_sha256": "1d6f3f9c00d76744889494a1f80bd56aba81f67aa4e8766873e4d604cefddaf1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_project_quality`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_project_quality_agent.py` and in the RCI capsule.

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

Manage project quality Configuration Bulk Setup — Applies a bulk configuration change to manage project quality from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-project-quality
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_project_quality_agent.py` and embedded as the fenced Python below (sha256 1d6f3f9c00d76744…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_project_quality_agent.py` first:

```bash
python3 configure_manage_project_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_project_quality_agent.py   # or on stdin
python3 configure_manage_project_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project quality Configuration Bulk Setup — Applies a bulk configuration change to manage project quality from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-project-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_project_quality',
    "version": '2.0.0',
    "display_name": 'Manage project quality Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage project quality from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-project-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-project-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dc59b91fe812ac6b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/manage-project-quality'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/configure-manage-project-quality', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureManageProjectQuality(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageProjectQuality'
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
    print(ConfigureManageProjectQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
