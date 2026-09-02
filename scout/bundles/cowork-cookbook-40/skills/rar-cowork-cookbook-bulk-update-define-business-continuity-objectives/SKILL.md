---
name: "rar-cowork-cookbook-bulk-update-define-business-continuity-objectives"
description: "Applies a bulk field update across define business continuity objectives records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_business_continuity_objectives", "rar_sha256": "8a97b92ac8a83fddf2ad98a358bc11696decd7d5cf4636fa4defaecfd67bf23f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_define_business_continuity_objectives_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-define-business-continuity-objectives:343d45d5aff4f92c404fe879a2862bb60864fa8d6cead9d2960c5a93569c835c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_define_business_continuity_objectives`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_define_business_continuity_objectives_agent.py` is
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

Define business continuity objectives Bulk Field Update — Applies a bulk field update across define business continuity objectives records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-business-continuity-objectives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_business_continuity_objectives_agent.py` and embedded as the fenced Python below (sha256 8a97b92ac8a83fdd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_business_continuity_objectives_agent.py` first:

```bash
python3 bulk_update_define_business_continuity_objectives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_business_continuity_objectives_agent.py   # or on stdin
python3 bulk_update_define_business_continuity_objectives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define business continuity objectives Bulk Field Update — Applies a bulk field update across define business continuity objectives records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-business-continuity-objectives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_business_continuity_objectives',
    "version": '2.0.0',
    "display_name": 'Define business continuity objectives Bulk Field Update',
    "description": 'Applies a bulk field update across define business continuity objectives records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-define-business-continuity-objectives',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-business-continuity-objectives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8c3aa56f9b3e5c04',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/define-business-continuity-objectives'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-define-business-continuity-objectives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateDefineBusinessContinuityObjectives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineBusinessContinuityObjectives'
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
    print(BulkUpdateDefineBusinessContinuityObjectives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
