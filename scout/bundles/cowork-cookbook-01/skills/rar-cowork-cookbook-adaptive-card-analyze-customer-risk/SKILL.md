---
name: "rar-cowork-cookbook-adaptive-card-analyze-customer-risk"
description: "Generates a read-only Adaptive Card JSON file visualizing customer risk status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_customer_risk", "rar_sha256": "19418a5e98a8a2dcb5309f0437e98f2c5daebef64b4d5ef89922143c56b3d23a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_analyze_customer_risk`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_analyze_customer_risk_agent.py` and in the RCI capsule.

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

Analyze customer risk Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing customer risk status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-customer-risk
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-analyze-customer-risk-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_analyze_customer_risk_agent.py` and embedded as the fenced Python below (sha256 19418a5e98a8a2dc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_analyze_customer_risk_agent.py` first:

```bash
python3 adaptive_card_analyze_customer_risk_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_analyze_customer_risk_agent.py   # or on stdin
python3 adaptive_card_analyze_customer_risk_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze customer risk Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing customer risk status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-analyze-customer-risk
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_analyze_customer_risk',
    "version": '3.0.2',
    "display_name": 'Analyze customer risk Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing customer risk status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-analyze-customer-risk',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-analyze-customer-risk',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cce0ba2a59a8925b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-customer-risk'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-analyze-customer-risk', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and file name.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-analyze-customer-risk-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical analyze customer risk status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-analyze-customer-risk-2026-05-24-card.json' that visualizes the current state of analyze customer risk. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current analyze customer risk KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing customer risk status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding.', 'example_request': 'Make me an Adaptive Card JSON of customer risk status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-analyze-customer-risk-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and file name.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a customer risk snapshot as an Adaptive Card JSON to embed in Teams, Outlook, or a dashboard. Requires the Cowork D365 ERP plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardAnalyzeCustomerRisk(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAnalyzeCustomerRisk'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and file name.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-analyze-customer-risk-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardAnalyzeCustomerRisk().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
