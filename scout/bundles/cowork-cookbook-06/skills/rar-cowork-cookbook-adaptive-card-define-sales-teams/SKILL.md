---
name: "rar-cowork-cookbook-adaptive-card-define-sales-teams"
description: "Generates a read-only Adaptive Card JSON file visualizing define sales teams status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_sales_teams", "rar_sha256": "34fd94c017a473aa96c22ac7df8acb4983d8f11bb7aef2e3e7e1d4fad880f36e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_sales_teams`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_sales_teams_agent.py` and in the RCI capsule.

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

Define sales teams Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing define sales teams status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-sales-teams
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
      "description": "Date the snapshot represents, used in the timestamp and filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_count": {
      "description": "Number of KPI tiles to include (3-5).",
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
      "description": "Name of the Adaptive Card JSON file to produce.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_sales_teams_agent.py` and embedded as the fenced Python below (sha256 34fd94c017a473aa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_sales_teams_agent.py` first:

```bash
python3 adaptive_card_define_sales_teams_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_sales_teams_agent.py   # or on stdin
python3 adaptive_card_define_sales_teams_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define sales teams Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing define sales teams status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-sales-teams
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_sales_teams',
    "version": '3.0.2',
    "display_name": 'Define sales teams Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing define sales teams status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-sales-teams',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-sales-teams',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c85f8ef5bec40be8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/define-sales-teams'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/adaptive-card-define-sales-teams', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'as_of_date': 'Date the snapshot represents, used in the timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'Number of KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical define sales teams status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-define-sales-teams-2026-05-24-card.json' that visualizes the current state of define sales teams. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current define sales teams KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing define sales teams status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card JSON of define sales teams status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date the snapshot represents, used in the timestamp and filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}, {'description': 'Number of KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of define sales teams status pulled from D365 ERP without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardDefineSalesTeams(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineSalesTeams'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date the snapshot represents, used in the timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'Number of KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}},
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
    print(AdaptiveCardDefineSalesTeams().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
