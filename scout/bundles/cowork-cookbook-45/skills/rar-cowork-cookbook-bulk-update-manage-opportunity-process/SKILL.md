---
name: "rar-cowork-cookbook-bulk-update-manage-opportunity-process"
description: "Applies a bulk field update across manage opportunity process records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_opportunity_process", "rar_sha256": "11c530647d46e95ddce250ee2ad825c123af4e438f5809c087a3b0d0635c37f5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_manage_opportunity_process_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-manage-opportunity-process:741ea0c8ba29ef6218083476d43513819dd18cf2bfc626c78bb9c753ab998b8d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_manage_opportunity_process`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_manage_opportunity_process_agent.py` is
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

Manage opportunity process Bulk Field Update — Applies a bulk field update across manage opportunity process records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-opportunity-process
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_opportunity_process_agent.py` and embedded as the fenced Python below (sha256 11c530647d46e95d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_opportunity_process_agent.py` first:

```bash
python3 bulk_update_manage_opportunity_process_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_opportunity_process_agent.py   # or on stdin
python3 bulk_update_manage_opportunity_process_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage opportunity process Bulk Field Update — Applies a bulk field update across manage opportunity process records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-opportunity-process
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_opportunity_process',
    "version": '2.0.0',
    "display_name": 'Manage opportunity process Bulk Field Update',
    "description": 'Applies a bulk field update across manage opportunity process records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-manage-opportunity-process',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-opportunity-process',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '34c83edfbdd942b2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/manage-opportunity-process'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/bulk-update-manage-opportunity-process', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateManageOpportunityProcess(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageOpportunityProcess'
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
    print(BulkUpdateManageOpportunityProcess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
