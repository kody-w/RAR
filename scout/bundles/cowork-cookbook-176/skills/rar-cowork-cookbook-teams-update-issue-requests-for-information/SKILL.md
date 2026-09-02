---
name: "rar-cowork-cookbook-teams-update-issue-requests-for-information"
description: "Drafts a Teams channel post on issue requests for information status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_issue_requests_for_information", "rar_sha256": "4013420969b4b11c2fef9177e66263d1ee9ca415df53794e4c29e18edcf7af11", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_issue_requests_for_information_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-issue-requests-for-information:1bc8041ace443d8e0b8624b113dbbb818cffa7e430e3a6e7f56dc55a0032a677", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_issue_requests_for_information`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_issue_requests_for_information_agent.py` is
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

Issue requests for information Teams Channel Update — Drafts a Teams channel post on issue requests for information status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-issue-requests-for-information
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_issue_requests_for_information_agent.py` and embedded as the fenced Python below (sha256 4013420969b4b11c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_issue_requests_for_information_agent.py` first:

```bash
python3 teams_update_issue_requests_for_information_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_issue_requests_for_information_agent.py   # or on stdin
python3 teams_update_issue_requests_for_information_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue requests for information Teams Channel Update — Drafts a Teams channel post on issue requests for information status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-issue-requests-for-information
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_issue_requests_for_information',
    "version": '2.0.0',
    "display_name": 'Issue requests for information Teams Channel Update',
    "description": 'Drafts a Teams channel post on issue requests for information status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-issue-requests-for-information',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-issue-requests-for-information',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ba529d59cde5bc78',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/issue-requests-for-information'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-issue-requests-for-information', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateIssueRequestsForInformation(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateIssueRequestsForInformation'
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
    print(TeamsUpdateIssueRequestsForInformation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
