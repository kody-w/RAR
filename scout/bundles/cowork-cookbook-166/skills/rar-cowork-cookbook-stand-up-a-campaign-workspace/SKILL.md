---
name: "rar-cowork-cookbook-stand-up-a-campaign-workspace"
description: "Builds a Monday.com campaign board from an intake brief plus recent email and Teams threads, grouped by workstream with owner, deliverable, status, due date and dependency notes, flagging open decisions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/stand_up_a_campaign_workspace", "rar_sha256": "0313e215fc92edf9bb22fc890b79777bebb69bfa246d6c033fda7a5d25b54c00", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "integration", "monday_com"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/stand_up_a_campaign_workspace`. The original RAPP
agent is preserved byte-for-byte in `stand_up_a_campaign_workspace_agent.py` and in the RCI capsule.

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

Stand up a campaign workspace — Builds a Monday.com campaign board from an intake brief plus recent email and Teams threads, grouped by workstream with owner, deliverable, status, due date and dependency notes, flagging open decisions.

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
  Upstream entry : https://coworkcookbook.com/recipes/stand-up-a-campaign-workspace
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
    "campaign_name": {
      "description": "Name of the campaign being launched.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "context_threads": {
      "description": "Email and Teams discussions where the campaign has been pre-shaped.",
      "type": "string"
    },
    "intake_brief": {
      "description": "The attached campaign intake brief document.",
      "type": "string"
    },
    "launch_date": {
      "description": "Target launch date for the campaign.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `stand_up_a_campaign_workspace_agent.py` and embedded as the fenced Python below (sha256 0313e215fc92edf9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `stand_up_a_campaign_workspace_agent.py` first:

```bash
python3 stand_up_a_campaign_workspace_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 stand_up_a_campaign_workspace_agent.py   # or on stdin
python3 stand_up_a_campaign_workspace_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Stand up a campaign workspace — Builds a Monday.com campaign board from an intake brief plus recent email and Teams threads, grouped by workstream with owner, deliverable, status, due date and dependency notes, flagging open decisions.

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
  Upstream entry : https://coworkcookbook.com/recipes/stand-up-a-campaign-workspace
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/stand_up_a_campaign_workspace',
    "version": '3.0.3',
    "display_name": 'Stand up a campaign workspace',
    "description": 'Builds a Monday.com campaign board from an intake brief plus recent email and Teams threads, grouped by workstream with owner, deliverable, status, due date and dependency notes, flagging open decisions.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'intermediate', 'integration', 'monday_com'],
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
        "upstream_slug": 'stand-up-a-campaign-workspace',
        "upstream_url": 'https://coworkcookbook.com/recipes/stand-up-a-campaign-workspace',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9b98bc893aae14c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'monday-com', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/oversee-active-campaigns'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/stand-up-a-campaign-workspace', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: monday.com plugin enabled and connected to your workspace', 'Output matches: A Monday.com campaign board capturing workstreams, owners, deliverables, milestones, and key dates - built from your intake brief and recent campaign threads - so the campaign starts the way you want it to run.'], 'confidence': 1.0, 'deliverable': 'A Monday.com campaign board capturing workstreams, owners, deliverables, milestones, and key dates - built from your intake brief and recent campaign threads - so the campaign starts the way you want it to run.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'campaign_name': 'Name of the campaign being launched.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'context_threads': 'Email and Teams discussions where the campaign has been pre-shaped.', 'intake_brief': 'The attached campaign intake brief document.', 'launch_date': 'Target launch date for the campaign.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Spin up a working campaign board grounded in real context - not a blank template - so the team has a single source of truth before the kickoff calendar invite goes out. A Monday.com campaign board capturing workstreams, owners, deliverables, milestones, and key dates - built from your intake brief and recent campaign threads - so the campaign starts the way you want it to run.', 'expected_output': 'A Monday.com campaign board capturing workstreams, owners, deliverables, milestones, and key dates - built from your intake brief and recent campaign threads - so the campaign starts the way you want it to run.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'monday.com plugin enabled and connected to your workspace'], 'prompt': "I'm spinning up [Campaign name] launching on [Launch Date] and I want the campaign workspace ready before kickoff. The [Intake Brief] is attached and there's a handful of email threads and Teams discussions where we've been pre-shaping this campaign - pull from those too.\n\nIdentify the active workstreams (creative, content, channel, partner, exec, measurement - whatever applies based on context), the owners likely tied to each, the deliverables, and the key milestones we need to hit between now and launch.\n\nThen build the campaign board in Monday.com with the structure: workstream, owner, deliverable, status, due date, and dependency notes. Group by workstream. Pre-fill owners and deliverables you can infer, and flag anything that needs my decision before kickoff.", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: monday.com plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A Monday.com campaign board capturing workstreams, owners, deliverables, milestones, and key dates - built from your intake brief and recent campaign threads - so the campaign starts the way you want it to run.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a Monday.com campaign board from an intake brief plus recent email and Teams threads, grouped by workstream with owner, deliverable, status, due date and dependency notes, flagging open decisions.', 'example_request': 'Set up the Monday.com campaign board for Aurora Launch, going live March 14 — brief attached.', 'inputs': [{'description': 'Name of the campaign being launched.', 'name': 'campaign_name'}, {'description': 'Target launch date for the campaign.', 'name': 'launch_date'}, {'description': 'The attached campaign intake brief document.', 'name': 'intake_brief'}, {'description': 'Email and Teams discussions where the campaign has been pre-shaped.', 'name': 'context_threads'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a campaign is being spun up and the team needs a populated campaign board in Monday.com before the kickoff meeting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: monday.com plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class StandUpACampaignWorkspace(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'StandUpACampaignWorkspace'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'campaign_name': {'description': 'Name of the campaign being launched.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'context_threads': {'description': 'Email and Teams discussions where the campaign has been pre-shaped.', 'type': 'string'}, 'intake_brief': {'description': 'The attached campaign intake brief document.', 'type': 'string'}, 'launch_date': {'description': 'Target launch date for the campaign.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(StandUpACampaignWorkspace().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
