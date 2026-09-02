---
name: "rar-cowork-cookbook-bulk-update-classify-assets"
description: "Applies a bulk field update across classify assets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_classify_assets", "rar_sha256": "c90d612c8ce595d78be31b846763b9661be59bf8200d5b2147a1ecf6d63580bc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_classify_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-classify-assets:04ddb81019f65bbd26d2803dcff30157ead9871ca63ba03abade9b8504b98da5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_classify_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_classify_assets_agent.py` is
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

Classify assets Bulk Field Update — Applies a bulk field update across classify assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-classify-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_classify_assets_agent.py` and embedded as the fenced Python below (sha256 c90d612c8ce595d7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_classify_assets_agent.py` first:

```bash
python3 bulk_update_classify_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_classify_assets_agent.py   # or on stdin
python3 bulk_update_classify_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Classify assets Bulk Field Update — Applies a bulk field update across classify assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-classify-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_classify_assets',
    "version": '2.0.0',
    "display_name": 'Classify assets Bulk Field Update',
    "description": 'Applies a bulk field update across classify assets records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-classify-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-classify-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '162e9ab3fb3bdcad',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/classify-assets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-classify-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateClassifyAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateClassifyAssets'
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
    print(BulkUpdateClassifyAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
