---
name: "rar-cowork-cookbook-adaptive-card-create-and-track-tasks-for-a-case"
description: "Generates a read-only Adaptive Card JSON file visualizing create-and-track-tasks-for-a-case status from Dynamics 365 ERP (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_create_and_track_tasks_for_a_case", "rar_sha256": "8893c1e06fe51a0b1139af45eaa9c811f76f141ab4d85f7891619affa320797b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_create_and_track_tasks_for_a_case`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_create_and_track_tasks_for_a_case_agent.py` and in the RCI capsule.

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

Create and track tasks for a case Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing create-and-track-tasks-for-a-case status from Dynamics 365 ERP (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-create-and-track-tasks-for-a-case
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
      "description": "Date used for the card timestamp and filename.",
      "type": "string"
    },
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-create-and-track-tasks-for-a-case-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_create_and_track_tasks_for_a_case_agent.py` and embedded as the fenced Python below (sha256 8893c1e06fe51a0b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_create_and_track_tasks_for_a_case_agent.py` first:

```bash
python3 adaptive_card_create_and_track_tasks_for_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_create_and_track_tasks_for_a_case_agent.py   # or on stdin
python3 adaptive_card_create_and_track_tasks_for_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create and track tasks for a case Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing create-and-track-tasks-for-a-case status from Dynamics 365 ERP (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-create-and-track-tasks-for-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_create_and_track_tasks_for_a_case',
    "version": '3.0.2',
    "display_name": 'Create and track tasks for a case Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing create-and-track-tasks-for-a-case status from Dynamics 365 ERP (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-create-and-track-tasks-for-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-create-and-track-tasks-for-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a932a607d862c59d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/create-and-track-tasks-for-a-case'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/adaptive-card-create-and-track-tasks-for-a-case', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-create-and-track-tasks-for-a-case-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical create and track tasks for a case status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-create-and-track-tasks-for-a-case-2026-05-24-card.json' that visualizes the current state of create and track tasks for a case. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current create and track tasks for a case KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing create-and-track-tasks-for-a-case status from Dynamics 365 ERP (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of case task status from D365 USMF for today, ready to drop into Teams.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-create-and-track-tasks-for-a-case-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and filename.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an embeddable Adaptive Card snapshot of case task status from D365 F&SCM for Teams, Outlook, or a dashboard, without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardCreateAndTrackTasksForACase(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardCreateAndTrackTasksForACase'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-create-and-track-tasks-for-a-case-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardCreateAndTrackTasksForACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
