---
name: "rar-cowork-cookbook-d365-prospect-to-quote-estimate-and-quote-sales"
description: "Scopes the conversation to Dynamics 365 F&SCM prospect-to-quote work, specifically the Estimate and quote sales subdomain (8 L3 processes), answering against legal entity USMF via the D365 ERP plugin."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_prospect_to_quote_estimate_and_quote_sales", "rar_sha256": "eb60c52ca6631cca8e18a225dd1cd80534b8ca45e6ab16bbe36352352fed18bd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_prospect_to_quote_estimate_and_quote_sales`. The original RAPP
agent is preserved byte-for-byte in `d365_prospect_to_quote_estimate_and_quote_sales_agent.py` and in the RCI capsule.

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

D365 Estimate and quote sales Expert — Scopes the conversation to Dynamics 365 F&SCM prospect-to-quote work, specifically the Estimate and quote sales subdomain (8 L3 processes), answering against legal entity USMF via the D365 ERP plugin.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-prospect-to-quote-estimate-and-quote-sales
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_prospect_to_quote_estimate_and_quote_sales_agent.py` and embedded as the fenced Python below (sha256 eb60c52ca6631cca…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_prospect_to_quote_estimate_and_quote_sales_agent.py` first:

```bash
python3 d365_prospect_to_quote_estimate_and_quote_sales_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_prospect_to_quote_estimate_and_quote_sales_agent.py   # or on stdin
python3 d365_prospect_to_quote_estimate_and_quote_sales_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Estimate and quote sales Expert — Scopes the conversation to Dynamics 365 F&SCM prospect-to-quote work, specifically the Estimate and quote sales subdomain (8 L3 processes), answering against legal entity USMF via the D365 ERP plugin.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-prospect-to-quote-estimate-and-quote-sales
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_prospect_to_quote_estimate_and_quote_sales',
    "version": '3.0.3',
    "display_name": 'D365 Estimate and quote sales Expert',
    "description": 'Scopes the conversation to Dynamics 365 F&SCM prospect-to-quote work, specifically the Estimate and quote sales subdomain (8 L3 processes), answering against legal entity USMF via the D365 ERP plugin.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-prospect-to-quote-estimate-and-quote-sales',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-prospect-to-quote-estimate-and-quote-sales',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ea85c5510aa3d14a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'prospect-to-quote/d365-prospect-to-quote-estimate-and-quote-sales', 'uses_skills': {'custom': ['d365-prospect-to-quote-estimate-and-quote-sales'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Estimate and quote sales Expert** skill for this conversation. From now on, scope your help to the prospect to quote domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Scopes the conversation to Dynamics 365 F&SCM prospect-to-quote work, specifically the Estimate and quote sales subdomain (8 L3 processes), answering against legal entity USMF via the D365 ERP plugin.', 'example_request': 'Act as the D365 Estimate and quote sales expert and walk me through creating a sales quotation in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user needs guidance on D365 F&SCM estimate and quote sales processes, entities, or USMF conventions within prospect to quote.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365ProspectToQuoteEstimateAndQuoteSales(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ProspectToQuoteEstimateAndQuoteSales'
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
    print(D365ProspectToQuoteEstimateAndQuoteSales().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
