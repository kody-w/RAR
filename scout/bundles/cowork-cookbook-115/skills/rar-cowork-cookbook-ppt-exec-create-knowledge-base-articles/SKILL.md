---
name: "rar-cowork-cookbook-ppt-exec-create-knowledge-base-articles"
description: "Builds a read-only executive PowerPoint deck on knowledge base article creation status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_create_knowledge_base_articles", "rar_sha256": "f4411788997e2d6796bda466cc64398d9f75aac11ddc907cac65d8770cca15cf", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
