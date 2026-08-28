---
name: "rar-cowork-cookbook-configure-define-project-stakeholders"
description: "Applies a bulk configuration change to define project stakeholders from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_project_stakeholders", "rar_sha256": "d49142da720f1bcdd02ce47bd03e327d03399991fe73c1fe373f18fe0d87a228", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_project_stakeholders`. The original RAPP
agent is preserved byte-for-byte in `configure_define_project_stakeholders_agent.py` and in the RCI capsule.

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

Define project stakeholders Configuration Bulk Setup — Applies a bulk configuration change to define project stakeholders from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-project-stakeholders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_project_stakeholders_agent.py` and embedded as the fenced Python below (sha256 d49142da720f1bcd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_project_stakeholders_agent.py` first:

```bash
python3 configure_define_project_stakeholders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_project_stakeholders_agent.py   # or on stdin
python3 configure_define_project_stakeholders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define project stakeholders Configuration Bulk Setup — Applies a bulk configuration change to define project stakeholders from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-project-stakeholders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_project_stakeholders',
    "version": '2.0.0',
    "display_name": 'Define project stakeholders Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to define project stakeholders from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-define-project-stakeholders',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-project-stakeholders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0794b831574d11bf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/define-project-stakeholders'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/configure-define-project-stakeholders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDefineProjectStakeholders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineProjectStakeholders'
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
    print(ConfigureDefineProjectStakeholders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
