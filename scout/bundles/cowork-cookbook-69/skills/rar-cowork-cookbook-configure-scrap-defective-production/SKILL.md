---
name: "rar-cowork-cookbook-configure-scrap-defective-production"
description: "Applies a bulk configuration change to scrap defective production from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_scrap_defective_production", "rar_sha256": "198f76b2a40912d5aba751db8ef12a82f0cbcd2652a1ee74b6806ad3024b1d55", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_scrap_defective_production`. The original RAPP
agent is preserved byte-for-byte in `configure_scrap_defective_production_agent.py` and in the RCI capsule.

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

Scrap defective production Configuration Bulk Setup — Applies a bulk configuration change to scrap defective production from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-scrap-defective-production
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_scrap_defective_production_agent.py` and embedded as the fenced Python below (sha256 198f76b2a40912d5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_scrap_defective_production_agent.py` first:

```bash
python3 configure_scrap_defective_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_scrap_defective_production_agent.py   # or on stdin
python3 configure_scrap_defective_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Scrap defective production Configuration Bulk Setup — Applies a bulk configuration change to scrap defective production from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-scrap-defective-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_scrap_defective_production',
    "version": '2.0.1',
    "display_name": 'Scrap defective production Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to scrap defective production from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-scrap-defective-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-scrap-defective-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fff1efb887008ee0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/scrap-defective-production'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/configure-scrap-defective-production', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureScrapDefectiveProduction(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureScrapDefectiveProduction'
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
    print(ConfigureScrapDefectiveProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
