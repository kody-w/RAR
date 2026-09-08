---
name: "rar-cowork-cookbook-adaptive-card-schedule-dock-appointments"
description: "Generates a read-only Adaptive Card JSON file visualizing dock appointment scheduling status from Dynamics 365 F&SCM (legal entity USMF), with header, KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_schedule_dock_appointments", "rar_sha256": "adb0cb697f772fd0286e2831388be0b9350a12ad27254a9286ace1e6f0d60a1f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
