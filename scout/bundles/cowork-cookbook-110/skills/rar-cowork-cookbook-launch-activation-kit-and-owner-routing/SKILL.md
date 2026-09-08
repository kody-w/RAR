---
name: "rar-cowork-cookbook-launch-activation-kit-and-owner-routing"
description: "Builds a full launch activation kit (customer announcement, exec blog, partner one-pager, field talking points, creator pack, sales quick-start deck, social calendar, owner routing plan) and files each asset by owner wit"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/launch_activation_kit_and_owner_routing", "rar_sha256": "c3395e1272dce98f7a6668b166354a8afe0154c66ac6ca85744204bb487255f4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
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
