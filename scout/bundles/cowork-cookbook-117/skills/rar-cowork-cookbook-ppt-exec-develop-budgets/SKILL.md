---
name: "rar-cowork-cookbook-ppt-exec-develop-budgets"
description: "Builds a read-only executive PowerPoint deck on develop budgets from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_budgets", "rar_sha256": "42bfc97704d8c1c62bfe3cc8bd61c523f987a47563313e9b82776f335e814acc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
