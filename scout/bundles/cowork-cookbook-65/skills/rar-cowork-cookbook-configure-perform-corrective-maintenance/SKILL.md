---
name: "rar-cowork-cookbook-configure-perform-corrective-maintenance"
description: "Applies a bulk configuration change to perform corrective maintenance from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_perform_corrective_maintenance", "rar_sha256": "df5e82680e7ad84014431dea0d94d12df57c8e162a67743ed9e9edcedd1b7e02", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_perform_corrective_maintenance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-perform-corrective-maintenance:fc78a1d9accaf5f293a82786f11205855b5136bddb202663f9b650da0069b06a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_perform_corrective_maintenance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_perform_corrective_maintenance_agent.py` is
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

Perform corrective maintenance Configuration Bulk Setup — Applies a bulk configuration change to perform corrective maintenance from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-perform-corrective-maintenance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_perform_corrective_maintenance_agent.py` and embedded as the fenced Python below (sha256 df5e82680e7ad840…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_perform_corrective_maintenance_agent.py` first:

```bash
python3 configure_perform_corrective_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_perform_corrective_maintenance_agent.py   # or on stdin
python3 configure_perform_corrective_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform corrective maintenance Configuration Bulk Setup — Applies a bulk configuration change to perform corrective maintenance from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-perform-corrective-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_perform_corrective_maintenance',
    "version": '2.0.0',
    "display_name": 'Perform corrective maintenance Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to perform corrective maintenance from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-perform-corrective-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-perform-corrective-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0f2fbd3fbf95fa0b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/perform-corrective-maintenance'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-perform-corrective-maintenance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigurePerformCorrectiveMaintenance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePerformCorrectiveMaintenance'
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
    print(ConfigurePerformCorrectiveMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
