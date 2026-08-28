---
name: "rar-cowork-cookbook-teams-update-issue-requests-for-information"
description: "Drafts a Teams channel post on issue requests for information status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_issue_requests_for_information", "rar_sha256": "d84e13c79df51ddf2dbc93f4ea10717b28d23582451067319f31c9a12c3c5e60", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_issue_requests_for_information`. The original RAPP
agent is preserved byte-for-byte in `teams_update_issue_requests_for_information_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_issue_requests_for_information_agent.py` and embedded as the fenced Python below (sha256 d84e13c79df51ddf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_issue_requests_for_information_agent.py` first:

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
    "version": '2.0.1',
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
