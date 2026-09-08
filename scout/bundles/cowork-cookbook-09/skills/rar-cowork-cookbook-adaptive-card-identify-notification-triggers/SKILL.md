---
name: "rar-cowork-cookbook-adaptive-card-identify-notification-triggers"
description: "Generates a read-only Adaptive Card JSON file showing notification trigger status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_identify_notification_triggers", "rar_sha256": "e5023f593f0b801b2c1ae7d21675ef5950ca9aff8c3cf4a08300193b8d6048bc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_identify_notification_triggers`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_identify_notification_triggers_agent.py` and in the RCI capsule.

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

Identify notification triggers Status Adaptive Card — Generates a read-only Adaptive Card JSON file showing notification trigger status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-notification-triggers
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
    "as_of_date": {
      "description": "Date used for the card timestamp and filename.",
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
      "description": "D365 F&SCM legal entity to query, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-identify-notification-triggers-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_identify_notification_triggers_agent.py` and embedded as the fenced Python below (sha256 e5023f593f0b801b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_identify_notification_triggers_agent.py` first:

```bash
python3 adaptive_card_identify_notification_triggers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_identify_notification_triggers_agent.py   # or on stdin
python3 adaptive_card_identify_notification_triggers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify notification triggers Status Adaptive Card — Generates a read-only Adaptive Card JSON file showing notification trigger status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-notification-triggers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_identify_notification_triggers',
    "version": '3.0.2',
    "display_name": 'Identify notification triggers Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file showing notification trigger status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-identify-notification-triggers',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-identify-notification-triggers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f850ce772e162f5c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/identify-notification-triggers'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-identify-notification-triggers', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_buttons': 'The 2-3 action buttons to place on the card.', 'as_of_date': 'Date used for the card timestamp and filename.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_count': 'How many KPI tiles to include (3-5).', 'legal_entity': 'D365 F&SCM legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-identify-notification-triggers-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical identify notification triggers status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-identify-notification-triggers-2026-05-24-card.json' that visualizes the current state of identify notification triggers. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current identify notification triggers KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file showing notification trigger status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON of notification trigger status in USMF for 2026-05-24, read-only.', 'inputs': [{'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-identify-notification-triggers-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date used for the card timestamp and filename.', 'name': 'as_of_date'}, {'description': 'How many KPI tiles to include (3-5).', 'name': 'kpi_count'}, {'description': 'The 2-3 action buttons to place on the card.', 'name': 'action_buttons'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-ready Adaptive Card snapshot of identify notification triggers status from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardIdentifyNotificationTriggers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardIdentifyNotificationTriggers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_buttons': {'description': 'The 2-3 action buttons to place on the card.', 'type': 'string'}, 'as_of_date': {'description': 'Date used for the card timestamp and filename.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_count': {'description': 'How many KPI tiles to include (3-5).', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-identify-notification-triggers-2026-05-24-card.json.', 'type': 'string'}},
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
    print(AdaptiveCardIdentifyNotificationTriggers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6eZOjWJLnV9HGmG1VDZkBCBCQY222SOgAJE4hjsq2LO77EIcE1NZ334cUkZnVnT27Nbv/rPIIAe/57T93j8fvL07fxVXz8ulFC5xysXfyPImDZuGU/mJT3asmAz+qzAX/Fl5Vdk3i9l3VtC8fXvyg9Zqk7pKqBNv3QRk0The0C2fRBI7/sSrzccH4DlhwCxYbp/EXvCaJizDJg0UbV/ekjBZl1SVh4jkzkQUgHkWAd9s5Xd8uwqYqFuxYOkXitQtsRSx2/13bnBZhBcRbRIBquciDyMkXQdkl3fhhcU+6eCHI3KIDPNoPYJXK7BdNdf/w0MfxHmyAAl1Vtq9AhWBwihosffn0698/vCTg+8un31+83GnBrZd34WfZOX9mEo7idwKfn/LOtsidMgI76hEYswTXddAAMQtwyw/CxdvVz22Qhx8W//7v2d1povaXT5/Lxdvn88v8R+2BEeJg0VVO2wX+wnNqx01yoNvrgsnvztgC03Z9U85GboG5yuj1ufMbpape/G1+9vOTyWsUdD9/fqnq2TlA5s8vvyyA/T6/NP38/XWmUv/8y2te3YPm51++0Wl7Nw28biYGpH798nb9RhYs/LY0CRdfNHm7eePVBF5SB4D4d/rNn6fob+TeTPLlufjnqv6w+DHlWZ+/AXmf0eYCuj8mC2wAdr68plVS/vzGo6lAjDilF/z8y78i68WBl+VJ2/0f0f31STgG8Q2s9WaSXz483Pf3BfSm21ea/5ptDQLmr2gClr+z+2qof0X74dl/IJ0nJcjMd1/+kNyPNkB/W/z6L3X7zzZ8WISfX9ggB9nTOG4efFr8/giRX3/yv9386e9/ANL/WzJa1Tfeg8KXwimTMGi7L19+/al93P7p77/+1NcgigOn+NI3+Y9o/siuDz5/suDbqp//vBfw18usrO7l4msOLX6v6v/W/PG6uDh54n+7335afJ+J8wdazEq8M32a4LtsbIGs39nxl5c/AAqVQJv+AVUzCP3bvy1OiddUbRV2C82r+m4BHNwlRTALf46TdgH+zqjRBMCubQIM+7YOxP/s4VniKlz89j+8B55/9N7wHHbe8O2LBwDuS/KGcF++x+Qvb5jc/va6OAMeFbhMSgC5KiPLn0snAntm/nUTtEFzA5jljl3wEaT2x/nLIikXv/0VNl8eFF/r8bcHYidPPFQ33IyFbZ8Hr7PWRgyg/6mjB4pWMAReD5jllQckC5/YDwSqclB4utlCbZbk+cJPANqA4jU+aAMrfpqJ/fbbb67Txp/LJ3hji2dVa2Gw4Ks4i48fgYphnkRx97kMvLha/PT7Hz8t/ufiP9v1ID7zkEFBefMRkPBRBkHO9QVYBtwHHA4A5eGj3/94MzQgA+rpAngUGCl4bgYxmwX+u9W1A/NxSawWbgCsDSxd1FXTzTU16V4XXLj4Ki9gOj+aa0Zctd3CD+qgBF7wRkDVAep8tSRwyaIFDmlDUEz7Nnhw/c1tnIeIBUh+p/ttcdrIoEJVOfhvFvOxCGyuSuDM/GtMPO8DIs1P7WL9TuJ1Ic5RuqidxqnjxnnjETpPv8yV/W07IO4syuD+uZzLcjCb6hEqT/NEc7eReG8u/fjoKbyqAPjgt++8o7eOxF+cH/W0+Vy2b+ngNLMrPFAeANOoT/y5SPzHW0iB3qTP/Yf9gKQzpTcv+G9eecTge0PwwxamXWjPHubP/c/nfomg+OL/v1ZpVpjZ79Xtnjlv2cVWPKvW0xFzTzg77NlGAtIPno+k+9a9vCPUO1B/LvMERFUz/sdz5UPPtzVP8OsbYG2VUR/0QewAVWe6j9CeQ7Vp5qRwPpfvFWHW4AF/QGqAAyBP5vB8Zzg/fZc0Bsk+X3/rDh6hAGwOFAfhu6h7NwehFQaB7zpeBqSanfTuPBDnwZyq9zjx4j9pNdsWhBOgvwBCJCDhQNV4/YrSz6fvov9p47MJmrc8GsQeZGfzIADkCGYBZ5fMHgPidc8WHOj56UEEqFHU3ay7C0IDaPq8GTTBtU/apJud+7RrUANM/jj/fGo63w2GGqQEMBYI/LoH1n2kyhxuBWhxgAwALUDmFEkJSj4wypsRHgSdYs57gKtvPemT4uP2m0LBI7/mWvW+cVZk3jOX/2fUOuX4PTycfxQmgF4xr3jw/cdI+8ptpj1DZAtgDnB8f/rsE16fpf7ZSyze6X76pxnn5782Bj2Kt/7nAPi0iLuubj/B8LPgvtfbVwBQ8FPW9mvt/TgXxY/vRfHj90n+8R1M/sTjqf6nxV+T808k3vLk0wJ9RV6R+dHxLc7ePsAsm49r6yM+P/1cqsE3KAXsqwKINztxBMX+a917XwKKX9QAqAGLn3WwncvnHVTsB/ADj3wuvw/8OfFAXSmjOVDb6jtAeDQAIAmeDvxan8CjsgO8/bmNjIJ5jHukSRu8fCr7PP/wAmAw+Gvj21yOijnQ23n+AykFGrQuCR5XTyj88gaF850/D75zxC4/Yv8AmTP6gDYbyF29V8jGn2XtxnoW7jm9zf2e036pwi8+MNg/02bB3bmG+l+jeSbzyCiA/MUjkR/GmlX+IfUH6g3dP5OWHl+c/HXBBgBh8/b7VHorgXML8F3GP70FvOQB+3xY+I8SBuQCAsymm9HCaUH6AVl/KEtWJ19AhS1/IM2hugPEAVDwtSTNBkxKL+8BDP2MfSR++SHJR1H78ixqPzDft0r4ffWbSV97AE0fFsFr9LrQtdPuh9S/9un/TNoArdBMx68+zV3Bhzcc/jA7HVx9HZOAmd4G18fvG8q+ePn06zyizVH32DJ/AXvAj6+bvv5yxQ1e/v4juR5g/eXd8f8snTiDMChSs9f+VV8xB2hT+b0XvJnhr0DSxyWyXH1EiI9L/LH8NW1Ba/bPNgTCPgoRKOez3t8M+k2t6jGGzmoBM3TP35r8/gKyEcjTOW/5+DbHgOUAtz+2c58GA/QCDMH1E2fAs/+rCeeNVhs7oKsGxAICWWIhQWMh4lII6i491AlIf4muSCIA9wnEc2gnDCkP80LcQSgMQVAacyl/heCU6wF6T+T6MjemySzfLBwwC7BiEHx7DG75b4o9FZmt9nWgekDQU7/fX9wVPicL3nLM87OBadRdEUdXLV1oWoUVt9PjXrOGtpnG+hpVtpFlAlIbOX3keshwbH0bIZtzzChbizXS03mLXeRWgfAzwd9KabVfJgy+mzJp3x1ErR4jiTzXFJxLRNhT5+FGb66GYRstPR6PlL3bWraZFU4q2EdJrVW+vFzSi5aO4n3FC3KWD/vaGSC5C+HRDsZsNCzNuGy2en3HksCGCkiEcHiiV9A2aLNc5zuKarPl/d5ztRpYKFZI8I4qcYPkd8fkuqLCxIBhIpiQ7pKWvO9a0b4q9CbjdWTrXeDe7rfjtQmTm7+it/HZ1FlBDmQMqcfbXTNJ0YrX21u7ujZCC+nyUNFhWI6w1ZvnCaKCDRHc5PIOl10YirGwDS722qqSRug6s+LuDRp329FIWiY2Nb2RqV2/u5tGLBQDJiLX80UtDAi4n9vDGnvaM9K1ueqtHRHT8swOJy6hsiLX6OCirb08Knm3UY7tUukuugki6LhNghOSjvi9p64uESQdYZ7ca4LRZq0Q6povMkvZVPE0Dlf7EOxWNyRRNGcs04sa+9Em1Nix7cbpVFONgWMbV+2aU5gVBcHT1YbdKBc5wadEurOkvoLbacDq4pDXPIMojtuA/moyeIs6aANnVYiumJUTqybCXtAouvcFExKYqhuu2QJPbU1a591xmGpV03UHDQV9MEe0pE+lS2yDsaaE/UVX9JwwVWUZh23MXuw9T3qCBa33Q7PXCI3ktukIfKOejj69xgvBjQ5sI6BCTDiNldx9JthVeilyJV7Dh3gT18X2vpxuZmwo10vkCL543VOX6mikjDtk2Grl5FaMFIViasUwNXs3vDYgju6lvcEOexM38j7elJBxCcyeSW9oGt+IxBvPzPlI7cK2MqPE4OENn4mbCb+hqoLcoO4abvbLy8WoBi/nh/UpPVGQTHVL3s41Pz45HUFu1gGPWyOfkFg6Ypm07Ss3gLZymCJATnPPxbebEkIMfCcqeN+0dziRVATuJxIK4MG7qYEb3a+DqyK3SCzrY08b0nKXtNfsKmr8QRW2BYLw0mkXhSdDyndwi6s5nuoXfjvK5tgWcFUsLdeL2kuwwmVjeTjuyIb1HE3RiA0OhLeCzPKSFkME79CtkV1kmji3XsuDaHBiDzKU6VlKdTcCJSUFeyJ5OhlEWr5FVqa5VBg6a0xsbM4ZFC0rTsyVL5nLFk13KYMMHCok9GBsoY6B0kG81JttUVA6xE0cUgua0eVl0Q1eQ24dhPFPAVmEG7/EL26sFiUOnY8CEZ/ljiG0PMUPUTFcO4c7M9VOYQQOm7QTvhRoYZkaMMrciayNxkqmKj7XEkhLhbU0VOUErawTeRaG7HJiJMUYjyf7eB/QTJh8ondCWjJPDllCrYLXtGJfuDzatuvhqqZ2ZV/1vmbqnK5ypN/DurmttlEyMP3qWGKsXaKjVuuao9LTWWRhtKCclWAdp5WzXYfbjT+2UBST0RG6qEpZsP1JkmVugMaemgbWjVT7wGqgpI9IZXEmcRBww7TWSCFoDnGtJaROErOa/ItLDtrBLk4CRV/WHcsMMQ5f9y3hDHRNhSyD5JKsUf4BX01y50yVtVd9u9Tu645Z1mhGqFLViaRyk9uIHjfxkg7hcsMMPa+wZ25aksla4gnNAKlBRWGwFv0dy2rbkOONs9b6S/GQnK0V2wfDUnEta3edMnrnQdAOjbdnUVkeWVOg7jiapak97c7l5lCeiJu7QhUfoAJSmDYX6wnSVeR21DyoLSFfca+SdU6gwfGFNFpexB3Pc1viQOgnJR0GPnd9TkpYBV1Nq31q+INw04Vo7/CYQU9Jnl/6PeSNN4/Z5RaCyDcLCdv9lfYatPFAhOGnLb/y/H6Kbd4sroMohDoJQVKDDHY/7XAFrrVhJNciQ2G5nujWBa7VEgpWzL1i6KHYXsouHeCIErhD2i23W9Oikgi9wavVdpvB8OYQw8djM0D9ATHnnM0afNeXt/w8qNY24cR2o9yYyfXja6KsXVfY175fdyp1Y/MtEduVA90nZudZVCiz9xWcsfBh4DnMRtXLdqzWCG4zN9xrj+zRPspRoE5Kyfkn4Lr1XpdiC6/RRh2snMy9oS3zlrA22e0QI8J6b401TubXw9UZVblGEpS6GT6d+dxePPYniOUw9+QbEMf4SJWv2HV2sdzQ1DnVva0nK7qOa9O395lgYJQTD+s6zPtpuzumm/1q5/VpRsgVdj5rMglCfRzXorK9rJVY9hzmzB6X54K4oACzsQxY4a7C5+UyahVP31q1HK5stSJPbukMnX89x2s99+Ijfa0rS7ht6r3L3fQLNjr5tbfUdKelA0ehY8JcwXCvJ+t8vA5XJS7uGDcMZ++6TY8m3nfL/S4W+hE5ivy4Fxlth4AW4IiLKp9S+jWzbHRnICf5WHMptL7wSTURjdCk/NorxWa72hqeqqw3UX0CZRYlQvcm6YiylFJFP/GKBWs963plm9/xapxicy2ubgHJF9rApNSVzC6svT92iYuI8DEZJBRVMnnyvYtd95dLiyQ8Kl8qkTmqaw++0M625+uhVUdQ3RKqoax7IDt6ycH5mV/vjmbvD6VXYUF46dhKhXTbqfI60S6ZQlr+ljE2k8lFabS9RhHfNNe6GBK+tDhvr54RzGph5xTLFcr0+jaMR7hTmfFuktvaPd+X/VHzMz6vknHULz7tEfIOCkuAAhGJUDv+thx8OVay8uSlNnRrDDvjzlTiHKqzyyubDA/gMKHF6XwnsdwaU/t0JY4JhDvJyU4BZivXPRIUSOXyVamYWaTUvMXRUpHqvHlCKhLleo5iik5PRUZfTpc4g/3DxJgXT5Lu6o6vK2/cBmVU20Tl2DRF4CY+XI7JdqvsJ/Z29MRNGll6THGGpQtaeV4N3GDeBM85DjiMEBVyYo3RyGyLhq8sw19ObKwmS3uqbweNXveKt9449yOvXfNLDWeqWJ1R/Cx0zXj1LhjrpzAM4zIHXw9qsdr4VinlFAHp8Q1bumOg5I6cnCrzwIub9VINedbWHbXNh3rywgs8DeVajrxzU8acpid+H+tWtlk3Oz7bIE3i4F29tBX+anAWebhskZYJiuiq+llIUeUBvlzHZd0o4SZzNC3CbH5rTfbmYijNWOItMgYZVKldz+9BsVD2qMjA6yV2L9OGEBUKg5RSlLMOpYl4VYEOvUdRCCE42Kh1WWD97nRBJMvQTxV/spNjYcXYMSqJ3WASWnJZ+8Je2OVkVW2vKusDa8K6D200+UgXKHE2u1ObJB0wl3yrK7i4cdmxjcWbpPhd797QvkIKR5bP2xjG8dttygn4Spu7IJrasiq3e4pDgw3c4ZcIBhjm32sqdZQ04LHAWt2nDgmnmMQynCBOUGwem5UwkG4sVgJUIZsu5ooUiEOkxiTbx0ZY4ZmS+FezPmwYSd4RJzna7nUGZr2dVLZnKULWYa0sUUMiLrtms2bdWhzKMRWvLl5mROaIjl3caWedVaDXlTihqqV6ZM/tloPyvN+FXrAv3HpX0MZyu9JoHLS7O+N+hhXbQO98bPfsCWvH7Uoc3IY4Sxt6bVzNo5FE+W2U6JOUSdeWoChOFHGIVDPakBtpv+lOuNOSablcQtaAUXJiCFB6g12Hv1/40BGu0Z6zodXSGShKr0hoy7e2HvvhiG1qlutA813ZEcfhe4ZNSalp9Z47ImtDr3b+qrI8GnKUvS8lJ2EsNCzg6t7i4iXq3odKZdKQOU1RJRpMTDmES+vK8QQXunaUN4zNVMaRF8R07Vn7XGqvbBad1A2ZtfWaCEXztJlSF+nsvcO2S/zEyVU8uBPPJQk6ncO70xNspsEdRdZb/+pUnCfsQRBoV5w86A5J6CGckJAgS3UmqZobD8y6KW9G0FHu2ei9CaCEj4TReiOI8eGeyONZMFqFdHeumQu1OpTEmstISLSXS36rRmndeyR5cmSkGSX4gqVZhwl5dGWYdd6Ux1PZx1iME25wslVXYciiDnoj7fUqoZWqpdgpaU+SXvTWUWt4o0XC1AaTAkunpl9hU3AbXFIlzlYkgskxVxim6uw6iIfwEDFmEMYy2+42G37p3Ne2agt3IvQJNL7olTmmiI2lobaE2WBUEzyUcBXOwl2Ih4cQIOUgubQ35UfMy/j4noZiaIyEeKVcK3VCVTbiNu9XZSeumL2SS0XUo4djGeF3jqFXIXI9tP60Z5F8m2zEeCh1MoJB4AR3YnlpQvKiGLvufLixqONfMLkS4KUAxfIBGoZtYQ2luWc9lj6dzQOz9FfJUcFPV3atwym9DVHjFmYsxYr83Q616orfAg4E5cZX6D1JH2D93G3FJdkKVXL2i3RgA8lNcQvVJ4evwto8JMEaFVbpxDdSzBbkbonU0wbMoq68Xo3sURVKPhCWCmVjhLmlpM6698EV0aEB9EMy18j9yqfO10PkhD5K9dAE5orVlU68FQmn916XsiKWrp59Nm9Xo1sTFE44dO8erFXk7xIjP5PCfoyncHKE5cnhyUa745h+xUNqJ65RMJUvDRZKYaQ1J4b1eznEbI6lmQ71RxiaGPm43iKIYlc3uhRSlTmecNNnOdShIFiX+/h2NMQc4IWrGv7NYXFYHI1pvTmu8SVroqcEMUI8aBl+0nNyEsI69c4k1pOn2x5XgXfvo3++gQllX48r56wHRQ6T2A1GLvKYNkh1PF1geFXA8YCL8PZIn+IbGZ1GHB3vEQNumhlesknh7it8GiSrL45ynMYuVqgqmOuvK7JBEx9ZGlCShK0lRwdecAuIQFAaKbyhMJ0CBDntYfvIKhH/7FI+rRJLvL72XbuEWMmTvGG8JecDHZcHDiK9docGK4fGj+Spa041k6h6iZEoAWPupeSxPWeiJOuZqdN5vaL4fJq1TrNtyt0W20OAO7QKzEa9XjFTPu9UTwrk9V5MIzxXQbtvaChshFjlhnGsXHyXr5mTxm+pQE5QEcKO54rGhu2ZQ33TiY5rzYk1rRGjaY8i7lGj5NhpDoaqW0EilhJWZ/5Er3INuqdbbx9e6/JIjjm0FbxmQuKmYdJLzWU7I9NGeq+uArjS2aLX7tmGWUqWWYJ2bbwJWYT56o4mLKlhgowQecrSJT7bd1x2KxWkNIUdaKAxd0p2d7ZQEAeifMIJ9igvgUkTiH6YKogkISVJYK2Jzrm8RlkXwe5+gYrIpl2ZUeBNG3igpNEdm9MN6hSxcVEP9Sa4G8h9d6i5C0yjln9Ke1IaLryn6q6UBWISXDXMPNb7pT9CUpucx3taoDqCTI5REc6eSJtq7IPmtCd7+6gdJGIn3qJjSURYeC4bdrVpBpIABbqXbWlJ3bxQWmEOezbKDlpLDoWB2SowJ/1crqXu2PadI9ZneoXre8vxTktnX8GSVJ2925qaPCZeX7SDegmgQ7tf2wzcp3C2CW0wx4+lRfSerbK6iwnWrThf3RLZ5MF9TcTLAGvF/QRZaIM6t31S9HbIu/VQkvf+WJZYReD+GSIG0pe3VytwL3cFheRijOo4CUV5czFNJID5ZLpdyaBAuxq/WQ0WOMubsIaEHUafyeiGOfIhVfaONgWQ6iYbbNgX93VzF3dh4Tb5BGM35RrhagXcWUoymFYJco2Qhk0ROUSTKCSIBEDmkwdTkTudlP1KbdXUUmrGjm8qPZAaY+UhWajdkrRjDb41E7PZJaZ0CjNjEAR/T9EHDsBxQNRCBUa/SdiVaQ1f2qNicwTCIpqJG9l1HC1jMmCew1dbmZISD8LSdnkEU5RAYpKNL3E+v14O9kESnbPkyGTSFPItXR9u1VrfUZVpxS6T7NDtZkMK8JqF/WidsshJxa56f/FZ3POwcHTGfn3pQDCEeawE6VETscDcycbytt6U06Xq77J+U/VmXPkF0hynxBRR1+nOO3cF3/MT0tR7YRhY6uQt7fBgd5ZN8M3JZ6/I6cDfXSpBJJ2icaTHbWGFXTeYPOwuBFYTu2paj/aBQ2DzMmJLMjEGgg+icGdlMVxGGweVBWt3HMptOgirbH2+352hsWlnGWtBhgX7gxTomK4HLXkcGh90iyVOyxYzTlAho0EcWdwhLHo9pmGiW4spfhyzaYkiKy7lxWlbZOwIFmyPxztbEv0Bgx0Ilv1NvAnvKieOy5siGZSH2WO7R7GrTxIYhR0bd1muWiE7lTGFaJMpI2CNntNw6R0Gd5VIsFprGap26akl15FdZfYop07f9esQ25E+UlZqMUBWJ7VB5049bffkxiRAJ56uxd3GOoppFdQ+ThbxpMDWtpuukmJ63F7SjPgeb6ObAQKBocOGtpkDW009m3OX0nQ7skZWMQgq/xwy7gVf9iuEn1DMwBWEo/KDsTpWQa5iDK27aBkTqKmLgxgGFOyO6LpDgzKI3GEXEstmfwwJqoZPOwspINrbY0dMOrlppPsjtVlunNEWIdf2fXuneKKONp6tmzCqbnyMEpBR7UtKlvumANZDnMgN2JthkF5DD40Bw7s6NhOfPt3pJrNGS4Vo7MZ23N0ba4e9kEJ969CQC2V4p0+mKmf4XYF2Rz3bcOwqt+ipuDINxwllHaUjAo/aOYJ7U9SIQPT5zZQPJbMqwo2z8WNR4wfdx85IdUCyBAsiSpMIgOMq45LRsEQMvCsp7CbGzK68nlwIt2my2UWTJq8J3RXWy45SXOzUVLUt4jvctjC9SIRij29RyVSCQ26h9L2Db/iK2udbsl2rpUy2e/ianDXb3q6TnLIh/NwTlG0crwYZV5dyTA6mt4JiWC4GgUD1E8Mwf/vby4eXb0duL/+l19rmU5//ZwdMz3Oi97dYHueKgeN/evD69F8T7+8fXhovAcI9D9dA8xq9HU39w9Hax79yWjhTGp9vkL0fRz9P6jsnmt+9fklKv2/BsP6lrfLHuy1gh9u38zua7fwarwd+fn9g+iflHtfPN1SC5ktXfXmeMs4nbEk5v7wS+Mm3y+jtAPLDi//2vtQXbEV8CZp6Vv7t1QigM/aKvC5f/vhf3mt7gCEvAAA= -->
