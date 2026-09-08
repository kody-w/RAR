---
name: "rar-cowork-cookbook-ppt-exec-use-the-knowledge-base-to-find-a-solution"
description: "Builds a read-only executive PowerPoint deck on knowledge-base solution status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_use_the_knowledge_base_to_find_a_solution", "rar_sha256": "3dd256eb4d67352174d1af48784e862b87fba58b72af7ed4fe9bb6ab6218403e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_use_the_knowledge_base_to_find_a_solution`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_use_the_knowledge_base_to_find_a_solution_agent.py` and in the RCI capsule.

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

Use the knowledge base to find a solution Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on knowledge-base solution status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-use-the-knowledge-base-to-find-a-solution
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to report on, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-<topic>-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period for the trend comparison (monthly review).",
      "type": "string"
    },
    "topic": {
      "description": "Subject of the deck, e.g. use the knowledge base to find a solution.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_use_the_knowledge_base_to_find_a_solution_agent.py` and embedded as the fenced Python below (sha256 3dd256eb4d673521…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_use_the_knowledge_base_to_find_a_solution_agent.py` first:

```bash
python3 ppt_exec_use_the_knowledge_base_to_find_a_solution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_use_the_knowledge_base_to_find_a_solution_agent.py   # or on stdin
python3 ppt_exec_use_the_knowledge_base_to_find_a_solution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Use the knowledge base to find a solution Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on knowledge-base solution status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-use-the-knowledge-base-to-find-a-solution
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_use_the_knowledge_base_to_find_a_solution',
    "version": '3.0.3',
    "display_name": 'Use the knowledge base to find a solution Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on knowledge-base solution status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-use-the-knowledge-base-to-find-a-solution',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-use-the-knowledge-base-to-find-a-solution',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '433036748fd7bc51',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/use-the-knowledge-base-to-find-a-solution'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/ppt-exec-use-the-knowledge-base-to-find-a-solution', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-<topic>-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period for the trend comparison (monthly review).', 'topic': 'Subject of the deck, e.g. use the knowledge base to find a solution.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for use the knowledge base to find a solution reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on use the knowledge base to find a solution for a 15-minute monthly review. Produce 'ppt-exec-use-the-knowledge-base-to-find-a-solution-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads use the knowledge base to find a solution data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on knowledge-base solution status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': 'Build an executive PowerPoint deck on knowledge base solution status for USMF for our monthly 15-minute review.', 'inputs': [{'description': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Subject of the deck, e.g. use the knowledge base to find a solution.', 'name': 'topic'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-<topic>-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period for the trend comparison (monthly review).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready PPTX for a 15-minute monthly review of knowledge-base solution status sourced from Dynamics 365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecUseTheKnowledgeBaseToFindASolution(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecUseTheKnowledgeBaseToFindASolution'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-<topic>-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period for the trend comparison (monthly review).', 'type': 'string'}, 'topic': {'description': 'Subject of the deck, e.g. use the knowledge base to find a solution.', 'type': 'string'}},
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
    print(PptExecUseTheKnowledgeBaseToFindASolution().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
