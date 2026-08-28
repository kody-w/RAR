---
name: "rar-cowork-cookbook-bulk-update-analyze-product-quality-data"
description: "Applies a bulk field update across analyze product quality data records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_product_quality_data", "rar_sha256": "90d693ba118ce65a08d31346a02f43fd5f82db0292cb3622893ed71dad95f755", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_product_quality_data_agent.py` and embedded as the fenced Python below (sha256 90d693ba118ce65a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_product_quality_data_agent.py` first:

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
    "version": '2.0.0',
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
