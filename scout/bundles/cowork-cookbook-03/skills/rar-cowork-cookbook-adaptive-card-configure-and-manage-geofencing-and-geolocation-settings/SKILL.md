---
name: "rar-cowork-cookbook-adaptive-card-configure-and-manage-geofencing-and-geolocation-settings"
description: "Generates a read-only Adaptive Card JSON file summarizing geofencing and geolocation settings status from Dynamics 365 F&SCM, with header, 3-5 KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_configure_and_manage_geofencing_and_geolocation_settings", "rar_sha256": "7ac60928b413629764ec854f1c7ee41a77db6f0c1b4fede8111d0926a87b9322", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
