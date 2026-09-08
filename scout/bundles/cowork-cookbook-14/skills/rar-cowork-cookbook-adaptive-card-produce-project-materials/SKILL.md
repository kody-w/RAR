---
name: "rar-cowork-cookbook-adaptive-card-produce-project-materials"
description: "Generates a read-only Adaptive Card JSON file snapshotting produce project materials status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_produce_project_materials", "rar_sha256": "9d0301b5c60d25d20589b542d1a411d08f95aa3e0cbf4b46180e7b8e17a251f1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_produce_project_materials`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_produce_project_materials_agent.py` and in the RCI capsule.

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

Produce project materials Status Adaptive Card — Generates a read-only Adaptive Card JSON file snapshotting produce project materials status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-produce-project-materials
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
    },
    "snapshot_date": {
      "description": "Date used in the card timestamp and output filename.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_produce_project_materials_agent.py` and embedded as the fenced Python below (sha256 9d0301b5c60d25d2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_produce_project_materials_agent.py` first:

```bash
python3 adaptive_card_produce_project_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_produce_project_materials_agent.py   # or on stdin
python3 adaptive_card_produce_project_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Produce project materials Status Adaptive Card — Generates a read-only Adaptive Card JSON file snapshotting produce project materials status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-produce-project-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_produce_project_materials',
    "version": '3.0.2',
    "display_name": 'Produce project materials Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file snapshotting produce project materials status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-produce-project-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-produce-project-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3c1a7df59d48ae22',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/produce-project-materials'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/adaptive-card-produce-project-materials', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce.', 'snapshot_date': 'Date used in the card timestamp and output filename.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical produce project materials status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-produce-project-materials-2026-05-24-card.json' that visualizes the current state of produce project materials. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current produce project materials KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file snapshotting produce project materials status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of produce project materials status in USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date used in the card timestamp and output filename.', 'name': 'snapshot_date'}, {'description': 'Name of the Adaptive Card JSON file to produce.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-renderable Adaptive Card showing current produce project materials status from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardProduceProjectMaterials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardProduceProjectMaterials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce.', 'type': 'string'}, 'snapshot_date': {'description': 'Date used in the card timestamp and output filename.', 'type': 'string'}},
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
    print(AdaptiveCardProduceProjectMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
