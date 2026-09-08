---
name: "rar-cowork-cookbook-ppt-exec-onboard-new-suppliers"
description: "Builds a read-only executive PowerPoint deck on supplier onboarding status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_onboard_new_suppliers", "rar_sha256": "71ee3111458f3819713948a9f978c41f5e542eaa5ebf15a14a72b5bc778e6db0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_onboard_new_suppliers`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_onboard_new_suppliers_agent.py` and in the RCI capsule.

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

Onboard new suppliers Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on supplier onboarding status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-onboard-new-suppliers
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
      "description": "Prior period to compare trends against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to pull data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-onboard-new-suppliers-2026-05-24.pptx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_onboard_new_suppliers_agent.py` and embedded as the fenced Python below (sha256 71ee3111458f3819…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_onboard_new_suppliers_agent.py` first:

```bash
python3 ppt_exec_onboard_new_suppliers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_onboard_new_suppliers_agent.py   # or on stdin
python3 ppt_exec_onboard_new_suppliers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new suppliers Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on supplier onboarding status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-onboard-new-suppliers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_onboard_new_suppliers',
    "version": '3.0.3',
    "display_name": 'Onboard new suppliers Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on supplier onboarding status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-onboard-new-suppliers',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-onboard-new-suppliers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f32eb1fa15e1c9ad',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/onboard-new-suppliers'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/ppt-exec-onboard-new-suppliers', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare trends against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-onboard-new-suppliers-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for onboard new suppliers reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on onboard new suppliers for a 15-minute monthly review. Produce 'ppt-exec-onboard-new-suppliers-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads onboard new suppliers data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on supplier onboarding status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on new supplier onboarding for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-onboard-new-suppliers-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare trends against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready supplier onboarding deck from D365 F&SCM for a short monthly review, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecOnboardNewSuppliers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecOnboardNewSuppliers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare trends against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-onboard-new-suppliers-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecOnboardNewSuppliers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
