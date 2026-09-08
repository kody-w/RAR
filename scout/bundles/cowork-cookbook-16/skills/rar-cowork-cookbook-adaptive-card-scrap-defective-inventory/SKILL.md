---
name: "rar-cowork-cookbook-adaptive-card-scrap-defective-inventory"
description: "Generates a read-only Adaptive Card JSON file summarizing scrap defective inventory status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_scrap_defective_inventory", "rar_sha256": "bf192d9d5666ebaa7178bb920036b009b636f9759a93bca89cef43d53096a9fe", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_scrap_defective_inventory`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_scrap_defective_inventory_agent.py` and in the RCI capsule.

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

Scrap defective inventory Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing scrap defective inventory status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-scrap-defective-inventory
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
      "description": "Date/timestamp the snapshot represents, used in the card header and filename.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-scrap-defective-inventory-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_scrap_defective_inventory_agent.py` and embedded as the fenced Python below (sha256 bf192d9d5666ebaa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_scrap_defective_inventory_agent.py` first:

```bash
python3 adaptive_card_scrap_defective_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_scrap_defective_inventory_agent.py   # or on stdin
python3 adaptive_card_scrap_defective_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Scrap defective inventory Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing scrap defective inventory status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-scrap-defective-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_scrap_defective_inventory',
    "version": '3.0.2',
    "display_name": 'Scrap defective inventory Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing scrap defective inventory status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-scrap-defective-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-scrap-defective-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c976fa5120880212',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/scrap-defective-inventory'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-scrap-defective-inventory', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date/timestamp the snapshot represents, used in the card header and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-scrap-defective-inventory-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical scrap defective inventory status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-scrap-defective-inventory-2026-05-24-card.json' that visualizes the current state of scrap defective inventory. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current scrap defective inventory KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing scrap defective inventory status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of scrap defective inventory status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-scrap-defective-inventory-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date/timestamp the snapshot represents, used in the card header and filename.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of scrap defective inventory status for Teams, Outlook, or a dashboard, without changing D365 data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardScrapDefectiveInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardScrapDefectiveInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date/timestamp the snapshot represents, used in the card header and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-scrap-defective-inventory-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardScrapDefectiveInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
