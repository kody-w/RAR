---
name: "rar-cowork-cookbook-adaptive-card-approve-budgets"
description: "Generates a read-only Adaptive Card JSON file visualizing approve budgets status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_approve_budgets", "rar_sha256": "8a60430f1918309e3a0a091f120d4d2d5baee5138a38a29c378fe7712a6de8ed", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
