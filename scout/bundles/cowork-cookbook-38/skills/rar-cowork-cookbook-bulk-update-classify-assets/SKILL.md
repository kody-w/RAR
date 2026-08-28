---
name: "rar-cowork-cookbook-bulk-update-classify-assets"
description: "Applies a bulk field update across classify assets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_classify_assets", "rar_sha256": "9ef5ea62c87426220a8f94650e59f777aa3c5511911b54e0d45bd7069726d558", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_classify_assets`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_classify_assets_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_classify_assets_agent.py` and embedded as the fenced Python below (sha256 9ef5ea62c8742622…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_classify_assets_agent.py` first:

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
    "version": '2.0.1',
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
