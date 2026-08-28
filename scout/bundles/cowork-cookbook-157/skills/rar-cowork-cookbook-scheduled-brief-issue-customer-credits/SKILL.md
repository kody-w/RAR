---
name: "rar-cowork-cookbook-scheduled-brief-issue-customer-credits"
description: "Schedulable morning-brief email summarizing issue customer credits for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_issue_customer_credits", "rar_sha256": "2ef99e9cdc5b4cd71b77d4b6125f6aa0ff037918f9860b03db8a868b97a2840b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_issue_customer_credits`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_issue_customer_credits_agent.py` and in the RCI capsule.

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
