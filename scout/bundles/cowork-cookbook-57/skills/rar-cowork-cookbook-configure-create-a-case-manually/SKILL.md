---
name: "rar-cowork-cookbook-configure-create-a-case-manually"
description: "Applies a bulk configuration change to create a case manually from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_create_a_case_manually", "rar_sha256": "941712f5811073f894c1f99438baff5c2237120352922b122bc5bbf8e285cc07", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_create_a_case_manually_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-create-a-case-manually:aa4bb4cca43f8d2cd88b07f75e3981989c9227f76ca7edd0bb0ef0a593504014", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_create_a_case_manually`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_create_a_case_manually_agent.py` is
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
