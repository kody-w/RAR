---
name: "rar-cowork-cookbook-configure-create-solution-blueprint"
description: "Applies a bulk configuration change to create solution blueprint from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_create_solution_blueprint", "rar_sha256": "df9368891f9ba84a576f283d229f110d0c4da50174e751195b91717063513595", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_create_solution_blueprint`. The original RAPP
agent is preserved byte-for-byte in `configure_create_solution_blueprint_agent.py` and in the RCI capsule.

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
