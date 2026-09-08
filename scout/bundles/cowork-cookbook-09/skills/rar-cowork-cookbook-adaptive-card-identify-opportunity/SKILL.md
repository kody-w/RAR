---
name: "rar-cowork-cookbook-adaptive-card-identify-opportunity"
description: "Generates a read-only Adaptive Card JSON file visualizing identify-opportunity status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_identify_opportunity", "rar_sha256": "961c0ac56630f8c11c304e39be7294b1819e04b1710bb9c9a7de223bce996620", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
