---
name: "rar-cowork-cookbook-configure-define-business-continuity-objectives"
description: "Applies a bulk configuration change to define business continuity objectives from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_business_continuity_objectives", "rar_sha256": "6db96d63a916cfd6bde5760b95defba133987f1698e9a4e210f6f776b8964aa2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_define_business_continuity_objectives_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-define-business-continuity-objectives:b9c2ac077bb912b4e5d15a6d37ce8c0a6d118794b4a497c8b9fb8c5d91fe941a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_define_business_continuity_objectives`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_define_business_continuity_objectives_agent.py` is
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

Define business continuity objectives Configuration Bulk Setup — Applies a bulk configuration change to define business continuity objectives from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-business-continuity-objectives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_business_continuity_objectives_agent.py` and embedded as the fenced Python below (sha256 6db96d63a916cfd6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_business_continuity_objectives_agent.py` first:

```bash
python3 configure_define_business_continuity_objectives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_business_continuity_objectives_agent.py   # or on stdin
python3 configure_define_business_continuity_objectives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define business continuity objectives Configuration Bulk Setup — Applies a bulk configuration change to define business continuity objectives from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-business-continuity-objectives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_business_continuity_objectives',
    "version": '2.0.0',
    "display_name": 'Define business continuity objectives Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to define business continuity objectives from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-define-business-continuity-objectives',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-business-continuity-objectives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5545c1055898def6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/define-business-continuity-objectives'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-define-business-continuity-objectives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDefineBusinessContinuityObjectives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineBusinessContinuityObjectives'
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
    print(ConfigureDefineBusinessContinuityObjectives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
