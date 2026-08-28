---
name: "rar-cowork-cookbook-bulk-update-analyze-product-quality-data"
description: "Applies a bulk field update across analyze product quality data records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_product_quality_data", "rar_sha256": "21310cd4b074b23c55697d80ae9377f8ecf57a05d64d99ab4595e25b574635be", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_analyze_product_quality_data`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_analyze_product_quality_data_agent.py` and in the RCI capsule.

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

Analyze product quality data Bulk Field Update — Applies a bulk field update across analyze product quality data records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-product-quality-data
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_product_quality_data_agent.py` and embedded as the fenced Python below (sha256 21310cd4b074b23c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_product_quality_data_agent.py` first:

```bash
python3 bulk_update_analyze_product_quality_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_product_quality_data_agent.py   # or on stdin
python3 bulk_update_analyze_product_quality_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze product quality data Bulk Field Update — Applies a bulk field update across analyze product quality data records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-product-quality-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_product_quality_data',
    "version": '2.0.1',
    "display_name": 'Analyze product quality data Bulk Field Update',
    "description": 'Applies a bulk field update across analyze product quality data records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-analyze-product-quality-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-product-quality-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fb160fdeca29c360',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/analyze-product-performance/analyze-product-quality-data'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/bulk-update-analyze-product-quality-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateAnalyzeProductQualityData(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeProductQualityData'
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
    print(BulkUpdateAnalyzeProductQualityData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
