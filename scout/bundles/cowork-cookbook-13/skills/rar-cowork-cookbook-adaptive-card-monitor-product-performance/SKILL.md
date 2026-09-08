---
name: "rar-cowork-cookbook-adaptive-card-monitor-product-performance"
description: "Generates a read-only Adaptive Card JSON file summarizing product performance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_product_performance", "rar_sha256": "c40bb92eea5bf570aa331a4f71c1ee1ee9a80805eb5fe15df3505f1afa2159b7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_monitor_product_performance`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_monitor_product_performance_agent.py` and in the RCI capsule.

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

Monitor product performance Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing product performance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-product-performance
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
      "description": "The 2-3 action buttons to include on the card.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Date/timestamp the snapshot represents, used in the card header and filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5).",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-monitor-product-performance-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_monitor_product_performance_agent.py` and embedded as the fenced Python below (sha256 c40bb92eea5bf570…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_monitor_product_performance_agent.py` first:

```bash
python3 adaptive_card_monitor_product_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_monitor_product_performance_agent.py   # or on stdin
python3 adaptive_card_monitor_product_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor product performance Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing product performance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-product-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_monitor_product_performance',
    "version": '3.0.2',
    "display_name": 'Monitor product performance Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing product performance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-monitor-product-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-monitor-product-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e88f3f472b492d32',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/analyze-product-performance/monitor-product-performance'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/adaptive-card-monitor-product-performance', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to include on the card.', 'as_of_date': 'Date/timestamp the snapshot represents, used in the card header and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-monitor-product-performance-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical monitor product performance status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-monitor-product-performance-2026-05-24-card.json' that visualizes the current state of monitor product performance. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current monitor product performance KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing product performance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing monitor product performance status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-monitor-product-performance-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date/timestamp the snapshot represents, used in the card header and filename.', 'name': 'as_of_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to include on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of product performance status from D365 ERP data, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardMonitorProductPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMonitorProductPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to include on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date/timestamp the snapshot represents, used in the card header and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-monitor-product-performance-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardMonitorProductPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
