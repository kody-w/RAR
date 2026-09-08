---
name: "rar-cowork-cookbook-adaptive-card-identify-notification-triggers"
description: "Generates a read-only Adaptive Card JSON file showing notification trigger status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, a RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_identify_notification_triggers", "rar_sha256": "e5023f593f0b801b2c1ae7d21675ef5950ca9aff8c3cf4a08300193b8d6048bc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1: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 -->
