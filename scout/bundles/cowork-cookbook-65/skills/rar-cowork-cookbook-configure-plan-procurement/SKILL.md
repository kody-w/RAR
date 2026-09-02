---
name: "rar-cowork-cookbook-configure-plan-procurement"
description: "Applies a bulk configuration change to plan procurement from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_procurement", "rar_sha256": "1301ac4224bd8ecea0de14487bacb2ce15157dc086e0e8956a49bc5a2365097b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_plan_procurement_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-plan-procurement:813a155320f160cd031902565f61418d8f2f487362c47ad4089ef6f3005f96e2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_plan_procurement`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_plan_procurement_agent.py` is
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

Plan procurement Configuration Bulk Setup — Applies a bulk configuration change to plan procurement from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-procurement
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_procurement_agent.py` and embedded as the fenced Python below (sha256 1301ac4224bd8ece…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_procurement_agent.py` first:

```bash
python3 configure_plan_procurement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_procurement_agent.py   # or on stdin
python3 configure_plan_procurement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan procurement Configuration Bulk Setup — Applies a bulk configuration change to plan procurement from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-procurement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_procurement',
    "version": '2.0.0',
    "display_name": 'Plan procurement Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to plan procurement from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-plan-procurement',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-procurement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ec4ac3a0c0b91806',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-procurement'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-plan-procurement', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigurePlanProcurement(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanProcurement'
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
    print(ConfigurePlanProcurement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
