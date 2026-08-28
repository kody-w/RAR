---
name: "rar-cowork-cookbook-bulk-update-perform-a-skill-gap-analysis"
description: "Applies a bulk field update across perform a skill gap analysis records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_perform_a_skill_gap_analysis", "rar_sha256": "5fb0b0d09268b33ea228fac612d7b4cc24185eebe87e249f701ef90d38548984", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_perform_a_skill_gap_analysis`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_perform_a_skill_gap_analysis_agent.py` and in the RCI capsule.

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
