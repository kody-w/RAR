---
name: "rar-cowork-cookbook-bulk-update-purchase-assets"
description: "Applies a bulk field update across purchase assets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_purchase_assets", "rar_sha256": "f524cb2346478d42c95cf9fcb1412a05563cd596405a624b8b4792855dba7b31", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_purchase_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-purchase-assets:59517f4681417a99a42e5bbcc91bcd5214fa5b18c8eba908a90bb7d9e6d41d32", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_purchase_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_purchase_assets_agent.py` is
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

Purchase assets Bulk Field Update — Applies a bulk field update across purchase assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-purchase-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_purchase_assets_agent.py` and embedded as the fenced Python below (sha256 f524cb2346478d42…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_purchase_assets_agent.py` first:

```bash
python3 bulk_update_purchase_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_purchase_assets_agent.py   # or on stdin
python3 bulk_update_purchase_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Purchase assets Bulk Field Update — Applies a bulk field update across purchase assets records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-purchase-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_purchase_assets',
    "version": '2.0.0',
    "display_name": 'Purchase assets Bulk Field Update',
    "description": 'Applies a bulk field update across purchase assets records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-purchase-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-purchase-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dc6286a232c60202',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/purchase-assets'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-purchase-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdatePurchaseAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePurchaseAssets'
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
    print(BulkUpdatePurchaseAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
