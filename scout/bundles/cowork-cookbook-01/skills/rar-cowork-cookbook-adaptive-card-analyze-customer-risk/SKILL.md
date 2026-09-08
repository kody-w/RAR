---
name: "rar-cowork-cookbook-adaptive-card-analyze-customer-risk"
description: "Generates a read-only Adaptive Card JSON file visualizing customer risk status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons for Teams/Outlook embedding."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_analyze_customer_risk", "rar_sha256": "19418a5e98a8a2dcb5309f0437e98f2c5daebef64b4d5ef89922143c56b3d23a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
