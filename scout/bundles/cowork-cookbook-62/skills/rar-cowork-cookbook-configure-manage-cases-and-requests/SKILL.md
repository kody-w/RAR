---
name: "rar-cowork-cookbook-configure-manage-cases-and-requests"
description: "Applies a bulk configuration change to manage cases and requests from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_cases_and_requests", "rar_sha256": "6ffd0aa33c7046ca4a0e14693e1192c174916d79c7e3f4d9795932fc18604cfe", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_cases_and_requests`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_cases_and_requests_agent.py` and in the RCI capsule.

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

Manage cases and requests Configuration Bulk Setup — Applies a bulk configuration change to manage cases and requests from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-cases-and-requests
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_cases_and_requests_agent.py` and embedded as the fenced Python below (sha256 6ffd0aa33c7046ca…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_cases_and_requests_agent.py` first:

```bash
python3 configure_manage_cases_and_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_cases_and_requests_agent.py   # or on stdin
python3 configure_manage_cases_and_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage cases and requests Configuration Bulk Setup — Applies a bulk configuration change to manage cases and requests from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-cases-and-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_cases_and_requests',
    "version": '2.0.1',
    "display_name": 'Manage cases and requests Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage cases and requests from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-manage-cases-and-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-cases-and-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aa38585afc0d58e5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/manage-cases-and-requests'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-manage-cases-and-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureManageCasesAndRequests(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageCasesAndRequests'
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
    print(ConfigureManageCasesAndRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
