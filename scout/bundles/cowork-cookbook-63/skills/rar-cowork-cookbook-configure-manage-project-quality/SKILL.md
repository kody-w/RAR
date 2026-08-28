---
name: "rar-cowork-cookbook-configure-manage-project-quality"
description: "Applies a bulk configuration change to manage project quality from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_project_quality", "rar_sha256": "5cc2a8a84d84395952b2f8e7cf86897dfa56fe503a98ab16c0621f736f26ea3f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_project_quality_agent.py` and embedded as the fenced Python below (sha256 5cc2a8a84d843959…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_project_quality_agent.py` first:

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
    "version": '2.0.1',
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
