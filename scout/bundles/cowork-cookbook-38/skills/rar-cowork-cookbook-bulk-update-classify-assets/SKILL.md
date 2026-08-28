---
name: "rar-cowork-cookbook-bulk-update-classify-assets"
description: "Applies a bulk field update across classify assets records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_classify_assets", "rar_sha256": "c90d612c8ce595d78be31b846763b9661be59bf8200d5b2147a1ecf6d63580bc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
