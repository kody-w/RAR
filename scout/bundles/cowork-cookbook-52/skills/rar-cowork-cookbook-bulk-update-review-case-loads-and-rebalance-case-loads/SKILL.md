---
name: "rar-cowork-cookbook-bulk-update-review-case-loads-and-rebalance-case-loads"
description: "Applies a bulk field update across review case loads and rebalance case loads records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_review_case_loads_and_rebalance_case_loads", "rar_sha256": "6662cbcb751534dd7b60f22e166cf12ba697209d5cb431e05f99f510e493d640", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_review_case_loads_and_rebalance_case_loads`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_review_case_loads_and_rebalance_case_loads_agent.py` and in the RCI capsule.

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

Review case loads and rebalance case loads Bulk Field Update — Applies a bulk field update across review case loads and rebalance case loads records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-review-case-loads-and-rebalance-case-loads
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_review_case_loads_and_rebalance_case_loads_agent.py` and embedded as the fenced Python below (sha256 6662cbcb751534dd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_review_case_loads_and_rebalance_case_loads_agent.py` first:

```bash
python3 bulk_update_review_case_loads_and_rebalance_case_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_review_case_loads_and_rebalance_case_loads_agent.py   # or on stdin
python3 bulk_update_review_case_loads_and_rebalance_case_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Review case loads and rebalance case loads Bulk Field Update — Applies a bulk field update across review case loads and rebalance case loads records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-review-case-loads-and-rebalance-case-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_review_case_loads_and_rebalance_case_loads',
    "version": '2.0.0',
    "display_name": 'Review case loads and rebalance case loads Bulk Field Update',
    "description": 'Applies a bulk field update across review case loads and rebalance case loads records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-review-case-loads-and-rebalance-case-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-review-case-loads-and-rebalance-case-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9d1f62145e2e3e9e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/analyze-case-performance/review-case-loads-and-rebalance-case-loads'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/bulk-update-review-case-loads-and-rebalance-case-loads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateReviewCaseLoadsAndRebalanceCaseLoads(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReviewCaseLoadsAndRebalanceCaseLoads'
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
    print(BulkUpdateReviewCaseLoadsAndRebalanceCaseLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
