---
name: "rar-cowork-cookbook-ppt-exec-implement-cloud-solutions"
description: "Builds a read-only executive PowerPoint deck on cloud-solution implementation status from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_implement_cloud_solutions", "rar_sha256": "c07322e19b6777546a663a0c89a06c2126431fd582e2188f119f031f2988506e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
