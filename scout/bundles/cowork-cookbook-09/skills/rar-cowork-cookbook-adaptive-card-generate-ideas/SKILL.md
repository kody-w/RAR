---
name: "rar-cowork-cookbook-adaptive-card-generate-ideas"
description: "Generates a read-only Adaptive Card JSON file visualizing current generate-ideas status from Dynamics 365 ERP for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_generate_ideas", "rar_sha256": "ad79c4378ae9b07638d31a178e44fef78f6c5808705ef77d767e184fb91a6f5e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_generate_ideas`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_generate_ideas_agent.py` and in the RCI capsule.

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

Generate ideas Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing current generate-ideas status from Dynamics 365 ERP for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-generate-ideas
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
    "action_buttons": {
      "description": "The 2-3 action buttons to place on the card.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5), each with current value and trend arrow.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-generate-ideas-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_generate_ideas_agent.py` and embedded as the fenced Python below (sha256 ad79c4378ae9b076…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_generate_ideas_agent.py` first:

```bash
python3 adaptive_card_generate_ideas_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_generate_ideas_agent.py   # or on stdin
python3 adaptive_card_generate_ideas_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Generate ideas Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing current generate-ideas status from Dynamics 365 ERP for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-generate-ideas
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_generate_ideas',
    "version": '3.0.2',
    "display_name": 'Generate ideas Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing current generate-ideas status from Dynamics 365 ERP for a given legal entity, with KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-generate-ideas',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-generate-ideas',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2babaad61f2a7797',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/generate-ideas'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/adaptive-card-generate-ideas', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-generate-ideas-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical generate ideas status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-generate-ideas-2026-05-24-card.json' that visualizes the current state of generate ideas. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current generate ideas KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing current generate-ideas status from Dynamics 365 ERP for a given legal entity, with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of generate ideas status from D365 USMF with 4 KPI tiles and a RAG row.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-generate-ideas-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an Adaptive Card JSON snapshot of generate ideas status from D365 F&SCM to embed in Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardGenerateIdeas(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardGenerateIdeas'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-generate-ideas-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardGenerateIdeas().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
