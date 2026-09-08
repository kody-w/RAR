---
name: "rar-cowork-cookbook-adaptive-card-receive-supplier-credits"
description: "Generates a read-only Adaptive Card JSON file visualizing receive supplier credits status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_receive_supplier_credits", "rar_sha256": "6235404a057406264f3c01ac0ed3df19adc7d1cb56459270c8c4eb7281e18c80", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_receive_supplier_credits`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_receive_supplier_credits_agent.py` and in the RCI capsule.

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

Receive supplier credits Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing receive supplier credits status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-receive-supplier-credits
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
      "description": "Date the snapshot represents, used in the card timestamp and filename.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-receive-supplier-credits-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_receive_supplier_credits_agent.py` and embedded as the fenced Python below (sha256 6235404a05740626…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_receive_supplier_credits_agent.py` first:

```bash
python3 adaptive_card_receive_supplier_credits_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_receive_supplier_credits_agent.py   # or on stdin
python3 adaptive_card_receive_supplier_credits_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Receive supplier credits Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing receive supplier credits status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-receive-supplier-credits
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_receive_supplier_credits',
    "version": '3.0.2',
    "display_name": 'Receive supplier credits Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing receive supplier credits status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.',
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
        "upstream_slug": 'adaptive-card-receive-supplier-credits',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-receive-supplier-credits',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6f6f28d6190af570',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/receive-supplier-credits'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/adaptive-card-receive-supplier-credits', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date the snapshot represents, used in the card timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-receive-supplier-credits-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical receive supplier credits status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-receive-supplier-credits-2026-05-24-card.json' that visualizes the current state of receive supplier credits. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current receive supplier credits KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing receive supplier credits status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.', 'example_request': 'Make an Adaptive Card showing receive supplier credits status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date the snapshot represents, used in the card timestamp and filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-receive-supplier-credits-2026-05-24-card.json.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of receive supplier credits status from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardReceiveSupplierCredits(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardReceiveSupplierCredits'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date the snapshot represents, used in the card timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-receive-supplier-credits-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardReceiveSupplierCredits().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
