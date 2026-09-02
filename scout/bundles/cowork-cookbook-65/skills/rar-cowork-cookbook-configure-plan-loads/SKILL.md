---
name: "rar-cowork-cookbook-configure-plan-loads"
description: "Applies a bulk configuration change to plan loads from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_loads", "rar_sha256": "302e62cbe452c8a143701623a132f214a9f81c36713dd8321685bdbf46146a83", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_plan_loads_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-plan-loads:42aaf9ceb0ae7d22c4e0947398416d0c4c5e75c5142d5cc68f83c15271833828", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_plan_loads`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_plan_loads_agent.py` is
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

Plan loads Configuration Bulk Setup — Applies a bulk configuration change to plan loads from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-loads
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_loads_agent.py` and embedded as the fenced Python below (sha256 302e62cbe452c8a1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_loads_agent.py` first:

```bash
python3 configure_plan_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_loads_agent.py   # or on stdin
python3 configure_plan_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan loads Configuration Bulk Setup — Applies a bulk configuration change to plan loads from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_loads',
    "version": '2.0.0',
    "display_name": 'Plan loads Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to plan loads from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-plan-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '51bb804c681b8b23',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/plan-loads'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-plan-loads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigurePlanLoads(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanLoads'
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
    print(ConfigurePlanLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
