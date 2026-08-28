---
name: "rar-cowork-cookbook-configure-process-allocations"
description: "Applies a bulk configuration change to process allocations from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_process_allocations", "rar_sha256": "0e808d8ba638c6d77f28177fea276c15fe48995371b9cc971522af16b8c91803", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_process_allocations`. The original RAPP
agent is preserved byte-for-byte in `configure_process_allocations_agent.py` and in the RCI capsule.

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

Process allocations Configuration Bulk Setup — Applies a bulk configuration change to process allocations from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-process-allocations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_process_allocations_agent.py` and embedded as the fenced Python below (sha256 0e808d8ba638c6d7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_process_allocations_agent.py` first:

```bash
python3 configure_process_allocations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_process_allocations_agent.py   # or on stdin
python3 configure_process_allocations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process allocations Configuration Bulk Setup — Applies a bulk configuration change to process allocations from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-process-allocations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_process_allocations',
    "version": '2.0.0',
    "display_name": 'Process allocations Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to process allocations from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-process-allocations',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-process-allocations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd3389183098435b9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/process-allocations'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-process-allocations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureProcessAllocations(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureProcessAllocations'
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
    print(ConfigureProcessAllocations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
