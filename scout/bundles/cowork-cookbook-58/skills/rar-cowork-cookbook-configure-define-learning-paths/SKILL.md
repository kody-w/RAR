---
name: "rar-cowork-cookbook-configure-define-learning-paths"
description: "Applies a bulk configuration change to define learning paths from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_learning_paths", "rar_sha256": "e687b6514a290fc0eddf7e6c726574bcbc2ec26e2636afe95a4703d39872d2f8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_learning_paths_agent.py` and embedded as the fenced Python below (sha256 e687b6514a290fc0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_learning_paths_agent.py` first:

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
    "version": '2.0.0',
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
