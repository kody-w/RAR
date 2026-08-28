---
name: "rar-cowork-cookbook-bulk-update-review-case-loads-and-rebalance-case-loads"
description: "Applies a bulk field update across review case loads and rebalance case loads records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_review_case_loads_and_rebalance_case_loads", "rar_sha256": "0476f5d5a97346829061f0a2756b924b6b1585c81823e47fa7924c166186a47d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_review_case_loads_and_rebalance_case_loads_agent.py` and embedded as the fenced Python below (sha256 0476f5d5a9734682…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_review_case_loads_and_rebalance_case_loads_agent.py` first:

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
    "version": '2.0.1',
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
