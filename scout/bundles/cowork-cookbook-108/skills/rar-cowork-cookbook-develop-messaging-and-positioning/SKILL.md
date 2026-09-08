---
name: "rar-cowork-cookbook-develop-messaging-and-positioning"
description: "Builds a Monday.com messaging and positioning board for a named product or campaign, grouped by section (value pillars, feature-to-benefit, persona cards, business alignment, competitive positioning), pre-filled from you"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/develop_messaging_and_positioning", "rar_sha256": "e2d99b4302accf938befe16fa3de5a96995218af879eb7ef82d5f751cef4ba84", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "integration", "monday_com"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/develop_messaging_and_positioning`. The original RAPP
agent is preserved byte-for-byte in `develop_messaging_and_positioning_agent.py` and in the RCI capsule.

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

Develop messaging and positioning — Builds a Monday.com messaging and positioning board for a named product or campaign, grouped by section (value pillars, feature-to-benefit, persona cards, business alignment, competitive positioning), pre-filled from you

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
  Upstream entry : https://coworkcookbook.com/recipes/develop-messaging-and-positioning
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
    "audience": {
      "description": "The target audience the messaging should be tailored to.",
      "type": "string"
    },
    "competitor_name": {
      "description": "The competitor to differentiate against in the positioning statements.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
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
    "product_or_campaign_name": {
      "description": "The product or campaign the messaging and positioning is being developed for.",
      "type": "string"
    },
    "source_documents": {
      "description": "Product Strategy doc, Customer Insights Report, Competitive Summary, and approved Brand Voice guidelines to pull from.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `develop_messaging_and_positioning_agent.py` and embedded as the fenced Python below (sha256 e2d99b4302accf93…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `develop_messaging_and_positioning_agent.py` first:

```bash
python3 develop_messaging_and_positioning_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 develop_messaging_and_positioning_agent.py   # or on stdin
python3 develop_messaging_and_positioning_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop messaging and positioning — Builds a Monday.com messaging and positioning board for a named product or campaign, grouped by section (value pillars, feature-to-benefit, persona cards, business alignment, competitive positioning), pre-filled from you

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
  Upstream entry : https://coworkcookbook.com/recipes/develop-messaging-and-positioning
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/develop_messaging_and_positioning',
    "version": '3.0.3',
    "display_name": 'Develop messaging and positioning',
    "description": 'Builds a Monday.com messaging and positioning board for a named product or campaign, grouped by section (value pillars, feature-to-benefit, persona cards, business alignment, competitive positioning), pre-filled from you',
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
        "upstream_slug": 'develop-messaging-and-positioning',
        "upstream_url": 'https://coworkcookbook.com/recipes/develop-messaging-and-positioning',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b57f6e2e90962c54',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'monday-com', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/develop-campaign-themes-and-messages'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/develop-messaging-and-positioning', 'uses_skills': {'custom': [], 'ootb': [], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: monday.com plugin enabled and connected to your workspace', 'Output matches: A Monday.com board capturing value pillars, persona messaging, business alignment, and competitive positioning - grounded in your real product, customer, and competitive context.'], 'confidence': 1.0, 'deliverable': 'A Monday.com board capturing value pillars, persona messaging, business alignment, and competitive positioning - grounded in your real product, customer, and competitive context.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'audience': 'The target audience the messaging should be tailored to.', 'competitor_name': 'The competitor to differentiate against in the positioning statements.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'product_or_campaign_name': 'The product or campaign the messaging and positioning is being developed for.', 'source_documents': 'Product Strategy doc, Customer Insights Report, Competitive Summary, and approved Brand Voice guidelines to pull from.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Move messaging development out of scattered docs into one working surface the team can pressure-test together. A Monday.com board capturing value pillars, persona messaging, business alignment, and competitive positioning - grounded in your real product, customer, and competitive context.', 'expected_output': 'A Monday.com board capturing value pillars, persona messaging, business alignment, and competitive positioning - grounded in your real product, customer, and competitive context.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'monday.com plugin enabled and connected to your workspace'], 'prompt': "I'm developing the messaging and positioning for [Product/Campaign name], tailored to [Audience] and I want one working surface the team can pressure-test.\n\nPull the product strategy from [Product Strategy doc], the customer insights from [Customer Insights Report], the competitive positioning from [Competitive Summary], and any approved brand voice guidance from [Brand Voice guidelines].\n\nBuild a Monday.com messaging and positioning board with the following structure:\n\nValue pillars:\n\nThree to four pillars that anchor the positioning, with proof points and the customer challenge each one resolves\n\nFeature-to-benefit translation:\n\nEach major feature mapped to a customer-facing benefit and a real use case example\n\nPersona messaging:\n\nPer-persona cards covering goals, challenges, triggers, and success metrics\n\nBusiness alignment:\n\nHow each pillar connects back to our business objectives and target audience\n\nCompetitive positioning:\n\nTwo to three positioning statements that differentiate us from [Competitor name] grounded in customer outcomes and unique advantages\n\nGroup the board by section so each part of the architecture is its own working surface. Pre-fill what you can pull from the source docs and flag any pillar, persona, or competitive angle where we're missing input - so the team knows exactly where to focus the next round of work.", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: monday.com plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A Monday.com board capturing value pillars, persona messaging, business alignment, and competitive positioning - grounded in your real product, customer, and competitive context.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a Monday.com messaging and positioning board for a named product or campaign, grouped by section (value pillars, feature-to-benefit, persona cards, business alignment, competitive positioning), pre-filled from you', 'example_request': 'Build a messaging and positioning board for Atlas Cloud aimed at IT admins, using our strategy and insights docs, vs. Acme.', 'inputs': [{'description': 'The product or campaign the messaging and positioning is being developed for.', 'name': 'product_or_campaign_name'}, {'description': 'The target audience the messaging should be tailored to.', 'name': 'audience'}, {'description': 'Product Strategy doc, Customer Insights Report, Competitive Summary, and approved Brand Voice guidelines to pull from.', 'name': 'source_documents'}, {'description': 'The competitor to differentiate against in the positioning statements.', 'name': 'competitor_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a team needs messaging and positioning consolidated into one Monday.com board to pressure-test, with gaps flagged for the next round of work.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: monday.com plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DevelopMessagingAndPositioning(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DevelopMessagingAndPositioning'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'The target audience the messaging should be tailored to.', 'type': 'string'}, 'competitor_name': {'description': 'The competitor to differentiate against in the positioning statements.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'product_or_campaign_name': {'description': 'The product or campaign the messaging and positioning is being developed for.', 'type': 'string'}, 'source_documents': {'description': 'Product Strategy doc, Customer Insights Report, Competitive Summary, and approved Brand Voice guidelines to pull from.', 'type': 'string'}},
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
    print(DevelopMessagingAndPositioning().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
