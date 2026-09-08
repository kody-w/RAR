---
name: "rar-cowork-cookbook-d365-prospect-to-quote-estimate-and-quote-sales"
description: "Scopes the conversation to Dynamics 365 F&SCM prospect-to-quote work, specifically the Estimate and quote sales subdomain (8 L3 processes), answering against legal entity USMF via the D365 ERP plugin."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_prospect_to_quote_estimate_and_quote_sales", "rar_sha256": "eb60c52ca6631cca8e18a225dd1cd80534b8ca45e6ab16bbe36352352fed18bd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
