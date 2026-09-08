---
name: "rar-cowork-cookbook-scheduled-brief-issue-customer-credits"
description: "Builds a morning brief on issue customer credits from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Te"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_issue_customer_credits", "rar_sha256": "e154f701417cf34157284c8cf0de46b5338b47b974a19685e4e2713b2195743b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

Issue customer credits Scheduled Email Brief — Builds a morning brief on issue customer credits from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Te

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to query; the recipe uses USMF.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "owner": {
      "description": "Responsible owner who receives the drafted brief email.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_issue_customer_credits_agent.py` and embedded as the fenced Python below (sha256 e154f701417cf341…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_issue_customer_credits_agent.py` first:

```bash
python3 scheduled_brief_issue_customer_credits_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_issue_customer_credits_agent.py   # or on stdin
python3 scheduled_brief_issue_customer_credits_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue customer credits Scheduled Email Brief — Builds a morning brief on issue customer credits from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Te

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

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
    "version": '3.0.3',
    "display_name": 'Issue customer credits Scheduled Email Brief',
    "description": 'Builds a morning brief on issue customer credits from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Te',
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
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b592514c8f58b334',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; the recipe uses USMF.', 'owner': 'Responsible owner who receives the drafted brief email.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where issue customer credits stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on issue customer credits for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads issue customer credits, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on issue customer credits from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Te', 'example_request': 'Send me the 7am weekday morning brief on issue customer credits in USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted brief email.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a recurring (daily or weekday-morning) brief on issue customer credits is needed for the responsible owner, with a drafted email and Teams post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefIssueCustomerCredits(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefIssueCustomerCredits'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted brief email.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
