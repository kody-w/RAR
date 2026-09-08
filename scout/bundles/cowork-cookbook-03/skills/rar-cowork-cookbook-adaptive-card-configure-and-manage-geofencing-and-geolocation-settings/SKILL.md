---
name: "rar-cowork-cookbook-adaptive-card-configure-and-manage-geofencing-and-geolocation-settings"
description: "Generates a read-only Adaptive Card JSON file summarizing geofencing and geolocation settings status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_and_manage_geofencing_and_geolocation_settings", "rar_sha256": "7ac60928b413629764ec854f1c7ee41a77db6f0c1b4fede8111d0926a87b9322", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_configure_and_manage_geofencing_and_geolocation_settings`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_configure_and_manage_geofencing_and_geolocation_settings_agent.py` and in the RCI capsule.

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

Configure and manage geofencing and geolocation settings Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing geofencing and geolocation settings status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-geofencing-and-geolocation-settings
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
      "description": "Date used for the card timestamp and file name.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to read from, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-and-manage-geofencing-and-geolocation-settings-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_configure_and_manage_geofencing_and_geolocation_settings_agent.py` and embedded as the fenced Python below (sha256 7ac60928b4136297…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_configure_and_manage_geofencing_and_geolocation_settings_agent.py` first:

```bash
python3 adaptive_card_configure_and_manage_geofencing_and_geolocation_settings_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_configure_and_manage_geofencing_and_geolocation_settings_agent.py   # or on stdin
python3 adaptive_card_configure_and_manage_geofencing_and_geolocation_settings_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage geofencing and geolocation settings Status Adaptive Card — Generates a read-only Adaptive Card JSON file summarizing geofencing and geolocation settings status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-geofencing-and-geolocation-settings
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_configure_and_manage_geofencing_and_geolocation_settings',
    "version": '3.0.2',
    "display_name": 'Configure and manage geofencing and geolocation settings Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file summarizing geofencing and geolocation settings status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and action buttons.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-configure-and-manage-geofencing-and-geolocation-settings',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-configure-and-manage-geofencing-and-geolocation-settings',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8e83c189a707a0a1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-geofencing-and-geolocation-settings'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-configure-and-manage-geofencing-and-geolocation-settings', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'as_of_date': 'Date used for the card timestamp and file name.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to read from, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-and-manage-geofencing-and-geolocation-settings-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical configure and manage geofencing and geolocation settings status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-configure-and-manage-geofencing-and-geolocation-settings-2026-05-24-card.json' that visualizes the current state of configure and manage geofencing and geolocation settings. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current configure and manage geofencing and geolocation settings KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file summarizing geofencing and geolocation settings status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON showing geofencing and geolocation settings status for USMF as of 2026-05-24.', 'inputs': [{'description': 'Dynamics 365 legal entity to read from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-and-manage-geofencing-and-geolocation-settings-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and file name.', 'name': 'as_of_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable Adaptive Card snapshot of geofencing/geolocation settings status for Teams, Outlook, or a dashboard. No data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardConfigureAndManageGeofencingAndGeolocationSettings(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConfigureAndManageGeofencingAndGeolocationSettings'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'as_of_date': {'description': 'Date used for the card timestamp and file name.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to read from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-configure-and-manage-geofencing-and-geolocation-settings-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardConfigureAndManageGeofencingAndGeolocationSettings().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
