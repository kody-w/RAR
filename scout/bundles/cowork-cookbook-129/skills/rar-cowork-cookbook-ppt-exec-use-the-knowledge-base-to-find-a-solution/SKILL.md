---
name: "rar-cowork-cookbook-ppt-exec-use-the-knowledge-base-to-find-a-solution"
description: "Builds a read-only executive PowerPoint deck on knowledge-base solution status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_use_the_knowledge_base_to_find_a_solution", "rar_sha256": "3dd256eb4d67352174d1af48784e862b87fba58b72af7ed4fe9bb6ab6218403e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
