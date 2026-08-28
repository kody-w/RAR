---
name: "rar-cowork-cookbook-bulk-update-issue-requests-for-proposals"
description: "Applies a bulk field update across issue requests for proposals records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_issue_requests_for_proposals", "rar_sha256": "3aaf5e19007e42bcf2c8f36d7d32a51590bec80831e57de756ed95608ec3d0cb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
