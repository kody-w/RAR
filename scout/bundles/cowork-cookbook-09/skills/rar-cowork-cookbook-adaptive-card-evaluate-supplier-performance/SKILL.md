---
name: "rar-cowork-cookbook-adaptive-card-evaluate-supplier-performance"
description: "Generates a read-only Adaptive Card JSON file visualizing supplier performance status from Dynamics 365 F&SCM (legal entity USMF), with a header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_evaluate_supplier_performance", "rar_sha256": "d171701aa932eb9622554c1a2ec2070c648267b33a2acd816fc30c07f0ebb7ae", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_evaluate_supplier_performance`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_evaluate_supplier_performance_agent.py` and in the RCI capsule.

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

Evaluate supplier performance Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing supplier performance status from Dynamics 365 F&SCM (legal entity USMF), with a header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-evaluate-supplier-performance
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
      "description": "The date the snapshot represents, used in the card header timestamp and filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "The D365 F&SCM legal entity to read from, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-evaluate-supplier-performance-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_evaluate_supplier_performance_agent.py` and embedded as the fenced Python below (sha256 d171701aa932eb96…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_evaluate_supplier_performance_agent.py` first:

```bash
python3 adaptive_card_evaluate_supplier_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_evaluate_supplier_performance_agent.py   # or on stdin
python3 adaptive_card_evaluate_supplier_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Evaluate supplier performance Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing supplier performance status from Dynamics 365 F&SCM (legal entity USMF), with a header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-evaluate-supplier-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_evaluate_supplier_performance',
    "version": '3.0.2',
    "display_name": 'Evaluate supplier performance Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing supplier performance status from Dynamics 365 F&SCM (legal entity USMF), with a header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-evaluate-supplier-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-evaluate-supplier-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ca528cbd3bb3451c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/evaluate-supplier-performance'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/adaptive-card-evaluate-supplier-performance', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'The date the snapshot represents, used in the card header timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'The D365 F&SCM legal entity to read from, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-evaluate-supplier-performance-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical evaluate supplier performance status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-evaluate-supplier-performance-2026-05-24-card.json' that visualizes the current state of evaluate supplier performance. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current evaluate supplier performance KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing supplier performance status from Dynamics 365 F&SCM (legal entity USMF), with a header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons.', 'example_request': 'Make an Adaptive Card of supplier performance status for USMF as of 2026-05-24.', 'inputs': [{'description': 'The D365 F&SCM legal entity to read from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-evaluate-supplier-performance-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'The date the snapshot represents, used in the card header timestamp and filename.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a supplier performance status snapshot as an Adaptive Card to embed in Teams, Outlook, or a dashboard. No data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardEvaluateSupplierPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardEvaluateSupplierPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'The date the snapshot represents, used in the card header timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'The D365 F&SCM legal entity to read from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-evaluate-supplier-performance-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardEvaluateSupplierPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
