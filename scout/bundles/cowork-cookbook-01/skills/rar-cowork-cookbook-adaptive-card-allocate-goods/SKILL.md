---
name: "rar-cowork-cookbook-adaptive-card-allocate-goods"
description: "Generates a read-only Adaptive Card JSON file visualizing allocate goods status from Dynamics 365 F&SCM for a legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_allocate_goods", "rar_sha256": "f59e7dbbd2e83fcb199a482a4b842e93db794de6f3bffdc2657740ed43ed076b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
