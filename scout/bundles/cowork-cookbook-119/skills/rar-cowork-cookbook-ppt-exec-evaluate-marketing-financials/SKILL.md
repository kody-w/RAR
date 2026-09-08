---
name: "rar-cowork-cookbook-ppt-exec-evaluate-marketing-financials"
description: "Builds a read-only executive PowerPoint deck on marketing financials from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_evaluate_marketing_financials", "rar_sha256": "c1e7812a9f000dba82a4abcc826dff2ab69c69f1170a5ae35a100e7d1d9fac92", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_evaluate_marketing_financials`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_evaluate_marketing_financials_agent.py` and in the RCI capsule.

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

Evaluate marketing financials Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on marketing financials from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-evaluate-marketing-financials
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
      "description": "Dynamics 365 legal entity to pull financials from, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-evaluate-marketing-financials-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length of the review the deck must fit, e.g. 15 minutes.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison (e.g. monthly review as of a given date).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_evaluate_marketing_financials_agent.py` and embedded as the fenced Python below (sha256 c1e7812a9f000dba…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_evaluate_marketing_financials_agent.py` first:

```bash
python3 ppt_exec_evaluate_marketing_financials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_evaluate_marketing_financials_agent.py   # or on stdin
python3 ppt_exec_evaluate_marketing_financials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Evaluate marketing financials Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on marketing financials from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-evaluate-marketing-financials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_evaluate_marketing_financials',
    "version": '3.0.3',
    "display_name": 'Evaluate marketing financials Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on marketing financials from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-evaluate-marketing-financials',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-evaluate-marketing-financials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0f4f6efc91ca4458',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/evaluate-marketing-financials'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/ppt-exec-evaluate-marketing-financials', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull financials from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-evaluate-marketing-financials-2026-05-24.pptx.', 'review_length': 'Length of the review the deck must fit, e.g. 15 minutes.', 'review_period': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of a given date).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for evaluate marketing financials reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on evaluate marketing financials for a 15-minute monthly review. Produce 'ppt-exec-evaluate-marketing-financials-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads evaluate marketing financials data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on marketing financials from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build a 15-minute exec PowerPoint on marketing financials for USMF from D365, with charts and speaker notes.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull financials from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-evaluate-marketing-financials-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of a given date).', 'name': 'review_period'}, {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'name': 'review_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready marketing financials deck from D365 F&SCM for a short monthly review, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecEvaluateMarketingFinancials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecEvaluateMarketingFinancials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull financials from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-evaluate-marketing-financials-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of a given date).', 'type': 'string'}},
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
    print(PptExecEvaluateMarketingFinancials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
