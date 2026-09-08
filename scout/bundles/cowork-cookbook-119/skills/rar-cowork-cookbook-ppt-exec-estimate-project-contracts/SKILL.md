---
name: "rar-cowork-cookbook-ppt-exec-estimate-project-contracts"
description: "Builds a read-only executive PowerPoint deck on estimate project contracts from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_estimate_project_contracts", "rar_sha256": "0827873676b947300a5bba55f1304ad13d171d684f7860493e47321f49b2ba53", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
