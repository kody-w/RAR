---
name: "rar-cowork-cookbook-configure-define-posting-policies"
description: "Applies a bulk configuration change to define posting policies from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_posting_policies", "rar_sha256": "8f8f066b5f619cc0e2ad6f6e0cf8a848993419c14ad01fadac3d00ce144a003e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_posting_policies`. The original RAPP
agent is preserved byte-for-byte in `configure_define_posting_policies_agent.py` and in the RCI capsule.

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

Define posting policies Configuration Bulk Setup — Applies a bulk configuration change to define posting policies from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-posting-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_posting_policies_agent.py` and embedded as the fenced Python below (sha256 8f8f066b5f619cc0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_posting_policies_agent.py` first:

```bash
python3 configure_define_posting_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_posting_policies_agent.py   # or on stdin
python3 configure_define_posting_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define posting policies Configuration Bulk Setup — Applies a bulk configuration change to define posting policies from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-posting-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_posting_policies',
    "version": '2.0.1',
    "display_name": 'Define posting policies Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to define posting policies from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-define-posting-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-posting-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8bd7de4a8d7e0be2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/define-posting-policies'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-define-posting-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDefinePostingPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefinePostingPolicies'
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
    print(ConfigureDefinePostingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
