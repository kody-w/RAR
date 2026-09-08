---
name: "rar-cowork-cookbook-map-a-customer-journey-for-a-campaign"
description: "Builds a Miro customer journey board for a named campaign from its brief, audience definition, and messaging files, plus a stage/channel/asset/owner/status tracking table; call before asset production."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/map_a_customer_journey_for_a_campaign", "rar_sha256": "3c30c9bb144354f962b9a24a887995c89ab7d18bf95f5e287cb507f40fced766", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "integration", "miro"]}
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
