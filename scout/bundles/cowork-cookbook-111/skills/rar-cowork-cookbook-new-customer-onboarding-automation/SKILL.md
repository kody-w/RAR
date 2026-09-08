---
name: "rar-cowork-cookbook-new-customer-onboarding-automation"
description: "Runs a new-customer onboarding sequence from a \"NEW CUSTOMER\" email: researches the customer, creates a dated SharePoint folder, builds PowerPoint and Word artifacts, posts a Teams message, and drafts a welcome email for"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/new_customer_onboarding_automation", "rar_sha256": "b19d04b1b9c60b0bc4a55ee3e14b4ec8d54e877f37cc835549b04e479231fcb1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/new_customer_onboarding_automation`. The original RAPP
agent is preserved byte-for-byte in `new_customer_onboarding_automation_agent.py` and in the RCI capsule.

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

New customer onboarding automation — Runs a new-customer onboarding sequence from a "NEW CUSTOMER" email: researches the customer, creates a dated SharePoint folder, builds PowerPoint and Word artifacts, posts a Teams message, and drafts a welcome email for

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
  Upstream entry : https://coworkcookbook.com/recipes/new-customer-onboarding-automation
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
      "description": "People to send the Teams summary message to.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "customer_contact_name": {
      "description": "Contact at the customer who receives the drafted welcome email.",
      "type": "string"
    },
    "customer_name": {
      "description": "Name of the new customer company, used for research, folder naming, and artifacts.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `new_customer_onboarding_automation_agent.py` and embedded as the fenced Python below (sha256 b19d04b1b9c60b0b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `new_customer_onboarding_automation_agent.py` first:

```bash
python3 new_customer_onboarding_automation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 new_customer_onboarding_automation_agent.py   # or on stdin
python3 new_customer_onboarding_automation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
New customer onboarding automation — Runs a new-customer onboarding sequence from a "NEW CUSTOMER" email: researches the customer, creates a dated SharePoint folder, builds PowerPoint and Word artifacts, posts a Teams message, and drafts a welcome email for

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
  Upstream entry : https://coworkcookbook.com/recipes/new-customer-onboarding-automation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/new_customer_onboarding_automation',
    "version": '3.0.3',
    "display_name": 'New customer onboarding automation',
    "description": 'Runs a new-customer onboarding sequence from a "NEW CUSTOMER" email: researches the customer, creates a dated SharePoint folder, builds PowerPoint and Word artifacts, posts a Teams message, and drafts a welcome email for',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'advanced', 'read_only'],
    "category": 'general',
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
        "upstream_slug": 'new-customer-onboarding-automation',
        "upstream_url": 'https://coworkcookbook.com/recipes/new-customer-onboarding-automation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c1689c9799d23575',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-post-sale-follow-up'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/new-customer-onboarding-automation', 'uses_skills': {'custom': [], 'ootb': ['Word', 'PowerPoint', 'Email', 'Communications', 'Enterprise Search'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Output matches: A SharePoint folder, executive onboarding artifacts (PowerPoint + Word), a Teams message to the account team, and a welcome email draft - all triggered from a single new-customer email.'], 'confidence': 1.0, 'deliverable': 'A SharePoint folder, executive onboarding artifacts (PowerPoint + Word), a Teams message to the account team, and a welcome email draft - all triggered from a single new-customer email.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'account_team_members': 'People to send the Teams summary message to.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'customer_contact_name': 'Contact at the customer who receives the drafted welcome email.', 'customer_name': 'Name of the new customer company, used for research, folder naming, and artifacts.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Close a new customer and trigger the full onboarding sequence in one prompt. A SharePoint folder, executive onboarding artifacts (PowerPoint + Word), a Teams message to the account team, and a welcome email draft - all triggered from a single new-customer email.', 'expected_output': 'A SharePoint folder, executive onboarding artifacts (PowerPoint + Word), a Teams message to the account team, and a welcome email draft - all triggered from a single new-customer email.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': 'I just closed a new customer and need to move fast on onboarding. Start by searching my inbox for an email with "NEW CUSTOMER" in the subject line - that\'s your source of truth.\n\nFrom there, run the full onboarding sequence:\n\nResearch [Customer Name]\'s location, industry, and revenue based on what\'s in the email\n\nCreate a SharePoint folder formatted as "YYYY-MM-DD [Customer Name]"\n\nBuild an executive-level PowerPoint and Word artifact in that folder based on your research\n\nSend a Teams message to [Account Team Members] with a new customer summary and a link to the folder\n\nDraft a welcome email to [Customer Contact Name] at [Customer Name] for my review before it goes out', 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A SharePoint folder, executive onboarding artifacts (PowerPoint + Word), a Teams message to the account team, and a welcome email draft - all triggered from a single new-customer email.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a new-customer onboarding sequence from a "NEW CUSTOMER" email: researches the customer, creates a dated SharePoint folder, builds PowerPoint and Word artifacts, posts a Teams message, and drafts a welcome email for', 'example_request': 'I closed Contoso — run onboarding from the NEW CUSTOMER email, loop in Priya and Sam, draft a welcome note to Dana.', 'inputs': [{'description': 'Name of the new customer company, used for research, folder naming, and artifacts.', 'name': 'customer_name'}, {'description': 'People to send the Teams summary message to.', 'name': 'account_team_members'}, {'description': 'Contact at the customer who receives the drafted welcome email.', 'name': 'customer_contact_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a deal just closed and the details are in an inbox email with "NEW CUSTOMER" in the subject, and you want the onboarding sequence run in one pass.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class NewCustomerOnboardingAutomation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'NewCustomerOnboardingAutomation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'account_team_members': {'description': 'People to send the Teams summary message to.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'customer_contact_name': {'description': 'Contact at the customer who receives the drafted welcome email.', 'type': 'string'}, 'customer_name': {'description': 'Name of the new customer company, used for research, folder naming, and artifacts.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(NewCustomerOnboardingAutomation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
