---
name: "rar-cowork-cookbook-ppt-exec-update-work-order-details"
description: "Builds a read-only executive PowerPoint deck on update work order details from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_update_work_order_details", "rar_sha256": "3fa57521757d521b82f882848afa8cb374d9dfce25179a6918d32f241511fd15", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
