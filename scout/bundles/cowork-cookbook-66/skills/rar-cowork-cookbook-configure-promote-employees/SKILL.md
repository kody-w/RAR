---
name: "rar-cowork-cookbook-configure-promote-employees"
description: "Applies a bulk configuration change to promote employees from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_promote_employees", "rar_sha256": "93bd6854a46a5baf33a9d4eb5b33be767a59dcc43aca1a9f19a70919046e7dba", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_promote_employees`. The original RAPP
agent is preserved byte-for-byte in `configure_promote_employees_agent.py` and in the RCI capsule.

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

Promote employees Configuration Bulk Setup — Applies a bulk configuration change to promote employees from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-promote-employees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_promote_employees_agent.py` and embedded as the fenced Python below (sha256 93bd6854a46a5baf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_promote_employees_agent.py` first:

```bash
python3 configure_promote_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_promote_employees_agent.py   # or on stdin
python3 configure_promote_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Promote employees Configuration Bulk Setup — Applies a bulk configuration change to promote employees from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-promote-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_promote_employees',
    "version": '2.0.1',
    "display_name": 'Promote employees Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to promote employees from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-promote-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-promote-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '761f58cc84276241',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/promote-employees'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-promote-employees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigurePromoteEmployees(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePromoteEmployees'
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
    print(ConfigurePromoteEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
