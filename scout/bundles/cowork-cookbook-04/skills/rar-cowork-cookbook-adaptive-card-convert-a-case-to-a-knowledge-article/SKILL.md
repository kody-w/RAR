---
name: "rar-cowork-cookbook-adaptive-card-convert-a-case-to-a-knowledge-article"
description: "Generates a read-only Adaptive Card JSON file visualizing convert-a-case-to-a-knowledge-article status for a D365 F&SCM legal entity, with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_convert_a_case_to_a_knowledge_article", "rar_sha256": "3225b9f29549e340d0996646cae5f8aba08ca51f32af185c4282b71ebcdcdcca", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
