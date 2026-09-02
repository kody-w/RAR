---
name: "rar-cowork-cookbook-configure-configure-and-maintain-electronically-generated-documents"
description: "Applies a bulk configuration change to configure and maintain electronically generated documents from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_configure_and_maintain_electronically_generated_documents", "rar_sha256": "466f1e02bc14b4c0f38847dca78e3eab6ae2b3c2dc813fd6d3c68b8c449fde99", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_configure_and_maintain_electronically_generated_documents_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-configure-and-maintain-electronically-generated-documents:ab36a736d4988f6368bcb9f0dfdc042ed2d5d6e2aad49e85cc37e55c8a36d799", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_configure_and_maintain_electronically_generated_documents`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_configure_and_maintain_electronically_generated_documents_agent.py` is
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
