---
name: "rar-cowork-cookbook-bulk-update-perform-a-skill-gap-analysis"
description: "Applies a bulk field update across perform a skill gap analysis records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_perform_a_skill_gap_analysis", "rar_sha256": "5fb0b0d09268b33ea228fac612d7b4cc24185eebe87e249f701ef90d38548984", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_perform_a_skill_gap_analysis_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-perform-a-skill-gap-analysis:1f698033442af243d75e318c6c339c69fafcd7bef822d2784743e3a0469494fd", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_perform_a_skill_gap_analysis`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_perform_a_skill_gap_analysis_agent.py` is
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

Perform a skill gap analysis Bulk Field Update — Applies a bulk field update across perform a skill gap analysis records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-perform-a-skill-gap-analysis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_perform_a_skill_gap_analysis_agent.py` and embedded as the fenced Python below (sha256 5fb0b0d09268b33e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_perform_a_skill_gap_analysis_agent.py` first:

```bash
python3 bulk_update_perform_a_skill_gap_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_perform_a_skill_gap_analysis_agent.py   # or on stdin
python3 bulk_update_perform_a_skill_gap_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform a skill gap analysis Bulk Field Update — Applies a bulk field update across perform a skill gap analysis records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-perform-a-skill-gap-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_perform_a_skill_gap_analysis',
    "version": '2.0.0',
    "display_name": 'Perform a skill gap analysis Bulk Field Update',
    "description": 'Applies a bulk field update across perform a skill gap analysis records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-perform-a-skill-gap-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-perform-a-skill-gap-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6fc4fa7a50ff0a4b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/perform-a-skill-gap-analysis'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-perform-a-skill-gap-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdatePerformASkillGapAnalysis(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePerformASkillGapAnalysis'
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
    print(BulkUpdatePerformASkillGapAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
