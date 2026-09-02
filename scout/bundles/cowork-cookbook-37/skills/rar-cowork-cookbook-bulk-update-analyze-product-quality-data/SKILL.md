---
name: "rar-cowork-cookbook-bulk-update-analyze-product-quality-data"
description: "Applies a bulk field update across analyze product quality data records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_product_quality_data", "rar_sha256": "90d693ba118ce65a08d31346a02f43fd5f82db0292cb3622893ed71dad95f755", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_analyze_product_quality_data_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-analyze-product-quality-data:be83f17f9e15e164556ff771a7d25ee8909f0279a0cef1797c69e5798a817b3c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_analyze_product_quality_data`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_analyze_product_quality_data_agent.py` is
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
