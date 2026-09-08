---
name: "rar-cowork-cookbook-ppt-exec-manage-employee-travel"
description: "Builds a read-only executive PowerPoint deck on employee travel status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_employee_travel", "rar_sha256": "52eb08f480a30988ef5c8f5f1394d85b50ee0260abfe0b2a1fdfd8f8c544ec70", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_manage_employee_travel`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_manage_employee_travel_agent.py` and in the RCI capsule.

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

Manage employee travel Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on employee travel status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-employee-travel
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
      "description": "Dynamics 365 legal entity to pull travel data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-manage-employee-travel-2026-05-24.pptx.",
      "type": "string"
    },
    "reporting_period": {
      "description": "Current period and the prior period to compare against for the trend chart.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. a 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_employee_travel_agent.py` and embedded as the fenced Python below (sha256 52eb08f480a30988…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_employee_travel_agent.py` first:

```bash
python3 ppt_exec_manage_employee_travel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_employee_travel_agent.py   # or on stdin
python3 ppt_exec_manage_employee_travel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage employee travel Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on employee travel status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-employee-travel
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_employee_travel',
    "version": '3.0.3',
    "display_name": 'Manage employee travel Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on employee travel status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-manage-employee-travel',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-employee-travel',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '318f395c2b61ad9f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/manage-employee-travel'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/ppt-exec-manage-employee-travel', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull travel data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-manage-employee-travel-2026-05-24.pptx.', 'reporting_period': 'Current period and the prior period to compare against for the trend chart.', 'review_length': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for manage employee travel reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on manage employee travel for a 15-minute monthly review. Produce 'ppt-exec-manage-employee-travel-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage employee travel data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on employee travel status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': 'Build an executive PowerPoint on employee travel from D365 legal entity USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull travel data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-manage-employee-travel-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Current period and the prior period to compare against for the trend chart.', 'name': 'reporting_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready travel-management deck for a short monthly review, sourced from Dynamics 365 F&SCM without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecManageEmployeeTravel(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageEmployeeTravel'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull travel data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-manage-employee-travel-2026-05-24.pptx.', 'type': 'string'}, 'reporting_period': {'description': 'Current period and the prior period to compare against for the trend chart.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecManageEmployeeTravel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
