---
name: "rar-cowork-cookbook-ppt-exec-pay-employees"
description: "Builds a read-only executive PowerPoint deck on pay employees status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_pay_employees", "rar_sha256": "3feee1e350dfeb036e9c7699cc411b4fb3a6e1632ea046832c67a08b59cba9e3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
