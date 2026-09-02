---
name: "rar-cowork-cookbook-bulk-update-use-similar-cases-to-find-a-solution"
description: "Applies a bulk field update across use similar cases to find a solution records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_use_similar_cases_to_find_a_solution", "rar_sha256": "713c5500c6596fa07e1792f4899387f99eb14bf74a152e5794d9219a6c91c640", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_use_similar_cases_to_find_a_solution_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-use-similar-cases-to-find-a-solution:726dbfc4c2200d6502ac894e3330552a5ec0b2f59617e1482086369f75a3bb8d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_use_similar_cases_to_find_a_solution`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_use_similar_cases_to_find_a_solution_agent.py` is
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

Use similar cases to find a solution Bulk Field Update — Applies a bulk field update across use similar cases to find a solution records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-use-similar-cases-to-find-a-solution
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_use_similar_cases_to_find_a_solution_agent.py` and embedded as the fenced Python below (sha256 713c5500c6596fa0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_use_similar_cases_to_find_a_solution_agent.py` first:

```bash
python3 bulk_update_use_similar_cases_to_find_a_solution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_use_similar_cases_to_find_a_solution_agent.py   # or on stdin
python3 bulk_update_use_similar_cases_to_find_a_solution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Use similar cases to find a solution Bulk Field Update — Applies a bulk field update across use similar cases to find a solution records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-use-similar-cases-to-find-a-solution
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_use_similar_cases_to_find_a_solution',
    "version": '2.0.0',
    "display_name": 'Use similar cases to find a solution Bulk Field Update',
    "description": 'Applies a bulk field update across use similar cases to find a solution records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-use-similar-cases-to-find-a-solution',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-use-similar-cases-to-find-a-solution',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c51801f48f829295',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/use-similar-cases-to-find-a-solution'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/bulk-update-use-similar-cases-to-find-a-solution', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateUseSimilarCasesToFindASolution(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateUseSimilarCasesToFindASolution'
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
    print(BulkUpdateUseSimilarCasesToFindASolution().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
