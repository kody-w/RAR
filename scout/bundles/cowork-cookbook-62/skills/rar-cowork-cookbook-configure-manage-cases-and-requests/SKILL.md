---
name: "rar-cowork-cookbook-configure-manage-cases-and-requests"
description: "Applies a bulk configuration change to manage cases and requests from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_cases_and_requests", "rar_sha256": "4e8d983ab97a670e4c3fac19a00fb9b01fb31b5dfcf26fab33d5c09aaf84b82d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_manage_cases_and_requests_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-manage-cases-and-requests:db1bf29d60d8426d64c38a351a60d4d07b22d14357c863fe06176744b139d0e5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_manage_cases_and_requests`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_manage_cases_and_requests_agent.py` is
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
