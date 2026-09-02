---
name: "rar-cowork-cookbook-configure-plan-product-transitions"
description: "Applies a bulk configuration change to plan product transitions from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_product_transitions", "rar_sha256": "d7cfc9eba04dbafda2d31cf8956b945837be3d25b66b82d4179620577ed277dc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_plan_product_transitions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-plan-product-transitions:7dde5eb4e5e2bfd07d5a3a0c42169eb2dd83a5989a40e48982d75b7a61f1f3e5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_plan_product_transitions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_plan_product_transitions_agent.py` is
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

Plan product transitions Configuration Bulk Setup — Applies a bulk configuration change to plan product transitions from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-product-transitions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_product_transitions_agent.py` and embedded as the fenced Python below (sha256 d7cfc9eba04dbafd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_product_transitions_agent.py` first:

```bash
python3 configure_plan_product_transitions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_product_transitions_agent.py   # or on stdin
python3 configure_plan_product_transitions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan product transitions Configuration Bulk Setup — Applies a bulk configuration change to plan product transitions from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-product-transitions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_product_transitions',
    "version": '2.0.0',
    "display_name": 'Plan product transitions Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to plan product transitions from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-plan-product-transitions',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-product-transitions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '96a0c95a433b1bfb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/plan-product-transitions'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/configure-plan-product-transitions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigurePlanProductTransitions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanProductTransitions'
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
    print(ConfigurePlanProductTransitions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
