---
name: "rar-cowork-cookbook-adaptive-card-define-warehouse-management-kpis"
description: "Generates a read-only Adaptive Card JSON file visualizing warehouse management KPI status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_warehouse_management_kpis", "rar_sha256": "a33e7a0f7adb8b989bce268d7377b969e5d804c3f778737568baf5fbfa99de05", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_warehouse_management_kpis`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_warehouse_management_kpis_agent.py` and in the RCI capsule.

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

Define warehouse management KPIs Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing warehouse management KPI status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-warehouse-management-kpis
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to read KPIs from (e.g. USMF).",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-warehouse-management-kpis-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_warehouse_management_kpis_agent.py` and embedded as the fenced Python below (sha256 a33e7a0f7adb8b98…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_warehouse_management_kpis_agent.py` first:

```bash
python3 adaptive_card_define_warehouse_management_kpis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_warehouse_management_kpis_agent.py   # or on stdin
python3 adaptive_card_define_warehouse_management_kpis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define warehouse management KPIs Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing warehouse management KPI status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-warehouse-management-kpis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_warehouse_management_kpis',
    "version": '3.0.2',
    "display_name": 'Define warehouse management KPIs Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing warehouse management KPI status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-warehouse-management-kpis',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-warehouse-management-kpis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ea2dadab3875024f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/analyze-warehouse-operations/define-warehouse-management-kpis'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-define-warehouse-management-kpis', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to read KPIs from (e.g. USMF).', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-warehouse-management-kpis-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical define warehouse management KPIs status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-define-warehouse-management-kpis-2026-05-24-card.json' that visualizes the current state of define warehouse management KPIs. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current define warehouse management KPIs KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing warehouse management KPI status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card showing warehouse management KPIs for USMF that I can drop into Teams.', 'inputs': [{'description': 'D365 F&SCM legal entity to read KPIs from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-warehouse-management-kpis-2026-05-24-card.json.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an Adaptive Card snapshot of warehouse management KPIs from D365 F&SCM to embed in Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDefineWarehouseManagementKpis(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineWarehouseManagementKpis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to read KPIs from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-warehouse-management-kpis-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDefineWarehouseManagementKpis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
