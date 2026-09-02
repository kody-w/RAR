---
name: "rar-cowork-cookbook-bulk-update-issue-requests-for-proposals"
description: "Applies a bulk field update across issue requests for proposals records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_issue_requests_for_proposals", "rar_sha256": "3aaf5e19007e42bcf2c8f36d7d32a51590bec80831e57de756ed95608ec3d0cb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_issue_requests_for_proposals_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-issue-requests-for-proposals:00a7cf202681c4b335a66ec29601895415c5c38e7cd5d9dd7d15efbc58d2f9d3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_issue_requests_for_proposals`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_issue_requests_for_proposals_agent.py` is
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

Issue requests for proposals Bulk Field Update — Applies a bulk field update across issue requests for proposals records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-issue-requests-for-proposals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_issue_requests_for_proposals_agent.py` and embedded as the fenced Python below (sha256 3aaf5e19007e42bc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_issue_requests_for_proposals_agent.py` first:

```bash
python3 bulk_update_issue_requests_for_proposals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_issue_requests_for_proposals_agent.py   # or on stdin
python3 bulk_update_issue_requests_for_proposals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue requests for proposals Bulk Field Update — Applies a bulk field update across issue requests for proposals records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-issue-requests-for-proposals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_issue_requests_for_proposals',
    "version": '2.0.0',
    "display_name": 'Issue requests for proposals Bulk Field Update',
    "description": 'Applies a bulk field update across issue requests for proposals records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-issue-requests-for-proposals',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-issue-requests-for-proposals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '143ba44c25ccabf6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/issue-requests-for-proposals'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/bulk-update-issue-requests-for-proposals', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateIssueRequestsForProposals(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateIssueRequestsForProposals'
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
    print(BulkUpdateIssueRequestsForProposals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
