---
name: "rar-cowork-cookbook-ppt-exec-develop-tax-strategy"
description: "Builds a read-only executive PowerPoint deck on develop tax strategy from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_tax_strategy", "rar_sha256": "46bfd431b7028b7d6067cfbb386ccda46264361dc701179d521878b34de18955", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_tax_strategy`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_tax_strategy_agent.py` and in the RCI capsule.

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

Develop tax strategy Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on develop tax strategy from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-tax-strategy
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
      "description": "Prior period to trend current results against.",
      "type": "string"
    },
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
      "description": "Target .pptx filename, e.g. ppt-exec-develop-tax-strategy-2026-05-24.pptx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_tax_strategy_agent.py` and embedded as the fenced Python below (sha256 46bfd431b7028b7d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_tax_strategy_agent.py` first:

```bash
python3 ppt_exec_develop_tax_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_tax_strategy_agent.py   # or on stdin
python3 ppt_exec_develop_tax_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop tax strategy Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on develop tax strategy from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-tax-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_tax_strategy',
    "version": '3.0.3',
    "display_name": 'Develop tax strategy Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on develop tax strategy from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-develop-tax-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-tax-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '68248a488b134fca',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-tax-strategy'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-develop-tax-strategy', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to trend current results against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-develop-tax-strategy-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for develop tax strategy reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on develop tax strategy for a 15-minute monthly review. Produce 'ppt-exec-develop-tax-strategy-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads develop tax strategy data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on develop tax strategy from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on develop tax strategy for USMF from D365 for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-develop-tax-strategy-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to trend current results against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready tax strategy status deck from D365 F&SCM for a short monthly review, without modifying any ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDevelopTaxStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopTaxStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to trend current results against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-develop-tax-strategy-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecDevelopTaxStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
