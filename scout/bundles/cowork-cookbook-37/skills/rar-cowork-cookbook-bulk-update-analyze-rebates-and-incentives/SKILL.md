---
name: "rar-cowork-cookbook-bulk-update-analyze-rebates-and-incentives"
description: "Applies a bulk field update across analyze rebates and incentives records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_rebates_and_incentives", "rar_sha256": "e86090b3d7a95d535bee06304055d4420ecd7b8b0a3d89686d79f81032d1f5d5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_analyze_rebates_and_incentives_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-analyze-rebates-and-incentives:b4e25cb66386c402b7fd4696b9b00b22bf3ce2c9c0c091c63aa27a4cb5235e27", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_analyze_rebates_and_incentives`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_analyze_rebates_and_incentives_agent.py` is
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

Analyze rebates and incentives Bulk Field Update — Applies a bulk field update across analyze rebates and incentives records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-rebates-and-incentives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_rebates_and_incentives_agent.py` and embedded as the fenced Python below (sha256 e86090b3d7a95d53…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_rebates_and_incentives_agent.py` first:

```bash
python3 bulk_update_analyze_rebates_and_incentives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_rebates_and_incentives_agent.py   # or on stdin
python3 bulk_update_analyze_rebates_and_incentives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze rebates and incentives Bulk Field Update — Applies a bulk field update across analyze rebates and incentives records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-rebates-and-incentives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_rebates_and_incentives',
    "version": '2.0.0',
    "display_name": 'Analyze rebates and incentives Bulk Field Update',
    "description": 'Applies a bulk field update across analyze rebates and incentives records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-analyze-rebates-and-incentives',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-rebates-and-incentives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3567aeccdf74d2eb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/analyze-rebates-and-incentives'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/bulk-update-analyze-rebates-and-incentives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateAnalyzeRebatesAndIncentives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeRebatesAndIncentives'
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
    print(BulkUpdateAnalyzeRebatesAndIncentives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
