---
name: "rar-cowork-cookbook-weekly-external-customer-email-review"
description: "Reviews the past week's unread external customer emails for action items, creates in-thread draft replies in your Outlook Drafts for review, then sends you an email summary and a Teams self-message reminder."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/weekly_external_customer_email_review", "rar_sha256": "76a71569a4638c5e6ca08ececbaa8598c1fbd23d7613f797c7ae1de2fb50ce83", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "read_only", "analysis"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/weekly_external_customer_email_review`. The original RAPP
agent is preserved byte-for-byte in `weekly_external_customer_email_review_agent.py` and in the RCI capsule.

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

Weekly external customer email review — Reviews the past week's unread external customer emails for action items, creates in-thread draft replies in your Outlook Drafts for review, then sends you an email summary and a Teams self-message reminder.

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
  Upstream entry : https://coworkcookbook.com/recipes/weekly-external-customer-email-review
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
    "account_team_members": {
      "description": "Names or addresses of account team members whose action items should also be captured.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `weekly_external_customer_email_review_agent.py` and embedded as the fenced Python below (sha256 76a71569a4638c5e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `weekly_external_customer_email_review_agent.py` first:

```bash
python3 weekly_external_customer_email_review_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 weekly_external_customer_email_review_agent.py   # or on stdin
python3 weekly_external_customer_email_review_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Weekly external customer email review — Reviews the past week's unread external customer emails for action items, creates in-thread draft replies in your Outlook Drafts for review, then sends you an email summary and a Teams self-message reminder.

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
  Upstream entry : https://coworkcookbook.com/recipes/weekly-external-customer-email-review
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/weekly_external_customer_email_review',
    "version": '3.0.3',
    "display_name": 'Weekly external customer email review',
    "description": "Reviews the past week's unread external customer emails for action items, creates in-thread draft replies in your Outlook Drafts for review, then sends you an email summary and a Teams self-message reminder.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'prospect_to_quote', 'intermediate', 'read_only', 'analysis'],
    "category": 'analysis',
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
        "upstream_slug": 'weekly-external-customer-email-review',
        "upstream_url": 'https://coworkcookbook.com/recipes/weekly-external-customer-email-review',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '12c3a53ef66cfc91',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/nurture-trust-relationship-regularly-with-customer'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/weekly-external-customer-email-review', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Scheduling', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Output matches: Outlook draft replies waiting in your Drafts folder, an email summary reminder, and a Teams self-message - queued every Monday morning so the inbox is already moving when you sit down.'], 'confidence': 1.0, 'deliverable': 'Outlook draft replies waiting in your Drafts folder, an email summary reminder, and a Teams self-message - queued every Monday morning so the inbox is already moving when you sit down.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'account_team_members': 'Names or addresses of account team members whose action items should also be captured.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Every Monday, surface action items from external customer emails, draft replies in thread, and remind yourself to review before anything goes out. Outlook draft replies waiting in your Drafts folder, an email summary reminder, and a Teams self-message - queued every Monday morning so the inbox is already moving when you sit down.', 'expected_output': 'Outlook draft replies waiting in your Drafts folder, an email summary reminder, and a Teams self-message - queued every Monday morning so the inbox is already moving when you sit down.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': 'Every Monday morning, I want this to run automatically: review all unread emails from the previous week from external customers only - specifically those with action items for me or [Account Team Members]. For each one, create a draft reply directly in that email thread (not a new email) and store it in my Outlook Drafts folder for my review before anything goes out.\n\nOnce the drafts are ready, send me an email summary reminding me to review them, and send a Teams message to myself with the same reminder.', 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Outlook draft replies waiting in your Drafts folder, an email summary reminder, and a Teams self-message - queued every Monday morning so the inbox is already moving when you sit down.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Reviews the past week's unread external customer emails for action items, creates in-thread draft replies in your Outlook Drafts for review, then sends you an email summary and a Teams self-message reminder.", 'example_request': "Every Monday, review last week's unread external customer emails, draft in-thread replies, and remind me to review them.", 'inputs': [{'description': 'Names or addresses of account team members whose action items should also be captured.', 'name': 'account_team_members'}], 'model': 'claude-opus-5', 'when_to_use': 'Call on Monday mornings (or on demand) to triage unread external customer email from the prior week and queue draft replies for review before sending.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class WeeklyExternalCustomerEmailReview(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WeeklyExternalCustomerEmailReview'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'account_team_members': {'description': 'Names or addresses of account team members whose action items should also be captured.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(WeeklyExternalCustomerEmailReview().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
