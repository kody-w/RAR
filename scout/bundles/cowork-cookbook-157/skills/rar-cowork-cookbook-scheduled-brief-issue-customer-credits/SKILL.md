---
name: "rar-cowork-cookbook-scheduled-brief-issue-customer-credits"
description: "Builds a morning brief on issue customer credits from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Te"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_issue_customer_credits", "rar_sha256": "e154f701417cf34157284c8cf0de46b5338b47b974a19685e4e2713b2195743b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
