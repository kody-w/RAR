---
name: "rar-cowork-cookbook-configure-create-a-case-manually"
description: "Applies a bulk configuration change to create a case manually from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_create_a_case_manually", "rar_sha256": "941712f5811073f894c1f99438baff5c2237120352922b122bc5bbf8e285cc07", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_create_a_case_manually_agent.py` and embedded as the fenced Python below (sha256 941712f5811073f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_create_a_case_manually_agent.py` first:

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
    "version": '2.0.0',
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
