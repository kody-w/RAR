---
name: "rar-cowork-cookbook-configure-configure-and-maintain-electronically-generated-documents"
description: "Applies a bulk configuration change to configure and maintain electronically generated documents from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_configure_and_maintain_electronically_generated_documents", "rar_sha256": "2174feae5e386d86c524fb6f420d384aa1390c691ad50f66081d44ce77c622ff", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_configure_and_maintain_electronically_generated_documents`. The original RAPP
agent is preserved byte-for-byte in `configure_configure_and_maintain_electronically_generated_documents_agent.py` and in the RCI capsule.

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

Configure and maintain electronically generated documents Configuration Bulk Setup — Applies a bulk configuration change to configure and maintain electronically generated documents from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-configure-and-maintain-electronically-generated-documents
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_configure_and_maintain_electronically_generated_documents_agent.py` and embedded as the fenced Python below (sha256 2174feae5e386d86…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_configure_and_maintain_electronically_generated_documents_agent.py` first:

```bash
python3 configure_configure_and_maintain_electronically_generated_documents_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_configure_and_maintain_electronically_generated_documents_agent.py   # or on stdin
python3 configure_configure_and_maintain_electronically_generated_documents_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and maintain electronically generated documents Configuration Bulk Setup — Applies a bulk configuration change to configure and maintain electronically generated documents from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-configure-and-maintain-electronically-generated-documents
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_configure_and_maintain_electronically_generated_documents',
    "version": '2.0.1',
    "display_name": 'Configure and maintain electronically generated documents Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to configure and maintain electronically generated documents from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-configure-and-maintain-electronically-generated-documents',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-configure-and-maintain-electronically-generated-documents',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f7d10deddcb5e331',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-maintain-electronically-generated-documents'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-configure-and-maintain-electronically-generated-documents', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureConfigureAndMaintainElectronicallyGeneratedDocuments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureConfigureAndMaintainElectronicallyGeneratedDocuments'
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
    print(ConfigureConfigureAndMaintainElectronicallyGeneratedDocuments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
