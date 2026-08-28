---
name: "rar-cowork-cookbook-bulk-update-create-a-case-manually"
description: "Applies a bulk field update across create a case manually records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_create_a_case_manually", "rar_sha256": "f6bd9640d0290ec2267136492b113c55c7621273149cb7aa218730f8a5e9e1ca", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_create_a_case_manually_agent.py` and embedded as the fenced Python below (sha256 f6bd9640d0290ec2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_create_a_case_manually_agent.py` first:

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
    "version": '2.0.0',
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
