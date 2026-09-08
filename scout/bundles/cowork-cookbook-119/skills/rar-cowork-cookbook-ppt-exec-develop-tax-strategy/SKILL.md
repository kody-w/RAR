---
name: "rar-cowork-cookbook-ppt-exec-develop-tax-strategy"
description: "Builds a read-only executive PowerPoint deck on develop tax strategy from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_tax_strategy", "rar_sha256": "46bfd431b7028b7d6067cfbb386ccda46264361dc701179d521878b34de18955", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
