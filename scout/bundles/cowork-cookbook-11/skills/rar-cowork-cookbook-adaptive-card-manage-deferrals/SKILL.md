---
name: "rar-cowork-cookbook-adaptive-card-manage-deferrals"
description: "Generates a read-only Adaptive Card JSON file visualizing manage deferrals status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_deferrals", "rar_sha256": "16ea3f507018aec5d50f50743f124e9ab09fb5771d1eff27d0b909fc8701ea29", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_deferrals`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_deferrals_agent.py` and in the RCI capsule.

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

Manage deferrals Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing manage deferrals status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-deferrals
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
      "description": "Date used for the card timestamp and output filename.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_deferrals_agent.py` and embedded as the fenced Python below (sha256 16ea3f507018aec5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_deferrals_agent.py` first:

```bash
python3 adaptive_card_manage_deferrals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_deferrals_agent.py   # or on stdin
python3 adaptive_card_manage_deferrals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage deferrals Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing manage deferrals status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-deferrals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_deferrals',
    "version": '3.0.2',
    "display_name": 'Manage deferrals Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing manage deferrals status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-deferrals',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-deferrals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3299af75815b00b4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/manage-deferrals'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-manage-deferrals', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'as_of_date': 'Date used for the card timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical manage deferrals status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-manage-deferrals-2026-05-24-card.json' that visualizes the current state of manage deferrals. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current manage deferrals KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing manage deferrals status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of manage deferrals status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used for the card timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-renderable Adaptive Card snapshot of manage deferrals status from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardManageDeferrals(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageDeferrals'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date used for the card timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}},
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
    print(AdaptiveCardManageDeferrals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
