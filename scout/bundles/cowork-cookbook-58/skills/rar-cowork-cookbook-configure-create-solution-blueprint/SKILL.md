---
name: "rar-cowork-cookbook-configure-create-solution-blueprint"
description: "Applies a bulk configuration change to create solution blueprint from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_create_solution_blueprint", "rar_sha256": "df9368891f9ba84a576f283d229f110d0c4da50174e751195b91717063513595", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_create_solution_blueprint_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-create-solution-blueprint:32ee3a47971729ee6b5f20f1d23b4281d5e5a0045a915fd93122d09beecbfb4e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_create_solution_blueprint`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_create_solution_blueprint_agent.py` is
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

Create solution blueprint Configuration Bulk Setup — Applies a bulk configuration change to create solution blueprint from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-create-solution-blueprint
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_create_solution_blueprint_agent.py` and embedded as the fenced Python below (sha256 df9368891f9ba84a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_create_solution_blueprint_agent.py` first:

```bash
python3 configure_create_solution_blueprint_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_create_solution_blueprint_agent.py   # or on stdin
python3 configure_create_solution_blueprint_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create solution blueprint Configuration Bulk Setup — Applies a bulk configuration change to create solution blueprint from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-create-solution-blueprint
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_create_solution_blueprint',
    "version": '2.0.0',
    "display_name": 'Create solution blueprint Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to create solution blueprint from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-create-solution-blueprint',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-create-solution-blueprint',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0b771f23f0be4b93',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/create-solution-blueprint'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-create-solution-blueprint', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureCreateSolutionBlueprint(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureCreateSolutionBlueprint'
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
    print(ConfigureCreateSolutionBlueprint().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
