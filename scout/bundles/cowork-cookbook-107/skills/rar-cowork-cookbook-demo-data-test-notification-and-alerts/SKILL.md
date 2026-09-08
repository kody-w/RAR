---
name: "rar-cowork-cookbook-demo-data-test-notification-and-alerts"
description: "Generates 25 realistic demo records for test notification and alerts in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, then creates them and returns each record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_test_notification_and_alerts", "rar_sha256": "b7660427078f13ec9147f22094a1342b9a747302059635c50b4b7af6ae4a694e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_test_notification_and_alerts`. The original RAPP
agent is preserved byte-for-byte in `demo_data_test_notification_and_alerts_agent.py` and in the RCI capsule.

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

Test notification and alerts Demo Data Generator — Generates 25 realistic demo records for test notification and alerts in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, then creates them and returns each record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-test-notification-and-alerts
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
      "description": "Sandbox D365 legal entity to generate records in (default USMF).",
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
    "record_count": {
      "description": "How many demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-test-notification-and-alerts-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_test_notification_and_alerts_agent.py` and embedded as the fenced Python below (sha256 b7660427078f13ec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_test_notification_and_alerts_agent.py` first:

```bash
python3 demo_data_test_notification_and_alerts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_test_notification_and_alerts_agent.py   # or on stdin
python3 demo_data_test_notification_and_alerts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test notification and alerts Demo Data Generator — Generates 25 realistic demo records for test notification and alerts in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, then creates them and returns each record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-test-notification-and-alerts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_test_notification_and_alerts',
    "version": '3.0.3',
    "display_name": 'Test notification and alerts Demo Data Generator',
    "description": "Generates 25 realistic demo records for test notification and alerts in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, then creates them and returns each record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-test-notification-and-alerts',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-test-notification-and-alerts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '29e2c01eb4965b50',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/test-notification-and-alerts'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-test-notification-and-alerts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to generate records in (default USMF).', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-test-notification-and-alerts-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic test notification and alerts data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for test notification and alerts. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-test-notification-and-alerts-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic test notification and alerts records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for test notification and alerts in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, then creates them and returns each record's primary key.", 'example_request': 'Generate 25 demo test notification and alerts records in USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to generate records in (default USMF).', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-test-notification-and-alerts-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need seeded demo/training/pilot data for test notification and alerts in a D365 sandbox. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataTestNotificationAndAlerts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTestNotificationAndAlerts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to generate records in (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-test-notification-and-alerts-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataTestNotificationAndAlerts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
