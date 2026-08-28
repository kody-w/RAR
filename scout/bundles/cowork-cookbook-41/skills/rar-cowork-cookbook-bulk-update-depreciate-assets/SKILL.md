---
name: "rar-cowork-cookbook-bulk-update-depreciate-assets"
description: "Applies a bulk field update across depreciate assets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_depreciate_assets", "rar_sha256": "4511dbdb7b8759b8775f9d6a613bbdd117e70da252ca5c61da0f6482ec56600c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_depreciate_assets`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_depreciate_assets_agent.py` and in the RCI capsule.

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
