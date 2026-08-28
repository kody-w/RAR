---
name: "rar-cowork-cookbook-configure-onboard-new-contractors"
description: "Applies a bulk configuration change to onboard new contractors from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_onboard_new_contractors", "rar_sha256": "1f1dbfe356a18d80b8bff0b074120888c940cbac118bdb94709aaea014e2b2e0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_onboard_new_contractors_agent.py` and embedded as the fenced Python below (sha256 1f1dbfe356a18d80…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_onboard_new_contractors_agent.py` first:

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
    "version": '2.0.0',
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
