---
name: "rar-cowork-cookbook-adaptive-card-evaluate-supplier-performance"
description: "Generates a read-only Adaptive Card JSON file visualizing supplier performance status from Dynamics 365 F&SCM (legal entity USMF), with a header, 3-5 KPI tiles with trend arrows, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_evaluate_supplier_performance", "rar_sha256": "d171701aa932eb9622554c1a2ec2070c648267b33a2acd816fc30c07f0ebb7ae", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
