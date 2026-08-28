---
name: "rar-cowork-cookbook-configure-identify-workplace-hazards"
description: "Applies a bulk configuration change to identify workplace hazards from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_identify_workplace_hazards", "rar_sha256": "1a98541adc262c8fdcd388a589dc212658e6023a36487a3991536b302002534a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_identify_workplace_hazards`. The original RAPP
agent is preserved byte-for-byte in `configure_identify_workplace_hazards_agent.py` and in the RCI capsule.

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

Identify workplace hazards Configuration Bulk Setup — Applies a bulk configuration change to identify workplace hazards from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-identify-workplace-hazards
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_identify_workplace_hazards_agent.py` and embedded as the fenced Python below (sha256 1a98541adc262c8f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_identify_workplace_hazards_agent.py` first:

```bash
python3 configure_identify_workplace_hazards_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_identify_workplace_hazards_agent.py   # or on stdin
python3 configure_identify_workplace_hazards_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify workplace hazards Configuration Bulk Setup — Applies a bulk configuration change to identify workplace hazards from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-identify-workplace-hazards
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_identify_workplace_hazards',
    "version": '2.0.1',
    "display_name": 'Identify workplace hazards Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to identify workplace hazards from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-identify-workplace-hazards',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-identify-workplace-hazards',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '700ef15654dd09eb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/identify-workplace-hazards'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-identify-workplace-hazards', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureIdentifyWorkplaceHazards(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureIdentifyWorkplaceHazards'
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
    print(ConfigureIdentifyWorkplaceHazards().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
