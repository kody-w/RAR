---
name: "rar-cowork-cookbook-scheduled-brief-issue-requests-for-proposals"
description: "Schedulable morning-brief email summarizing issue requests for proposals for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_issue_requests_for_proposals", "rar_sha256": "8d644ff18bbe71d00fda3123ed21306c632ba2a13ec1e60ff0918637ac09e78e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
