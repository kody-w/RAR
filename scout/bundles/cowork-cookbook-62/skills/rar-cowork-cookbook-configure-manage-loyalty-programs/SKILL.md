---
name: "rar-cowork-cookbook-configure-manage-loyalty-programs"
description: "Applies a bulk configuration change to manage loyalty programs from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_loyalty_programs", "rar_sha256": "34e0c51e619251516ed581b2845feb28f7bc6f6a55e984ec3db25d65cf271224", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_loyalty_programs`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_loyalty_programs_agent.py` and in the RCI capsule.

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

Manage loyalty programs Configuration Bulk Setup — Applies a bulk configuration change to manage loyalty programs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-loyalty-programs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_loyalty_programs_agent.py` and embedded as the fenced Python below (sha256 34e0c51e61925151…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_loyalty_programs_agent.py` first:

```bash
python3 configure_manage_loyalty_programs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_loyalty_programs_agent.py   # or on stdin
python3 configure_manage_loyalty_programs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage loyalty programs Configuration Bulk Setup — Applies a bulk configuration change to manage loyalty programs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-loyalty-programs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_loyalty_programs',
    "version": '2.0.1',
    "display_name": 'Manage loyalty programs Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage loyalty programs from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-loyalty-programs',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-loyalty-programs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7b20f4a724994b1a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/manage-loyalty-programs'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/configure-manage-loyalty-programs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureManageLoyaltyPrograms(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageLoyaltyPrograms'
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
    print(ConfigureManageLoyaltyPrograms().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
