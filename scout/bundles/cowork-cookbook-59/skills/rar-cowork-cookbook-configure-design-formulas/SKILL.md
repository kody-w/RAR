---
name: "rar-cowork-cookbook-configure-design-formulas"
description: "Applies a bulk configuration change to design formulas from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_design_formulas", "rar_sha256": "d7783435fa1706485b67ce2cc13b05242ebf8dda715892f2107e166bbf7a59d9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_design_formulas_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-design-formulas:f7e37ace978e765289c8c191214adff4579da01e20fca9e90555c5409c4413c7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_design_formulas`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_design_formulas_agent.py` is
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
