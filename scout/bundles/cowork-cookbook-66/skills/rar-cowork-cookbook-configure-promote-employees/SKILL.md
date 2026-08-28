---
name: "rar-cowork-cookbook-configure-promote-employees"
description: "Applies a bulk configuration change to promote employees from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_promote_employees", "rar_sha256": "4aa7190ca9f153f44328a80868925905a9c20ca2726d8ac6dae93338a85a816d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_promote_employees_agent.py` and embedded as the fenced Python below (sha256 4aa7190ca9f153f4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_promote_employees_agent.py` first:

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
    "version": '2.0.0',
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
