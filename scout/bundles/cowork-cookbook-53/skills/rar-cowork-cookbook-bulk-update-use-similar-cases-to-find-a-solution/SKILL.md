---
name: "rar-cowork-cookbook-bulk-update-use-similar-cases-to-find-a-solution"
description: "Applies a bulk field update across use similar cases to find a solution records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_use_similar_cases_to_find_a_solution", "rar_sha256": "8c4654eaded25674ddffac05bc81ad0a85d37e7abeb948eb8c56f7cab8091f7f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_use_similar_cases_to_find_a_solution`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_use_similar_cases_to_find_a_solution_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_use_similar_cases_to_find_a_solution_agent.py` and embedded as the fenced Python below (sha256 8c4654eaded25674…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_use_similar_cases_to_find_a_solution_agent.py` first:

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
    "version": '2.0.1',
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
