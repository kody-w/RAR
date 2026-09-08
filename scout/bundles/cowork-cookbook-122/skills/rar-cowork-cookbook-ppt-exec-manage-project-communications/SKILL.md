---
name: "rar-cowork-cookbook-ppt-exec-manage-project-communications"
description: "Builds a read-only executive PowerPoint deck on manage project communications status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_project_communications", "rar_sha256": "9b6ed062bbe48bf60f205ccedc24e3d06e86951c416f95a735b3ea6da0b5dcd6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
