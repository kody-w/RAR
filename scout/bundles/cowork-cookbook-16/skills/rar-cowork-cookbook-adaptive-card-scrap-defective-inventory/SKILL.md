---
name: "rar-cowork-cookbook-adaptive-card-scrap-defective-inventory"
description: "Generates a read-only Adaptive Card JSON file summarizing scrap defective inventory status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_scrap_defective_inventory", "rar_sha256": "bf192d9d5666ebaa7178bb920036b009b636f9759a93bca89cef43d53096a9fe", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
