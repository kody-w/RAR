---
name: "rar-cowork-cookbook-adaptive-card-generate-ideas"
description: "Generates a read-only Adaptive Card JSON file visualizing current generate-ideas status from Dynamics 365 ERP for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_generate_ideas", "rar_sha256": "ad79c4378ae9b07638d31a178e44fef78f6c5808705ef77d767e184fb91a6f5e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
