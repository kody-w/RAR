---
name: "rar-cowork-cookbook-teams-update-issue-customer-credits"
description: "Drafts a Teams channel post on issue customer credits status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_issue_customer_credits", "rar_sha256": "e2d2fa90623c3dbeb1b64b3028755df59ae079ee2924339841c99ab8438b871e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
