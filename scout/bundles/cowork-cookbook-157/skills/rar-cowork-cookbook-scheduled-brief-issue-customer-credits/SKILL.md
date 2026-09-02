---
name: "rar-cowork-cookbook-scheduled-brief-issue-customer-credits"
description: "Schedulable morning-brief email summarizing issue customer credits for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_issue_customer_credits", "rar_sha256": "2ef99e9cdc5b4cd71b77d4b6125f6aa0ff037918f9860b03db8a868b97a2840b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_issue_customer_credits_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-issue-customer-credits:6ea04eb6af08b851cd2b0ebf639ecf66e0b05f2c4c6beb96b198d2c5ada42474", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_issue_customer_credits`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_issue_customer_credits_agent.py` is
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

Issue customer credits Scheduled Email Brief — Schedulable morning-brief email summarizing issue customer credits for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-issue-customer-credits
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_issue_customer_credits_agent.py` and embedded as the fenced Python below (sha256 2ef99e9cdc5b4cd7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_issue_customer_credits_agent.py` first:

```bash
python3 scheduled_brief_issue_customer_credits_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_issue_customer_credits_agent.py   # or on stdin
python3 scheduled_brief_issue_customer_credits_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue customer credits Scheduled Email Brief — Schedulable morning-brief email summarizing issue customer credits for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-issue-customer-credits
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_issue_customer_credits',
    "version": '2.0.0',
    "display_name": 'Issue customer credits Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing issue customer credits for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-issue-customer-credits',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-issue-customer-credits',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '07052f42776df812',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/issue-customer-credits'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/scheduled-brief-issue-customer-credits', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefIssueCustomerCredits(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefIssueCustomerCredits'
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
    print(ScheduledBriefIssueCustomerCredits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
