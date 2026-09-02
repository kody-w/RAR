---
name: "rar-cowork-cookbook-bulk-update-follow-up-on-a-case"
description: "Applies a bulk field update across follow up on a case records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_follow_up_on_a_case", "rar_sha256": "d1b1f4b9bd945a02bea0cd8111703fc908ebedf4929b6d05d7526d70b8904db6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_follow_up_on_a_case_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-follow-up-on-a-case:049f8d24855a4844f481820c40f1f3ba094c3363e0592b4fcccf9da2beb4381b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_follow_up_on_a_case`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_follow_up_on_a_case_agent.py` is
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
