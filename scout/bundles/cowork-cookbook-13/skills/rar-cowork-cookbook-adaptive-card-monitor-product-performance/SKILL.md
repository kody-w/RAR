---
name: "rar-cowork-cookbook-adaptive-card-monitor-product-performance"
description: "Generates a read-only Adaptive Card JSON file summarizing product performance status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, trend arrows, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_product_performance", "rar_sha256": "c40bb92eea5bf570aa331a4f71c1ee1ee9a80805eb5fe15df3505f1afa2159b7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
