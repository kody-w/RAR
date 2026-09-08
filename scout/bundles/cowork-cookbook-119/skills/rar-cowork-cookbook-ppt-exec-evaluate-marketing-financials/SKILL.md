---
name: "rar-cowork-cookbook-ppt-exec-evaluate-marketing-financials"
description: "Builds a read-only executive PowerPoint deck on marketing financials from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_evaluate_marketing_financials", "rar_sha256": "c1e7812a9f000dba82a4abcc826dff2ab69c69f1170a5ae35a100e7d1d9fac92", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
