---
name: "rar-cowork-cookbook-build-an-account-research-brief"
description: "Produces a Word account research brief for a named customer by pulling Dynamics 365 Sales opportunity, contact, activity and pipeline data and cross-referencing the last 60 days of your emails, meetings and Teams threads"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_an_account_research_brief", "rar_sha256": "1223721cc03b3b24a87d4bb6dec8a31821a62b1dcc448f5785d21c4ff9722bc4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/build_an_account_research_brief`. The original RAPP
agent is preserved byte-for-byte in `build_an_account_research_brief_agent.py` and in the RCI capsule.

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

Build an account research brief — Produces a Word account research brief for a named customer by pulling Dynamics 365 Sales opportunity, contact, activity and pipeline data and cross-referencing the last 60 days of your emails, meetings and Teams threads

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
  Upstream entry : https://coworkcookbook.com/recipes/build-an-account-research-brief
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
      "description": "The account/customer to research, used to pull the Dynamics 365 Sales record and match engagement history.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `build_an_account_research_brief_agent.py` and embedded as the fenced Python below (sha256 1223721cc03b3b24…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `build_an_account_research_brief_agent.py` first:

```bash
python3 build_an_account_research_brief_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 build_an_account_research_brief_agent.py   # or on stdin
python3 build_an_account_research_brief_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Build an account research brief — Produces a Word account research brief for a named customer by pulling Dynamics 365 Sales opportunity, contact, activity and pipeline data and cross-referencing the last 60 days of your emails, meetings and Teams threads

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
  Upstream entry : https://coworkcookbook.com/recipes/build-an-account-research-brief
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/build_an_account_research_brief',
    "version": '3.0.3',
    "display_name": 'Build an account research brief',
    "description": 'Produces a Word account research brief for a named customer by pulling Dynamics 365 Sales opportunity, contact, activity and pipeline data and cross-referencing the last 60 days of your emails, meetings and Teams threads',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'prospect_to_quote', 'advanced', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'build-an-account-research-brief',
        "upstream_url": 'https://coworkcookbook.com/recipes/build-an-account-research-brief',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b4c94809436a2872',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/maintain-contacts-and-accounts'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/build-an-account-research-brief', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Email', 'Meetings', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment', 'Prerequisite: A Dynamics 365 Sales licence', 'Output matches: A Word account research brief - opportunity overview, key contacts, recent engagement signals, and active pipeline - built directly from Dynamics 365 Sales data and grounded in your Microsoft 365 work history.'], 'confidence': 1.0, 'deliverable': 'A Word account research brief - opportunity overview, key contacts, recent engagement signals, and active pipeline - built directly from Dynamics 365 Sales data and grounded in your Microsoft 365 work history.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'customer_name': 'The account/customer to research, used to pull the Dynamics 365 Sales record and match engagement history.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Walk into account planning already knowing the shape of the opportunity - pipeline, stakeholders, recent activity, and where the deal sits - without piecing it together from CRM tabs. A Word account research brief - opportunity overview, key contacts, recent engagement signals, and active pipeline - built directly from Dynamics 365 Sales data and grounded in your Microsoft 365 work history.', 'expected_output': 'A Word account research brief - opportunity overview, key contacts, recent engagement signals, and active pipeline - built directly from Dynamics 365 Sales data and grounded in your Microsoft 365 work history.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment', 'A Dynamics 365 Sales licence'], 'prompt': "I'm getting ready to plan my next move on [Customer Name] and I need a real picture of the account before I start. Pull the opportunity overview, the key contacts, the recent activity history, and any active pipeline from Dynamics 365 Sales - anything material happening on this account.\n\nThen cross-reference that with my recent emails, meeting recordings, and Teams threads from the past 60 days to capture the engagement signals - who's leaning in, who's gone quiet, what they're actually asking for versus what's in the formal CRM notes. Pull customer sentiment from what they've said in meetings and derive insights into how the conversation has shifted over time.\n\nBring it all together as a Word account research brief - opportunity state, contact map, engagement signals, sentiment read, open risks, and where I should focus this week. I want to walk into planning already knowing what matters.", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A Word account research brief - opportunity overview, key contacts, recent engagement signals, and active pipeline - built directly from Dynamics 365 Sales data and grounded in your Microsoft 365 work history.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Produces a Word account research brief for a named customer by pulling Dynamics 365 Sales opportunity, contact, activity and pipeline data and cross-referencing the last 60 days of your emails, meetings and Teams threads', 'example_request': 'Build me an account research brief on Contoso before my planning session.', 'inputs': [{'description': 'The account/customer to research, used to pull the Dynamics 365 Sales record and match engagement history.', 'name': 'customer_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when preparing to plan a move on a specific account and you need opportunity state, contact map, engagement signals, sentiment, risks and focus areas in one brief.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Dynamics 365 Sales plugin enabled in your Cowork session, bound to your CRM environment.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BuildAnAccountResearchBrief(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BuildAnAccountResearchBrief'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'customer_name': {'description': 'The account/customer to research, used to pull the Dynamics 365 Sales record and match engagement history.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(BuildAnAccountResearchBrief().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
