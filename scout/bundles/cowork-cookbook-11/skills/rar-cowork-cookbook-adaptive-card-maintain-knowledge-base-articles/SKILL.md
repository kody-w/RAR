---
name: "rar-cowork-cookbook-adaptive-card-maintain-knowledge-base-articles"
description: "Generates a read-only Adaptive Card JSON file summarizing knowledge base article maintenance status from Dynamics 365 ERP, with header, KPI tiles, RAG row, and action buttons; call when you need an embeddable status card"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_maintain_knowledge_base_articles", "rar_sha256": "ad5761df3168d4dec896a5c7b573605ea035fc2a1f333f70cf86a605df16ec57", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_maintain_knowledge_base_articles`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_maintain_knowledge_base_articles_agent.py` and in the RCI capsule.

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

Maintain knowledge base articles Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing knowledge base article maintenance status from Dynamics 365 ERP, with header, KPI tiles, RAG row, and action buttons; call when you need an embeddable status card

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-maintain-knowledge-base-articles
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
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-maintain-knowledge-base-articles-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_maintain_knowledge_base_articles_agent.py` and embedded as the fenced Python below (sha256 ad5761df3168d4de…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_maintain_knowledge_base_articles_agent.py` first:

```bash
python3 adaptive_card_maintain_knowledge_base_articles_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_maintain_knowledge_base_articles_agent.py   # or on stdin
python3 adaptive_card_maintain_knowledge_base_articles_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain knowledge base articles Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing knowledge base article maintenance status from Dynamics 365 ERP, with header, KPI tiles, RAG row, and action buttons; call when you need an embeddable status card

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-maintain-knowledge-base-articles
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_maintain_knowledge_base_articles',
    "version": '3.0.2',
    "display_name": 'Maintain knowledge base articles Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing knowledge base article maintenance status from Dynamics 365 ERP, with header, KPI tiles, RAG row, and action buttons; call when you need an embeddable status card',
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
        "upstream_slug": 'adaptive-card-maintain-knowledge-base-articles',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-maintain-knowledge-base-articles',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4cfa87e3154c9d35',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/establish-a-knowledge-base/maintain-knowledge-base-articles'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/adaptive-card-maintain-knowledge-base-articles', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and file name.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-maintain-knowledge-base-articles-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical maintain knowledge base articles status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-maintain-knowledge-base-articles-2026-05-24-card.json' that visualizes the current state of maintain knowledge base articles. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current maintain knowledge base articles KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing knowledge base article maintenance status from Dynamics 365 ERP, with header, KPI tiles, RAG row, and action buttons; call when you need an embeddable status card', 'example_request': 'Make an Adaptive Card JSON of knowledge base article status in USMF for 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-maintain-knowledge-base-articles-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and file name.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'When a user wants a Teams/Outlook-ready Adaptive Card snapshot of knowledge base article status from D365 F&SCM, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardMaintainKnowledgeBaseArticles(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMaintainKnowledgeBaseArticles'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and file name.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-maintain-knowledge-base-articles-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardMaintainKnowledgeBaseArticles().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
