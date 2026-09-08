---
name: "rar-cowork-cookbook-adaptive-card-schedule-dock-appointments"
description: "Generates a read-only Adaptive Card JSON file visualizing dock appointment scheduling status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_schedule_dock_appointments", "rar_sha256": "adb0cb697f772fd0286e2831388be0b9350a12ad27254a9286ace1e6f0d60a1f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_schedule_dock_appointments`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_schedule_dock_appointments_agent.py` and in the RCI capsule.

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

Schedule dock appointments Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing dock appointment scheduling status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-schedule-dock-appointments
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
      "description": "Snapshot date used in the card timestamp and output filename.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 F&SCM legal entity to report on (e.g. USMF).",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-schedule-dock-appointments-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_schedule_dock_appointments_agent.py` and embedded as the fenced Python below (sha256 adb0cb697f772fd0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_schedule_dock_appointments_agent.py` first:

```bash
python3 adaptive_card_schedule_dock_appointments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_schedule_dock_appointments_agent.py   # or on stdin
python3 adaptive_card_schedule_dock_appointments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Schedule dock appointments Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing dock appointment scheduling status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-schedule-dock-appointments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_schedule_dock_appointments',
    "version": '3.0.2',
    "display_name": 'Schedule dock appointments Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing dock appointment scheduling status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-schedule-dock-appointments',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-schedule-dock-appointments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '64d2e1e708d9fdb5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/schedule-dock-appointments'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-schedule-dock-appointments', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Snapshot date used in the card timestamp and output filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-schedule-dock-appointments-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical schedule dock appointments status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-schedule-dock-appointments-2026-05-24-card.json' that visualizes the current state of schedule dock appointments. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current schedule dock appointments KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing dock appointment scheduling status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons.', 'example_request': 'Make me an Adaptive Card showing dock appointment status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 F&SCM legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Snapshot date used in the card timestamp and output filename.', 'name': 'as_of_date'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-schedule-dock-appointments-2026-05-24-card.json.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of dock appointment status for Teams, Outlook, or a dashboard. Read-only; no data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardScheduleDockAppointments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardScheduleDockAppointments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Snapshot date used in the card timestamp and output filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-schedule-dock-appointments-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardScheduleDockAppointments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
