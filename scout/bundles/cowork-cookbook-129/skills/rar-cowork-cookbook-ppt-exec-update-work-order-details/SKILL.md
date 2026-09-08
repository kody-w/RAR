---
name: "rar-cowork-cookbook-ppt-exec-update-work-order-details"
description: "Builds a read-only executive PowerPoint deck on update work order details from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_update_work_order_details", "rar_sha256": "3fa57521757d521b82f882848afa8cb374d9dfce25179a6918d32f241511fd15", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_update_work_order_details`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_update_work_order_details_agent.py` and in the RCI capsule.

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

Update work order details Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on update work order details from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-update-work-order-details
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
      "description": "Dynamics 365 legal entity to report on (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-update-work-order-details-2026-05-24.pptx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_update_work_order_details_agent.py` and embedded as the fenced Python below (sha256 3fa57521757d521b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_update_work_order_details_agent.py` first:

```bash
python3 ppt_exec_update_work_order_details_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_update_work_order_details_agent.py   # or on stdin
python3 ppt_exec_update_work_order_details_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update work order details Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on update work order details from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-update-work-order-details
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_update_work_order_details',
    "version": '3.0.3',
    "display_name": 'Update work order details Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on update work order details from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-update-work-order-details',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-update-work-order-details',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '337caced559416fb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/update-work-order-details'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/ppt-exec-update-work-order-details', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare trends against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-update-work-order-details-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for update work order details reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on update work order details for a 15-minute monthly review. Produce 'ppt-exec-update-work-order-details-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads update work order details data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on update work order details from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.', 'example_request': 'Build a 15-minute exec PowerPoint on update work order details for USMF from D365, read-only.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-update-work-order-details-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare trends against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX summarizing update work order details status for a monthly or periodic review meeting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecUpdateWorkOrderDetails(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecUpdateWorkOrderDetails'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare trends against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-update-work-order-details-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecUpdateWorkOrderDetails().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
