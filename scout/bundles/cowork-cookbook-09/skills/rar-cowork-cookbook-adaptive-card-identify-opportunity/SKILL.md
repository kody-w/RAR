---
name: "rar-cowork-cookbook-adaptive-card-identify-opportunity"
description: "Generates a read-only Adaptive Card JSON file visualizing identify-opportunity status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_identify_opportunity", "rar_sha256": "961c0ac56630f8c11c304e39be7294b1819e04b1710bb9c9a7de223bce996620", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_identify_opportunity`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_identify_opportunity_agent.py` and in the RCI capsule.

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

Identify opportunity Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing identify-opportunity status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-opportunity
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
      "description": "Date the status snapshot represents, used in the card header timestamp and filename.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-identify-opportunity-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_identify_opportunity_agent.py` and embedded as the fenced Python below (sha256 961c0ac56630f8c1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_identify_opportunity_agent.py` first:

```bash
python3 adaptive_card_identify_opportunity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_identify_opportunity_agent.py   # or on stdin
python3 adaptive_card_identify_opportunity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify opportunity Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing identify-opportunity status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-opportunity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_identify_opportunity',
    "version": '3.0.2',
    "display_name": 'Identify opportunity Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing identify-opportunity status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-identify-opportunity',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-identify-opportunity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c58bdcdcfe8d7112',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/identify-opportunity'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/adaptive-card-identify-opportunity', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date the status snapshot represents, used in the card header timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-identify-opportunity-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical identify opportunity status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-identify-opportunity-2026-05-24-card.json' that visualizes the current state of identify opportunity. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current identify opportunity KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing identify-opportunity status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card JSON of identify opportunity status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-identify-opportunity-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date the status snapshot represents, used in the card header timestamp and filename.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of identify opportunity status from D365 ERP for Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardIdentifyOpportunity(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardIdentifyOpportunity'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date the status snapshot represents, used in the card header timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-identify-opportunity-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardIdentifyOpportunity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
