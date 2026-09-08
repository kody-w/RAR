---
name: "rar-cowork-cookbook-product-launch-readiness-scorecard"
description: "Scores released products from a chosen release window on six setup checks (dimension groups, default order settings, active sales price, BOM for manufactured items, sales tax group, approval) and returns an Excel workboo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/product_launch_readiness_scorecard", "rar_sha256": "b6ec5f73504f1fa0a08c464884371381a0c5b87896afd3b6339348f6880b59d2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/product_launch_readiness_scorecard`. The original RAPP
agent is preserved byte-for-byte in `product_launch_readiness_scorecard_agent.py` and in the RCI capsule.

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

Released Product Launch Readiness Scorecard — Scores released products from a chosen release window on six setup checks (dimension groups, default order settings, active sales price, BOM for manufactured items, sales tax group, approval) and returns an Excel workboo

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
  Upstream entry : https://coworkcookbook.com/recipes/product-launch-readiness-scorecard
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
    },
    "rag_thresholds": {
      "description": "Optional score cutoffs for the RAG indicator (default <60 Red, 60-85 Amber, 85+ Green).",
      "type": "string"
    },
    "release_window": {
      "description": "Period for products released, e.g. last 6 months; use FY2017 for the USMF demo tenant.",
      "type": "string"
    },
    "teams_channel": {
      "description": "Optional target channel for posting the Adaptive Card summary, e.g. product-launch.",
      "type": "string"
    },
    "tenant_or_legal_entity": {
      "description": "D365 F&SCM tenant/legal entity to query, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `product_launch_readiness_scorecard_agent.py` and embedded as the fenced Python below (sha256 b6ec5f73504f1fa0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `product_launch_readiness_scorecard_agent.py` first:

```bash
python3 product_launch_readiness_scorecard_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 product_launch_readiness_scorecard_agent.py   # or on stdin
python3 product_launch_readiness_scorecard_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Released Product Launch Readiness Scorecard — Scores released products from a chosen release window on six setup checks (dimension groups, default order settings, active sales price, BOM for manufactured items, sales tax group, approval) and returns an Excel workboo

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
  Upstream entry : https://coworkcookbook.com/recipes/product-launch-readiness-scorecard
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/product_launch_readiness_scorecard',
    "version": '3.0.3',
    "display_name": 'Released Product Launch Readiness Scorecard',
    "description": 'Scores released products from a chosen release window on six setup checks (dimension groups, default order settings, active sales price, BOM for manufactured items, sales tax group, approval) and returns an Excel workboo',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'product-launch-readiness-scorecard',
        "upstream_url": 'https://coworkcookbook.com/recipes/product-launch-readiness-scorecard',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '06293f2b67612fb8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/product-launch-readiness-scorecard', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the Product designer or Item maintainer role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: Workbook with per-product readiness score and an Adaptive Card summary.'], 'confidence': 1.0, 'deliverable': 'Workbook with per-product readiness score and an Adaptive Card summary.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'rag_thresholds': 'Optional score cutoffs for the RAG indicator (default <60 Red, 60-85 Amber, 85+ Green).', 'release_window': 'Period for products released, e.g. last 6 months; use FY2017 for the USMF demo tenant.', 'teams_channel': 'Optional target channel for posting the Adaptive Card summary, e.g. product-launch.', 'tenant_or_legal_entity': 'D365 F&SCM tenant/legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Prevents launch-day surprises by catching the setup gaps that block sales orders, MRP runs, or warehouse picking while there is still time to fix them.', 'expected_output': 'Workbook with per-product readiness score and an Adaptive Card summary.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the Product designer or Item maintainer role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'List released products released in the last 6 months (for the USMF demo tenant, broaden to FY2017). For each product, score launch readiness on a 0-100 scale based on: dimension groups set, default order settings present, active sales price configured, BOM exists for manufactured items, sales tax group assigned, and item is approved. Produce an Excel workbook with one row per product and a column per check (1/0), a total score, and a RAG indicator (<60 Red, 60-85 Amber, 85+ Green). Also produce an Adaptive Card summarizing counts in each RAG bucket, ready to post in Teams. Do not modify any product setup.', 'steps': ['Paste the prompt in Cowork.', 'Review the workbook; assign owners to fix the Red and Amber items.', 'Post the Adaptive Card to the product-launch Teams channel.'], 'tenant_caveat': 'Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF. Cowork scored all 206 released products on 6 readiness checks (dimension groups, default order settings, active sales price, BOM for manufactured items, sales tax group, item approved). Score = checks passed / 6 x 100. Real results: Red 12 products (5.8%, score < 60), Amber 188 products (91.3%, score 60-84), Green 6 products (2.9%, score >= 85). Real workbook ProductReadiness-2026-05-23.xlsx with one row per product, per-check 1/0 columns, total score, and RAG indicator. Cowork also rendered a donut-chart visualization of the RAG distribution inline in the chat.', 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Scores newly released products on readiness for launch and surfaces the specific setup gaps blocking each one.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Scores released products from a chosen release window on six setup checks (dimension groups, default order settings, active sales price, BOM for manufactured items, sales tax group, approval) and returns an Excel workboo', 'example_request': 'Score launch readiness for products released in the last 6 months in USMF and give me the workbook and Teams card.', 'inputs': [{'description': 'Period for products released, e.g. last 6 months; use FY2017 for the USMF demo tenant.', 'name': 'release_window'}, {'description': 'D365 F&SCM tenant/legal entity to query, e.g. USMF.', 'name': 'tenant_or_legal_entity'}, {'description': 'Optional score cutoffs for the RAG indicator (default <60 Red, 60-85 Amber, 85+ Green).', 'name': 'rag_thresholds'}, {'description': 'Optional target channel for posting the Adaptive Card summary, e.g. product-launch.', 'name': 'teams_channel'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need launch readiness of recently released D365 F&SCM products scored and summarized before a product launch review, without changing any setup.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt in Cowork.', 'Review the workbook; assign owners to fix the Red and Amber items.', 'Post the Adaptive Card to the product-launch Teams channel.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ProductLaunchReadinessScorecard(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ProductLaunchReadinessScorecard'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'rag_thresholds': {'description': 'Optional score cutoffs for the RAG indicator (default <60 Red, 60-85 Amber, 85+ Green).', 'type': 'string'}, 'release_window': {'description': 'Period for products released, e.g. last 6 months; use FY2017 for the USMF demo tenant.', 'type': 'string'}, 'teams_channel': {'description': 'Optional target channel for posting the Adaptive Card summary, e.g. product-launch.', 'type': 'string'}, 'tenant_or_legal_entity': {'description': 'D365 F&SCM tenant/legal entity to query, e.g. USMF.', 'type': 'string'}},
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
    print(ProductLaunchReadinessScorecard().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
