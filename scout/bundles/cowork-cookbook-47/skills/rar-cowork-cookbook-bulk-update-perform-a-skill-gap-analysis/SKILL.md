---
name: "rar-cowork-cookbook-bulk-update-perform-a-skill-gap-analysis"
description: "Applies a bulk field update across perform a skill gap analysis records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_perform_a_skill_gap_analysis", "rar_sha256": "a4c57ac0b98a9841bcacefc42362d4e2094c88f950f51785d9d14d5d61d4fdf5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_perform_a_skill_gap_analysis_agent.py` and embedded as the fenced Python below (sha256 a4c57ac0b98a9841…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_perform_a_skill_gap_analysis_agent.py` first:

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
    "version": '2.0.1',
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
