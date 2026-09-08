---
name: "rar-cowork-cookbook-prepare-for-a-customer-meeting-deep"
description: "Assembles a customer meeting prep set in Microsoft 365 Copilot Cowork: a Word brief from mail, calendar, files and Dynamics 365 Sales data, an Excel trends overview, a PowerPoint pitch, a prep calendar block, and a draft"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prepare_for_a_customer_meeting_deep", "rar_sha256": "f9f11838cbd2ee3cbe74411cd8871ec9366cc1d4cd6c38571c44b9df41bd2c0c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/prepare_for_a_customer_meeting_deep`. The original RAPP
agent is preserved byte-for-byte in `prepare_for_a_customer_meeting_deep_agent.py` and in the RCI capsule.

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

Prepare for a customer meeting — Assembles a customer meeting prep set in Microsoft 365 Copilot Cowork: a Word brief from mail, calendar, files and Dynamics 365 Sales data, an Excel trends overview, a PowerPoint pitch, a prep calendar block, and a draft

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
  Upstream entry : https://coworkcookbook.com/recipes/prepare-for-a-customer-meeting-deep
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
    "account_team_contact_1": {
      "description": "First account team recipient of the draft customer update email.",
      "type": "string"
    },
    "account_team_contact_2": {
      "description": "Second account team recipient of the draft customer update email.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "customer_brief_template": {
      "description": "Customer Brief Template.docx to attach and use for the briefing document.",
      "type": "string"
    },
    "customer_name": {
      "description": "The customer or account the meeting is with.",
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
    "prep_attendee_name": {
      "description": "Person to include on the 30-minute prep block tomorrow morning.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prepare_for_a_customer_meeting_deep_agent.py` and embedded as the fenced Python below (sha256 f9f11838cbd2ee3c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prepare_for_a_customer_meeting_deep_agent.py` first:

```bash
python3 prepare_for_a_customer_meeting_deep_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prepare_for_a_customer_meeting_deep_agent.py   # or on stdin
python3 prepare_for_a_customer_meeting_deep_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare for a customer meeting — Assembles a customer meeting prep set in Microsoft 365 Copilot Cowork: a Word brief from mail, calendar, files and Dynamics 365 Sales data, an Excel trends overview, a PowerPoint pitch, a prep calendar block, and a draft

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
  Upstream entry : https://coworkcookbook.com/recipes/prepare-for-a-customer-meeting-deep
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/prepare_for_a_customer_meeting_deep',
    "version": '3.0.3',
    "display_name": 'Prepare for a customer meeting',
    "description": 'Assembles a customer meeting prep set in Microsoft 365 Copilot Cowork: a Word brief from mail, calendar, files and Dynamics 365 Sales data, an Excel trends overview, a PowerPoint pitch, a prep calendar block, and a draft',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'advanced', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'prepare-for-a-customer-meeting-deep',
        "upstream_url": 'https://coworkcookbook.com/recipes/prepare-for-a-customer-meeting-deep',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2f0a5bba79f52586',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/maintain-contacts-and-accounts'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/prepare-for-a-customer-meeting-deep', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Excel', 'PowerPoint', 'Email', 'Calendar Management', 'Scheduling'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment', 'Prerequisite: A Dynamics 365 Sales licence', 'Output matches: A Word briefing document, an Excel customer trends overview, a client-ready PowerPoint pitch, a calendar prep block, and a draft customer update email - all sequenced before the meeting.'], 'confidence': 1.0, 'deliverable': 'A Word briefing document, an Excel customer trends overview, a client-ready PowerPoint pitch, a calendar prep block, and a draft customer update email - all sequenced before the meeting.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'account_team_contact_1': 'First account team recipient of the draft customer update email.', 'account_team_contact_2': 'Second account team recipient of the draft customer update email.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'customer_brief_template': 'Customer Brief Template.docx to attach and use for the briefing document.', 'customer_name': 'The customer or account the meeting is with.', 'prep_attendee_name': 'Person to include on the 30-minute prep block tomorrow morning.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Walk into your next customer meeting fully briefed - context pulled, deck built, prep time blocked. A Word briefing document, an Excel customer trends overview, a client-ready PowerPoint pitch, a calendar prep block, and a draft customer update email - all sequenced before the meeting.', 'expected_output': 'A Word briefing document, an Excel customer trends overview, a client-ready PowerPoint pitch, a calendar prep block, and a draft customer update email - all sequenced before the meeting.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment', 'A Dynamics 365 Sales licence'], 'prompt': "I have a customer meeting with [Customer Name] coming up and need to be fully prepared. Pull together relevant emails, calendar items, and file context into a briefing document using the attached template.\n\nAlso use Dynamics 365 data to pull the account's open opportunities and recent CRM activity into the brief.\n\nAdditionally, create an Excel overview of customer data with usage and sales trend graphs over time. Then build a client-ready presentation that covers our competitive differentiation, key opportunities, and recommended next steps.\n\nPrompt 2:\n\nSchedule 30 minutes of focus prep time for me tomorrow morning with [Prep Attendee Name]. Then draft a customer update email covering status update, findings summaries, and current proposals - addressed to [Account Team Contact 1] and [Account Team Contact 2] on the account team, ready for my review before sending.\n\nAttach: [Customer Brief Template.docx]", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A Word briefing document, an Excel customer trends overview, a client-ready PowerPoint pitch, a calendar prep block, and a draft customer update email - all sequenced before the meeting.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Assembles a customer meeting prep set in Microsoft 365 Copilot Cowork: a Word brief from mail, calendar, files and Dynamics 365 Sales data, an Excel trends overview, a PowerPoint pitch, a prep calendar block, and a draft', 'example_request': 'Prep me for my Contoso meeting: brief, Excel trends, deck, 30-min prep hold with Dana, and a draft update email.', 'inputs': [{'description': 'The customer or account the meeting is with.', 'name': 'customer_name'}, {'description': 'Person to include on the 30-minute prep block tomorrow morning.', 'name': 'prep_attendee_name'}, {'description': 'First account team recipient of the draft customer update email.', 'name': 'account_team_contact_1'}, {'description': 'Second account team recipient of the draft customer update email.', 'name': 'account_team_contact_2'}, {'description': 'Customer Brief Template.docx to attach and use for the briefing document.', 'name': 'customer_brief_template'}], 'model': 'claude-opus-5', 'when_to_use': 'Call before an upcoming customer meeting when you want briefing, deck, Excel trends, a prep hold, and a draft account-team email prepared for review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PrepareForACustomerMeetingDeep(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PrepareForACustomerMeetingDeep'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'account_team_contact_1': {'description': 'First account team recipient of the draft customer update email.', 'type': 'string'}, 'account_team_contact_2': {'description': 'Second account team recipient of the draft customer update email.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'customer_brief_template': {'description': 'Customer Brief Template.docx to attach and use for the briefing document.', 'type': 'string'}, 'customer_name': {'description': 'The customer or account the meeting is with.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'prep_attendee_name': {'description': 'Person to include on the 30-minute prep block tomorrow morning.', 'type': 'string'}},
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
    print(PrepareForACustomerMeetingDeep().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
