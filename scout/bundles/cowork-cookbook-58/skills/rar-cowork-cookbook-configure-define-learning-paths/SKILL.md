---
name: "rar-cowork-cookbook-configure-define-learning-paths"
description: "Applies a bulk configuration change to define learning paths from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_learning_paths", "rar_sha256": "7bf2a8b69e209a0dd8a8d21e90213509def818c14511f9a9baceabface979dc0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_learning_paths`. The original RAPP
agent is preserved byte-for-byte in `configure_define_learning_paths_agent.py` and in the RCI capsule.

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

Define learning paths Configuration Bulk Setup — Applies a bulk configuration change to define learning paths from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-learning-paths
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_learning_paths_agent.py` and embedded as the fenced Python below (sha256 7bf2a8b69e209a0d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_learning_paths_agent.py` first:

```bash
python3 configure_define_learning_paths_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_learning_paths_agent.py   # or on stdin
python3 configure_define_learning_paths_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define learning paths Configuration Bulk Setup — Applies a bulk configuration change to define learning paths from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-learning-paths
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_learning_paths',
    "version": '2.0.1',
    "display_name": 'Define learning paths Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to define learning paths from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-define-learning-paths',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-learning-paths',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6f2a4466caad25d3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/define-learning-paths'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-define-learning-paths', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDefineLearningPaths(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineLearningPaths'
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
    print(ConfigureDefineLearningPaths().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
