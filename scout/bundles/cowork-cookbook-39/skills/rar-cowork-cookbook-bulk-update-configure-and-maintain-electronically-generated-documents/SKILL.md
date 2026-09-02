---
name: "rar-cowork-cookbook-bulk-update-configure-and-maintain-electronically-generated-documents"
description: "Applies a bulk field update across configure and maintain electronically generated documents records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_configure_and_maintain_electronically_generated_documents", "rar_sha256": "4bd54dcbf5ae5bbc615439fa1a41a753fb09d71f23050a557af4834bdf48ed5c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_configure_and_maintain_electronically_generated_documents_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-configure-and-maintain-electronically-generated-documents:1945a9fc252ef17b8a4825f23b72553bf0fbf175bd100f049716255ff5cb090b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_configure_and_maintain_electronically_generated_documents`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_configure_and_maintain_electronically_generated_documents_agent.py` is
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
