---
name: "rar-cowork-cookbook-configure-model-service-capacity"
description: "Applies a bulk configuration change to model service capacity from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_model_service_capacity", "rar_sha256": "ed257c1d4b006b61f7d8ab5b2c749da16cb970c9d0c0ca97b0471aa09b2511f6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_model_service_capacity_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-model-service-capacity:d7f758b4346aab7a255daedf98d72d85b39d3f09af3c237817822122c4dccf1b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_model_service_capacity`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_model_service_capacity_agent.py` is
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

Model service capacity Configuration Bulk Setup — Applies a bulk configuration change to model service capacity from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-model-service-capacity
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_model_service_capacity_agent.py` and embedded as the fenced Python below (sha256 ed257c1d4b006b61…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_model_service_capacity_agent.py` first:

```bash
python3 configure_model_service_capacity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_model_service_capacity_agent.py   # or on stdin
python3 configure_model_service_capacity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Model service capacity Configuration Bulk Setup — Applies a bulk configuration change to model service capacity from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-model-service-capacity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_model_service_capacity',
    "version": '2.0.0',
    "display_name": 'Model service capacity Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to model service capacity from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-model-service-capacity',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-model-service-capacity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6342220e43654c34',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/model-service-capacity'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/configure-model-service-capacity', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureModelServiceCapacity(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureModelServiceCapacity'
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
    print(ConfigureModelServiceCapacity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
