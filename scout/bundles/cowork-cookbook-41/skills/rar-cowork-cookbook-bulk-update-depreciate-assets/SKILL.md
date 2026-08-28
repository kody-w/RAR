---
name: "rar-cowork-cookbook-bulk-update-depreciate-assets"
description: "Applies a bulk field update across depreciate assets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_depreciate_assets", "rar_sha256": "b0bda8245ca262ffd3066310a986559587133646cd6456ec2db54079899527b7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_depreciate_assets_agent.py` and embedded as the fenced Python below (sha256 b0bda8245ca262ff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_depreciate_assets_agent.py` first:

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
    "version": '2.0.1',
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
