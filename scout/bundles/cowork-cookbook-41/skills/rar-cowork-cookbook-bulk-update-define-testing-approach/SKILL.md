---
name: "rar-cowork-cookbook-bulk-update-define-testing-approach"
description: "Applies a bulk field update across define testing approach records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_testing_approach", "rar_sha256": "64e351eaf58f88a44dbe451f4a62677216b4d430bd5defc3179bf68fde9d491c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_define_testing_approach_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-define-testing-approach:f6daf7a9ccab8c1235960f35bf019fb54f7e8c4f1580cee43932a3d11d25e1d5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_define_testing_approach`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_define_testing_approach_agent.py` is
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

Define testing approach Bulk Field Update — Applies a bulk field update across define testing approach records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-testing-approach
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_testing_approach_agent.py` and embedded as the fenced Python below (sha256 64e351eaf58f88a4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_testing_approach_agent.py` first:

```bash
python3 bulk_update_define_testing_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_testing_approach_agent.py   # or on stdin
python3 bulk_update_define_testing_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define testing approach Bulk Field Update — Applies a bulk field update across define testing approach records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-testing-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_testing_approach',
    "version": '2.0.0',
    "display_name": 'Define testing approach Bulk Field Update',
    "description": 'Applies a bulk field update across define testing approach records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-testing-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-testing-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6ef18c3412cdef16',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-testing-approach'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-define-testing-approach', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDefineTestingApproach(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineTestingApproach'
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
    print(BulkUpdateDefineTestingApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
