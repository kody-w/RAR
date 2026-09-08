---
name: "rar-cowork-cookbook-adaptive-card-define-service-contracts"
description: "Generates a read-only Adaptive Card JSON file visualizing define service contracts status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_service_contracts", "rar_sha256": "4317780fad0deb03f437c454a6141ea4ab2ef6efdb015995ebc1f1afc54e6a4b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
