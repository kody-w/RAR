---
name: "rar-cowork-cookbook-bulk-update-follow-up-on-a-case"
description: "Applies a bulk field update across follow up on a case records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_follow_up_on_a_case", "rar_sha256": "a793ee05bf8215ed22daf0458fc48685a1155e85d3442a7670d2bd8a8116aee7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_follow_up_on_a_case`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_follow_up_on_a_case_agent.py` and in the RCI capsule.

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

Follow up on a case Bulk Field Update — Applies a bulk field update across follow up on a case records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-follow-up-on-a-case
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_follow_up_on_a_case_agent.py` and embedded as the fenced Python below (sha256 a793ee05bf8215ed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_follow_up_on_a_case_agent.py` first:

```bash
python3 bulk_update_follow_up_on_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_follow_up_on_a_case_agent.py   # or on stdin
python3 bulk_update_follow_up_on_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Follow up on a case Bulk Field Update — Applies a bulk field update across follow up on a case records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-follow-up-on-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_follow_up_on_a_case',
    "version": '2.0.1',
    "display_name": 'Follow up on a case Bulk Field Update',
    "description": 'Applies a bulk field update across follow up on a case records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-follow-up-on-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-follow-up-on-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3f45a246bc5bfa88',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/follow-up-on-a-case'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/bulk-update-follow-up-on-a-case', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateFollowUpOnACase(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateFollowUpOnACase'
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
    print(BulkUpdateFollowUpOnACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
