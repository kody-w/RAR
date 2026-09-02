---
name: "rar-cowork-cookbook-configure-develop-supplier-segments"
description: "Applies a bulk configuration change to develop supplier segments from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_supplier_segments", "rar_sha256": "b06fcb2513c60ae7d9a56153bf3ebddabbe0a07db785a820bcf6f8a32b344613", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_develop_supplier_segments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-develop-supplier-segments:d9bf923554e7a4fec8e599e558d41368b9c7098294ec99de742aed2002440cc9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_develop_supplier_segments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_develop_supplier_segments_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_supplier_segments_agent.py` and embedded as the fenced Python below (sha256 b06fcb2513c60ae7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_supplier_segments_agent.py` first:

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
    "version": '2.0.0',
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
