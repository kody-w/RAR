---
name: "rar-cowork-cookbook-configure-report-quality-non-conformance"
description: "Applies a bulk configuration change to report quality non-conformance from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_report_quality_non_conformance", "rar_sha256": "21880988fc6314536b7a792e312fdb16cd47b4d5747e2152fab3d6d45e1ce924", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_report_quality_non_conformance`. The original RAPP
agent is preserved byte-for-byte in `configure_report_quality_non_conformance_agent.py` and in the RCI capsule.

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

Report quality non-conformance Configuration Bulk Setup — Applies a bulk configuration change to report quality non-conformance from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-report-quality-non-conformance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_report_quality_non_conformance_agent.py` and embedded as the fenced Python below (sha256 21880988fc631453…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_report_quality_non_conformance_agent.py` first:

```bash
python3 configure_report_quality_non_conformance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_report_quality_non_conformance_agent.py   # or on stdin
python3 configure_report_quality_non_conformance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report quality non-conformance Configuration Bulk Setup — Applies a bulk configuration change to report quality non-conformance from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-report-quality-non-conformance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_report_quality_non_conformance',
    "version": '2.0.1',
    "display_name": 'Report quality non-conformance Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to report quality non-conformance from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-report-quality-non-conformance',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-report-quality-non-conformance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '184d2447414bdcf0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/report-quality-non-conformance'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-report-quality-non-conformance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureReportQualityNonConformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReportQualityNonConformance'
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
    print(ConfigureReportQualityNonConformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
