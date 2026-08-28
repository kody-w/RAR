---
name: "rar-cowork-cookbook-configure-develop-supplier-segments"
description: "Applies a bulk configuration change to develop supplier segments from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_supplier_segments", "rar_sha256": "b06fcb2513c60ae7d9a56153bf3ebddabbe0a07db785a820bcf6f8a32b344613", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_supplier_segments`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_supplier_segments_agent.py` and in the RCI capsule.

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

Develop supplier segments Configuration Bulk Setup — Applies a bulk configuration change to develop supplier segments from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-supplier-segments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_supplier_segments_agent.py` and embedded as the fenced Python below (sha256 b06fcb2513c60ae7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_supplier_segments_agent.py` first:

```bash
python3 configure_develop_supplier_segments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_supplier_segments_agent.py   # or on stdin
python3 configure_develop_supplier_segments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop supplier segments Configuration Bulk Setup — Applies a bulk configuration change to develop supplier segments from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-supplier-segments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_supplier_segments',
    "version": '2.0.0',
    "display_name": 'Develop supplier segments Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to develop supplier segments from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-develop-supplier-segments',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-supplier-segments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '25dedf71e9cc4f16',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/develop-supplier-segments'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-develop-supplier-segments', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureDevelopSupplierSegments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopSupplierSegments'
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
    print(ConfigureDevelopSupplierSegments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
