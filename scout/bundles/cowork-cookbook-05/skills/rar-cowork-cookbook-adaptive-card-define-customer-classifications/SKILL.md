---
name: "rar-cowork-cookbook-adaptive-card-define-customer-classifications"
description: "Generates a read-only Adaptive Card JSON file visualizing customer classification setup status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_customer_classifications", "rar_sha256": "137ccf982f3a5efba4f670468f7f489cb7b1a7ad8df8bc76f96984593f536f31", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_customer_classifications`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_customer_classifications_agent.py` and in the RCI capsule.

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

Define customer classifications Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing customer classification setup status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-customer-classifications
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
      "description": "Date used for the card timestamp and filename.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-customer-classifications-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_customer_classifications_agent.py` and embedded as the fenced Python below (sha256 137ccf982f3a5efb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_customer_classifications_agent.py` first:

```bash
python3 adaptive_card_define_customer_classifications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_customer_classifications_agent.py   # or on stdin
python3 adaptive_card_define_customer_classifications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define customer classifications Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing customer classification setup status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-customer-classifications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_customer_classifications',
    "version": '3.0.2',
    "display_name": 'Define customer classifications Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing customer classification setup status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-define-customer-classifications',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-customer-classifications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c4dd18f098f23533',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-customer-classifications'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-define-customer-classifications', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-customer-classifications-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical define customer classifications status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-define-customer-classifications-2026-05-24-card.json' that visualizes the current state of define customer classifications. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current define customer classifications KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing customer classification setup status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON for define customer classifications status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-customer-classifications-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and filename.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of define-customer-classifications status from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDefineCustomerClassifications(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineCustomerClassifications'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-customer-classifications-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDefineCustomerClassifications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
