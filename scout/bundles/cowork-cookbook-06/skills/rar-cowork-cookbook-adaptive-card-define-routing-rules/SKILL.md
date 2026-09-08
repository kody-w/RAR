---
name: "rar-cowork-cookbook-adaptive-card-define-routing-rules"
description: "Generates a read-only Adaptive Card JSON file visualizing define routing rules status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_routing_rules", "rar_sha256": "1c2dfb0b1b635a266eb9186ff98efa4cb4768c46c1bfbbd2ada66832e3125804", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
