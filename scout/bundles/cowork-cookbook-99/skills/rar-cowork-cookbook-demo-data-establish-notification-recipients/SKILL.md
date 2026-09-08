---
name: "rar-cowork-cookbook-demo-data-establish-notification-recipients"
description: "Generates 25 realistic demo records for establish notification recipients in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_establish_notification_recipients", "rar_sha256": "206a9080a329df370820fd48642b47bf2504f10e015012b7245182a153d12130", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_establish_notification_recipients`. The original RAPP
agent is preserved byte-for-byte in `demo_data_establish_notification_recipients_agent.py` and in the RCI capsule.

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

Establish notification recipients Demo Data Generator — Generates 25 realistic demo records for establish notification recipients in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-establish-notification-recipients
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
      "description": "Sandbox D365 legal entity to target; defaults to USMF. Must not be production.",
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
      "description": "Number of demo records to generate; defaults to 25.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-establish-notification-recipients-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_establish_notification_recipients_agent.py` and embedded as the fenced Python below (sha256 206a9080a329df37…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_establish_notification_recipients_agent.py` first:

```bash
python3 demo_data_establish_notification_recipients_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_establish_notification_recipients_agent.py   # or on stdin
python3 demo_data_establish_notification_recipients_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish notification recipients Demo Data Generator — Generates 25 realistic demo records for establish notification recipients in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-establish-notification-recipients
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_establish_notification_recipients',
    "version": '3.0.3',
    "display_name": 'Establish notification recipients Demo Data Generator',
    "description": "Generates 25 realistic demo records for establish notification recipients in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-establish-notification-recipients',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-establish-notification-recipients',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '13ca7737f413d5db',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/establish-notification-recipients'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-establish-notification-recipients', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'record_count': 'Number of demo records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-establish-notification-recipients-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic establish notification recipients data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for establish notification recipients. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-establish-notification-recipients-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic establish notification recipients records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for establish notification recipients in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo establish notification recipient records in USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-establish-notification-recipients-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/training data for establish notification recipients in a D365 sandbox tenant. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataEstablishNotificationRecipients(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataEstablishNotificationRecipients'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-establish-notification-recipients-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataEstablishNotificationRecipients().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
