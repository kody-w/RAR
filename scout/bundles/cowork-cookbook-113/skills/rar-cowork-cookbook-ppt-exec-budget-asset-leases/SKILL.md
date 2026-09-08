---
name: "rar-cowork-cookbook-ppt-exec-budget-asset-leases"
description: "Builds a read-only executive PowerPoint deck on budget asset leases from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_budget_asset_leases", "rar_sha256": "8890f57042b0e08913483fed7e899ca4f57b8ab81331737227ef25b7a2ff4824", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_budget_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_budget_asset_leases_agent.py` and in the RCI capsule.

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

Budget asset leases Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on budget asset leases from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-budget-asset-leases
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
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Target .pptx filename, e.g. ppt-exec-budget-asset-leases-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison (e.g. month of the review).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_budget_asset_leases_agent.py` and embedded as the fenced Python below (sha256 8890f57042b0e089…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_budget_asset_leases_agent.py` first:

```bash
python3 ppt_exec_budget_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_budget_asset_leases_agent.py   # or on stdin
python3 ppt_exec_budget_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Budget asset leases Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on budget asset leases from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-budget-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_budget_asset_leases',
    "version": '3.0.3',
    "display_name": 'Budget asset leases Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on budget asset leases from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ppt-exec-budget-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-budget-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'be45c0f2ac5ced08',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/budget-asset-leases'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-budget-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-budget-asset-leases-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison (e.g. month of the review).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for budget asset leases reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on budget asset leases for a 15-minute monthly review. Produce 'ppt-exec-budget-asset-leases-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads budget asset leases data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on budget asset leases from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': "Make an exec PowerPoint on budget asset leases for USMF for this month's 15-minute review, with speaker notes.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-budget-asset-leases-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison (e.g. month of the review).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a monthly 15-minute executive review deck on budget asset leases sourced from Dynamics 365 F&SCM, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecBudgetAssetLeases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecBudgetAssetLeases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-budget-asset-leases-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison (e.g. month of the review).', 'type': 'string'}},
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
    print(PptExecBudgetAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
