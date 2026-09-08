---
name: "rar-cowork-cookbook-map-a-customer-journey-for-a-campaign"
description: "Builds a Miro customer journey board for a named campaign from its brief, audience definition, and messaging files, plus a stage/channel/asset/owner/status tracking table; call before asset production."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/map_a_customer_journey_for_a_campaign", "rar_sha256": "3c30c9bb144354f962b9a24a887995c89ab7d18bf95f5e287cb507f40fced766", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "integration", "miro"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/map_a_customer_journey_for_a_campaign`. The original RAPP
agent is preserved byte-for-byte in `map_a_customer_journey_for_a_campaign_agent.py` and in the RCI capsule.

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

Map a customer journey for a campaign — Builds a Miro customer journey board for a named campaign from its brief, audience definition, and messaging files, plus a stage/channel/asset/owner/status tracking table; call before asset production.

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
  Upstream entry : https://coworkcookbook.com/recipes/map-a-customer-journey-for-a-campaign
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
      "description": "Name of the campaign the journey is being mapped for.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "onedrive_folder": {
      "description": "OneDrive folder holding the campaign brief, audience definition, and messaging guidance.",
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
    "team_channel": {
      "description": "Teams channel with recent strategy threads that shaped the campaign angle.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `map_a_customer_journey_for_a_campaign_agent.py` and embedded as the fenced Python below (sha256 3c30c9bb144354f9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `map_a_customer_journey_for_a_campaign_agent.py` first:

```bash
python3 map_a_customer_journey_for_a_campaign_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 map_a_customer_journey_for_a_campaign_agent.py   # or on stdin
python3 map_a_customer_journey_for_a_campaign_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Map a customer journey for a campaign — Builds a Miro customer journey board for a named campaign from its brief, audience definition, and messaging files, plus a stage/channel/asset/owner/status tracking table; call before asset production.

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
  Upstream entry : https://coworkcookbook.com/recipes/map-a-customer-journey-for-a-campaign
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/map_a_customer_journey_for_a_campaign',
    "version": '3.0.3',
    "display_name": 'Map a customer journey for a campaign',
    "description": 'Builds a Miro customer journey board for a named campaign from its brief, audience definition, and messaging files, plus a stage/channel/asset/owner/status tracking table; call before asset production.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'intermediate', 'integration', 'miro'],
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
        "upstream_slug": 'map-a-customer-journey-for-a-campaign',
        "upstream_url": 'https://coworkcookbook.com/recipes/map-a-customer-journey-for-a-campaign',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0c01bc961ade4c31',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'miro', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/identify-campaign-audiences'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/map-a-customer-journey-for-a-campaign', 'uses_skills': {'custom': [], 'ootb': [], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Miro plugin enabled and connected to your workspace', "Output matches: A Miro customer journey board mapping the audience's path from awareness through conversion - stages, touchpoints, channels, and message moments visualized in one place - paired with a tracking table for asset alignment."], 'confidence': 1.0, 'deliverable': "A Miro customer journey board mapping the audience's path from awareness through conversion - stages, touchpoints, channels, and message moments visualized in one place - paired with a tracking table for asset alignment.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'campaign_name': 'Name of the campaign the journey is being mapped for.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'onedrive_folder': 'OneDrive folder holding the campaign brief, audience definition, and messaging guidance.', 'team_channel': 'Teams channel with recent strategy threads that shaped the campaign angle.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Turn a campaign brief into a clear, visual customer journey the team can rally around - instead of arguing over interpretations of the same Word doc. A Miro customer journey board mapping the audience's path from awareness through conversion - stages, touchpoints, channels, and message moments visualized in one place - paired with a tracking table for asset alignment.", 'expected_output': "A Miro customer journey board mapping the audience's path from awareness through conversion - stages, touchpoints, channels, and message moments visualized in one place - paired with a tracking table for asset alignment.", 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Miro plugin enabled and connected to your workspace'], 'prompt': "I'm building out the customer journey for [Campaign name] and I want the team aligned on the path before we get into asset production. Pull the campaign brief, the audience definition, and any messaging guidance from [OneDrive folder] - plus any recent strategy threads from [Team channel] that have shaped the angle.\n\nBuild a Miro customer journey board that maps the audience's path from initial awareness through consideration, decision, and post-conversion engagement. For each stage, capture the customer mindset, the channels we'll show up in, the key message moments, and the assets that need to land there.\n\nThen add a tracking table beneath the journey summarizing each stage with stage, channel, asset, owner, and status.\n\nPre-fill what you can infer from the brief and flag any stage where we're missing channel coverage or asset alignment.", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Miro plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': "A Miro customer journey board mapping the audience's path from awareness through conversion - stages, touchpoints, channels, and message moments visualized in one place - paired with a tracking table for asset alignment."}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a Miro customer journey board for a named campaign from its brief, audience definition, and messaging files, plus a stage/channel/asset/owner/status tracking table; call before asset production.', 'example_request': 'Map the customer journey for the Spring Launch campaign using the brief in our Campaigns OneDrive folder and the #launch channel.', 'inputs': [{'description': 'Name of the campaign the journey is being mapped for.', 'name': 'campaign_name'}, {'description': 'OneDrive folder holding the campaign brief, audience definition, and messaging guidance.', 'name': 'onedrive_folder'}, {'description': 'Teams channel with recent strategy threads that shaped the campaign angle.', 'name': 'team_channel'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when a campaign brief exists and the team needs an agreed visual journey from awareness to post-conversion before producing assets.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Miro plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class MapACustomerJourneyForACampaign(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'MapACustomerJourneyForACampaign'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'campaign_name': {'description': 'Name of the campaign the journey is being mapped for.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'onedrive_folder': {'description': 'OneDrive folder holding the campaign brief, audience definition, and messaging guidance.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'team_channel': {'description': 'Teams channel with recent strategy threads that shaped the campaign angle.', 'type': 'string'}},
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
    print(MapACustomerJourneyForACampaign().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
