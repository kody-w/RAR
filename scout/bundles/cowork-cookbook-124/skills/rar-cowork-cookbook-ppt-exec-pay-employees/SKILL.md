---
name: "rar-cowork-cookbook-ppt-exec-pay-employees"
description: "Builds a read-only executive PowerPoint deck on pay employees status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_pay_employees", "rar_sha256": "3feee1e350dfeb036e9c7699cc411b4fb3a6e1632ea046832c67a08b59cba9e3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_pay_employees`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_pay_employees_agent.py` and in the RCI capsule.

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

Pay employees Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on pay employees status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-pay-employees
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
      "description": "D365 legal entity to report on (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-pay-employees-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length of the review the deck must fit, e.g. 15 minutes.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and comparison prior period for the trend chart (monthly review).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_pay_employees_agent.py` and embedded as the fenced Python below (sha256 3feee1e350dfeb03…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_pay_employees_agent.py` first:

```bash
python3 ppt_exec_pay_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_pay_employees_agent.py   # or on stdin
python3 ppt_exec_pay_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pay employees Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on pay employees status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-pay-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_pay_employees',
    "version": '3.0.3',
    "display_name": 'Pay employees Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on pay employees status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-pay-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-pay-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b59eee25a897fd66',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/pay-employees'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/ppt-exec-pay-employees', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-pay-employees-2026-05-24.pptx.', 'review_length': 'Length of the review the deck must fit, e.g. 15 minutes.', 'review_period': 'Reporting period and comparison prior period for the trend chart (monthly review).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for pay employees reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on pay employees for a 15-minute monthly review. Produce 'ppt-exec-pay-employees-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads pay employees data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on pay employees status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': "Build the executive pay employees PowerPoint deck for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-pay-employees-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and comparison prior period for the trend chart (monthly review).', 'name': 'review_period'}, {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'name': 'review_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready pay employees deck from Dynamics 365 F&SCM for a short monthly review, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecPayEmployees(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPayEmployees'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-pay-employees-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and comparison prior period for the trend chart (monthly review).', 'type': 'string'}},
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
    print(PptExecPayEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
