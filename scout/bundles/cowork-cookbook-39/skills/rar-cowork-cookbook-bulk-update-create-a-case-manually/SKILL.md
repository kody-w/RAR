---
name: "rar-cowork-cookbook-bulk-update-create-a-case-manually"
description: "Applies a bulk field update across create a case manually records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_create_a_case_manually", "rar_sha256": "a72d5272bc09f946bc98de85802237b0101c1afb53883ccc175b2d407d649982", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_create_a_case_manually`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_create_a_case_manually_agent.py` and in the RCI capsule.

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

Create a case manually Bulk Field Update — Applies a bulk field update across create a case manually records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-create-a-case-manually
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_create_a_case_manually_agent.py` and embedded as the fenced Python below (sha256 a72d5272bc09f946…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_create_a_case_manually_agent.py` first:

```bash
python3 bulk_update_create_a_case_manually_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_create_a_case_manually_agent.py   # or on stdin
python3 bulk_update_create_a_case_manually_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create a case manually Bulk Field Update — Applies a bulk field update across create a case manually records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-create-a-case-manually
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_create_a_case_manually',
    "version": '2.0.1',
    "display_name": 'Create a case manually Bulk Field Update',
    "description": 'Applies a bulk field update across create a case manually records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-create-a-case-manually',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-create-a-case-manually',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a54d9cf903bdc2b8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/create-a-case-manually'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/bulk-update-create-a-case-manually', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateCreateACaseManually(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateCreateACaseManually'
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
    print(BulkUpdateCreateACaseManually().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
