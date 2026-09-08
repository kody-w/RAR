---
name: "rar-cowork-cookbook-launch-activation-kit-and-owner-routing"
description: "Builds a full launch activation kit (customer announcement, exec blog, partner one-pager, field talking points, creator pack, sales quick-start deck, social calendar, owner routing plan) and files each asset by owner wit"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/launch_activation_kit_and_owner_routing", "rar_sha256": "c3395e1272dce98f7a6668b166354a8afe0154c66ac6ca85744204bb487255f4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/launch_activation_kit_and_owner_routing`. The original RAPP
agent is preserved byte-for-byte in `launch_activation_kit_and_owner_routing_agent.py` and in the RCI capsule.

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

Launch activation kit and owner routing — Builds a full launch activation kit (customer announcement, exec blog, partner one-pager, field talking points, creator pack, sales quick-start deck, social calendar, owner routing plan) and files each asset by owner wit

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
  Upstream entry : https://coworkcookbook.com/recipes/launch-activation-kit-and-owner-routing
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
    "exec_direction": {
      "description": "Executive name and the meeting, email, or briefing where they set direction.",
      "type": "string"
    },
    "kickoff_meeting": {
      "description": "Launch kickoff meeting name and date to ground content in.",
      "type": "string"
    },
    "launch_date": {
      "description": "The launch date to sequence assets around.",
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
    "owner_map_and_workspace": {
      "description": "Optional owner map for routing, plus the launch workspace folder to file assets into.",
      "type": "string"
    },
    "product_name": {
      "description": "Name of the product launching.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `launch_activation_kit_and_owner_routing_agent.py` and embedded as the fenced Python below (sha256 c3395e1272dce98f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `launch_activation_kit_and_owner_routing_agent.py` first:

```bash
python3 launch_activation_kit_and_owner_routing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 launch_activation_kit_and_owner_routing_agent.py   # or on stdin
python3 launch_activation_kit_and_owner_routing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Launch activation kit and owner routing — Builds a full launch activation kit (customer announcement, exec blog, partner one-pager, field talking points, creator pack, sales quick-start deck, social calendar, owner routing plan) and files each asset by owner wit

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
  Upstream entry : https://coworkcookbook.com/recipes/launch-activation-kit-and-owner-routing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/launch_activation_kit_and_owner_routing',
    "version": '3.0.3',
    "display_name": 'Launch activation kit and owner routing',
    "description": 'Builds a full launch activation kit (customer announcement, exec blog, partner one-pager, field talking points, creator pack, sales quick-start deck, social calendar, owner routing plan) and files each asset by owner wit',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'advanced', 'integration', 'fabric_iq'],
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
        "upstream_slug": 'launch-activation-kit-and-owner-routing',
        "upstream_url": 'https://coworkcookbook.com/recipes/launch-activation-kit-and-owner-routing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '855a1a0a116eab96',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'fabric-iq', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/create-marketing-material'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/launch-activation-kit-and-owner-routing', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Excel', 'PowerPoint', 'Email', 'Calendar Management', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Fabric IQ plugin enabled in your Cowork session', 'Output matches: A fully-routed launch package across Word, PowerPoint, and Excel - every asset substantiated with Fabric IQ performance data, sequenced by audience beat, filed into a launch workspace by owner, with review requests sent.'], 'confidence': 1.0, 'deliverable': 'A fully-routed launch package across Word, PowerPoint, and Excel - every asset substantiated with Fabric IQ performance data, sequenced by audience beat, filed into a launch workspace by owner, with review requests sent.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'exec_direction': 'Executive name and the meeting, email, or briefing where they set direction.', 'kickoff_meeting': 'Launch kickoff meeting name and date to ground content in.', 'launch_date': 'The launch date to sequence assets around.', 'owner_map_and_workspace': 'Optional owner map for routing, plus the launch workspace folder to file assets into.', 'product_name': 'Name of the product launching.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Build the full launch kit across customer, field, partner, exec, and creator audiences - grounded in real performance baselines and proof points - and get every asset to the right owner with a review deadline. A fully-routed launch package across Word, PowerPoint, and Excel - every asset substantiated with Fabric IQ performance data, sequenced by audience beat, filed into a launch workspace by owner, with review requests sent.', 'expected_output': 'A fully-routed launch package across Word, PowerPoint, and Excel - every asset substantiated with Fabric IQ performance data, sequenced by audience beat, filed into a launch workspace by owner, with review requests sent.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Fabric IQ plugin enabled in your Cowork session'], 'prompt': "[Product name] launches on [Launch Date] and I'm the launch owner. I need the full activation kit built out and every asset handed to the right owner with a review deadline - customer, field, partner, exec, all in lockstep.\n\nGround everything in the context from the [Launch kickoff meeting] on [Date], the exec direction [Executive name] laid out in [Meeting/Email/Briefing], and the external announcements and market activity happening around this launch. If [Owner map] is attached, use it for routing; otherwise infer owners from the most active stakeholders across recent launch discussions.\n\nBuild the following BOM:\n\nCustomer announcement (Word)\n\nExec blog post (Word)\n\nPartner one-pager (Word)\n\nField talking points (Word)\n\nCreator promotional pack - talking points for creators, influencers, and exec voices (Word)\n\nSales enablement quick-start (PowerPoint)\n\nMulti-channel social calendar for launch week (Excel)\n\nOwner routing plan with assets, owners, and review deadlines (Excel)\n\nHand each asset to its owner with a review deadline, sequenced so the launch hits each audience at the right beat. File every asset into the [Launch Workspace] folder, organized by owner - that's the working folder for launch week.\n\nWorkflow tip - Plan in Chat, execute in Cowork\n\nDo your upfront brainstorming, strategy, and planning work in Copilot Chat - explore options, pressure-test the angle, sharpen the brief.\n\nOnce you know what you need to accomplish, bring the clear ask to Cowork for the large-scale execution. Cowork is at its best when you arrive with a defined outcome and the right context - not when you're still figuring out what you want", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Fabric IQ plugin enabled in your Cowork session.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A fully-routed launch package across Word, PowerPoint, and Excel - every asset substantiated with Fabric IQ performance data, sequenced by audience beat, filed into a launch workspace by owner, with review requests sent.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a full launch activation kit (customer announcement, exec blog, partner one-pager, field talking points, creator pack, sales quick-start deck, social calendar, owner routing plan) and files each asset by owner wit', 'example_request': 'Build the full launch activation kit for Contoso Edge launching March 10 and route every asset to owners with review deadlines.', 'inputs': [{'description': 'Name of the product launching.', 'name': 'product_name'}, {'description': 'The launch date to sequence assets around.', 'name': 'launch_date'}, {'description': 'Launch kickoff meeting name and date to ground content in.', 'name': 'kickoff_meeting'}, {'description': 'Executive name and the meeting, email, or briefing where they set direction.', 'name': 'exec_direction'}, {'description': 'Optional owner map for routing, plus the launch workspace folder to file assets into.', 'name': 'owner_map_and_workspace'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you own a product launch and need customer, field, partner, exec, and creator assets drafted, routed to owners with review deadlines, and filed in a launch workspace.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Fabric IQ plugin enabled in your Cowork session.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class LaunchActivationKitAndOwnerRouting(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'LaunchActivationKitAndOwnerRouting'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'exec_direction': {'description': 'Executive name and the meeting, email, or briefing where they set direction.', 'type': 'string'}, 'kickoff_meeting': {'description': 'Launch kickoff meeting name and date to ground content in.', 'type': 'string'}, 'launch_date': {'description': 'The launch date to sequence assets around.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner_map_and_workspace': {'description': 'Optional owner map for routing, plus the launch workspace folder to file assets into.', 'type': 'string'}, 'product_name': {'description': 'Name of the product launching.', 'type': 'string'}},
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
    print(LaunchActivationKitAndOwnerRouting().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
