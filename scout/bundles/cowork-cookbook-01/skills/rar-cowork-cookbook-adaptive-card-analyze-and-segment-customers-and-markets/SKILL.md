---
name: "rar-cowork-cookbook-adaptive-card-analyze-and-segment-customers-and-markets"
description: "Generates a read-only Adaptive Card JSON file summarizing customer and market segmentation status from Dynamics 365 F&SCM, with KPI tiles, RAG row, and action buttons for Teams, Outlook, or dashboards."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_and_segment_customers_and_markets", "rar_sha256": "84e26137802c4362cb7b1f4e46264a411a9540aa3ed1495271fff95337803670", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
