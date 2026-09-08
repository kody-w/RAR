---
name: "rar-cowork-cookbook-ppt-exec-budget-asset-leases"
description: "Builds a read-only executive PowerPoint deck on budget asset leases from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_budget_asset_leases", "rar_sha256": "8890f57042b0e08913483fed7e899ca4f57b8ab81331737227ef25b7a2ff4824", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
