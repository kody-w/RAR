---
name: "rar-cowork-cookbook-product-launch-readiness-scorecard"
description: "Scores released products from a chosen release window on six setup checks (dimension groups, default order settings, active sales price, BOM for manufactured items, sales tax group, approval) and returns an Excel workboo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/product_launch_readiness_scorecard", "rar_sha256": "b6ec5f73504f1fa0a08c464884371381a0c5b87896afd3b6339348f6880b59d2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
