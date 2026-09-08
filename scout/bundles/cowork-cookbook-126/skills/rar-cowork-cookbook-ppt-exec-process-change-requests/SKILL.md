---
name: "rar-cowork-cookbook-ppt-exec-process-change-requests"
description: "Builds a read-only executive PowerPoint deck on process change requests from Dynamics 365 ERP data for a given legal entity, with title, KPI, trend, red-flag, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_process_change_requests", "rar_sha256": "cea195f85fc42d7b72bbe2e67e64b3afb9ee28984fecc04128b8565eaeb1362f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
