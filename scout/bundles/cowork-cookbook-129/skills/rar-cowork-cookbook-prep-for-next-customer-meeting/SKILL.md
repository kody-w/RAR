---
name: "rar-cowork-cookbook-prep-for-next-customer-meeting"
description: "Produces a meeting-prep brief in Word for a named customer, combining Dynamics 365 Sales account history, open opportunities and recent activity with your recent emails and meetings; call it before a customer call."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/prep_for_next_customer_meeting", "rar_sha256": "72e095a2c367e02dd92226c527996c37e85949f2debc938b1b93c6428c73ff53", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "beginner", "integration", "dynamics_365_sales"]}
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
