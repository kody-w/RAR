---
name: "rar-cowork-cookbook-bulk-update-use-similar-cases-to-find-a-solution"
description: "Applies a bulk field update across use similar cases to find a solution records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_use_similar_cases_to_find_a_solution", "rar_sha256": "713c5500c6596fa07e1792f4899387f99eb14bf74a152e5794d9219a6c91c640", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
