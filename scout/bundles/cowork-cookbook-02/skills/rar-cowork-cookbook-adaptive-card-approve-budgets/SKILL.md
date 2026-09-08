---
name: "rar-cowork-cookbook-adaptive-card-approve-budgets"
description: "Generates a read-only Adaptive Card JSON file visualizing approve budgets status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_approve_budgets", "rar_sha256": "8a60430f1918309e3a0a091f120d4d2d5baee5138a38a29c378fe7712a6de8ed", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_approve_budgets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_approve_budgets_agent.py` and in the RCI capsule.

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

Approve budgets Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing approve budgets status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-approve-budgets
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
      "description": "Date used for the snapshot and in the output filename, e.g. 2026-05-24.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-approve-budgets-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_approve_budgets_agent.py` and embedded as the fenced Python below (sha256 8a60430f1918309e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_approve_budgets_agent.py` first:

```bash
python3 adaptive_card_approve_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_approve_budgets_agent.py   # or on stdin
python3 adaptive_card_approve_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Approve budgets Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing approve budgets status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-approve-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_approve_budgets',
    "version": '3.0.2',
    "display_name": 'Approve budgets Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing approve budgets status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-approve-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-approve-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ae58edc5f618b4c7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/approve-budgets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-approve-budgets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the snapshot and in the output filename, e.g. 2026-05-24.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-approve-budgets-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical approve budgets status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-approve-budgets-2026-05-24-card.json' that visualizes the current state of approve budgets. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current approve budgets KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing approve budgets status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card showing approve budgets status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used for the snapshot and in the output filename, e.g. 2026-05-24.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-approve-budgets-2026-05-24-card.json.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an Adaptive Card snapshot of approve budgets status to embed in Teams, Outlook, or a dashboard, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardApproveBudgets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardApproveBudgets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the snapshot and in the output filename, e.g. 2026-05-24.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-approve-budgets-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardApproveBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
