---
name: "rar-cowork-cookbook-configure-process-allocations"
description: "Applies a bulk configuration change to process allocations from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_process_allocations", "rar_sha256": "0e808d8ba638c6d77f28177fea276c15fe48995371b9cc971522af16b8c91803", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_process_allocations_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-process-allocations:9322f723ee836503700f766b4491341cc66268e20ac46ab5dc7279b55d5ae227", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_process_allocations`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_process_allocations_agent.py` is
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
