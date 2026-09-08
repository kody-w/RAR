---
name: "rar-cowork-cookbook-adaptive-card-convert-a-case-to-a-knowledge-article"
description: "Generates a read-only Adaptive Card JSON file visualizing convert-a-case-to-a-knowledge-article status for a D365 F&SCM legal entity, with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_convert_a_case_to_a_knowledge_article", "rar_sha256": "3225b9f29549e340d0996646cae5f8aba08ca51f32af185c4282b71ebcdcdcca", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_convert_a_case_to_a_knowledge_article`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_convert_a_case_to_a_knowledge_article_agent.py` and in the RCI capsule.

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

Convert a case to a knowledge article Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing convert-a-case-to-a-knowledge-article status for a D365 F&SCM legal entity, with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-convert-a-case-to-a-knowledge-article
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
    "as_of_date": {
      "description": "Date used for the card timestamp and file name.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to report on (e.g. USMF).",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-convert-a-case-to-a-knowledge-article-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_convert_a_case_to_a_knowledge_article_agent.py` and embedded as the fenced Python below (sha256 3225b9f29549e340…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_convert_a_case_to_a_knowledge_article_agent.py` first:

```bash
python3 adaptive_card_convert_a_case_to_a_knowledge_article_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_convert_a_case_to_a_knowledge_article_agent.py   # or on stdin
python3 adaptive_card_convert_a_case_to_a_knowledge_article_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Convert a case to a knowledge article Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing convert-a-case-to-a-knowledge-article status for a D365 F&SCM legal entity, with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-convert-a-case-to-a-knowledge-article
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_convert_a_case_to_a_knowledge_article',
    "version": '3.0.2',
    "display_name": 'Convert a case to a knowledge article Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing convert-a-case-to-a-knowledge-article status for a D365 F&SCM legal entity, with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-convert-a-case-to-a-knowledge-article',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-convert-a-case-to-a-knowledge-article',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '854622c7d22d02d8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/convert-a-case-to-a-knowledge-article'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/adaptive-card-convert-a-case-to-a-knowledge-article', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and file name.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-convert-a-case-to-a-knowledge-article-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical convert a case to a knowledge article status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-convert-a-case-to-a-knowledge-article-2026-05-24-card.json' that visualizes the current state of convert a case to a knowledge article. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current convert a case to a knowledge article KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing convert-a-case-to-a-knowledge-article status for a D365 F&SCM legal entity, with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.', 'example_request': 'Make an Adaptive Card JSON showing case-to-knowledge-article status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-convert-a-case-to-a-knowledge-article-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and file name.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an Adaptive Card JSON snapshot of case-to-knowledge-article status to embed in Teams, Outlook, or a dashboard. No data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardConvertACaseToAKnowledgeArticle(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConvertACaseToAKnowledgeArticle'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and file name.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-convert-a-case-to-a-knowledge-article-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardConvertACaseToAKnowledgeArticle().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
