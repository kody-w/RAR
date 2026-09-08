---
name: "rar-cowork-cookbook-weekly-external-customer-email-review"
description: "Reviews the past week's unread external customer emails for action items, creates in-thread draft replies in your Outlook Drafts for review, then sends you an email summary and a Teams self-message reminder."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/weekly_external_customer_email_review", "rar_sha256": "76a71569a4638c5e6ca08ececbaa8598c1fbd23d7613f797c7ae1de2fb50ce83", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "prospect_to_quote", "intermediate", "read_only", "analysis"]}
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
