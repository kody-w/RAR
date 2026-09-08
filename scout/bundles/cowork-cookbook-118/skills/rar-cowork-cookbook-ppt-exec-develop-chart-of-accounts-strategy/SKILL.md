---
name: "rar-cowork-cookbook-ppt-exec-develop-chart-of-accounts-strategy"
description: "Builds a read-only executive PowerPoint deck on chart of accounts strategy from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_chart_of_accounts_strategy", "rar_sha256": "da82d5882fa484e0dcbf0154f4463de8698ba63b1091e294c52a964db8dc21e4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_chart_of_accounts_strategy`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_chart_of_accounts_strategy_agent.py` and in the RCI capsule.

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

Develop chart of accounts strategy Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on chart of accounts strategy from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-chart-of-accounts-strategy
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
    "comparison_period": {
      "description": "Prior period to chart the trend against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-develop-chart-of-accounts-strategy-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Meeting length the deck is scoped for, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_chart_of_accounts_strategy_agent.py` and embedded as the fenced Python below (sha256 da82d5882fa484e0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_chart_of_accounts_strategy_agent.py` first:

```bash
python3 ppt_exec_develop_chart_of_accounts_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_chart_of_accounts_strategy_agent.py   # or on stdin
python3 ppt_exec_develop_chart_of_accounts_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop chart of accounts strategy Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on chart of accounts strategy from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-chart-of-accounts-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_chart_of_accounts_strategy',
    "version": '3.0.3',
    "display_name": 'Develop chart of accounts strategy Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on chart of accounts strategy from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-develop-chart-of-accounts-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-chart-of-accounts-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1160f9221b8d895a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-chart-of-accounts-strategy'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-develop-chart-of-accounts-strategy', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to chart the trend against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-chart-of-accounts-strategy-2026-05-24.pptx.', 'review_length': 'Meeting length the deck is scoped for, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for develop chart of accounts strategy reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on develop chart of accounts strategy for a 15-minute monthly review. Produce 'ppt-exec-develop-chart-of-accounts-strategy-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads develop chart of accounts strategy data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on chart of accounts strategy from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.', 'example_request': 'Build the exec chart of accounts strategy deck for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-chart-of-accounts-strategy-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Meeting length the deck is scoped for, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to chart the trend against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX status deck on chart of accounts strategy for a short monthly review, sourced from D365 F&SCM without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDevelopChartOfAccountsStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopChartOfAccountsStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to chart the trend against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-chart-of-accounts-strategy-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Meeting length the deck is scoped for, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecDevelopChartOfAccountsStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
