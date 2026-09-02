---
name: "rar-cowork-cookbook-bulk-update-depreciate-assets"
description: "Applies a bulk field update across depreciate assets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_depreciate_assets", "rar_sha256": "4511dbdb7b8759b8775f9d6a613bbdd117e70da252ca5c61da0f6482ec56600c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_depreciate_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-depreciate-assets:ad2455b672722fd128090e2ee0f0a3c29f423c2eae8458cd04ef86f1db05f6f6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_depreciate_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_depreciate_assets_agent.py` is
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

Depreciate assets Bulk Field Update — Applies a bulk field update across depreciate assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-depreciate-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_depreciate_assets_agent.py` and embedded as the fenced Python below (sha256 4511dbdb7b8759b8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_depreciate_assets_agent.py` first:

```bash
python3 bulk_update_depreciate_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_depreciate_assets_agent.py   # or on stdin
python3 bulk_update_depreciate_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Depreciate assets Bulk Field Update — Applies a bulk field update across depreciate assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-depreciate-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_depreciate_assets',
    "version": '2.0.0',
    "display_name": 'Depreciate assets Bulk Field Update',
    "description": 'Applies a bulk field update across depreciate assets records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-depreciate-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-depreciate-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '84e4691ec265f7dd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/depreciate-assets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-depreciate-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateDepreciateAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDepreciateAssets'
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
    print(BulkUpdateDepreciateAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
