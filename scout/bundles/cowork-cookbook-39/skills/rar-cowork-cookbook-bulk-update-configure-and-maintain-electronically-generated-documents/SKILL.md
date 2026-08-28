---
name: "rar-cowork-cookbook-bulk-update-configure-and-maintain-electronically-generated-documents"
description: "Applies a bulk field update across configure and maintain electronically generated documents records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_configure_and_maintain_electronically_generated_documents", "rar_sha256": "4bd54dcbf5ae5bbc615439fa1a41a753fb09d71f23050a557af4834bdf48ed5c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_configure_and_maintain_electronically_generated_documents_agent.py` and embedded as the fenced Python below (sha256 4bd54dcbf5ae5bbc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_configure_and_maintain_electronically_generated_documents_agent.py` first:

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
    "version": '2.0.0',
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
