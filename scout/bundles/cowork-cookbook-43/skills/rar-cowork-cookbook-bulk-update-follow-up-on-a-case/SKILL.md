---
name: "rar-cowork-cookbook-bulk-update-follow-up-on-a-case"
description: "Applies a bulk field update across follow up on a case records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_follow_up_on_a_case", "rar_sha256": "d1b1f4b9bd945a02bea0cd8111703fc908ebedf4929b6d05d7526d70b8904db6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_follow_up_on_a_case_agent.py` and embedded as the fenced Python below (sha256 d1b1f4b9bd945a02…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_follow_up_on_a_case_agent.py` first:

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
    "version": '2.0.0',
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
