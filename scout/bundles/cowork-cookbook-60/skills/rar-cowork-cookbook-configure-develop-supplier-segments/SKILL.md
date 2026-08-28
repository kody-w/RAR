---
name: "rar-cowork-cookbook-configure-develop-supplier-segments"
description: "Applies a bulk configuration change to develop supplier segments from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_supplier_segments", "rar_sha256": "e71914246652e3e5b14b3ef8bc8530ea2af7787bd840647d478ca84c72dbfe56", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_supplier_segments_agent.py` and embedded as the fenced Python below (sha256 e71914246652e3e5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_supplier_segments_agent.py` first:

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
    "version": '2.0.1',
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
