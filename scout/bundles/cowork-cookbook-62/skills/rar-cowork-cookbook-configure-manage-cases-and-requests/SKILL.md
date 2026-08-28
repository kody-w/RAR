---
name: "rar-cowork-cookbook-configure-manage-cases-and-requests"
description: "Applies a bulk configuration change to manage cases and requests from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_cases_and_requests", "rar_sha256": "4e8d983ab97a670e4c3fac19a00fb9b01fb31b5dfcf26fab33d5c09aaf84b82d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_cases_and_requests_agent.py` and embedded as the fenced Python below (sha256 4e8d983ab97a670e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_cases_and_requests_agent.py` first:

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
    "version": '2.0.0',
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
