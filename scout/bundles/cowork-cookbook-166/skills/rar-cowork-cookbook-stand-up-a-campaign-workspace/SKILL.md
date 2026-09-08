---
name: "rar-cowork-cookbook-stand-up-a-campaign-workspace"
description: "Builds a Monday.com campaign board from an intake brief plus recent email and Teams threads, grouped by workstream with owner, deliverable, status, due date and dependency notes, flagging open decisions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/stand_up_a_campaign_workspace", "rar_sha256": "0313e215fc92edf9bb22fc890b79777bebb69bfa246d6c033fda7a5d25b54c00", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "integration", "monday_com"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916WbOjVrbmX1HnfbB9lZmMYsgbFdGAhCSQADGIwVmRZp4HMQiQu/57b6Rz0naVq+6tiH5qOZwSsPea17fWOptfP7hDn9Tthy8ftNCtVnu3KNIkbFduFay4eqzbHHzVuQf+X/l11bepN/R12334+CEIO79Nmz6tK7CdHdIi6Fbu6lxXgTt/9uty5btl46ZxtfJqtw1WUQvuASZp1bt5uPLaNIxWTTF0qzb0w6pfhaWbFk/WeuiW3apP2tANuo+ruK2HJgxW3rxaROp6cL9cjWmfrOqxCtuPqyAs0nvYul4Rflx1vdsPYFswhKvA7cMnySBswioIK39eVXUfgsdR4cZxWsWrGjwBz/20A7p0n4Fu4QREL8Luw5ef//rxQwp+f/jy6we/cLtuMVUPCBoNw73pZy4yNa4fgp2FW8VgSTMDs1bgugnbqG5LcCtYtH1d/diFRfRx9Z//mY9uG3c/fflard4+Xz8s/6lDBbQPV33tdj1Q3Hcb10uLtJ8/r5hidOfFZv3QVovFgTmAFp9fO3+jVDervyzPfnwx+RyH/Y9fPwBdW3fx2dcPP63qFvBrh+X354VK8+NPn4t6DNsff/qNTjd4Wej3CzEg9edvb9dvZMHC35am0eqbpuy4N17ArWkTAuK/02/5vER/I/dmkm+vxT/WzcfVn1Ne9PkLkPcVdx6g++dkgQ3Azg+fszqtfnzj0db3sHIrP/zxp39G1k9CPy/Srv8f0f35RTgB8Qms9WaSnz4+3ffX1fpNt+80/znbBgTMv6MJWP7O7ruh/hntp2f/jnSRVmH33Zd/Su7PNqz/svr5n+r2rzaANPv6Yftbdn5Z/foMkZ9/+F3K/vDXvwHS/y0ZrR5a/0nhW+lWaRR2/bdvP//QPW//8NeffxiaFzR8G9riz2j+mV2ffP5gwbdVP/5xL+BvVHkF8Gb1PYdWv9bN/2r/9nl1dYs0+O1+92X1+0xcPuvVosQ705cJfpeNHZD1d3b86cPfAOxUQJvBfz4G+PEf/7E6p35bd3XUrzS/HvoVcHCfluEivJ6k3SrtnqjRhsCuXQoM+7YOxP/i4UXiOlr98r/9J7J/8t+QHeoWQPs2NN/cb++Y/W18B7VfPq90QLRuUwCWbrFSGUX5WrnxgtiAYdOGXdjen+jch59ALn9afgCUX/3yL+l+e5L43My/PPE5fSGeyh0XtOuGIvy86GUmAJtfWvigdoRT6A+AelH7QJQoLRYgBxLUxR2g5WKDLk+LYhWkAE9AoZqftIGdvizEfvnlF8/tkq/VC56x1auCdRBY8F2c1adPQKeoSOOk/1qFflKvfvj1bz+s/s/qX+16El94KKBGvHkBSChosrQCWTWUYBlwEHApgIynF37925tlARlQw1bAZ2mUhq/NICrzMHg3s3ZgPqEbYuWFwLzAtGVTt/1SudL+8+oYrb7LC5guj5aqkNRd//ui1ycuUOe7JUENXHUg9Lpo/rgauvDJ9RevdZ8iliC93f6X1ZlTQA2qC/DPIuZzEdhcVykw//cgeN0HRNofuhX7TuLzSlricNW4rdskrfvGI3JffgG15307IO6uqnD8Wi2VNlxM9UyKl3nAImAZ/82lnxafg1akBAgQdO+8n2vcpVLqz4rZfq26t4B328UVPigAgGk8pMFSBv7rLaS6pB6K4Gk/IOlC6c0LwZtXnjH4rPeroQFSfm9pvofx6uuAwgi++v+oAVp0ZvZ7dbdn9N12tZN01X75YmkBF0FfXSNoR1YgIF9591uL8g5D72j8tSpSEFjt/F+vlU8Pvq15IdzQAt1URn3SB+EDfLHQfUb3Eq1tu+SF+7V6h/2PwM5PjAMOBlAAUmWJ0HeGy9N3SROQ78v1by3AMxqAN4BNQASvmsErQHRFYRh4rp+/2fzdqyDUwyVbxyT1kz9otQLUQUQB+isgRApyDnji83cofj19F/0PG1+dzrLl2QUOwCntkwCQI1wEXLy1+BaI1786bqDnlycRoEbZ9IvuHkgRoOnrZtiGtwF47+nWl13DBuDwp+X7pelyN5wakBXAWCD2mwFY95ktSwSUoI8BMoAgAMlTphWo68Aob0Z4EnTLJfUBtL41ni+Kz9tvCoXPFFsK0vvGRZFlzxKV79E//x4h9D8LE0CvXFY8+f59pH3nttBeULIDSAc4vj99NQOfX/X81TCs3ul++YeR5sd/b+p5VmjjjwHwZZX0fdN9gaBXVX0vqgsAQC9Zu1eB/TQ0n9xP75jw6TuC/IHoS98vq39PsD+QeEuMLyvkM/wZXh6d3gLr7QPswH1i7U/48vRrpYa/wSdgX5cgshavzQvcvNe69yWg4MVtGC+LX7WvW0rmCKr0E+yBC75Wv4/0JdNALaniJTK7+ncI8Cz6IOpfHvtek8Cjqge8gwXO4nCZxp550YUfvlRDUXz8UIGY+2+msKXmlEsod8vcBpIG9Fl9Gj6vvnciLzq//t0gKy0RDTL+Vere8TtckqRwhwq0vcEiUz83ixCv2Wvp1p6AM/X/SFB+/nCLz6ttCMCt6H4fxW8FaCnAv0u2l92AvXwg+McnhHdLwQR2W3RaEtXtQOSDoP9Xsnx7qx//KNPu7wpNkHb+0D3Rf/FlG/5R/QXkvBDUCIA0n7rEbf6JDV6F7duzsP0j0yXZAaC5iwl/o/2HYhjU/rNT+lPqL/N/W6zxJ8RBkxX2by56Fb13SHhn9adEv3fg/0jSBC3QUlaC+svSDXx8A1/wDaamj6vvA9BSfF8j6fNPB9UApv2fl+FrCcTnluUH2AO+vm/6/gcUL/zw13+QCwj2RHRQFxdavwn529L6ObQtKgDS/etvDL9+AEHvAuXdt7B/6/rBcgCAn7ql54EAKgDm4PqVv+DZvzcPvG0GYQBaUrAbxhAsRJFN5NNoGES056Fo5FM07JE0SZJe6HkE7UUuihMB4cMYFgUu6W4CdONtcB9ehHlBwLelq0sXgTY0GcE0jUY4gsJBEEYoHgQUQRH+hkRhl/ZcsJd2vd+25mkVvGn50mox4ffRZLHGm7K/fvAIHKw84N2ReX04aI34ngllU2ut24KaCgiO3VlRNUfyJakZdi5kmWpylOoBQWd2ZPfXXZZOe/5cjY6H3myXgep2Pd7Xl/VmMzrp7VKjZN/EB2eKZ7jLdal6NA9reYZEMjUaZpMj7LUMjjdY6M8qHQpDXj0C59CMYgJBoRwRVX6dzD1L0+tCc1MsatghyM/Wzd9se/8x6Zx/0/IbLZU3VUXBwNTGt+se5/KNLnqHiyEibQMPiVT7zdWrVDuTrkhVuA4XXFORGMzwtFElZL8xhkKy7+LE5bB/182N1alle2y0YjLLxLmqtYZL+ThJTnO6CGfeFMyioQ61Q6zvrXgqTDEg40hlroZTG1DJjtT9VJSkbAmboDrRunOjOkyB2ptfXo2cswvQMLR+Y5WGV1znx+WQI3u2Mh1i51vwiRPXW/NSWAyZusKhjZTeYFMiQ09xsucZ3nGumY3SMpaxm4O5w/StfYusaxhXjHw29kOMI3J9M5o54/NMgLXb3Mjx41oWaEkfTggSiRu4c093wG4t2YVcc/lRro3yeKTYqghPMtMacJOMtS0jvB60ZzjXa1osQNXhR/eGHEZLXDtOLT6YS3G5gtIjko2ECTIVPNypMbNM2O7gmTqInXjrko1cxOPEtk26vRDw3nRUfLhNjFvpjEJ5pKhJLXZx7Es/57JeIlR7O06IGB1h1NSmKmAjLD3SkkzNu83lYhS3q3kxE+vmEuKuavcTrCkIS7mRIBU7FT8o26F0svAin4ms220C4WLE0K3B7Jq9IB2fdBc2PVCuPnu1fkDbagguopq5KVMg7UWEpUxjivXDvXqwlttE5vBofbXbKyZ1aRudmIviiFbEHjZuIiNmIWb1ESKsGwsRZcaNihKO1bpOjJ0+aeSFSjpTYRurnhiKoPvMgK63dH7YFQgdZbsbz3imPyhTre9ZPJx2zRl0cIPoR8jpkIKkQ8PeuKu0p19akyW82xmidQiRqXVgu/kdVs5ZGigKPVHxNdz2hO0C/nB5OZrbNhgF9mheO1E0zIuKFM7h1CU+rvEY/9Dtw2NHxh10WbMOrhumEOyUsnSkbWJ2wUGQgiLNt/q6Ih1OSAkhPlzyNJvbUUzLKdjFKjHVIs2yCQvJGwrabqwtovej4ia8vxOR9Cgh17DN5GMRxJupJujOmxRbYHEZmtxiK0xmwksPse/aIZB3kOTu4DOJUrcLdxhl0SKHqg7U3L8SMhYZ5IhBtHbJ4vayU4DH8YNdq13Hhdr6EUTSKboiMd0bo9YdRWUPVaraPGp2kBGLVXk7W6s6f7gz97HYbARClBTRH4dmpOKDkHaV4Ddbzon2GH7iNHFf6ltu0z8wl05nwUOAOnMSD4czlQgxSDTXQ3MsC3ZIS9Jm2Z+c+3E8k1PykBCTE1CcUWnI5w+yfhev0sOsH91e4LnbtsL6IB98/2QZGjsIUpVAG/bu4o+coNd9WbSH3BsbRagGlvXFjp79UxhpaxbW6bzATc5EGReW2TMMl/OawobuLFRMiR8R7Sx3iexyrXCZTSc5zLSI6V205gaP5wwLC4wHQ1EDdR6UQJ5yKIOP6vXcqQl0zyo+QHTRqRzBOkgKF47S4G/ky+O0Pt3KwQv2OEI6D4LCxXMaaVCvttskl2B/4rh4J5b4TcIeVZnsZiJRWCpLG17V0J6TBFCFjpW2znX95rOHDr+rhhLRqq3yyFWc4FPMs8lUjzEuHRlcPgsnuTqqdyNYh9b9xiAcJp7ZnNHqy3jiEGtvWSqXimosJzBu1LJ7N6+9mO2YgGLa4uQdg6samh7D5L6DYm444ql2ztyZOe7ncQ04pm5koHTTR8xaHY/5Pk1wlD+gEuJ2vEgmjHsa0DzE8H5vMBPe4ZY66va2WtP3B0xKFr+/mBa2vzR0XdhUyRup4TYYcRWGvszgvcykEkSgR1DM5/yCh7gb9Jx8LNWLNaPrdX9O15JkVWjfK/cO/D65hYPliLe3HRJvUft4mTjWoypnpHBU5mYN2CnuC4S/THbKwhB62cOS1FuYPAZX434RxWZIvGMExwZ7qraWcAT5iKq7lqNwnesoleLu0EM5GmKyuQwecF0hV7vkPjn2NBVFtEkM3uA68hDtdpv2OqOygQkHe7YJUdhVwby2eym7YrJxxNuDrEBOMPjYsZ9q51Z5sC6ELX7VEUqRGJjhJKY63pBi58MbZ0hG3mCIYgzjneJ6VVw5uHq6badmI16ZZiCdHJ2sDhso3oCPsVLGsXzsH1trpo/OI6HsclSm4rg1S0K8Y2mO5OyNqZW6nOt+3uVbDy8JAJ4xx+6NGOOTOR1BCQnie22zl1LMcyGaSTMstMl1YKUagzwsWeOw2x7kw+RS7C5wN6mlWezci9vWtY47JDeYBx0WvGGDrtK+2JssUHdx2XFkc709kNCSxBre6Gd22x25YuL3O1yeB7QYbUsVZBNhfEeqPOUqBzt7C9mDsLusNa7wUa33RhuuRgsOWNh0WwWColNZBElubA+YyYyMtGsekxULNEcwl8noz5V253WFCHaCopZ2gKocwO+Ed3rLjQopLVisGML64KQApY6YfW0OccLafgZQ6eJTkabywmyFXVDHxoZps8rJCJ1y8f58jPcQ0UGQpvsXhp723m6QJsNqLY5hj63RyaOk3RG0xKtg9Dt8W52z2fKi+02VSvxwFH1xpqJWtFrssIcrUk5ZQS95AlL0G0XtQ1Kq8pOQ3XmhvIEB1F2z/dbL/Wazb4PThW/qUQv14+PIxMFFi/WJLkp0b0q30eJdmzU5Jdd5yYdxVsISauQRXd0eDBmSDS6hUCfZx0Kxy48hjR1LRLl6iDzYGudt03gvVrYiZdbFnRSHPNcKd8FsKSpaV5GIPE84ts57Qwhuk6vcBWPILEbTJ1UT5eIhXZRrMRknu9D0I3SdFV5EOVaiUEaMj96loIWMNJ1uuGrursx2xYlSD+WNN0LYZL1DYLUoeTwaM1LeJCrGZQNFpZHhasaHGjErPDWKmTKyZzfvjuOx20glc8ZrNMRswUTohB2qRDg6V8i90CE/DeuES3f9jcNh9Yb73d5tHjzszplPTKZfXNtuLondbg5hi2U5UrfLKdF4RsOuewM93uSYCaS1Q56cCSOJ2opR0/ZA1R4u7Z478AV2cy+gobHPnWBOvKb6O8VQxrxnUdrih5TDPA5HelzMBJ8iJNCmRqganKq5Gc+NVGL0DeJg5sxUqQ46lJlzdldMMXlnX9TH9NjsS2ug8z7ThNuVHcRoFCONE3f5NUGLzXRvnTl3qqA/wdH5QJNX/3i5HmVzczsJ1/okl8T9RLQ23lrDOb08tnETe87JLQubzgzHYJoZL33Ks6+H9Szts+JYepzSa62UVGKCOkWiXfeuIBpXvkVly13LrbY7lBOT9KmcWkbEygU83KzyOBaljno0v+FPlhiWM37Xx7N+i0Qc9N9xQ9/5w57RLBf34DE1JaXGGP8QO+Z29tgtTJMdAgqnDGCvn2umJjTQpiYnPqy8+9nYlJ55IYumuKWtR10jC94aZ4SsLUbX8r4d8GOWD5W5thWE2Q9Xa0OI1w0BJDcPrtzEF1Nr9jeJNKnTMbd4ewodB+Y2KErWfS2BMemiD2f4QnaGvSl8Qpy5IrW3F5NtNO5SQDUk6FSxgdOr4+m+1ochR6Sl4dZZIXNuVW+CB3o4H8LTbtrLfMbzc0KL1HncJ8YVMQZ3h6es2TAyU3YUMZdbxoFPhwRqLpKinTdEwrXJZHa6MVU7UTgyQzTfB1i6lqeO1e9KzKqGXeoll7jkWTYkTVMFb63vYssS9iSRq80Az30rZFtY7/vraJLeEbkfzJ7b+5SrEN1aCdkberdAIe9pDKZVK8ZKVbja3TXNHwHpQMF5YFBqI5jNPTII13qU1rEI42gvXHeG28r9mtwEA6GjnB7MKIdCzeROrc/hJCiBjOLaJdsZKWW5BXQ0Bq6NUF6XIIBNgyZf3asZpgevkOWHkMOQYdGXBiEfKkahukBS7D0C8UlUoisQSacfoBMPUXqUPfb7MVEYI0+utW+KOt67ws0Hc5q9w0DDMVx5YjvHWwmAH+i9TCpD24PxIK+7bnfcZ3Ppb/nDTDWFd5UclXIuI++sVV9DZcXOIKM/NOfbzr894pQ65lRk3gWZUXMJd1JprTL3/d7Pmd5jDn6rtDvWGa9H+4YzWCMSj8Gg4D2U3FjNSjCzjRkwNUtbWdHCqhLl85Y/y7NKZ0VyzPuLynCDfyLvYdyJG+4Ml49bk1CyO0XGZnS1OuyUAXaicq4UW5XGQ99tBg1W00fCVIwx2mEenqnQtrrq6pClmec3Vjk3DEaKu4BWGXdcr3FRQtBWczLzVNv7rXx6dHMUTr2ttUrQ8pykkSrEq9ypZ7tLdQnXJS2sWSzgB9AAQUmEyKyRD6UxnoIH6ItGWyAeDimXctptr4Z119fFfuQpsr/gXA2LN7xOb4SWdkxpESMrnPimOLJt26VlcL8/HGMquu0huE8GfNIlbTpd080atN1c4bXj9MigjLYidd7cbrF5h8EMj8T39oi5YqvSGqWW5/3tsqVpY3YYt+2PwSZQyDtqV9u2gnBZXffy4KGlW2+w0hYJzPEDzAgEngxGz3VtiIyOctKv7y5xOqIyAQAPHiUWD922DfviNpPrgtUPXhAFa3yURNqyTtfo0dYPc/IdOTl7JNk+BjbYFXgpIj0/QQ5OVBgoYuiVDgeF3pmaKKRQsTnMABl01vQPiCVehRnlcwTT3RpqSInYyT6t1BqEhK7LVpRBtkQWVH2DF2iP9luK5BVHb/nSjjB1XXe7Pb4Nzs3knSayGl3Kpm9GfzcFhil0A2HBwImsAw4AccQPE/4I1iXf4pGxX2eEgSolpuElw2SlOssQbyo7CJjfzrRRQEhoPfgQtVv3ujCrZ7+1ILyBMju5+ThoVZA2GnlCVMtLYROHlAmqcT5JmeFuiC2XNfE0RdTNh9NRvPuQB0rbUeXzmtwNx3WSrNnNMfbRSNorQ/6QpxvS5NdTqVeBQR780tGwmCK311tjjwGaGFJpbbwHe5B9ys4foc/rE9TMOVF4cp+1gm85BzYXgxxi7lYVBU3ol75z8zGfT0KpCfJ556WXjbC/0bMqOBVRtqaAISSeuhXTbzrAwdpad1SXDAJtfL9VKdCLFzStKR515LV4q8lHFgzuVTVS2/6OCGaQ7dfH9CKwJtrRY31rcIOY7W7dBSaKKFJn3erpIbZbmK2xfj5naFRqV53kzurorMVWrrB8ousbYVaFiKHsrp0dTkzOaufvt4QLOtzd9WTNQ+eNkJbKCBSAFWjAyRvcV4yd3m5gJTqWsZiBmo3S1yIb6VjAxstVUx/uoyJj8rw7a2sKsfXpRPSFgrhhBN33yn2ATuzYrlM8bXM7uQtUFRIn3rTi9XTMZdeCPfZyiR7y43Eebh4Hbf1gvpniKZlhnFhTOb6V10qxXgYKCVOxxvRuUsvO26QehFSmUXdqCuWKjBlWlxd/bB+u0ZER5dzvpVxmp83JRjw622WJOmX9BmX79ATGEYyI0/ZGbQ82dZcn8YoN9zvPuDJITHTCtJwslTMB4xtUJTEEpFrjbe5FZSZogCquMVxG5BQL43Cob6VV034XnjGfTY+1vM4wtj/xmclsNzVEn/bp9SA5B9VVOKZezycC6EE8em/qYrEnmUOpeIOc2ug9C/soomkzp1urcalgQ5A4gRN0elBoIkDlKKqr8rB7sAGpPJRkWFtGPZ9sM2IQnywRylETG7nfae16pqPtfTtMipyoyEUs2ccDnU4ZNogS66+LkoPjO37wDYNp+fm6FxQ9rCMxUl3EInc3mXfxSTirrH8PBwLK2AHi5IpKhnOcVUcLpXFo1rsd3ojGBb3Qmltj7cF/tEm3qzeCAqKBNHf6VOH+qQVzkp3FObaZU03pB7jCLw8wJ9TGcYJiViPE7CGN+z3o5bQSyW/tI0ZDBz0JMRSnjNI8yBMYox7IxasapTmACiFS2MUCTZs43y9kYmcnyHXpNKLWY48HA9PoJIwoyIU75e3dMTH7GBGDgk5SRgeclpEyjGnZeg1pmE6f+RqlWkq4RbAtXntSIyWsV1C/4WYPNnfD46zk4am3AhmF63m6nyytr9GNOYTVxN0Kx9uaijY9HJ4KS6RoDUnK1Zu8TuwDe9dJ3WkmYrQieb6OkcEP7k26U24VnBj7ql5m+4Cb1HZNuqyHAXBTXHFyTuszczBgRbzwp0cF12hxBPFf92sxEPdFDDFnLKtySd5EEicrVlAR1yEatDYMyTqfT+vYKix1PJ9NDFT3493qJDbz1iHVniWzk9PdfJTsLWwNLqPj8Xmf+tl2TUNEhDAJ0FhDTGKLwSexCEFhN2lPDy0ieRwwD/LhrGuQxBMpBhZ65IGBiSwUQpBmyV5UQJ5n58vU65nzaNlxpNKLBCpkbZmIaNENPSTlo77naV/N8w0hYeXkInQcClDca+ZxC8Nsci7NjEDmfUjoEh3kOiY34/bQ7EYwj2BHmhH47J4zqbuBDhg3MjKm1hQ6R14v3C0w8z4KhVd5fk2QEIOUcVOBgbXdgk7usgsf03WLiRJ+v22JcSzX7U2mqvtdDUmG9ALkWlEkOTJQ01reBp+FCHJSukDkJNqeEjp2JWy0pYl67FgYxtdE76CzfkvwWzKYt7snKUN0OLVkiROZr/h+1Ht7uUNuSNxQEp165NUbpBtZZBWxD12LaNHCNh9TGQepLmDd+GBxuGhhqIq2V82asx63SEJHgnptZex2UwXcpQYh0VaU08SFyvACeTt2qQJPHaFYCWwE4TmYEXs+sxPC3Dce4/QMfdzzLEwpaR4xwkEipelEJsyA3hQL2yS9SiYBRGygTsWNsE7uZFJgQ2fSEkNVhdXVB/cxhXd/Hji6UFKPe4REYbD+RF5GMD2wY19AlsKREFRGu2bcbxg0mNYtdYtPmzpHdnOFDAVlrtFs3ETylG1OGWloj1HXJ1iC4vUw7fDMy22GYf7ylw8fPywn3m/n1v+zl+KWo63/Zydsr8Ow9xdgnqeToRt8efL68j+U568fP7R+CqR5nR92xRC/Hbj93enhp3/5ssOydX69YfZ+YP461e/deHnd+kNaBUPXt/O3ri6eL76AHd7QLW9pdsuLvD74/v3Bat0nYfvheebth03/ra+/lW6bh8uztFreZgmDdDkyfl3GbwepHz+Uz/e0lkPHRbe3lyaASthn+DP24W//F11NICwbLwAA -->
