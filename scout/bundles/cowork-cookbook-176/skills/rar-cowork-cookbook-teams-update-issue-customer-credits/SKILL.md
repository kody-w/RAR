---
name: "rar-cowork-cookbook-teams-update-issue-customer-credits"
description: "Drafts a Teams channel post on issue customer credits status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_issue_customer_credits", "rar_sha256": "e2d2fa90623c3dbeb1b64b3028755df59ae079ee2924339841c99ab8438b871e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_issue_customer_credits_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-issue-customer-credits:11dc5f790fa22a33ec0cdd230328ace28f2c4f3b9d722411624cd4bdf7e3bffa", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_issue_customer_credits`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_issue_customer_credits_agent.py` is
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

Issue customer credits Teams Channel Update — Drafts a Teams channel post on issue customer credits status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-issue-customer-credits
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_issue_customer_credits_agent.py` and embedded as the fenced Python below (sha256 e2d2fa90623c3dbe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_issue_customer_credits_agent.py` first:

```bash
python3 teams_update_issue_customer_credits_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_issue_customer_credits_agent.py   # or on stdin
python3 teams_update_issue_customer_credits_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue customer credits Teams Channel Update — Drafts a Teams channel post on issue customer credits status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-issue-customer-credits
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_issue_customer_credits',
    "version": '2.0.0',
    "display_name": 'Issue customer credits Teams Channel Update',
    "description": 'Drafts a Teams channel post on issue customer credits status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-issue-customer-credits',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-issue-customer-credits',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aa149a3b2dd79ae7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/issue-customer-credits'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-issue-customer-credits', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateIssueCustomerCredits(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateIssueCustomerCredits'
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
    print(TeamsUpdateIssueCustomerCredits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
