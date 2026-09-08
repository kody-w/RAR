---
name: "rar-cowork-cookbook-d365-concept-to-market-prepare-marketing-campaigns"
description: "Scopes the conversation to a Dynamics 365 F&SCM expert for the Prepare marketing campaigns subdomain of Concept to market (7 L3 processes), answering using documented entities, USMF conventions, and honest-degrade option"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_concept_to_market_prepare_marketing_campaigns", "rar_sha256": "6c2e2f508217be5908dc1d7cd885fae213aa58ce8f43a7535da6ab82ec3aa81d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_concept_to_market_prepare_marketing_campaigns`. The original RAPP
agent is preserved byte-for-byte in `d365_concept_to_market_prepare_marketing_campaigns_agent.py` and in the RCI capsule.

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

D365 Prepare marketing campaigns Expert — Scopes the conversation to a Dynamics 365 F&SCM expert for the Prepare marketing campaigns subdomain of Concept to market (7 L3 processes), answering using documented entities, USMF conventions, and honest-degrade option

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-concept-to-market-prepare-marketing-campaigns
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_concept_to_market_prepare_marketing_campaigns_agent.py` and embedded as the fenced Python below (sha256 6c2e2f508217be59…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_concept_to_market_prepare_marketing_campaigns_agent.py` first:

```bash
python3 d365_concept_to_market_prepare_marketing_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_concept_to_market_prepare_marketing_campaigns_agent.py   # or on stdin
python3 d365_concept_to_market_prepare_marketing_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Prepare marketing campaigns Expert — Scopes the conversation to a Dynamics 365 F&SCM expert for the Prepare marketing campaigns subdomain of Concept to market (7 L3 processes), answering using documented entities, USMF conventions, and honest-degrade option

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-concept-to-market-prepare-marketing-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_concept_to_market_prepare_marketing_campaigns',
    "version": '3.0.3',
    "display_name": 'D365 Prepare marketing campaigns Expert',
    "description": 'Scopes the conversation to a Dynamics 365 F&SCM expert for the Prepare marketing campaigns subdomain of Concept to market (7 L3 processes), answering using documented entities, USMF conventions, and honest-degrade option',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'd365-concept-to-market-prepare-marketing-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-concept-to-market-prepare-marketing-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a03981c0ddbf594c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'concept-to-market/d365-concept-to-market-prepare-marketing-campaigns', 'uses_skills': {'custom': ['d365-concept-to-market-prepare-marketing-campaigns'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Prepare marketing campaigns Expert** skill for this conversation. From now on, scope your help to the concept to market domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Scopes the conversation to a Dynamics 365 F&SCM expert for the Prepare marketing campaigns subdomain of Concept to market (7 L3 processes), answering using documented entities, USMF conventions, and honest-degrade option', 'example_request': 'Act as the D365 Prepare marketing campaigns expert and help me set up a campaign in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user needs D365 F&SCM guidance limited to Prepare marketing campaigns under Concept to market, via the Cowork D365 ERP plugin on legal entity USMF.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365ConceptToMarketPrepareMarketingCampaigns(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ConceptToMarketPrepareMarketingCampaigns'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(D365ConceptToMarketPrepareMarketingCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abPayJrmX2FOR0y5Gtva0II7bsRISIAA7QIhyhUuLakFtG9Iqqn/PinAdtW9dW93RfenweFzkJT55rs+z5sn9eub0zZRXr19ejOAk802TpLEEahmTubPVvk9r27wV35z4f+Zl2dNFbttk1f12/s3H9ReFRdNnGfTdC8vQD1rIjCN60BVO9OTWZPPnBk/ZE4ae/WMoMjZ+n8bK2kG+gJUzSzIq8cctQKFU4FZ6lQ30MRZOPOctHDiMKtndev6eerE2SwPoDaZB4pmkvscO3tHzw7ErKhyD9Q1qH98D5Wv76CahLT19NPPvTYFWQP8GfwZNzGo38+OhrR+qppNitbvHzZHeQbq5oMPwsrxwSx/mvf+DfRQnQTUb59++vn9Wwy/v3369c1LnBreeuOhXS/FzFx6qPUySPpqz+qrOVBY4mQhnFUM0PWTcOgJ6IcU3vJBMHtdvatBEryf/fu/3+5OFdY/fvqczV6fz2/TP73NHq5rcqeeTPOcwnHjJG6GjzM2uTtDPatA01bQg86sbiZ/fHzO/C4pL2Z/m569ey7yMQTNu89vMJLVI3qf336cwQB9fqva6fvHSUrx7sePSQ79++7H73JgiK7AayZhUOuPX17XL7Fw4PehcTD7YqjC6rVWBby4AFD47+ybPk/VX+JeLvnyHPwuL97P/lzyZM/foL7P3HSh3D8XC30AZ759vOZx9u61RpXDVHBgEN/9+M/EehHwbklcN/8luT89BUcAZlL17uUSmJ5TCH6ezV+2fZP5z5ctYML8FUvg8K/LfXPUP5P9iOzfiU5iWATfYvmn4v5swvxvs5/+qW3/asL7WfD5jQdJDGHDcRPwafbrI0V++sH/fvOHn3+Dov9TMUbeVt5DwpfUyeIAVvOXLz/9UD9u//DzTz+0Bcxi4KRf2ir5M5l/5tfHOn/w4GvUuz/Ohesfs1uW3yFUfa2h2a958b+q3z7OTk4S+9/v159mv6/E6TOfTUZ8XfTpgt9VYw11/Z0ff3z7DSJRBq1pvcdjiB//9m8zKfaqvM6DZgYhuW1mMMBNnIJJeTOK61n8BOkKTBgdQ8e+xsH8nyI8aQxh9pf/4z3Q/4P3Qn/Ehxj3xXuC3Jcm//JEX1g2D5z78g24v3wD7l8+zky4Ul7FYZw5yUxnVfVz5oQQcCct4MwaVB1ELndowAdY4B+mLzOI87/89cW+POR+LIZfHjgeP7FRX4kTLtZtAj5OHrAikL3s9SDdgR54LVwyyT2oXxAnEzFAtfKkg7g6eau+xUky82OIPJD2hods6NFPk7BffvnFderoc/YEcmL25MMagQO+qTP78AFqHSRxGDWfM+BF+eyHX3/7YfZ/Z/9q1kP4tIYKCeYVL6jhzlDkGay/B5vBUMLgQ3B5xOvX317uhmIySOAwunEQvxgZ5u8N+F99b2zZDzhJzVwAfQ79nRZ59aDcuPk4E4PZN33hotOjiT+ivG5mPihA5oPMG6BUB5rzzZNZ3swmwq+D4T0kXfBY9Re3ch4qphAInOaXmbRSIVvlyUTe1Yu94OQ8i6H7v2XG8z4UUv1Qz7ivIj7O5CljZzD+ThFVzmuNwHnGBbLU1+mPjiMD98/ZRNNgctWjfJ7ugYOgZ7xXSD9MMYddQAqxwq+/rv0Y40ycaj64tfqc1a/SmHoUOBFSBVw0bGN/Ioz/eKVUHeVt4j/8B55tzSsK/isqjxycmoV/2e8Iz9boc4uj2GL2/3NjNbmD3Wx0YcOaAj8TZFO3n2Gaes0pnM/2FPY0L4NgSX7vc75i2VdI/5wlMcy5aviP58hHcF9jnjDZVlBVndUf8qHhMEyT3EfiT4lcVVPJOJ+zr9wBlZ89gBJ6HKIErKLJQV8XnJ5+1TSCUDBdf+8jHolS+ZP5MLlnResmMPECAHzX8W5Qq2oq3leYYRWAKQz3KPaiP1g1uRYmG5Q/g0rEsBwhv3z8hufPp19V/8PEZ7s0TXm0ki2s3eohAOoBJgWnwNzjBkKY0zxbe2jnp4cQaEYKswHa7sJ8g5Y+b4IKlG1cx80U6adfQQFx+8P0+2npdHdKQm9KC1gWRQu9+yikKWXSKfrxhCWwrtI4g80BdMrLCQ+BTjqhAkTdV/f6lPi4/TIIPKpvYrWvEydDpjlTozALoOrwzvB78DD/LE2gvCn7n177+0z7ttokewLQGuYwXPHr02dH8fHZFDy7jtlXuZ/+Ye/07q9trx40f/xjAnyaRU1T1J8Q5EnNX5n5I4Qv5Klr/WDpDy/i/NDkH56l/OFFnB++ocCHbyjwh5WeTvg0+2va/kHEq1o+zbCP6Ed0enR4ZdvrA52z+sDZHxbT08+ZDr7DLVwe4lEz0UEywLbgGzd+HQIJMqxAOA1+cmU9UewdsvqDHGBcPme/T/+p/CD3ZOGUrnX+O1h4NAmwFJ5h/MZh8FHWwLX9qe0MwcdptzapX4O3T1mbJO/fIOCCv77lm2grnVK+nvaNsLgmkI7B4+qBIH0zff3jnlp5fHGSjzMeQLRK6t+n5YtsJrL9XfU8bYa2TqzxfuZDT9UTOUKbp8WnynNqmMowiyfbmqGYjHnuDqd+8luz+Y/aWJDDJ/Dz808Tnb1/QQT8DTcI72ffen246mv3Na0AshZubH+a9hmTGx5Tpi9wDvz1bdK3vye44O3nf9ALKvbAHYjek6zvSn4fmj/2J5MJUHTz3E7/+gZd7kAfOC+nvxpcOByW6Yd6Im0EpilcHF4/Ewo++x9ofV8S68iBjRYUSXk4wAMSZXCMdgG5RBnfw3za8xmGDByAY4TjkIwHmGBBODRJkL5DOS6DAw8+YDAfynsm6pepV4knLScVp0KGuQ6+P4a3/Jd5T3Mm333rtCc3vKz89c2lFnDkdlGL7POzQpaYi+C0q0eH+Rmd9/1dVo5xpTv+AacL85Db2XXNbhy54v11flIXe0JMXA3T3Z2H5mS4USJ+yWb0Tg1keifGe6/AvfiqtcxqtwN0Sysjg2wcizH7jlGqYk3ODz6d7S97WtBb51w2/M7I9eGGpksjvy/AZV503ApBgn2lsJ1pcole7Y4iOtf35NG2lBsm3LS8OKeo2fqbSDia9+UJUa4Ns79cvBYlxzNxsA573dfbQqAEkBjbvb8rD/sVJZek3elnJjiZN3AqSrHXL9e7Ll23530MK8xZI/mo1fKQF6eVea8GCpUitSf8zMVI9xRxIdas7gY16npRRBunOB8M8Ybm9JZbSKfzmcRBoJ5jRDFOipqliKpvz+Tohv3FPlj6pZJlb401xHZDsIFhn5XykuG3MhmFQd/Tt0u/LfWBGOlRID0qiU7HcRXxYj1w5Dw7oNRFFajGi51qhc2Z/ZFdjMwGuYmKbKqaMYq7XgvE1PH8AojZSRAobGtjVrCnEsuXiYEtsyRa3Ya1ZZOR4Ac2n5HGwcpPYbk2sBtgU6Ct1vHScLTVIkNASfCwOpmdvGMMWltvZHYdJGiGpNzdLMFo92e1ss62ZYH9uowWir5OhDL1koW01p1BV0oSq3VazOsrlse6PO7CzVxGWG7L55x9l3RaU08OTIbqrHNOdh4SOUGZE25UCBmrhsavmNsRvR7EuI4wVT5uKmfBW4m3HnZG5OWE0qwXW/VQpJerpynScK0F0t8ZthYQx+3R4nIHZbVFfhYCBj0PVLgwTnZfKA3YJXwBH9sonju9FeqXS3vxLawk8kyMiIqUD+y5WruyVRlSyJwuK0TYnJnj2j9eEMWmRgPp9zTmLfaMnRnpJd4jbIaRPCMYvbI4S1FoBWRqS2kzx2RzYVLUQRyVMd8rBiyfLovmWTrwu/Ia7xYIb6DqtW7QMsNwK0mJM+a0SIv6XZDqic1KyDrqeLtQJGDHR2TZI+T1uh2bSuqWobVSimGJZFtqc/c2hRWni3Qwq7vsiIrJsvQhP8UUercdarxH/el435NWeyr1i9oLhtgHlbMOcNZOSXHO3TB3NzAHbNxdbueN0yhbxueGAVD1MhUGoxCP942Q710OK27rhiv7RczErLivPJXt1h7BjrmwW+ywkXXdwWHOG/eSyDfynqfLWMe2y/XRhoVQyKbVnKRzubr0VBiLEFIWq4KkwtNtqZV4kBt8xQmNlQkKYVJZejN19+CeuGbusd4xXp5PNaUs1eV4KlPFFXHPRBruklDNYW7ubfW8Pq58fWWrLhc7skG3/GZFiZZ+jzwBRJfxMufai9GP66U5bKqMp2tLE5cYm661/lSk2wrbApDLeeytQ3HYXU7Znc6ue8aESVB0lGXIsnkOVBIYTCqx92Bb5Cd8ia3Ksr+mEMlzYQ+bW4bBKgGm7u12NLSWRwm1Na4qmYs2qlSGT7ltGdgadyo6dd1hqMOvRHk3jHMezHl5bl9O66omB3dBjSp+6eJUpG3u4C3qq2v4NCpu/CJSFvY12h2jw/bUOjF22ArWebPae1WggI5WipDoyk62JSpTeBKcqHKwaGkMGZTXUFq9jl6GBeS59inYCVvgeDfp+/U2Hq1TwIpmMjTOcr7Vu0vgIaeeCfiqIFxW7/iwk1dej/CcFSSnkuJu6j5Tfax37yyVBhjf1pdYuZXDNmaoRF5wxzi8H/3toj2r96IWb5fU9DZ7ZE1uhGYjouIyz3eQbyCU9nuXWNY46RKbOMT8PVsUF0PDZRZNzUO8iA8bwzZDT8TOXOli7bnqjVgkWYM8Xgap2Jz58sIWh6277LNatZP4cvbZ/dpbIGaZ0GtXdAEWdnnAHu3bBo8YvDkgK7q1Vo210HjMayF6+w01xg63yeJB2hOoH3TjbT4Hbh1tRH1c8WuIb6iaL0rUuN7mo76TifoIyvtwy49M2bq02t+EXm43W9e88np6DNQRpQmElrd3T7e7hCQQ5LDVcVK/kL7GZwlgDk28EhQmthbhfgEM7JoP15xqT0aEnzxXBCOihb6G4ligueEqU4C6pYc+MHtyKWXZciOZpySswiznWHzYBL3DIFpZ3pDdwohLnNa5jWGKxyFCDS7Jxl7SkW0w7vktZo4tNeDbrBLioSi5vejpeuaYnnXYysNe9qSuvZmpg91wMFjsMsvTgLgubrHI3m17K6UZKNKNsDtTtq3OOcg0MFoL/ADJB43meevm2p1sL6KT7xgWGPl+s9nVtJN1WGM2utxzWiNFQU53+Shs1xegw7SEGTYs9kp2a1F9aVGnS5ka7BxaV+VEUd4Xh5UWHqJVD6i+Z/eiscYjvvcWcCtnlLfVsZL2jdAatTaGyl4Ii0iXyGZgzsoyyS3xdNqus8sx9YmtaG5DhlfvNZFHdnJLF35nhtshHez95coq7ZjnPbqHcXa3J6Gy20ETDFgReNU7yNnxhog/UTKv35NrNggMAbD5cbdjVuo6TEUiXXi0tNhqgjq4jnF0xAi0W83JSe9s0w6elgCuw3MuYxWXnaBjSh9K2tbcODjaO1arcO1dB4WSaAemo3zhAK47je4zq7vhVylxg0KCzKRsyZ201E+8kJSLqx8mN78z9tha2LBiFK/7OrYoVqt26Z6nBRuXfVouTAYu4F1KocoxhAwbnTXLnFkkPCTvSq3x2DZrp1sft9gSXJINPs8wQasXtSyPAO+DjmPbBNXCU3++LgkbUNmdwOv5qISbZKGM/hBs1hfKpxnc17z6vJAFTEurM6GtcuB1Cn8pCXNYHyNJyG7L48CJ6knNBSZYOn2cXJ16TeW3O1ed1gfj5lSb+xDUPJnv9p2zlUKDqmolGFRxjYfFHUcPZEWqxeVMoDdtUUlyLY/RsOGju8BpzD2OGMHsTFsnh5PXw1a0iyTcUficPGh6NG4X90Q0xVWwCfderlKpPSSOo1HXrNuQ/k3UbDdi73eQ8D1Y2ah23sZ8qUjChV2e/BN/1uaaSPqIteNToS83niFyyaB7LE4eefsynPr2LK1w62LdlgN2tvkD3hv1ASsqf62tLKEIfcYlWwQWPiusRKrZ7OJVRK7acH/R+Bpd82djVxw0pBr3GnemynXjnrGMX65KZhcj7ZWib9l2l15x88QU+M0Nx1pZt1srbcfNWazs+NTFu6vnlLoYSwunj7Q2PNhb99hGO6w+ewK9Oy+6G2I6kDs67GZdo/KUnSXPOvGwEyxwy6nWhxNDG5FMGVjMOvatTpo02dEmf8TK6wk2AhwVxLf0XqBcY++pQ69cqR6dZ2S235iNfGcbAzle+QDlihatecNl2DDD4sQ2myOEsOZqAdUUC1v3bfqq9zeWKoRQ0bVog1u6tzsUXrW2vKOprmD/RHV2Wrqo0DtSgQ85IfuRutqDZdRpV5PeXHJqgUjtaj4vIvs+6Jtybi/c7WjaQpbwYHtY00f05hy5eljurfnlJhII2JJKi5vHfMWttfI+WnoDXZrMvVV/tMdVd5CjGMmYC6nZxzpd3UWbpU1PMHUVu5wsjB6Pa7M+ZRSuePuFJPKnWhGoLvAdZG3s7hRnwXKwatnd4bpyJbk66O9j2IjE0sRxxvV6OWP9XZEcDhc+wT2W1/hSO13PexPW+MGUV528VOVIPfYUJHsnVyiFD5CuxaXjQeLUit0NPn5OeB4ITonuiBas6CpmuOBmimXO0fhpcxp27Tq60R44u2N0ke6YIW6l5NK7mJO7trb0riEw9bm581bEqojTzTqEaGjcXMGzmk1nREQfHdtapsv7adQJxqI6DbEFtV+frU7EuYUIi3uNnb1lumMVSsouZHJQTXfnbzM9HcZgHm05Dp9z6iZMwjbjRSq18G14v6qo3Zsha6yG3nVv+crbSIjZDL2wQwCR+LG6p1LVv/E27JVV2LEodovtrqeDf7FpuwF3amnTahcUYCPj7HgkRFW9a2oOeI3hqSK06JImkc7f3FR/LDAz6NYx7YSI2sI6d7tKuUv+xe/xWKoaXyqR5HLtFaqwWuj6c2sGl+zIldvTsgNur5r08bwlIOYdLfJuyP3KR5x+U9I4E0i8ornMDi0y2Pe4NF+g7EEwj0fZdhWUrYSTZLgZaam8ewk2uE6t2lEn4b4BnWtrf7xeLEKZ15V0RtFlUm/cEG/cS3YNnTaAocbWSH9XVo6OlwgijIzsE3Y/nM7rZAnEyHEjLDIuh8aypLoTPULiXH5UDp3JcTdkzm1ZFxTYPg1rbs7vj3J1EILjPQiBYY/yduyvdCH1rWwxHYqWlAd52SaSwEWP28w2GqXStli+5uhD7ZPhmCp3z7C31jZgVEovlMPmVJe+zePITlN3drxKAqLyg4sPGvvKL7u7xdfqwS1qSQHMfLe5SaTG8iO56eaU2VGZ78LN1WidfE9WCNLDtnAXshyaw1IxujNN1R64o2CXF7uck1J2LaV8sVxSC4quaXXYpKtQaw5nS6QGe7gNxvrcpJXVZmSQzo8KzhihpRAl12/5dgx0ih6GwO5jiVdpp7osSS9YiW1SLDR5DPU9mupxPOzmgGeZzBOkvTScBl6TFkFBnZqA4LjUOxtYB+QQblZ8QhAd5SSHjqhquyvZbLkwW2gNsYcs2i9vasYTFwekS5EZI4MnkBOSLZiLlJXbrubu1XzFEFg92pYqq5fDeiRAHl7uq11550hUOiD8ne6rfd0jKLUpT/J2Lab0nAOFF8asBFHnWjobejUKZ5namN4yukuQ5VJm7upJEnSAjrLrIAC4WQrpWs/A3KUotrmRndWmglnAZmFzwrBdFVdqPsgKcyj3HR/t987oKTefXtL4IqGDSnbtKvW2ZDUqdbNpPczuHN408Xjs9INaNQeQDJtNjp4COMrUpU6naimQoBFCvAsAeckxM7wfxC2CBmiBSWW5u0qAB32fnDG9O8ox4/dXh85YHiy4gqaoFgZleQEYccVdrG5tnymIqkzATpe8Oa2qy+JEKKpbFJg3MPi5W4/jubRL+si7iGwTHTv20aXpTuCMKof5EiG9EjFXRgm7NIzdF9XyUGGdhPkUGjeRFlP52Y5tLTw6DpcRTJJdOXcNymWpbviT59DmMXSbLPAJ1ABy00k07d39/rQ975bz9a67ieHpsi+FdaLe2lymlrhkofjq6Cfq6Iz0UTD7npEgPaxw+xreCHKIDbVN7ZERyR6A4ij2SMgZ1P46dndRks/7m38NiAbXvJIeFd2XaU8yuKXi2+56xIK13ra35obN62NON2Hqtzm9WnBlcZW6ZUm3csAua1ozYUHyl/2lXXn6MTkecB9nt3Su0Xnaz+eZOGY7wrno80D1AAVG4MjdHlmV2VJZ3Whwb0eT1pbZHiohW9GhAeXuHI8WYTbNXqrdYUQrRz65Z6Xr91myczml8+/jbr0EVp9WR7jT71N1Ptobrgsoc9f0VJQi/lFNQY446M30SA7Q85496iF+2YoGwoPR5SqaZH3e3feX7byVhKOgHjTscD+3dBt1e4Mou0qr6/39Ki9IkjdbJSn0iCJqRGkgshsNSbexue+oDYZTzVVh9gTYZofufEO4Pluq6eksp6EU14zmaNu88xg2q9i7cwAZPdIwP1uu9Y8wP5AQL9cDmjYF3eNki4FsT9CEj2ZNdIjw4x2oB1A1rYsgygHWIRJu9sFR6kbv2MugsseK6+9MrMmBuUYPmXM9MCggzHHIOxuRuFsDltyAQzy5khKzbo2eddLQ2936m3tutd08lwgM11WPylgJ3PiVeAi8K8reLGWuQXggrMw7sCztp9cx2C1bNCUCfEg3R8Y4CsQI+y6uUg8b32/mtUyJPqvT6vqowt42ht1SpfIB5usEijGUSzidlfblWLoVhng5jVg88JddNyxbJK1Rl8EWqt04YL7h5mqq3fepNY4lltm7zlNZur/aRWUtDFdCSJ/3l+PBQsGCRPaD7F+qU8WpC7cSCWJOeO5pdGViMVSrTkDQkcdboecYDah+ycPdg1XOo6UANwqH+a5qzfMpIGrj2Fwr7kDfyluksUphqTnhcuuaO57jMh5YuJVHimXLc/oJHYnqFIqauvUM5Ob1KcrDqj1uzTuz1xlW0PCagDvYo7JwxCUIcAXfgjWOuN18PBcatdrMWyvwKN0l0OvgnRQq9A/8hhqJw2JPHecXVpTpuaklhNDwCuyewYZBcIpMt+RywejZ3b3xxbimznNBOy1RY4cK4UlyEGRuoZrvhwtkuU/NYztSxHitAcL64rIRThv+zrLs3/729v5tOot6nSj9N955mf7+/z921PA8Mfh6iP04uwGO/+mx1qf/jpI/v3+rvBiq+DxyqZM2fB1V/N2By4e/foo5yRuer5p8PU17Htc1Tji9tPkWZ35bN9Xwpc6T9vVSpzu9xQDq+svrHYdvB1RfHq/9wMu8iUA1nVP9vcVv06tX0wk28GOnAa/L8HUs9f7Nf72Y8WXyF6iKyfjXySi0mfiIfiTefvt/hYRmg34rAAA= -->
