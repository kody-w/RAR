---
name: "rar-cowork-cookbook-scheduled-brief-issue-requests-for-proposals"
description: "Schedulable morning-brief email summarizing issue requests for proposals for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_issue_requests_for_proposals", "rar_sha256": "8d644ff18bbe71d00fda3123ed21306c632ba2a13ec1e60ff0918637ac09e78e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_issue_requests_for_proposals_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-issue-requests-for-proposals:bd22cf6354677696251210a90417f1c589202e2ff09271fa538055114a0b0cfb", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_issue_requests_for_proposals`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_issue_requests_for_proposals_agent.py` is
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

Issue requests for proposals Scheduled Email Brief — Schedulable morning-brief email summarizing issue requests for proposals for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-issue-requests-for-proposals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_issue_requests_for_proposals_agent.py` and embedded as the fenced Python below (sha256 8d644ff18bbe71d0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_issue_requests_for_proposals_agent.py` first:

```bash
python3 scheduled_brief_issue_requests_for_proposals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_issue_requests_for_proposals_agent.py   # or on stdin
python3 scheduled_brief_issue_requests_for_proposals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue requests for proposals Scheduled Email Brief — Schedulable morning-brief email summarizing issue requests for proposals for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-issue-requests-for-proposals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_issue_requests_for_proposals',
    "version": '2.0.0',
    "display_name": 'Issue requests for proposals Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing issue requests for proposals for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-issue-requests-for-proposals',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-issue-requests-for-proposals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a377a2a5e17d31f0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/issue-requests-for-proposals'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-issue-requests-for-proposals', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefIssueRequestsForProposals(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefIssueRequestsForProposals'
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
    print(ScheduledBriefIssueRequestsForProposals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
