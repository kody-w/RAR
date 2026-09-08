---
name: "rar-cowork-cookbook-adaptive-card-process-customer-refunds"
description: "Generates a read-only Adaptive Card JSON file visualizing process customer refunds status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_process_customer_refunds", "rar_sha256": "4d65203c89a0d6049c25283f4084206be8cceab217c47b709702c38c1516d55f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_process_customer_refunds`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_process_customer_refunds_agent.py` and in the RCI capsule.

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

Process customer refunds Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing process customer refunds status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-process-customer-refunds
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
      "description": "Date the card snapshot represents, used in the output filename and timestamp.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-process-customer-refunds-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_process_customer_refunds_agent.py` and embedded as the fenced Python below (sha256 4d65203c89a0d604…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_process_customer_refunds_agent.py` first:

```bash
python3 adaptive_card_process_customer_refunds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_process_customer_refunds_agent.py   # or on stdin
python3 adaptive_card_process_customer_refunds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer refunds Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing process customer refunds status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-process-customer-refunds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_process_customer_refunds',
    "version": '3.0.2',
    "display_name": 'Process customer refunds Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing process customer refunds status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-process-customer-refunds',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-process-customer-refunds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6dfa7476d5fe1855',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-refunds'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-process-customer-refunds', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date the card snapshot represents, used in the output filename and timestamp.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-process-customer-refunds-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical process customer refunds status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-process-customer-refunds-2026-05-24-card.json' that visualizes the current state of process customer refunds. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current process customer refunds KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing process customer refunds status from Dynamics 365 F&SCM (legal entity USMF), with header, 3-5 KPI tiles, a RAG row, and 2-3 action buttons.', 'example_request': 'Make me an Adaptive Card showing process customer refunds status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date the card snapshot represents, used in the output filename and timestamp.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-process-customer-refunds-2026-05-24-card.json.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of customer refund processing status for Teams, Outlook, or a dashboard. No data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardProcessCustomerRefunds(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardProcessCustomerRefunds'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date the card snapshot represents, used in the output filename and timestamp.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-process-customer-refunds-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardProcessCustomerRefunds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
