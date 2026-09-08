---
name: "rar-cowork-cookbook-adaptive-card-manage-deferrals"
description: "Generates a read-only Adaptive Card JSON file visualizing manage deferrals status from Dynamics 365 F&SCM for a given legal entity, with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_deferrals", "rar_sha256": "16ea3f507018aec5d50f50743f124e9ab09fb5771d1eff27d0b909fc8701ea29", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
