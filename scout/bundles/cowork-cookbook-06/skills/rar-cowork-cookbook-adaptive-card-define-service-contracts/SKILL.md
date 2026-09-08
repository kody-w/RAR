---
name: "rar-cowork-cookbook-adaptive-card-define-service-contracts"
description: "Generates a read-only Adaptive Card JSON file visualizing define service contracts status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_service_contracts", "rar_sha256": "4317780fad0deb03f437c454a6141ea4ab2ef6efdb015995ebc1f1afc54e6a4b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_service_contracts`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_service_contracts_agent.py` and in the RCI capsule.

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

Define service contracts Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing define service contracts status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-service-contracts
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
    "action_buttons": {
      "description": "The 2-3 action buttons to place on the card.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Date the snapshot represents, used in the timestamp and file name.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "How many KPI tiles to include (3-5).",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-service-contracts-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_service_contracts_agent.py` and embedded as the fenced Python below (sha256 4317780fad0deb03…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_service_contracts_agent.py` first:

```bash
python3 adaptive_card_define_service_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_service_contracts_agent.py   # or on stdin
python3 adaptive_card_define_service_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service contracts Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing define service contracts status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-service-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_service_contracts',
    "version": '3.0.2',
    "display_name": 'Define service contracts Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing define service contracts status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-define-service-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-service-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '10bcbf545da6e806',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/define-service-contracts'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/adaptive-card-define-service-contracts', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'as_of_date': 'Date the snapshot represents, used in the timestamp and file name.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_file_name': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-service-contracts-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical define service contracts status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-define-service-contracts-2026-05-24-card.json' that visualizes the current state of define service contracts. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current define service contracts KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing define service contracts status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing define service contracts status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date the snapshot represents, used in the timestamp and file name.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-service-contracts-2026-05-24-card.json.', 'name': 'output_file_name'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of define service contracts status from D365 ERP data, without changing any records.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDefineServiceContracts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineServiceContracts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date the snapshot represents, used in the timestamp and file name.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_file_name': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-service-contracts-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDefineServiceContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
