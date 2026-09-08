---
name: "rar-cowork-cookbook-adaptive-card-create-and-track-tasks-for-a-case"
description: "Generates a read-only Adaptive Card JSON file visualizing create-and-track-tasks-for-a-case status from Dynamics 365 ERP (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_create_and_track_tasks_for_a_case", "rar_sha256": "8893c1e06fe51a0b1139af45eaa9c811f76f141ab4d85f7891619affa320797b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
