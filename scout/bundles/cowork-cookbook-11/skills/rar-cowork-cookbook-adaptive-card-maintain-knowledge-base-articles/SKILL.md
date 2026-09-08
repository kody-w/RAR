---
name: "rar-cowork-cookbook-adaptive-card-maintain-knowledge-base-articles"
description: "Generates a read-only Adaptive Card JSON file summarizing knowledge base article maintenance status from Dynamics 365 ERP, with header, KPI tiles, RAG row, and action buttons; call when you need an embeddable status card"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_maintain_knowledge_base_articles", "rar_sha256": "ad5761df3168d4dec896a5c7b573605ea035fc2a1f333f70cf86a605df16ec57", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
