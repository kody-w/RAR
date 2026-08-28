---
name: "rar-cowork-cookbook-scheduled-brief-issue-requests-for-proposals"
description: "Schedulable morning-brief email summarizing issue requests for proposals for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_issue_requests_for_proposals", "rar_sha256": "5d89889c47e4eb4fb2f6b8fe0e5efda95217134c0a34287cb4a5a6ec0d658ca4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_issue_requests_for_proposals`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_issue_requests_for_proposals_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_issue_requests_for_proposals_agent.py` and embedded as the fenced Python below (sha256 5d89889c47e4eb4f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_issue_requests_for_proposals_agent.py` first:

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
    "version": '2.0.1',
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
