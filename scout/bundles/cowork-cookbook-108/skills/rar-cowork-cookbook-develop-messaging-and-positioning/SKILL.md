---
name: "rar-cowork-cookbook-develop-messaging-and-positioning"
description: "Builds a Monday.com messaging and positioning board for a named product or campaign, grouped by section (value pillars, feature-to-benefit, persona cards, business alignment, competitive positioning), pre-filled from you"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/develop_messaging_and_positioning", "rar_sha256": "e2d99b4302accf938befe16fa3de5a96995218af879eb7ef82d5f751cef4ba84", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "integration", "monday_com"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916WZOjWLLmX9HEfajqq8xkEwLyWpsNIAmEBEKAQFDZlsVy2DexSEBN/fc5KCIys7qr+942m6dRLRJwju/+uXtwfntx+y6umpfPLzpwy4Xg5nkSg2bhlsGCrx5Vk8GvKvPgfwu/Krsm8fquatqXDy8BaP0mqbukKuF2rk/yoF24C7kqA3f85FfFogBt60ZJGT3J1VWbzIvna69ym2ARVpDRonQLAJ82VdD73QLe8t2idpOo/LCImqqv4UNvXLTAnzcvfr67eQ8WdZLnbtN+WITA7foGfOyqjx4oQZh0HxY1aNqqdCGhJoBLvL5NSijKws0h1QKUcAkUrwYdlOcOfhTsL3AzJBZC6pBt2EAlxqqHyoIBCpWD9uXzL3/78JLA3y+ff3vxc7eFt1424A7yqpbf9WXLQP1OFG7PXfj1+aUeobFLeA0lhMoX8FYAwsXb1c8tyMMPi//8z+zhNlH7l89fysXb58vL/I/Wl4suBouuctsOyue7tesledKNnxZs/nDHdtEAaI1y9kMLfVVGn153fqdU1Yu/zs9+fmXyKQLdz19eKiiCO4v75eUvswu+vDT9/PvTTKX++S+f8uoBmp//8p1O23spdMlMDEr96evb9RtZuPD70iRcfNXVLf/GqwF+UgNI/Af95s+r6G/k3kzy9XXxz1X9YfHnlGd9/grlfY1GD9L9c7LQBnDny6e0Ssqf33g01R2UbumDn//yz8j6MfCzPGm7/xHdX14Jx8ANoLXeTAJjanbB3xbLN92+0fznbGsYMP+OJnD5O7tvhvpntJ+e/TvS+Zwg33z5p+T+bMPyr4tf/qlu/2oDzNsvMGtymH6N6+Xg8+K3Z4j88lPw/eZPf/sdkv5vyehV3/hPCl8Lt0xC0HZfv/7yU/u8/dPffvmpr2EUA7f42jf5n9H8M7s++fzBgm+rfv7jXsj/UmZl9SgX33Jo8VtV/6/m908LEwJO8P1++3nxYybOn+ViVuKd6asJfsjGFsr6gx3/8vI7xJ4SatM/wXCGnv/4j4Wc+E3VVmG30P2q7xbQwV1SgFl4I07aBfx3Ro0GglTTJtCwb+tg/KdvqFqFi1//t//E+4/+G94jwSuqff0G418hjH/9AS1//bQwIOGqSeBTN19orKp+Kd0IIuzMFCJpC5r7E787CKpV83H+sUjKxa//Le2vTzKf6vHXZ/FIXpFP4/cz6rV9Dj7N+lkxKN+08WH5AgPwe8ghr3woDkRxAOEfSlHlEOa72RZtBqF9ESQQV2AZG5+0ob0+z8R+/fVXz23jL+UrTBOL1/rWInDBN3EWHz9CvUJYSeLuSwn8uFr89NvvPy3+z+Jf7XoSn3mosGC8eQNKKOknZQGzq5+LEnQUdC2Ejqc3fvv9zbqQTAkLMvRdEibgdTOMzgwE76bWRfYjTq4XHoAmhuYt6qrp5iqbdJ8W+3DxTV7IdH40V4e4artFAGpQBqD0R0jVhep8s2RZdYsWhmAbjh8WfQueXH/1GvcpYgHT3O1+Xci8CmtRlcP/zWI+F8HN0H/Q/N8C4fU+JNL81C64dxKfFsocj4vabdw6btw3HqH76pe5M3jbDonDJgE8vpRz2QWzqZ7J8WoeuAhaxn9z6Vy5wVzcIRIE7Tvv5xp3rpjGs3I2X8r3dsJtZlf4sBBAplGfBHM5+K+3kGrjqs+Dp/2gpDOlNy8Eb155xuBb8f8X3c6XHkex1eL/5xZpNgQrCNpWYI3tZrFVDM1+ddDcNc6OfG00Ya/y1OmZjN/7l3eMeofqL2WewGhrxv96Xfl069uaV/iDCgUQcLQnfRhT0EEz3WfIzyHcNHOyuF/K95rwAdrxCYDQQhAfYP7MYfvOcH76LmkMQWC+/t4fPEMEegP6CIb1ou69HIZcCEDguX4GpWrmtH1zM4x/MKfwI078+A9aLSB1GGaQ/gIKkcBEhHXj0zecfn36LvofNr62QfOWZ4vYw6xtngSgHGAWcI6eR9JB8HK71yYd6vn5SQSqUdTdrLsH8wZq+noTNODWJ9CtM0a+2hXUEKA/zt+vms53wVDDsILGgglR99C6zxSaA7SATQ6UAaIIzKgiKWHRh0Z5M8KTIIxaqA7E27eu9JXi8/abQuCZd3O1et84KzLvmRuA1+hyy/FH2DD+LEwgvWJe8eT795H2jdtMe4bOFsIf5Pj+9LVT+PRa7F+7icU73c//MAX9/O8NSs/yffljAHxexF1Xt58R5LXkvlfcGRGQV1nb9+r78RtCfISsPv6QiH8g/Krz58W/J9wfSLwlx+cF9gn9hM6Pjm/B9faBtuA/cvbH1fz0S6mB77gK2VcFjK7Zc+MTi96K4PsSWAmjBkTz4tei2M619AHL97MKQDd8KX+M9jnbYJEpozk62+oHFHh2AzDyX732rVjBR2UHeQdz9xiBT/PQNYvfgpfPZZ/nH15mEP2fzGpzRSrmmG7nEQ9mD8TKLgHPK7cPktkk8+8/zr9zWHawlIMZ6V4XPYPrO8C/VRNvXpfkVfMEoFnObqxnwV4HtrnFe0feqvn6KvSfMfu+aMaxIAlhjYImSKCJYel8pst7/fuxrLSweD5raPtPWEMMHLp/ZHl6/nDzT4sNmOVvf0ysN9XmRuGH/H91I3SfD034YRFAxu1cvKAbZ+vO2OG2MBlhHv6pLN/a4H+UxoL9x1Pt6vNcij+8gRz8hqMLLF3vUwjk+jYXzhxA2cOR+5d5Apr9/Nwy/4B74Ne3Td/+tuGBl7/9iVxvdfgrdM97Hf4XfvqTqv13gfH3lR9GugfmH28QAIJ/aqLXJPgaVP5rC/mPIqhv7PVuTsMIJkjlf1jwfQsTFibevmznzrBdaM/WED75oerrPeyjGtgBzhK69bMeBjMWw0uzgtn17JjA60wGvVHDPHti9p/ICoV9FhwY9rMLvvv2u4Wr58D5tHDudq9/H/ntBaaiC0PHfUvGt4kFLof4/LGd+zQEAhZkCK9foQU++/dnmTcCbezCVhpSAHjAMN6KQHHX90OGoGF3DbB16BIBIF1mzTAkjtFuSFMM8CgQ0nhAhhSJ+SBceS69evnmnLkbTWahZolmHIcgB74/hreCN21epf/9GWJvo9MTdF6V+u3FW6/gSnHV7tnXD48sMd+zEE9rvGWT00OOdJyZNBpx9bwEu+DJVJ+K1Hq4Npp1qzu/C87ayZHsy2gc94CohMjDteXjTuyYsSSUIo5rPT/h2caza6/eJts0n8h2IIFPHVNuv30A3ulzqb5WiYLmtz4rHrnDucd9F0g5ODthiBAqQudl50hC0caD39LJ8oKn6lERDdnq9SFt/eFoyGmm9buu8APMZDM66fUik7ObsOrMIvB312SNn2/9Xqr69ECWlh5rUtHWekqb+uhWPeYaB+nRmzfL1NOLFes1Vm4r4yBsZau7rMaWlzL+Vnm5td3jfHfhrus+lxGblxTOY8ubJTqOHavenVvJRr6mgXqlB7/wSBrZ0jgC7mq13AmIxWf6yHf6tjl02DXxzLwMLo12UupzT+o7aR0XtMl1YNdkVa6sZNRy9JHYrHCWEi5+Jj9Y/sh6xXFY92czI8PoLuijrlmHdtXgJm8fwJC30B1t7jtFfUz5NMvWrkYGdumaCn3XLDosrb7CQhu0DXYuWjSRLtmFVFiR2ag8fb1pEicJN8ALqY6wWz4VGoVuJyk85P1uVaLeDRMf4oF0nIqf+LOpps0pasVoAugJUU90MLpxbRnnbrvNdUqsWjIxQwltD/xe8Q7Oeq25G1wzc79IpNhUijNMieFsetcqvj00T2EZ8wZtu13G+toTzHqsimSJb5He7tBMxbqKrc+XmLxqFyxWqyKnqqRipn2hRlrr1pf+Uozcnk6JFDUiMk8kPDtMNyE12KVbE3ZDc0q7ix51mRk0SiRktPecXNDx3YU53riz7NkPKXBRvtvYaCSFLZ5b07benbLloCeEdcKCwSuDIK95jtqb1KQthcpozTqs8WuORM0dm6KQEFGrzeU7yyGjduOlVRPsrTN+VBMa49UzIi3x4RYkV9PalfEq1KbH0N7VPWPTSoVUK6VnB9floqi+FGUbkoGMLevlMbBUubY2SztJl0K5csNVS4SNITrIyIsoXRrUGCCP9s4dqAtv17qesrsjObT2dszbkYiM/JJra0smHJ683rBD527Y5Tnar49H58FRk1AlxjKyEJfcGZpV2E2bWQGgyBM+bieFvvGxpTnXqFBMrNjVlhxdmoLfRgpL4ewywFbLctWWq8Jhi0eMdnvX5Haylh/3ldROJ/lq+6mMUedcp8Urme82ylCUoltsQrfYn7zeBUrlmhF5ibcqHKZUIlRX6Pl6C6YTcW6IoXKKKt3DzNOQiRF5L8hteUngBJicyUUyvVDxwdhIq/hmdQ7RqMLlIu6pHXrckvEYJciWUDc8pdfDhFvKXtzuycvFxxtRci7XpF4W+Hnr8/XJlol++agFL8vvFh9MnlitWmrYCsfyMI5EN8T3gFbr6aiX1uR2W9peDQGmlOC0F+SNftVbxgwyyytSE7/oURQOEBW6zbTi23ENTjtsm2cIPz7OCB1Ndf/Y2VXoXUZveOR+o1baPTLDw6rViRMqCmWa2ohjAmmVd9G228QK2PAkEe1ZU4pPK+t6ltBUkjY+uitgCPdeLOe5Wd2dbSD4D4+aYArRLD8xy0unNXeiLgd6PONRUZNrkUNK8YSlbYmmh+mYsx6I/GYp8SDsL1Sz83Fqt64ph1ki672yOesMs1llNopgXMnn1X5AxfVE3JOLOxpqjUYmp47JNd8EWPU4bl0278LCTGF9Cu1hCTsA9cY8+GOiHxg4iXH+EB9Inr/cHhn0aOLR5LT1sLaflDUEQetR1Lw+HviTXXkeOR0T75Fv3KrOTxIe1HK9ZBwLby9+xGaBdr7y8nVbmJ38uO2V4xWa0cYcQrhNbM06q2vQEKeDIV19pV8ZXMZupaGqwDKqwepqrh+XxjqriRl7cZoxnlbytK6qO9m6YANBIyeCWE7gXnKbQ2636ObCrNVDJ1Sk0tLjFFA78SbLkmuqopc+SJpdyoo3PSjX3e6FLkyTOxmEtxa5lBPC0CQINROhx+BmltoZLeTHRGBOez6z0yi5tNgN9NE8dQ9B949SIJmHkH302ZI5OOcLfgp9gsV2AR1hun1pkl5Gr2pC8Mr1sWsNoXBikO0fnseHj5anp4PI7+2LwiPoZT1O6EQNw25HrOMBS7cPq8WJVa4RlyHowy3VZlszghUs9/H0hqINfpK904rnJtHn+CvVdJVFCjHAhRt9rzcmSCNT9R8MuzVZDVUey1gaitBZyasxOqwSafWgVuOh3y2ZcU/jEp6sGWE7bMVuKunqcJMeG7YnPWnk7rJodKPG5de9vnHXzZDcpN1+5ezTZL02Lpiuw0jDPcQcU+3A8/Z+PIyVlWhnTD7vDvZW4yrFMKGIyx6j9vrNvfnUeqXDVuCMduF+/5CWaTho5T6/YHmBdnctsqcy4aQ9kCT3foO9jF+K7aUiU9qo+KTlG0PPS51GmsBZjarMTu2ez4dTzAGw7nc7NIrWx613EVfDeMDB2kOP7BEBvbQ9L/Wks3E99R6r+lo4qMLRll2qd2RMVoH10LelSFnsg1W29TRZWEYX5N3XWElqk+N4H3JuHaDSiQPZ3Ypu57HJVcwwSaaEsVnWfp5Et8Lh9KGYuG7Lc5Y+CWG1dDZViWWHfH+4C0pWO5dsN0zd0EmIwuvZ1k8PaxdhcnyVcE2i4tJ5EKvw1I8rbv7Txy4Tl8vOzMWCLjHab1fHzLnWdRcvpa21GU9nnzLLu2/hGSGflJtqXjJBv6tXkmbU42M/qVLExPU+WJEyfcZL/RqpsScnmFphLkkJ3bkQ9GSP79hsd9uhfLgHFTnoQ2fxdDIlp4dWZYxx3Qac4ZG+zPmXQzbl/HU8rnxNyR1dyzqpsIXeHxlgZBZieHkfdTmqKVGJbwgb2/J3A1rihvqyImyu5GE5pCBwnGg/6PzGPBLFpq9ZrUXmPySsqz0tZGUmadcyT5M4rkT2sqc8zCi86FbLAoZkzdZXdl5qR5KJbvZ1nB+LDX5iKMc+x+VGPqSH0NjjSXWRiTAZDT4qJTpL1+4+qvPDTUczvd7jqi+ctsuVOTrnztmQhySAvVAiVy6P9lx3UcFJs3oet/h6nPKhOl94M8H28W3UJzXjkdDGxc5A9cNwy7fkUYj86Qh7z0etRJZrT5f7ieFwkrDkUfGr2D6YjmZlm0riPJ0/H71yILPb4VwbrpwfvXXFoAZqLUmmduqDtHZKJbxLWIlvN64X1KAuak7V4o1nyfolwXgyNSvpctBrY/SwWrevmxtq61owUbKaczdUYUyjFbUcuxEr9pEdNW64j2bwaJ2oBey2VIq1uZt6lG/GjkcDy7IFuzVuWJ4cFVlat9i58xvN3G4gSDbAxO7ZjmzTsIiQm8bLa8cSPXKZPxRuONSnkfXHAcQaxsbUTvL4lYUbE5ZM1eEYCrukoYSQcu0aZ2IxWSamRRda1KE3r8rHcL87p8JK3MJCG9dR2WP7R04KgoktTd2qTg1/ous9yh7q6UKc6s0pKk62VMLA8cO6P1B04dxHcqns9pK/bYF31ysR1qIh8cVo5XoV8ThiiC7duxUnYrSSP1bL0dDEA0FjUnan2B5cp5sorVj2cmY23PkqDfbgoFNq7IZje8cI+b55xMtRpKSBbu+Hs5a20UqdhiqiQ6d3/QefqX1ziWzX9tmIJiibH3C5pJabw8RKSheM/GRLPOlmvGDgFzm+QpnDXd/b4tq7Y4YSbxJAFqV7JbtHdWF8qdInwNDdclt6jJ3X1oqsW/ZBcb1B7kW1MzCclmy3wKyHMnLX7CpPaQOHNyN32UExu/xQbC6HdZx6E7Ota+tuNHdt3UVyNZbXY+s0a4BSo4LsyyTTCsVDzfi4rfADikUKNSD6yt15w3g952imaKj4MGJj0LzLYBd1aEDQsZM4GCvjfAVmNUYhhTgbxD+PloteqjNJmFaTpnRyHkdD18pdQJ52JlI7oYBn9t7oCY1Ns2iKWTU2ztXOXS73mUvsAA4CVVLtFLge0wk3DJCoPtj9FXcejDAscbRi7GBceXAo33m4EleCGSk36uzDesGjebhfsg0wDJRf9fKOAZ1yJS8Kdrp7a2Y4nEnb59QM3agXtpU2Xe7sN4Ax7MHOz6XSg/uhCCMrE2RzkpmKOhjbKOdgzl2Pu1S4Z8QZNvS83ZaGVHSX5Hbda8HQ2E4G7NIqD0yWq4NaRCv/HJh5njNN2wj7qfTko2iXyT4XnXOkRO31mm/vF/+kWuJKXXar6+F6Ik5SbmkQD4prpt6XcBAckzynTldBKijftekA3524KwmcVbPGTpbJMKfIoE3gCckVuQ0rZhmZ2GbNIMbdqsPJOPp3SgvZjKBtJm3312g35Ch+O7r2aishV0UJzzpri5oUnklhg61ZRe4GAs6mDaOZ57TFSycQ9nnEcTcYjaixvQTnduWqfiz2QEvdy+Qpt97uN2rASi5e6Rcv7o7bjrr0YC8II+7sHktvA/CpL/2kroF4kg6PwU7GulJZX3C4rJQV17xowDd3xjE50OxFC7EYxY3ER7UTqWCT3AXkJRE60t4gMrBXUtwBu8NW954vruSZz7tzdsQrZmkd7Tvv4PHNKfH4IW9KhOBWp8tYHuB4c7oebrBLpauwbXHjUJtueXDIVMskT4v2AWILDzhJSja2m+Ascyv6UZzIe3DPjqsAs69CfmE7UVjy1GZXqEqZSkvGa5SdfRYT9GobI32lsC7oH5bnNtg9CpkzCZKhw0JVrI+bhpEtX+5w8FgS8ri6PoT1nWT23CFGsz0BEmYN9PM48dlkcMdcvmGlb3M5y1vmSvfJ03SzVELerzNSCAnlFvjjRZoK2Oj3x3JAY3kp2HCav4xF1yIbLMxRbAkGVr6wSLjkGNiwuOJVOYRbOj93zV23s8CC82HIHYcJ2ZjEBa9FWfDHOPKoAx0oDpW11/LEtAxeow6+P7F7NmYf3HBMpV64N0QhXb0SIfG0cvg7E+rgJEblRqXqx53rp8rdnNf+SVmjE3/16xu/haZCeuI0DceBDLodcupTxTOJdr2lMIK4lr5xsJqgqbFgLZHGGkP6XsmSGovumyWf7g5m7mVrtGgk5FZzg4RxxVY+DnXIND0qxqc7YEwsDXAk2DBERQGhcN2JoENZPbRSxSDFpRIOdL9EWXAQE9zwvNbTus6BcI85d6IJFIJWExEQ9YZEcEbdGCgtLjfgkl9t5w7ICcITbLkC0z4r4fHuFMRprfFKvgKpv7cQLj+7N9V2BVat7gjTEEiSYkmTS9K4RKx0eTpxdxvTmDIl6bh+1BviXKMxdvPsLb8FnKj18tqtpQcIscjf3pH6fNU1DU1vmqKFp618p9PzNG1p/nQWpa3D0dtKElFLW6tWJ2i1k1GEKUz9yemJiKY2Zqx5h1XeDkvq6PerYZgER9god2E38ndcJ/vNTpxqIlK9NmfHXDflGNl4TXOMZCLx1RXFOcsHo/Shbbcqt9aV3do8HE4g2XdOiRjd2YtIiu0KdL1euUpiSOujhnpU5qpodmMsEYPDr5YlyjQ+llGhsUlvcA98ubmYAe40j1LKjjo0/joWLhHbSMmED6jnXWh8ADcBBBf7lCn3E25ngGCK3WX5MPacECZ1YaCK0+8N39vK8THl0jyWklzLdPkhcGs3REerLNTGPQe0XdehH/cHAS2ZozJtr1Qdre0ICQcDQk/LmeyNUxBF9GTR4xUKKBJLds5Ar8B0cJwrdzq5Uc4AXVx2iqoibbvZqlMUcmR2Za8qEI8RbDTqzg8YbmNw7pGRq+x0ylN7ZYmWol0LgvCrHd5ThVsF4SD4mmhgcUbfJxZVDMK/2gnUJLmXoygP8nSwp+uYegJFUsV155yNyU2AzdyPnacwPofjDnE0ik2Iy3m8KdeHanooK2rwOk3DYtiHr+jVEpOvrAsbJlqiXctx3dNAgMtV5gK0jonOKyJ0Sw1HAcetYH10rmbe6OQuHo99NFw5FDWOKFlYamG0bFXe9mEko8zVlvmRQzYicsiWY7U39u4GkEMuYlrpClFYtM3xqPIbMMV2nwZZ6wnM2sVCSh491yMZMryXp2CZjfs1UwiAQpHOj6lzFyy3RRBQ6oNIiXjCWBqPeRKrCrm7pFPpeKee6TW5o+7LLtu0XnW+bdJ7WqHZ3a59P9iQ9VEdL7qf7a5bm61N/sTluReg5OGBrRt86yoSRo2Uey6DeHkj89TDw/ZqLgPCfBjT4apjDDNu7nLMXuvdIGDxKQOFwAiEGOy5xFwCTSTsoNgdl8xdZg+4pPnxUvO21Q1tHlMfERy51aJbrG5FubJOp5LRHh2XpZ3RkKhSnuqqK7AI7XWgnrjN8ri/g9IviSTDiAQM6xKo3SYZjhHd4Gotbhx13dzthikCEYhNxaHq6Nt60/O2cdlV0AAtqyrujpJFGxGlXGPy/S12kDNyJx8gmYekA3JIMtoScq+n+2NA6cz2ZrTWqPKELRgZOCqNxXjAF8j78ap3FU5aPRAn/pY73sZS9WFydjRXYHmTCfRYYWL4aFMumiiDTCdMCeltLE+Y2FxzOHPVR8K+pjvWBsaeLFRy3Vs0ReuoKh1xxm6EjEBp1rBqUmcb7sLIHSz1dHtzQ180DZ0MeR85nrKTEpThQRvWZBu63dS4g2cgIJo2p2VOaRauGWHRX2JmuVKUIF3FpO6soVO2UhaTyVUH5Hajwkl4JRE1cUQQJ2TVU7+Or2RoTIPWn09WEug3tMMx5OZTGskQx6MtG6GVG4IxLj3Ja8TbBvTumcSJkbVbpNphQ63X2KlL5ZbiMqfKnFH29F7pL/fw1vVkM+6nMyP35UW1cooS+3TDHelct6bV8ZaAttthXi0v0ZO3pti8D7RkI8KyOfIEsbWjrTA89OiKOCtrxT0OOy/CQ8oRcepkhKWG+juRvA6ydRIbRrz4ioP1GMmqpIYueVyos3Dwbtx6etyQ5nBYFkg0gqNLod6yOd2xBrmHVUNYE2mQIdJSAJbAMcRVlgra4X5uwSDjIntwg1DRO8o4rPPIOgYXrPEd+YpgJh8wiKTsc2Ja7krKnMQGd7uHCDYRk/ekRaX4HbYZCbNNqmVhW8QkQ/hSrzc0X3mOzPA3ZgiUyoilZmlaPUH3ZzSO01hd8Yqu7dnNzUwp4NqHOmITUCT7ylCV5pRiK6h1ucLQ5giMrR/oHt1lezwj93dTQ2mVj0Kel5iDMh2pfAOCLbiHlOBx9zi44xTSmuu24zahqKo9bFypm0meDql/BnmUBoDK6V2wD+UYAhSVoZIxHM9pxRdi3KhM3zsxHQIiutAbPwKn1V1TE5QLOznLCnrZofckvKTJmsSa7UE8R6g7weYlbVyVQ/Ij1+LpcGBZ9q8vH17mwwhvRwr+54cZ59d+/8/eML6+KHw/o/R8sQ3c4POT1+d/Q6a/fXhp/ARK9Poetc376O2F5N+9Rf34355JmbePrycE3w8SvB6+6NxoPjv/kpRB33bN+LWt8ucZJbjj/fDZfCDbh98/vpuvuhg0L89zCT6ou69d9bVwmwzMz5JyPngEgvnIw9tl9PZS+cNL8TxjN798nfV7O9sC1SI+oZ+Il9//Lw1C20v5MAAA -->
