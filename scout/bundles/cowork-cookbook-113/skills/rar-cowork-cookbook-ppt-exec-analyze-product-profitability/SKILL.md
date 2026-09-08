---
name: "rar-cowork-cookbook-ppt-exec-analyze-product-profitability"
description: "Builds a read-only executive PowerPoint deck on product profitability from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_product_profitability", "rar_sha256": "5ac8a9ff6f786623391662a25146c004e05ab742381404fc84d94fc0bdc7b5c8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
