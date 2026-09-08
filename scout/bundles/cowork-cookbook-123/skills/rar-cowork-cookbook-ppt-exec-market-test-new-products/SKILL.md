---
name: "rar-cowork-cookbook-ppt-exec-market-test-new-products"
description: "Builds a read-only executive PowerPoint deck on market test new products from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_market_test_new_products", "rar_sha256": "30ae15f5f35f700c4ca7b58cde75a6914cc7845396947e2449d7c4cc863fe606", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
