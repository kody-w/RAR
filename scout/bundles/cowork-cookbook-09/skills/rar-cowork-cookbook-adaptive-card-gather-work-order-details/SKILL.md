---
name: "rar-cowork-cookbook-adaptive-card-gather-work-order-details"
description: "Generates a read-only Adaptive Card JSON file visualizing gather work order details status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_gather_work_order_details", "rar_sha256": "842f9e6e42b90eab9f845b64f7f1fede76fd633e3fcc063db842247244d676cf", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_gather_work_order_details`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_gather_work_order_details_agent.py` and in the RCI capsule.

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

Gather work order details Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing gather work order details status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-gather-work-order-details
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
      "description": "Date/timestamp the card snapshot represents.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-gather-work-order-details-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_gather_work_order_details_agent.py` and embedded as the fenced Python below (sha256 842f9e6e42b90eab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_gather_work_order_details_agent.py` first:

```bash
python3 adaptive_card_gather_work_order_details_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_gather_work_order_details_agent.py   # or on stdin
python3 adaptive_card_gather_work_order_details_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Gather work order details Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing gather work order details status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-gather-work-order-details
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_gather_work_order_details',
    "version": '3.0.2',
    "display_name": 'Gather work order details Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing gather work order details status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-gather-work-order-details',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-gather-work-order-details',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ea770f9d4c3681b4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/gather-work-order-details'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/adaptive-card-gather-work-order-details', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date/timestamp the card snapshot represents.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-gather-work-order-details-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical gather work order details status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-gather-work-order-details-2026-05-24-card.json' that visualizes the current state of gather work order details. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current gather work order details KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing gather work order details status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing gather work order details status in USMF for today, ready to post in Teams.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-gather-work-order-details-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date/timestamp the card snapshot represents.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of gather work order details status for Teams, Outlook, or a dashboard, without changing D365 data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardGatherWorkOrderDetails(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardGatherWorkOrderDetails'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date/timestamp the card snapshot represents.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-gather-work-order-details-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardGatherWorkOrderDetails().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
