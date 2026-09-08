---
name: "rar-cowork-cookbook-ppt-exec-process-change-requests"
description: "Builds a read-only executive PowerPoint deck on process change requests from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_process_change_requests", "rar_sha256": "cea195f85fc42d7b72bbe2e67e64b3afb9ee28984fecc04128b8565eaeb1362f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_process_change_requests`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_process_change_requests_agent.py` and in the RCI capsule.

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

Process change requests Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on process change requests from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-process-change-requests
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
      "description": "Prior period to compare against for the trend chart.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-process-change-requests-2026-05-24.pptx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_process_change_requests_agent.py` and embedded as the fenced Python below (sha256 cea195f85fc42d7b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_process_change_requests_agent.py` first:

```bash
python3 ppt_exec_process_change_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_process_change_requests_agent.py   # or on stdin
python3 ppt_exec_process_change_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process change requests Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on process change requests from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-process-change-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_process_change_requests',
    "version": '3.0.3',
    "display_name": 'Process change requests Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on process change requests from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-process-change-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-process-change-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '38d89e2f070b0190',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/process-change-requests'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/ppt-exec-process-change-requests', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against for the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-process-change-requests-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for process change requests reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on process change requests for a 15-minute monthly review. Produce 'ppt-exec-process-change-requests-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads process change requests data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on process change requests from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes.', 'example_request': 'Build an executive PowerPoint on process change requests for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-process-change-requests-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare against for the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready .pptx summarizing process change request status for a short monthly review, without modifying any ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecProcessChangeRequests(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecProcessChangeRequests'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against for the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-process-change-requests-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecProcessChangeRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
