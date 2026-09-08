---
name: "rar-cowork-cookbook-adaptive-card-test-notification-and-alerts"
description: "Generates a read-only Adaptive Card JSON file visualizing test notification and alerts status from Dynamics 365 F&SCM for a given legal entity, with KPI tiles, RAG row, and action buttons."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_test_notification_and_alerts", "rar_sha256": "ffb340b2396719e53d549d20152e8119ad4258e0d08bb373bbfc215605be8ed1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
