---
name: "rar-cowork-cookbook-prepare-for-a-customer-meeting-deep"
description: "Assembles a customer meeting prep set in Microsoft 365 Copilot Cowork: a Word brief from mail, calendar, files and Dynamics 365 Sales data, an Excel trends overview, a PowerPoint pitch, a prep calendar block, and a draft"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prepare_for_a_customer_meeting_deep", "rar_sha256": "f9f11838cbd2ee3cbe74411cd8871ec9366cc1d4cd6c38571c44b9df41bd2c0c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
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
