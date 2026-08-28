---
name: "rar-cowork-cookbook-teams-update-issue-customer-credits"
description: "Drafts a Teams channel post on issue customer credits status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_issue_customer_credits", "rar_sha256": "41d478196590f64a8e7c65350ad418191eeec4198cb09637f4c457634a6773e7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_issue_customer_credits`. The original RAPP
agent is preserved byte-for-byte in `teams_update_issue_customer_credits_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_issue_customer_credits_agent.py` and embedded as the fenced Python below (sha256 41d478196590f64a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_issue_customer_credits_agent.py` first:

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
    "version": '2.0.1',
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
