---
name: "rar-cowork-cookbook-stand-up-an-account-plan-board"
description: "Builds a Monday.com account plan board for a named customer by pulling recent emails, meetings, and CRM notes to identify stakeholders, workstreams, owners, next steps, and due dates. Call when starting an account plan."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/stand_up_an_account_plan_board", "rar_sha256": "44fca67437db27adb8290b44c6cf4a59ce3e426a0a5816b436da3ad6db453d69", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "monday_com"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/stand_up_an_account_plan_board`. The original RAPP
agent is preserved byte-for-byte in `stand_up_an_account_plan_board_agent.py` and in the RCI capsule.

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

Stand up an account plan board — Builds a Monday.com account plan board for a named customer by pulling recent emails, meetings, and CRM notes to identify stakeholders, workstreams, owners, next steps, and due dates. Call when starting an account plan.

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
  Upstream entry : https://coworkcookbook.com/recipes/stand-up-an-account-plan-board
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
    "customer_name": {
      "description": "The account/customer name the plan is being built for.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `stand_up_an_account_plan_board_agent.py` and embedded as the fenced Python below (sha256 44fca67437db27ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `stand_up_an_account_plan_board_agent.py` first:

```bash
python3 stand_up_an_account_plan_board_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 stand_up_an_account_plan_board_agent.py   # or on stdin
python3 stand_up_an_account_plan_board_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Stand up an account plan board — Builds a Monday.com account plan board for a named customer by pulling recent emails, meetings, and CRM notes to identify stakeholders, workstreams, owners, next steps, and due dates. Call when starting an account plan.

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
  Upstream entry : https://coworkcookbook.com/recipes/stand-up-an-account-plan-board
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/stand_up_an_account_plan_board',
    "version": '3.0.3',
    "display_name": 'Stand up an account plan board',
    "description": 'Builds a Monday.com account plan board for a named customer by pulling recent emails, meetings, and CRM notes to identify stakeholders, workstreams, owners, next steps, and due dates. Call when starting an account plan.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'intermediate', 'integration', 'monday_com'],
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
        "upstream_slug": 'stand-up-an-account-plan-board',
        "upstream_url": 'https://coworkcookbook.com/recipes/stand-up-an-account-plan-board',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b947b5555e94eba3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'monday-com', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/maintain-contacts-and-accounts'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/stand-up-an-account-plan-board', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Meetings', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: monday.com plugin enabled and connected to your workspace', 'Output matches: A Monday.com account plan board capturing stakeholders, workstreams, next steps, and owners - built from your real customer context - so the account team has a single source of truth.'], 'confidence': 1.0, 'deliverable': 'A Monday.com account plan board capturing stakeholders, workstreams, next steps, and owners - built from your real customer context - so the account team has a single source of truth.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'customer_name': 'The account/customer name the plan is being built for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Move from a scattered account plan to a structured working board the full account team can run against. A Monday.com account plan board capturing stakeholders, workstreams, next steps, and owners - built from your real customer context - so the account team has a single source of truth.', 'expected_output': 'A Monday.com account plan board capturing stakeholders, workstreams, next steps, and owners - built from your real customer context - so the account team has a single source of truth.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'monday.com plugin enabled and connected to your workspace'], 'prompt': "I'm building out the account plan for [Customer Name] and need to give the account team a single working board. Pull recent emails, meetings, and CRM notes related to the account to identify key stakeholders, active workstreams, and outstanding next steps\n\nThen build a Monday.com board with the structure: Workstream name, owner, status, next step, due date. Group by workstream and pre-fill what you can infer.", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: monday.com plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A Monday.com account plan board capturing stakeholders, workstreams, next steps, and owners - built from your real customer context - so the account team has a single source of truth.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a Monday.com account plan board for a named customer by pulling recent emails, meetings, and CRM notes to identify stakeholders, workstreams, owners, next steps, and due dates. Call when starting an account plan.', 'example_request': 'Build an account plan board in Monday.com for Contoso from our recent emails, meetings, and CRM notes.', 'inputs': [{'description': 'The account/customer name the plan is being built for.', 'name': 'customer_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need a scattered account plan turned into a single structured Monday.com board the account team can work from.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: monday.com plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class StandUpAnAccountPlanBoard(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'StandUpAnAccountPlanBoard'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'customer_name': {'description': 'The account/customer name the plan is being built for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(StandUpAnAccountPlanBoard().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
