---
name: "rar-cowork-cookbook-ppt-exec-develop-budgets"
description: "Builds a read-only executive PowerPoint deck on develop budgets from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_budgets", "rar_sha256": "42bfc97704d8c1c62bfe3cc8bd61c523f987a47563313e9b82776f335e814acc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_budgets`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_budgets_agent.py` and in the RCI capsule.

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

Develop budgets Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on develop budgets from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-budgets
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
      "description": "Prior period to trend the current figures against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-develop-budgets-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_budgets_agent.py` and embedded as the fenced Python below (sha256 42bfc97704d8c1c6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_budgets_agent.py` first:

```bash
python3 ppt_exec_develop_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_budgets_agent.py   # or on stdin
python3 ppt_exec_develop_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop budgets Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on develop budgets from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_budgets',
    "version": '3.0.3',
    "display_name": 'Develop budgets Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on develop budgets from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-develop-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'de58a0e5bc5b0f06',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/develop-budgets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-develop-budgets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to trend the current figures against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-budgets-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for develop budgets reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on develop budgets for a 15-minute monthly review. Produce 'ppt-exec-develop-budgets-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop budgets data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on develop budgets from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build a 15-minute exec PowerPoint on develop budgets for legal entity USMF, with speaker notes and a trend vs prior period.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-budgets-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to trend the current figures against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive develop-budgets deck for a monthly review, sourced from Dynamics 365 ERP without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDevelopBudgets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopBudgets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to trend the current figures against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-budgets-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecDevelopBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
