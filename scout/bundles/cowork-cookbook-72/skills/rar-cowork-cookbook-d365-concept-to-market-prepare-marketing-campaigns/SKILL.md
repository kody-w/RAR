---
name: "rar-cowork-cookbook-d365-concept-to-market-prepare-marketing-campaigns"
description: "Scopes the conversation to a Dynamics 365 F&SCM expert for the Prepare marketing campaigns subdomain of Concept to market (7 L3 processes), answering using documented entities, USMF conventions, and honest-degrade option"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_concept_to_market_prepare_marketing_campaigns", "rar_sha256": "6c2e2f508217be5908dc1d7cd885fae213aa58ce8f43a7535da6ab82ec3aa81d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1: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 -->
