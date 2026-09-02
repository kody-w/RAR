---
name: "rar-cowork-cookbook-configure-define-project-stakeholders"
description: "Applies a bulk configuration change to define project stakeholders from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_project_stakeholders", "rar_sha256": "d49142da720f1bcdd02ce47bd03e327d03399991fe73c1fe373f18fe0d87a228", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_define_project_stakeholders_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-define-project-stakeholders:307cee7e0b818af4a17e5a75dd17b91a78c5879f6b43b8ce17853ce0fb3391c3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_define_project_stakeholders`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_define_project_stakeholders_agent.py` is
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
