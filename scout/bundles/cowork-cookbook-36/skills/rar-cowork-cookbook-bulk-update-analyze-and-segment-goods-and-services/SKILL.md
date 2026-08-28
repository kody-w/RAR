---
name: "rar-cowork-cookbook-bulk-update-analyze-and-segment-goods-and-services"
description: "Applies a bulk field update across analyze and segment goods and services records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_and_segment_goods_and_services", "rar_sha256": "e51c2dc320ca6713291445f61939927d97984eb587c5c0237d017e62312ff7a7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_and_segment_goods_and_services_agent.py` and embedded as the fenced Python below (sha256 e51c2dc320ca6713…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_and_segment_goods_and_services_agent.py` first:

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
    "version": '2.0.0',
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
