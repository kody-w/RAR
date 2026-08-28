---
name: "rar-cowork-cookbook-configure-design-formulas"
description: "Applies a bulk configuration change to design formulas from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_design_formulas", "rar_sha256": "d7783435fa1706485b67ce2cc13b05242ebf8dda715892f2107e166bbf7a59d9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_design_formulas_agent.py` and embedded as the fenced Python below (sha256 d7783435fa170648…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_design_formulas_agent.py` first:

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
    "version": '2.0.0',
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
