---
name: "rar-cowork-cookbook-ppt-exec-market-test-new-products"
description: "Builds a read-only executive PowerPoint deck on market test new products from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_market_test_new_products", "rar_sha256": "30ae15f5f35f700c4ca7b58cde75a6914cc7845396947e2449d7c4cc863fe606", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_market_test_new_products`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_market_test_new_products_agent.py` and in the RCI capsule.

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

Market test new products Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on market test new products from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-market-test-new-products
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
    "comparison_period": {
      "description": "Prior period to trend current results against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to pull data from (e.g. USMF).",
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
    "output_filename": {
      "description": "Target .pptx filename, e.g. ppt-exec-market-test-new-products-2026-05-24.pptx.",
      "type": "string"
    },
    "review_context": {
      "description": "Meeting length and cadence the deck is sized for, e.g. 15-minute monthly review.",
      "type": "string"
    },
    "topic": {
      "description": "Subject of the deck, e.g. market test new products.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_market_test_new_products_agent.py` and embedded as the fenced Python below (sha256 30ae15f5f35f700c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_market_test_new_products_agent.py` first:

```bash
python3 ppt_exec_market_test_new_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_market_test_new_products_agent.py   # or on stdin
python3 ppt_exec_market_test_new_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Market test new products Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on market test new products from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-market-test-new-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_market_test_new_products',
    "version": '3.0.3',
    "display_name": 'Market test new products Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on market test new products from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-market-test-new-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-market-test-new-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bbc44c861d083751',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/market-test-new-products'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/ppt-exec-market-test-new-products', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to trend current results against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-market-test-new-products-2026-05-24.pptx.', 'review_context': 'Meeting length and cadence the deck is sized for, e.g. 15-minute monthly review.', 'topic': 'Subject of the deck, e.g. market test new products.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for market test new products reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on market test new products for a 15-minute monthly review. Produce 'ppt-exec-market-test-new-products-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads market test new products data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on market test new products from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on market test new products from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Subject of the deck, e.g. market test new products.', 'name': 'topic'}, {'description': 'Target .pptx filename, e.g. ppt-exec-market-test-new-products-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Meeting length and cadence the deck is sized for, e.g. 15-minute monthly review.', 'name': 'review_context'}, {'description': 'Prior period to trend current results against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX summarizing market test new products status from D365 F&SCM for a monthly or periodic review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecMarketTestNewProducts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMarketTestNewProducts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to trend current results against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-market-test-new-products-2026-05-24.pptx.', 'type': 'string'}, 'review_context': {'description': 'Meeting length and cadence the deck is sized for, e.g. 15-minute monthly review.', 'type': 'string'}, 'topic': {'description': 'Subject of the deck, e.g. market test new products.', 'type': 'string'}},
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
    print(PptExecMarketTestNewProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
