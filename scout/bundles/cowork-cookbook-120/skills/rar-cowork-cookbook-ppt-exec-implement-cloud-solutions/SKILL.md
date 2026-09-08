---
name: "rar-cowork-cookbook-ppt-exec-implement-cloud-solutions"
description: "Builds a read-only executive PowerPoint deck on cloud-solution implementation status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_implement_cloud_solutions", "rar_sha256": "c07322e19b6777546a663a0c89a06c2126431fd582e2188f119f031f2988506e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_implement_cloud_solutions`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_implement_cloud_solutions_agent.py` and in the RCI capsule.

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

Implement cloud solutions Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on cloud-solution implementation status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-cloud-solutions
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-implement-cloud-solutions-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Meeting length/cadence the deck is scoped for, e.g. 15-minute monthly review.",
      "type": "string"
    },
    "topic": {
      "description": "Initiative or subject of the deck, e.g. 'implement cloud solutions'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_implement_cloud_solutions_agent.py` and embedded as the fenced Python below (sha256 c07322e19b677754…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_implement_cloud_solutions_agent.py` first:

```bash
python3 ppt_exec_implement_cloud_solutions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_implement_cloud_solutions_agent.py   # or on stdin
python3 ppt_exec_implement_cloud_solutions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement cloud solutions Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on cloud-solution implementation status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-cloud-solutions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_implement_cloud_solutions',
    "version": '3.0.3',
    "display_name": 'Implement cloud solutions Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on cloud-solution implementation status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-implement-cloud-solutions',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-implement-cloud-solutions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '535cb40703278c99',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/implement-cloud-solutions'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-implement-cloud-solutions', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to trend current results against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-implement-cloud-solutions-2026-05-24.pptx.', 'review_length': 'Meeting length/cadence the deck is scoped for, e.g. 15-minute monthly review.', 'topic': "Initiative or subject of the deck, e.g. 'implement cloud solutions'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for implement cloud solutions reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on implement cloud solutions for a 15-minute monthly review. Produce 'ppt-exec-implement-cloud-solutions-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads implement cloud solutions data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on cloud-solution implementation status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on implement cloud solutions from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': "Initiative or subject of the deck, e.g. 'implement cloud solutions'.", 'name': 'topic'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-implement-cloud-solutions-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Meeting length/cadence the deck is scoped for, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to trend current results against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX summarizing implement-cloud-solutions status from D365 F&SCM for a short monthly review, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecImplementCloudSolutions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecImplementCloudSolutions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to trend current results against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-implement-cloud-solutions-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Meeting length/cadence the deck is scoped for, e.g. 15-minute monthly review.', 'type': 'string'}, 'topic': {'description': "Initiative or subject of the deck, e.g. 'implement cloud solutions'.", 'type': 'string'}},
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
    print(PptExecImplementCloudSolutions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
