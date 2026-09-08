---
name: "rar-cowork-cookbook-adaptive-card-define-routing-rules"
description: "Generates a read-only Adaptive Card JSON file visualizing define routing rules status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_routing_rules", "rar_sha256": "1c2dfb0b1b635a266eb9186ff98efa4cb4768c46c1bfbbd2ada66832e3125804", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_routing_rules`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_routing_rules_agent.py` and in the RCI capsule.

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

Define routing rules Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing define routing rules status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-routing-rules
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
      "description": "The 2-3 action buttons to include on the card.",
      "type": "string"
    },
    "as_of_date": {
      "description": "Date the snapshot represents, used in the output filename and header timestamp.",
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
      "description": "D365 legal entity to report against, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-routing-rules-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_routing_rules_agent.py` and embedded as the fenced Python below (sha256 1c2dfb0b1b635a26…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_routing_rules_agent.py` first:

```bash
python3 adaptive_card_define_routing_rules_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_routing_rules_agent.py   # or on stdin
python3 adaptive_card_define_routing_rules_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define routing rules Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing define routing rules status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-routing-rules
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_routing_rules',
    "version": '3.0.2',
    "display_name": 'Define routing rules Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing define routing rules status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-routing-rules',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-routing-rules',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cec170e55a206e23',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-routing-rules'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/adaptive-card-define-routing-rules', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to include on the card.', 'as_of_date': 'Date the snapshot represents, used in the output filename and header timestamp.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-routing-rules-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical define routing rules status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-define-routing-rules-2026-05-24-card.json' that visualizes the current state of define routing rules. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current define routing rules KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing define routing rules status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing define routing rules status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date the snapshot represents, used in the output filename and header timestamp.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-routing-rules-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to include on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of define routing rules status from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDefineRoutingRules(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineRoutingRules'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to include on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date the snapshot represents, used in the output filename and header timestamp.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-define-routing-rules-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardDefineRoutingRules().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
