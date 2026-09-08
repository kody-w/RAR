---
name: "rar-cowork-cookbook-ppt-exec-estimate-project-contracts"
description: "Builds a read-only executive PowerPoint deck on estimate project contracts from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_estimate_project_contracts", "rar_sha256": "0827873676b947300a5bba55f1304ad13d171d684f7860493e47321f49b2ba53", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_estimate_project_contracts`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_estimate_project_contracts_agent.py` and in the RCI capsule.

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

Estimate project contracts Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on estimate project contracts from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-estimate-project-contracts
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
      "description": "Dynamics 365 legal entity to pull contract data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-estimate-project-contracts-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison (e.g. monthly review as of 2026-05-24).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_estimate_project_contracts_agent.py` and embedded as the fenced Python below (sha256 0827873676b94730…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_estimate_project_contracts_agent.py` first:

```bash
python3 ppt_exec_estimate_project_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_estimate_project_contracts_agent.py   # or on stdin
python3 ppt_exec_estimate_project_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Estimate project contracts Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on estimate project contracts from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-estimate-project-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_estimate_project_contracts',
    "version": '3.0.3',
    "display_name": 'Estimate project contracts Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on estimate project contracts from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-estimate-project-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-estimate-project-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c4d488164d965d0a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/estimate-project-contracts'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/ppt-exec-estimate-project-contracts', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull contract data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-estimate-project-contracts-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of 2026-05-24).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for estimate project contracts reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on estimate project contracts for a 15-minute monthly review. Produce 'ppt-exec-estimate-project-contracts-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads estimate project contracts data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on estimate project contracts from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.', 'example_request': "Build the executive PowerPoint deck on estimate project contracts for USMF for this month's 15-minute review.", 'inputs': [{'description': 'Dynamics 365 legal entity to pull contract data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-estimate-project-contracts-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of 2026-05-24).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a 15-minute monthly executive review deck on estimate project contracts status sourced from Dynamics 365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecEstimateProjectContracts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecEstimateProjectContracts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull contract data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-estimate-project-contracts-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison (e.g. monthly review as of 2026-05-24).', 'type': 'string'}},
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
    print(PptExecEstimateProjectContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
