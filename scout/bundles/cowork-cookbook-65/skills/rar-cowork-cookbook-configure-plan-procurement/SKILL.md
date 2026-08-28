---
name: "rar-cowork-cookbook-configure-plan-procurement"
description: "Applies a bulk configuration change to plan procurement from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_procurement", "rar_sha256": "1301ac4224bd8ecea0de14487bacb2ce15157dc086e0e8956a49bc5a2365097b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_plan_procurement`. The original RAPP
agent is preserved byte-for-byte in `configure_plan_procurement_agent.py` and in the RCI capsule.

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
