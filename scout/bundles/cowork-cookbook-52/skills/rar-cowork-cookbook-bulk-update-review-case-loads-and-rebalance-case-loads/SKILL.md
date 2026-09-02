---
name: "rar-cowork-cookbook-bulk-update-review-case-loads-and-rebalance-case-loads"
description: "Applies a bulk field update across review case loads and rebalance case loads records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_review_case_loads_and_rebalance_case_loads", "rar_sha256": "6662cbcb751534dd7b60f22e166cf12ba697209d5cb431e05f99f510e493d640", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_review_case_loads_and_rebalance_case_loads_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-review-case-loads-and-rebalance-case-loads:24c7ad7adf1bd21a880eda4d9e9687a868f31b6fdf82a152d85102324c73e7f0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_review_case_loads_and_rebalance_case_loads`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_review_case_loads_and_rebalance_case_loads_agent.py` is
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
