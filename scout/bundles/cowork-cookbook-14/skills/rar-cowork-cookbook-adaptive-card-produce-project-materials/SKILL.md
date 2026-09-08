---
name: "rar-cowork-cookbook-adaptive-card-produce-project-materials"
description: "Generates a read-only Adaptive Card JSON file snapshotting produce project materials status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_produce_project_materials", "rar_sha256": "9d0301b5c60d25d20589b542d1a411d08f95aa3e0cbf4b46180e7b8e17a251f1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
