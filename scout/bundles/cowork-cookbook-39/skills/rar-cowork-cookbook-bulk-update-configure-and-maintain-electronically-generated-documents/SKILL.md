---
name: "rar-cowork-cookbook-bulk-update-configure-and-maintain-electronically-generated-documents"
description: "Applies a bulk field update across configure and maintain electronically generated documents records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_configure_and_maintain_electronically_generated_documents", "rar_sha256": "e4c4cf28181a4639b4540f88a5799f19acef12725c281d080aca40510aff3b68", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_configure_and_maintain_electronically_generated_documents`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_configure_and_maintain_electronically_generated_documents_agent.py` and in the RCI capsule.

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

Configure and maintain electronically generated documents Bulk Field Update — Applies a bulk field update across configure and maintain electronically generated documents records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-configure-and-maintain-electronically-generated-documents
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_configure_and_maintain_electronically_generated_documents_agent.py` and embedded as the fenced Python below (sha256 e4c4cf28181a4639…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_configure_and_maintain_electronically_generated_documents_agent.py` first:

```bash
python3 bulk_update_configure_and_maintain_electronically_generated_documents_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_configure_and_maintain_electronically_generated_documents_agent.py   # or on stdin
python3 bulk_update_configure_and_maintain_electronically_generated_documents_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and maintain electronically generated documents Bulk Field Update — Applies a bulk field update across configure and maintain electronically generated documents records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-configure-and-maintain-electronically-generated-documents
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_configure_and_maintain_electronically_generated_documents',
    "version": '2.0.1',
    "display_name": 'Configure and maintain electronically generated documents Bulk Field Update',
    "description": 'Applies a bulk field update across configure and maintain electronically generated documents records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-configure-and-maintain-electronically-generated-documents',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-configure-and-maintain-electronically-generated-documents',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '66a927f7b613abda',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-maintain-electronically-generated-documents'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-configure-and-maintain-electronically-generated-documents', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateConfigureAndMaintainElectronicallyGeneratedDocuments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateConfigureAndMaintainElectronicallyGeneratedDocuments'
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
    print(BulkUpdateConfigureAndMaintainElectronicallyGeneratedDocuments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
