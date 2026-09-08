---
name: "rar-cowork-cookbook-ppt-exec-manage-project-communications"
description: "Builds a read-only executive PowerPoint deck on manage project communications status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_project_communications", "rar_sha256": "9b6ed062bbe48bf60f205ccedc24e3d06e86951c416f95a735b3ea6da0b5dcd6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_manage_project_communications`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_manage_project_communications_agent.py` and in the RCI capsule.

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

Manage project communications Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on manage project communications status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-project-communications
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
      "description": "Dynamics 365 legal entity to report on (e.g. USMF).",
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
      "description": "Target .pptx filename, e.g. ppt-exec-manage-project-communications-2026-05-24.pptx.",
      "type": "string"
    },
    "reporting_period": {
      "description": "Current period and prior period used for the trend comparison chart.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_project_communications_agent.py` and embedded as the fenced Python below (sha256 9b6ed062bbe48bf6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_project_communications_agent.py` first:

```bash
python3 ppt_exec_manage_project_communications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_project_communications_agent.py   # or on stdin
python3 ppt_exec_manage_project_communications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project communications Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on manage project communications status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-project-communications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_project_communications',
    "version": '3.0.3',
    "display_name": 'Manage project communications Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on manage project communications status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-manage-project-communications',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-project-communications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '786d07b165776d59',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/manage-project-communications'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/ppt-exec-manage-project-communications', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-manage-project-communications-2026-05-24.pptx.', 'reporting_period': 'Current period and prior period used for the trend comparison chart.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for manage project communications reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on manage project communications for a 15-minute monthly review. Produce 'ppt-exec-manage-project-communications-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage project communications data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on manage project communications status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on manage project communications for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-manage-project-communications-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Current period and prior period used for the trend comparison chart.', 'name': 'reporting_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX on manage project communications for a short monthly review, sourced from Dynamics 365 F&SCM without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecManageProjectCommunications(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageProjectCommunications'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-manage-project-communications-2026-05-24.pptx.', 'type': 'string'}, 'reporting_period': {'description': 'Current period and prior period used for the trend comparison chart.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecManageProjectCommunications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
