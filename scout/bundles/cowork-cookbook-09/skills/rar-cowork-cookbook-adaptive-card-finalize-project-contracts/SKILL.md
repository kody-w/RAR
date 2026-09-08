---
name: "rar-cowork-cookbook-adaptive-card-finalize-project-contracts"
description: "Generates a read-only Adaptive Card JSON file visualizing finalize-project-contracts status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_finalize_project_contracts", "rar_sha256": "328d9aab9b45c3942d1265e658b3a3da7b8ef32b2a883b5fd94e1e5796b08017", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_finalize_project_contracts`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_finalize_project_contracts_agent.py` and in the RCI capsule.

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

Finalize project contracts Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing finalize-project-contracts status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-finalize-project-contracts
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-finalize-project-contracts-2026-05-24-card.json.",
      "type": "string"
    },
    "snapshot_date": {
      "description": "Date the status snapshot reflects, used in the card header timestamp and filename.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_finalize_project_contracts_agent.py` and embedded as the fenced Python below (sha256 328d9aab9b45c394…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_finalize_project_contracts_agent.py` first:

```bash
python3 adaptive_card_finalize_project_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_finalize_project_contracts_agent.py   # or on stdin
python3 adaptive_card_finalize_project_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Finalize project contracts Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing finalize-project-contracts status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-finalize-project-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_finalize_project_contracts',
    "version": '3.0.2',
    "display_name": 'Finalize project contracts Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing finalize-project-contracts status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-finalize-project-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-finalize-project-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6bfbfd5a6050c082',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/finalize-project-contracts'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/adaptive-card-finalize-project-contracts', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-finalize-project-contracts-2026-05-24-card.json.', 'snapshot_date': 'Date the status snapshot reflects, used in the card header timestamp and filename.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical finalize project contracts status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-finalize-project-contracts-2026-05-24-card.json' that visualizes the current state of finalize project contracts. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current finalize project contracts KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing finalize-project-contracts status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card showing finalize project contracts status in USMF for 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-finalize-project-contracts-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date the status snapshot reflects, used in the card header timestamp and filename.', 'name': 'snapshot_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an Adaptive Card snapshot of finalize project contracts status to embed in Teams, Outlook, or a dashboard. No data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardFinalizeProjectContracts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardFinalizeProjectContracts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-finalize-project-contracts-2026-05-24-card.json.', 'type': 'string'}, 'snapshot_date': {'description': 'Date the status snapshot reflects, used in the card header timestamp and filename.', 'type': 'string'}},
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
    print(AdaptiveCardFinalizeProjectContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
