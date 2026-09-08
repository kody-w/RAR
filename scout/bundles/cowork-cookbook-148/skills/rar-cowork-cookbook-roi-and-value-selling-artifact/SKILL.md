---
name: "rar-cowork-cookbook-roi-and-value-selling-artifact"
description: "Builds an executive business value story for a named customer and product \u2014 strategic context, 9 use cases, 2x2 prioritization, pain\u2192outcome map, KPIs, transparent ROI model, and call to action \u2014 as a 5-7 slide deck and"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/roi_and_value_selling_artifact", "rar_sha256": "9de1fc3f83470e45fb02ca4d71814d88a94bee60d50c16047cfd13bcfb9741c8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/roi_and_value_selling_artifact`. The original RAPP
agent is preserved byte-for-byte in `roi_and_value_selling_artifact_agent.py` and in the RCI capsule.

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

ROI and value selling artifact — Builds an executive business value story for a named customer and product — strategic context, 9 use cases, 2x2 prioritization, pain→outcome map, KPIs, transparent ROI model, and call to action — as a 5-7 slide deck and

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
  Upstream entry : https://coworkcookbook.com/recipes/roi-and-value-selling-artifact
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
    "customer_and_product": {
      "description": "Customer name, their website, and the product being positioned, plus three use case categories.",
      "type": "string"
    },
    "industry_and_personas": {
      "description": "Customer industry and the primary persona(s) the story targets.",
      "type": "string"
    },
    "kpis_and_population": {
      "description": "Confirmed KPIs and the impacted user population.",
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
    "roi_assumptions": {
      "description": "Fully loaded hourly cost, volume metric, realization factor (default 0.75), license type, and engagement program.",
      "type": "string"
    },
    "strategic_priorities": {
      "description": "Known strategic priorities or pain points; left blank, they are researched or labeled as hypotheses.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `roi_and_value_selling_artifact_agent.py` and embedded as the fenced Python below (sha256 9de1fc3f83470e45…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `roi_and_value_selling_artifact_agent.py` first:

```bash
python3 roi_and_value_selling_artifact_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 roi_and_value_selling_artifact_agent.py   # or on stdin
python3 roi_and_value_selling_artifact_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
ROI and value selling artifact — Builds an executive business value story for a named customer and product — strategic context, 9 use cases, 2x2 prioritization, pain→outcome map, KPIs, transparent ROI model, and call to action — as a 5-7 slide deck and

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
  Upstream entry : https://coworkcookbook.com/recipes/roi-and-value-selling-artifact
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/roi_and_value_selling_artifact',
    "version": '3.0.3',
    "display_name": 'ROI and value selling artifact',
    "description": 'Builds an executive business value story for a named customer and product — strategic context, 9 use cases, 2x2 prioritization, pain→outcome map, KPIs, transparent ROI model, and call to action — as a 5-7 slide deck and',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'advanced', 'read_only'],
    "category": 'general',
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
        "upstream_slug": 'roi-and-value-selling-artifact',
        "upstream_url": 'https://coworkcookbook.com/recipes/roi-and-value-selling-artifact',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '75015fd71b3ec292',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/nurture-opportunities-and-finalize-the-sale'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/roi-and-value-selling-artifact', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Output matches: A 5-7 slide PowerPoint executive deck and an interactive HTML executive microsite - strategic context, 9 use cases, prioritization matrix, pain → outcome map, KPIs, transparent ROI model, and a workshop → pilot → scale call to action.'], 'confidence': 1.0, 'deliverable': 'A 5-7 slide PowerPoint executive deck and an interactive HTML executive microsite - strategic context, 9 use cases, prioritization matrix, pain → outcome map, KPIs, transparent ROI model, and a workshop → pilot → scale call to action.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'customer_and_product': 'Customer name, their website, and the product being positioned, plus three use case categories.', 'industry_and_personas': 'Customer industry and the primary persona(s) the story targets.', 'kpis_and_population': 'Confirmed KPIs and the impacted user population.', 'roi_assumptions': 'Fully loaded hourly cost, volume metric, realization factor (default 0.75), license type, and engagement program.', 'strategic_priorities': 'Known strategic priorities or pain points; left blank, they are researched or labeled as hypotheses.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Build an executive-level business value story for a customer - use cases, ROI model, and call to action - delivered as a deck and microsite. A 5-7 slide PowerPoint executive deck and an interactive HTML executive microsite - strategic context, 9 use cases, prioritization matrix, pain → outcome map, KPIs, transparent ROI model, and a workshop → pilot → scale call to action.', 'expected_output': 'A 5-7 slide PowerPoint executive deck and an interactive HTML executive microsite - strategic context, 9 use cases, prioritization matrix, pain → outcome map, KPIs, transparent ROI model, and a workshop → pilot → scale call to action.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': 'I need to build an executive-level business value story for [Customer Name] that positions [Product] as the right solution to their most pressing business priorities - delivered as a 5-7 slide PowerPoint and an interactive HTML executive microsite. Before you start, ask me these inputs one at a time: Customer website, industry, primary persona(s), known strategic priorities or pain points, confirmed KPIs, impacted user population, fully loaded hourly cost, volume metric, and realization factor (default 0.75 if unknown).\n\nIf any inputs are missing, generate clearly labeled hypotheses - "Hypothesis - validate with customer" - and proceed.\n\nWork through the following seven sections:\n\nCustomer Strategic Context: Pull the top 3 strategic priorities from the customer\'s website, public filings, or earnings calls. Include a one-line priority summary, one direct quote per priority, and the source URL. Skip if already provided.\n\n[Product] Use Cases: Generate 9 high-value use cases aligned to the customer\'s strategy, distributed across [Use Case Category 1], [Use Case Category 2], and [Use Case Category 3]. Present in a table: Category, Use Case Name, Customer-Specific Description, Business Outcome, Primary Metric Impacted, and Strategic Alignment.\n\nPrioritization View: Place all 9 use cases on a 2x2 matrix: Ease of Implementation (x-axis) vs. Business Impact (y-axis). Recommend 2-3 for a pilot and explain why.\n\nPain → Outcome → Solution Map: Build an executive table mapping: Pain/Constraint, Desired Business Outcome, and [Product] Capability that addresses it. Use customer language throughout - not vendor marketing language.\n\nKPIs: If already provided, use them. If not, propose 2-3 per outcome. For each include: Definition, baseline assumption (labeled), and the discovery question needed to validate it with the customer.\n\nROI Model: Build a transparent value model from the inputs collected: time/cost saved per user, annualized value, realization factor applied, estimated investment ([License Type] + pilot services, stated as assumptions), ROI %, and break-even timing. Design so assumptions are editable and changes visually update the ROI and break-even output.\n\nCall to Action: Close with a clear progression: Executive Alignment Workshop → Pilot Engagement (1-3 priority use cases with a measurement plan) → Scale via [Engagement Program].\n\nCite all public sources with quotes and URLs. Ensure all visuals are explicitly described so they can be recreated.', 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A 5-7 slide PowerPoint executive deck and an interactive HTML executive microsite - strategic context, 9 use cases, prioritization matrix, pain → outcome map, KPIs, transparent ROI model, and a workshop → pilot → scale call to action.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds an executive business value story for a named customer and product — strategic context, 9 use cases, 2x2 prioritization, pain→outcome map, KPIs, transparent ROI model, and call to action — as a 5-7 slide deck and', 'example_request': 'Build an ROI and value selling deck and microsite for Contoso positioning Copilot to their exec team.', 'inputs': [{'description': 'Customer name, their website, and the product being positioned, plus three use case categories.', 'name': 'customer_and_product'}, {'description': 'Customer industry and the primary persona(s) the story targets.', 'name': 'industry_and_personas'}, {'description': 'Known strategic priorities or pain points; left blank, they are researched or labeled as hypotheses.', 'name': 'strategic_priorities'}, {'description': 'Confirmed KPIs and the impacted user population.', 'name': 'kpis_and_population'}, {'description': 'Fully loaded hourly cost, volume metric, realization factor (default 0.75), license type, and engagement program.', 'name': 'roi_assumptions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when preparing an ROI or value-selling artifact for a specific customer and product ahead of an executive briefing, pilot pitch, or business case review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class RoiAndValueSellingArtifact(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'RoiAndValueSellingArtifact'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'customer_and_product': {'description': 'Customer name, their website, and the product being positioned, plus three use case categories.', 'type': 'string'}, 'industry_and_personas': {'description': 'Customer industry and the primary persona(s) the story targets.', 'type': 'string'}, 'kpis_and_population': {'description': 'Confirmed KPIs and the impacted user population.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'roi_assumptions': {'description': 'Fully loaded hourly cost, volume metric, realization factor (default 0.75), license type, and engagement program.', 'type': 'string'}, 'strategic_priorities': {'description': 'Known strategic priorities or pain points; left blank, they are researched or labeled as hypotheses.', 'type': 'string'}},
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
    print(RoiAndValueSellingArtifact().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
