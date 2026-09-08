---
name: "rar-cowork-cookbook-ppt-exec-create-knowledge-base-articles"
description: "Builds a read-only executive PowerPoint deck on knowledge base article creation status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_create_knowledge_base_articles", "rar_sha256": "f4411788997e2d6796bda466cc64398d9f75aac11ddc907cac65d8770cca15cf", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_create_knowledge_base_articles`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_create_knowledge_base_articles_agent.py` and in the RCI capsule.

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

Create knowledge base articles Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on knowledge base article creation status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-create-knowledge-base-articles
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
      "description": "D365 legal entity to report on (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-create-knowledge-base-articles-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period for the trend comparison (e.g. monthly review as of 2026-05-24).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_create_knowledge_base_articles_agent.py` and embedded as the fenced Python below (sha256 f4411788997e2d67…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_create_knowledge_base_articles_agent.py` first:

```bash
python3 ppt_exec_create_knowledge_base_articles_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_create_knowledge_base_articles_agent.py   # or on stdin
python3 ppt_exec_create_knowledge_base_articles_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create knowledge base articles Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on knowledge base article creation status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-create-knowledge-base-articles
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_create_knowledge_base_articles',
    "version": '3.0.3',
    "display_name": 'Create knowledge base articles Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on knowledge base article creation status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-create-knowledge-base-articles',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-create-knowledge-base-articles',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ecef3f970e9932bd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/establish-a-knowledge-base/create-knowledge-base-articles'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/ppt-exec-create-knowledge-base-articles', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-create-knowledge-base-articles-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period for the trend comparison (e.g. monthly review as of 2026-05-24).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for create knowledge base articles reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on create knowledge base articles for a 15-minute monthly review. Produce 'ppt-exec-create-knowledge-base-articles-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads create knowledge base articles data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on knowledge base article creation status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': "Build the executive PowerPoint deck on create knowledge base articles for USMF for this month's 15-minute review.", 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-create-knowledge-base-articles-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period for the trend comparison (e.g. monthly review as of 2026-05-24).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a 15-minute monthly executive review deck on create-knowledge-base-articles status sourced from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecCreateKnowledgeBaseArticles(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecCreateKnowledgeBaseArticles'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-create-knowledge-base-articles-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period for the trend comparison (e.g. monthly review as of 2026-05-24).', 'type': 'string'}},
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
    print(PptExecCreateKnowledgeBaseArticles().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
