---
name: "rar-cowork-cookbook-configure-create-a-case-manually"
description: "Applies a bulk configuration change to create a case manually from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_create_a_case_manually", "rar_sha256": "ac820a8c5a767f01069117b030e905c43be8824bca62d53ef92c438ca5a3f4dc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_create_a_case_manually`. The original RAPP
agent is preserved byte-for-byte in `configure_create_a_case_manually_agent.py` and in the RCI capsule.

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

Create a case manually Configuration Bulk Setup — Applies a bulk configuration change to create a case manually from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-create-a-case-manually
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_create_a_case_manually_agent.py` and embedded as the fenced Python below (sha256 ac820a8c5a767f01…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_create_a_case_manually_agent.py` first:

```bash
python3 configure_create_a_case_manually_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_create_a_case_manually_agent.py   # or on stdin
python3 configure_create_a_case_manually_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create a case manually Configuration Bulk Setup — Applies a bulk configuration change to create a case manually from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-create-a-case-manually
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_create_a_case_manually',
    "version": '2.0.1',
    "display_name": 'Create a case manually Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to create a case manually from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-create-a-case-manually',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-create-a-case-manually',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7e4ff30257501804',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/create-a-case-manually'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/configure-create-a-case-manually', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureCreateACaseManually(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureCreateACaseManually'
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
    print(ConfigureCreateACaseManually().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
