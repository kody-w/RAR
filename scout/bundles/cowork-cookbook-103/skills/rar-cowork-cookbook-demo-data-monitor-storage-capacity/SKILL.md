---
name: "rar-cowork-cookbook-demo-data-monitor-storage-capacity"
description: "Generates 25 realistic demo records for monitor storage capacity in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_storage_capacity", "rar_sha256": "b79d1efea201874628df88fe8e34020ec094e92f41d522db2e4c1f06ec63ef7a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_monitor_storage_capacity`. The original RAPP
agent is preserved byte-for-byte in `demo_data_monitor_storage_capacity_agent.py` and in the RCI capsule.

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

Monitor storage capacity Demo Data Generator — Generates 25 realistic demo records for monitor storage capacity in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-storage-capacity
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
      "description": "Sandbox D365 legal entity to create records in (default USMF).",
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
      "description": "Number of demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-monitor-storage-capacity-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_monitor_storage_capacity_agent.py` and embedded as the fenced Python below (sha256 b79d1efea2018746…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_monitor_storage_capacity_agent.py` first:

```bash
python3 demo_data_monitor_storage_capacity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_monitor_storage_capacity_agent.py   # or on stdin
python3 demo_data_monitor_storage_capacity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor storage capacity Demo Data Generator — Generates 25 realistic demo records for monitor storage capacity in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-storage-capacity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_monitor_storage_capacity',
    "version": '3.0.3',
    "display_name": 'Monitor storage capacity Demo Data Generator',
    "description": "Generates 25 realistic demo records for monitor storage capacity in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-monitor-storage-capacity',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-monitor-storage-capacity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4fab619c4533bea3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/monitor-storage-capacity'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-monitor-storage-capacity', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF).', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-monitor-storage-capacity-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic monitor storage capacity data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for monitor storage capacity. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-monitor-storage-capacity-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic monitor storage capacity records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for monitor storage capacity in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo monitor storage capacity records in USMF sandbox, stage to Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-monitor-storage-capacity-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need sandbox demo/training data for monitor storage capacity in Dynamics 365 F&SCM. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataMonitorStorageCapacity(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMonitorStorageCapacity'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-monitor-storage-capacity-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataMonitorStorageCapacity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
