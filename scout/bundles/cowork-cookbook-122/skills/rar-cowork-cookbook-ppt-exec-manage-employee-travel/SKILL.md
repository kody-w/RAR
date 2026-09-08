---
name: "rar-cowork-cookbook-ppt-exec-manage-employee-travel"
description: "Builds a read-only executive PowerPoint deck on employee travel status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_employee_travel", "rar_sha256": "52eb08f480a30988ef5c8f5f1394d85b50ee0260abfe0b2a1fdfd8f8c544ec70", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
