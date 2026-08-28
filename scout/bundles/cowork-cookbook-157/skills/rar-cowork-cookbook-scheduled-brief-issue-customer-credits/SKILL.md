---
name: "rar-cowork-cookbook-scheduled-brief-issue-customer-credits"
description: "Schedulable morning-brief email summarizing issue customer credits for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_issue_customer_credits", "rar_sha256": "31421a8a3f3850e972c2d040ea1d6b3509b9352bb709935eed8f84efcdb73b26", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_issue_customer_credits_agent.py` and embedded as the fenced Python below (sha256 31421a8a3f3850e9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_issue_customer_credits_agent.py` first:

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
    "version": '2.0.1',
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
