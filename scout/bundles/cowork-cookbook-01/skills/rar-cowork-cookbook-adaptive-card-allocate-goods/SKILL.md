---
name: "rar-cowork-cookbook-adaptive-card-allocate-goods"
description: "Generates a read-only Adaptive Card JSON file visualizing allocate goods status from Dynamics 365 F&SCM for a legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_allocate_goods", "rar_sha256": "f59e7dbbd2e83fcb199a482a4b842e93db794de6f3bffdc2657740ed43ed076b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_allocate_goods`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_allocate_goods_agent.py` and in the RCI capsule.

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

Allocate goods Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing allocate goods status from Dynamics 365 F&SCM for a legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-allocate-goods
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
    "output_file_name": {
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-allocate-goods-2026-05-24-card.json.",
      "type": "string"
    },
    "snapshot_date": {
      "description": "Date the status snapshot represents, used in the card header timestamp and file name.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_allocate_goods_agent.py` and embedded as the fenced Python below (sha256 f59e7dbbd2e83fcb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_allocate_goods_agent.py` first:

```bash
python3 adaptive_card_allocate_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_allocate_goods_agent.py   # or on stdin
python3 adaptive_card_allocate_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate goods Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing allocate goods status from Dynamics 365 F&SCM for a legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-allocate-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_allocate_goods',
    "version": '3.0.2',
    "display_name": 'Allocate goods Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing allocate goods status from Dynamics 365 F&SCM for a legal entity, with header, KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-allocate-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-allocate-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8e87f67f0f5de48d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/allocate-goods'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-allocate-goods', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_file_name': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-allocate-goods-2026-05-24-card.json.', 'snapshot_date': 'Date the status snapshot represents, used in the card header timestamp and file name.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical allocate goods status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-allocate-goods-2026-05-24-card.json' that visualizes the current state of allocate goods. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current allocate goods KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing allocate goods status from Dynamics 365 F&SCM for a legal entity, with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of allocate goods status in USMF for 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-allocate-goods-2026-05-24-card.json.', 'name': 'output_file_name'}, {'description': 'Date the status snapshot represents, used in the card header timestamp and file name.', 'name': 'snapshot_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an embeddable Adaptive Card snapshot of allocate goods status for Teams, Outlook, or a dashboard. No data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardAllocateGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAllocateGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_file_name': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-allocate-goods-2026-05-24-card.json.', 'type': 'string'}, 'snapshot_date': {'description': 'Date the status snapshot represents, used in the card header timestamp and file name.', 'type': 'string'}},
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
    print(AdaptiveCardAllocateGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
