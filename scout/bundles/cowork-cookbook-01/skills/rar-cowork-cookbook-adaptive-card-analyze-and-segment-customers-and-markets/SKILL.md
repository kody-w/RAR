---
name: "rar-cowork-cookbook-adaptive-card-analyze-and-segment-customers-and-markets"
description: "Generates a read-only Adaptive Card JSON file summarizing customer and market segmentation status from Dynamics 365 F&SCM, with KPI tiles, RAG row, and action buttons for Teams, Outlook, or dashboards."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_and_segment_customers_and_markets", "rar_sha256": "84e26137802c4362cb7b1f4e46264a411a9540aa3ed1495271fff95337803670", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_analyze_and_segment_customers_and_markets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_analyze_and_segment_customers_and_markets_agent.py` and in the RCI capsule.

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

Analyze and segment customers and markets Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing customer and market segmentation status from Dynamics 365 F&SCM, with KPI tiles, RAG row, and action buttons for Teams, Outlook, or dashboards.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-and-segment-customers-and-markets
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
      "description": "Date used for the card timestamp and filename.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-analyze-and-segment-customers-and-markets-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_analyze_and_segment_customers_and_markets_agent.py` and embedded as the fenced Python below (sha256 84e26137802c4362…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_analyze_and_segment_customers_and_markets_agent.py` first:

```bash
python3 adaptive_card_analyze_and_segment_customers_and_markets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_analyze_and_segment_customers_and_markets_agent.py   # or on stdin
python3 adaptive_card_analyze_and_segment_customers_and_markets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and segment customers and markets Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing customer and market segmentation status from Dynamics 365 F&SCM, with KPI tiles, RAG row, and action buttons for Teams, Outlook, or dashboards.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-and-segment-customers-and-markets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_analyze_and_segment_customers_and_markets',
    "version": '3.0.2',
    "display_name": 'Analyze and segment customers and markets Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing customer and market segmentation status from Dynamics 365 F&SCM, with KPI tiles, RAG row, and action buttons for Teams, Outlook, or dashboards.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-analyze-and-segment-customers-and-markets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-analyze-and-segment-customers-and-markets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '615f98b688cdb57c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/analyze-and-segment-customers-and-markets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/adaptive-card-analyze-and-segment-customers-and-markets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-analyze-and-segment-customers-and-markets-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical analyze and segment customers and markets status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-analyze-and-segment-customers-and-markets-2026-05-24-card.json' that visualizes the current state of analyze and segment customers and markets. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current analyze and segment customers and markets KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing customer and market segmentation status from Dynamics 365 F&SCM, with KPI tiles, RAG row, and action buttons for Teams, Outlook, or dashboards.', 'example_request': 'Make an Adaptive Card JSON of customer and market segmentation status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-analyze-and-segment-customers-and-markets-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and filename.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an Adaptive Card snapshot of customer/market segmentation status from D365 ERP to embed in Teams, email, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardAnalyzeAndSegmentCustomersAndMarkets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAnalyzeAndSegmentCustomersAndMarkets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-analyze-and-segment-customers-and-markets-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardAnalyzeAndSegmentCustomersAndMarkets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
