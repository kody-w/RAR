---
name: "rar-cowork-cookbook-configure-design-formulas"
description: "Applies a bulk configuration change to design formulas from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_design_formulas", "rar_sha256": "6cf80a767bda987fa590e4664e3d2c33585cd4791bc5eafd4a00bc703a6de000", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_design_formulas`. The original RAPP
agent is preserved byte-for-byte in `configure_design_formulas_agent.py` and in the RCI capsule.

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

Design formulas Configuration Bulk Setup — Applies a bulk configuration change to design formulas from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-design-formulas
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_design_formulas_agent.py` and embedded as the fenced Python below (sha256 6cf80a767bda987f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_design_formulas_agent.py` first:

```bash
python3 configure_design_formulas_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_design_formulas_agent.py   # or on stdin
python3 configure_design_formulas_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Design formulas Configuration Bulk Setup — Applies a bulk configuration change to design formulas from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-design-formulas
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_design_formulas',
    "version": '2.0.1',
    "display_name": 'Design formulas Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to design formulas from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-design-formulas',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-design-formulas',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8642107dd7a75fc6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/design-formulas'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/configure-design-formulas', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDesignFormulas(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDesignFormulas'
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
    print(ConfigureDesignFormulas().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
