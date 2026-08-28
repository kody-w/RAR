---
name: "rar-cowork-cookbook-configure-onboard-new-contractors"
description: "Applies a bulk configuration change to onboard new contractors from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_onboard_new_contractors", "rar_sha256": "5867d5cc9cd7c02c7b2f90049d0bb209b1b8c1b3e6a6124e103b1b210a8e5150", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_onboard_new_contractors`. The original RAPP
agent is preserved byte-for-byte in `configure_onboard_new_contractors_agent.py` and in the RCI capsule.

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

Onboard new contractors Configuration Bulk Setup — Applies a bulk configuration change to onboard new contractors from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-onboard-new-contractors
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_onboard_new_contractors_agent.py` and embedded as the fenced Python below (sha256 5867d5cc9cd7c02c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_onboard_new_contractors_agent.py` first:

```bash
python3 configure_onboard_new_contractors_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_onboard_new_contractors_agent.py   # or on stdin
python3 configure_onboard_new_contractors_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new contractors Configuration Bulk Setup — Applies a bulk configuration change to onboard new contractors from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-onboard-new-contractors
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_onboard_new_contractors',
    "version": '2.0.1',
    "display_name": 'Onboard new contractors Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to onboard new contractors from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-onboard-new-contractors',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-onboard-new-contractors',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a8a7440a353b2b4b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/onboard-new-contractors'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-onboard-new-contractors', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureOnboardNewContractors(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureOnboardNewContractors'
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
    print(ConfigureOnboardNewContractors().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
