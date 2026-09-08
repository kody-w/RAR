---
name: "rar-cowork-cookbook-ppt-exec-develop-chart-of-accounts-strategy"
description: "Builds a read-only executive PowerPoint deck on chart of accounts strategy from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_chart_of_accounts_strategy", "rar_sha256": "da82d5882fa484e0dcbf0154f4463de8698ba63b1091e294c52a964db8dc21e4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
