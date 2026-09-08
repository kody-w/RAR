---
name: "rar-cowork-cookbook-ppt-exec-analyze-product-profitability"
description: "Builds a read-only executive PowerPoint deck on product profitability from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_product_profitability", "rar_sha256": "5ac8a9ff6f786623391662a25146c004e05ab742381404fc84d94fc0bdc7b5c8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_analyze_product_profitability`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_analyze_product_profitability_agent.py` and in the RCI capsule.

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

Analyze product profitability Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on product profitability from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-analyze-product-profitability
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
    "legal_entity": {
      "description": "Dynamics 365 legal entity to analyze, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-analyze-product-profitability-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Review cadence and length the deck is sized for, e.g. 15-minute monthly review, plus the prior period to compare against.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_analyze_product_profitability_agent.py` and embedded as the fenced Python below (sha256 5ac8a9ff6f786623…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_analyze_product_profitability_agent.py` first:

```bash
python3 ppt_exec_analyze_product_profitability_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_analyze_product_profitability_agent.py   # or on stdin
python3 ppt_exec_analyze_product_profitability_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze product profitability Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on product profitability from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-analyze-product-profitability
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_analyze_product_profitability',
    "version": '3.0.3',
    "display_name": 'Analyze product profitability Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on product profitability from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-analyze-product-profitability',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-analyze-product-profitability',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1dd899911c788304',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/analyze-product-performance/analyze-product-profitability'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/ppt-exec-analyze-product-profitability', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to analyze, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-analyze-product-profitability-2026-05-24.pptx.', 'review_period': 'Review cadence and length the deck is sized for, e.g. 15-minute monthly review, plus the prior period to compare against.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for analyze product profitability reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on analyze product profitability for a 15-minute monthly review. Produce 'ppt-exec-analyze-product-profitability-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads analyze product profitability data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on product profitability from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on product profitability for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to analyze, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-analyze-product-profitability-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Review cadence and length the deck is sized for, e.g. 15-minute monthly review, plus the prior period to compare against.', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready product profitability deck for a short monthly review, sourced from Dynamics 365 ERP without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecAnalyzeProductProfitability(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecAnalyzeProductProfitability'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to analyze, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-analyze-product-profitability-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Review cadence and length the deck is sized for, e.g. 15-minute monthly review, plus the prior period to compare against.', 'type': 'string'}},
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
    print(PptExecAnalyzeProductProfitability().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
