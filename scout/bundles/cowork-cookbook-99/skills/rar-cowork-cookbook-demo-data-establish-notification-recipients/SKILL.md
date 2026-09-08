---
name: "rar-cowork-cookbook-demo-data-establish-notification-recipients"
description: "Generates 25 realistic demo records for establish notification recipients in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_establish_notification_recipients", "rar_sha256": "206a9080a329df370820fd48642b47bf2504f10e015012b7245182a153d12130", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
