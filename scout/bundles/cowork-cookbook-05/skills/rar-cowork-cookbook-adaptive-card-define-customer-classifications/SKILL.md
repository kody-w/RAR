---
name: "rar-cowork-cookbook-adaptive-card-define-customer-classifications"
description: "Generates a read-only Adaptive Card JSON file visualizing customer classification setup status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_customer_classifications", "rar_sha256": "137ccf982f3a5efba4f670468f7f489cb7b1a7ad8df8bc76f96984593f536f31", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
