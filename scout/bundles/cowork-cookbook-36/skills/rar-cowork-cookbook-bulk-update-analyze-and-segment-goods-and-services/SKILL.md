---
name: "rar-cowork-cookbook-bulk-update-analyze-and-segment-goods-and-services"
description: "Applies a bulk field update across analyze and segment goods and services records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_and_segment_goods_and_services", "rar_sha256": "33c6450f0212110b86dc2d64194689d03b486c5fbf9ecf037cc8531fbbf87b20", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_analyze_and_segment_goods_and_services`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_analyze_and_segment_goods_and_services_agent.py` and in the RCI capsule.

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

Analyze and segment goods and services Bulk Field Update — Applies a bulk field update across analyze and segment goods and services records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-and-segment-goods-and-services
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_and_segment_goods_and_services_agent.py` and embedded as the fenced Python below (sha256 33c6450f0212110b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_and_segment_goods_and_services_agent.py` first:

```bash
python3 bulk_update_analyze_and_segment_goods_and_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_and_segment_goods_and_services_agent.py   # or on stdin
python3 bulk_update_analyze_and_segment_goods_and_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and segment goods and services Bulk Field Update — Applies a bulk field update across analyze and segment goods and services records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-and-segment-goods-and-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_and_segment_goods_and_services',
    "version": '2.0.1',
    "display_name": 'Analyze and segment goods and services Bulk Field Update',
    "description": 'Applies a bulk field update across analyze and segment goods and services records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-analyze-and-segment-goods-and-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-and-segment-goods-and-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7d514fea47121dc5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/analyze-and-segment-goods-and-services'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/bulk-update-analyze-and-segment-goods-and-services', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateAnalyzeAndSegmentGoodsAndServices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeAndSegmentGoodsAndServices'
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
    print(BulkUpdateAnalyzeAndSegmentGoodsAndServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
