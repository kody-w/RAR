---
name: "rar-cowork-cookbook-ppt-exec-onboard-new-suppliers"
description: "Builds a read-only executive PowerPoint deck on supplier onboarding status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_onboard_new_suppliers", "rar_sha256": "71ee3111458f3819713948a9f978c41f5e542eaa5ebf15a14a72b5bc778e6db0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
