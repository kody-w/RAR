---
name: "rar-cowork-cookbook-configure-configure-and-maintain-electronically-generated-documents"
description: "Applies a bulk configuration change to configure and maintain electronically generated documents from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_configure_and_maintain_electronically_generated_documents", "rar_sha256": "466f1e02bc14b4c0f38847dca78e3eab6ae2b3c2dc813fd6d3c68b8c449fde99", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_configure_and_maintain_electronically_generated_documents_agent.py` and embedded as the fenced Python below (sha256 466f1e02bc14b4c0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_configure_and_maintain_electronically_generated_documents_agent.py` first:

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
    "version": '2.0.0',
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
