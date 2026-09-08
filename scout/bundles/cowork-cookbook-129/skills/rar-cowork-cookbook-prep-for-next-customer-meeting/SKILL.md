---
name: "rar-cowork-cookbook-prep-for-next-customer-meeting"
description: "Produces a meeting-prep brief in Word for a named customer, combining Dynamics 365 Sales account history, open opportunities and recent activity with your recent emails and meetings; call it before a customer call."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prep_for_next_customer_meeting", "rar_sha256": "72e095a2c367e02dd92226c527996c37e85949f2debc938b1b93c6428c73ff53", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "beginner", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/prep_for_next_customer_meeting`. The original RAPP
agent is preserved byte-for-byte in `prep_for_next_customer_meeting_agent.py` and in the RCI capsule.

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

Prep for my next customer meeting — Produces a meeting-prep brief in Word for a named customer, combining Dynamics 365 Sales account history, open opportunities and recent activity with your recent emails and meetings; call it before a customer call.

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
  Upstream entry : https://coworkcookbook.com/recipes/prep-for-next-customer-meeting
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
    "customer": {
      "description": "The customer or account name the meeting is with.",
      "type": "string"
    },
    "meeting_time": {
      "description": "When the meeting is, e.g. 9 a.m., used to identify the call being prepped for.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prep_for_next_customer_meeting_agent.py` and embedded as the fenced Python below (sha256 72e095a2c367e02d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prep_for_next_customer_meeting_agent.py` first:

```bash
python3 prep_for_next_customer_meeting_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prep_for_next_customer_meeting_agent.py   # or on stdin
python3 prep_for_next_customer_meeting_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prep for my next customer meeting — Produces a meeting-prep brief in Word for a named customer, combining Dynamics 365 Sales account history, open opportunities and recent activity with your recent emails and meetings; call it before a customer call.

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
  Upstream entry : https://coworkcookbook.com/recipes/prep-for-next-customer-meeting
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/prep_for_next_customer_meeting',
    "version": '3.0.3',
    "display_name": 'Prep for my next customer meeting',
    "description": 'Produces a meeting-prep brief in Word for a named customer, combining Dynamics 365 Sales account history, open opportunities and recent activity with your recent emails and meetings; call it before a customer call.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'beginner', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'prep-for-next-customer-meeting',
        "upstream_url": 'https://coworkcookbook.com/recipes/prep-for-next-customer-meeting',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '73ce0ae14f16acb9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/maintain-contacts-and-accounts'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/prep-for-next-customer-meeting', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Email', 'Calendar Management', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment', 'Prerequisite: A Dynamics 365 Sales licence', 'Output matches: A single meeting-prep brief pulling account history, open opportunities, recent activity, and calendar context.'], 'confidence': 1.0, 'deliverable': 'A single meeting-prep brief pulling account history, open opportunities, recent activity, and calendar context.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'customer': 'The customer or account name the meeting is with.', 'meeting_time': 'When the meeting is, e.g. 9 a.m., used to identify the call being prepped for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Walk into your next call already knowing the account cold - no scramble through CRM tabs and email. A single meeting-prep brief pulling account history, open opportunities, recent activity, and calendar context.', 'expected_output': 'A single meeting-prep brief pulling account history, open opportunities, recent activity, and calendar context.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment', 'A Dynamics 365 Sales licence'], 'prompt': "Help me prep for my 9 a.m. with [Customer]. Pull the account history, open opportunities, and recent activity from Dynamics 365 Sales, and cross-reference my recent emails and meetings so I know what's changed.\n\nGive me a tight brief in Word, including where the relationship stands, what's open, and the two or three things I should walk in ready to address.", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A single meeting-prep brief pulling account history, open opportunities, recent activity, and calendar context.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Produces a meeting-prep brief in Word for a named customer, combining Dynamics 365 Sales account history, open opportunities and recent activity with your recent emails and meetings; call it before a customer call.', 'example_request': 'Prep me for my 9 a.m. with Contoso — pull their D365 account history and recent emails into a Word brief.', 'inputs': [{'description': 'The customer or account name the meeting is with.', 'name': 'customer'}, {'description': 'When the meeting is, e.g. 9 a.m., used to identify the call being prepped for.', 'name': 'meeting_time'}], 'model': 'claude-opus-5', 'when_to_use': "Call before an upcoming customer meeting when you need the account's history, open opportunities, recent activity and email/calendar changes in one brief."}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PrepForNextCustomerMeeting(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PrepForNextCustomerMeeting'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'customer': {'description': 'The customer or account name the meeting is with.', 'type': 'string'}, 'meeting_time': {'description': 'When the meeting is, e.g. 9 a.m., used to identify the call being prepped for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(PrepForNextCustomerMeeting().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
