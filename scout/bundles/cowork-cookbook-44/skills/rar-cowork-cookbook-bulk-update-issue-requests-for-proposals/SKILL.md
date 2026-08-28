---
name: "rar-cowork-cookbook-bulk-update-issue-requests-for-proposals"
description: "Applies a bulk field update across issue requests for proposals records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_issue_requests_for_proposals", "rar_sha256": "d4f53cf6f0d301c56d70f76ee5d86df5dde65b797a8cbf99f8a9715c62dc3521", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_issue_requests_for_proposals`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_issue_requests_for_proposals_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_issue_requests_for_proposals_agent.py` and embedded as the fenced Python below (sha256 d4f53cf6f0d301c5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_issue_requests_for_proposals_agent.py` first:

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
    "version": '2.0.1',
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
