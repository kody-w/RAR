---
name: "rar-cowork-cookbook-demo-data-test-notification-and-alerts"
description: "Generates 25 realistic demo records for test notification and alerts in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, then creates them and returns each record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_test_notification_and_alerts", "rar_sha256": "b7660427078f13ec9147f22094a1342b9a747302059635c50b4b7af6ae4a694e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
