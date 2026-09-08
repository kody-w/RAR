---
name: "rar-cowork-cookbook-build-an-account-research-brief"
description: "Produces a Word account research brief for a named customer by pulling Dynamics 365 Sales opportunity, contact, activity and pipeline data and cross-referencing the last 60 days of your emails, meetings and Teams threads"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_an_account_research_brief", "rar_sha256": "1223721cc03b3b24a87d4bb6dec8a31821a62b1dcc448f5785d21c4ff9722bc4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
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
