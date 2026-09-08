---
name: "rar-cowork-cookbook-adaptive-card-test-notification-and-alerts"
description: "Generates a read-only Adaptive Card JSON file visualizing test notification and alerts status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_test_notification_and_alerts", "rar_sha256": "ffb340b2396719e53d549d20152e8119ad4258e0d08bb373bbfc215605be8ed1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_test_notification_and_alerts`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_test_notification_and_alerts_agent.py` and in the RCI capsule.

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

Test notification and alerts Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing test notification and alerts status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-test-notification-and-alerts
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-test-notification-and-alerts-2026-05-24-card.json.",
      "type": "string"
    },
    "snapshot_date": {
      "description": "Date the status snapshot represents, used in the card header timestamp and filename.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_test_notification_and_alerts_agent.py` and embedded as the fenced Python below (sha256 ffb340b2396719e5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_test_notification_and_alerts_agent.py` first:

```bash
python3 adaptive_card_test_notification_and_alerts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_test_notification_and_alerts_agent.py   # or on stdin
python3 adaptive_card_test_notification_and_alerts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test notification and alerts Status Adaptive Card — Generates a read-only Adaptive Card JSON file visualizing test notification and alerts status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.

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
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-test-notification-and-alerts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_test_notification_and_alerts',
    "version": '3.0.2',
    "display_name": 'Test notification and alerts Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file visualizing test notification and alerts status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.',
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
        "upstream_slug": 'adaptive-card-test-notification-and-alerts',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-test-notification-and-alerts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2a3a7ba5e87fd85c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/test-notification-and-alerts'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-test-notification-and-alerts', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-test-notification-and-alerts-2026-05-24-card.json.', 'snapshot_date': 'Date the status snapshot represents, used in the card header timestamp and filename.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical test notification and alerts status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-test-notification-and-alerts-2026-05-24-card.json' that visualizes the current state of test notification and alerts. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Generates an Adaptive Card JSON file with current test notification and alerts KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file visualizing test notification and alerts status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons.', 'example_request': 'Make an Adaptive Card JSON showing test notification and alerts status for USMF as of 2026-05-24.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-test-notification-and-alerts-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'Date the status snapshot represents, used in the card header timestamp and filename.', 'name': 'snapshot_date'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a Teams/Outlook-renderable Adaptive Card snapshot of test notification and alerts status from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardTestNotificationAndAlerts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardTestNotificationAndAlerts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-test-notification-and-alerts-2026-05-24-card.json.', 'type': 'string'}, 'snapshot_date': {'description': 'Date the status snapshot represents, used in the card header timestamp and filename.', 'type': 'string'}},
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
    print(AdaptiveCardTestNotificationAndAlerts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
