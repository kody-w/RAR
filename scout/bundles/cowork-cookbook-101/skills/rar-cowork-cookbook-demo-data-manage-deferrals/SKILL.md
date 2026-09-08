---
name: "rar-cowork-cookbook-demo-data-manage-deferrals"
description: "Generates 25 realistic demo deferral records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_deferrals", "rar_sha256": "ede42e3897f3550d98653bb449fc127ab36cedd810622e682dd139bb83a4d733", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_deferrals`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_deferrals_agent.py` and in the RCI capsule.

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

Manage deferrals Demo Data Generator — Generates 25 realistic demo deferral records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-deferrals
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
      "description": "Sandbox D365 legal entity to target; defaults to USMF.",
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
      "description": "Number of demo deferral records to generate; defaults to 25.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-manage-deferrals-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_deferrals_agent.py` and embedded as the fenced Python below (sha256 ede42e3897f3550d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_deferrals_agent.py` first:

```bash
python3 demo_data_manage_deferrals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_deferrals_agent.py   # or on stdin
python3 demo_data_manage_deferrals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage deferrals Demo Data Generator — Generates 25 realistic demo deferral records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-deferrals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_deferrals',
    "version": '3.0.3',
    "display_name": 'Manage deferrals Demo Data Generator',
    "description": "Generates 25 realistic demo deferral records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-manage-deferrals',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-deferrals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b639b5185cde1a1c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/manage-deferrals'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-manage-deferrals', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target; defaults to USMF.', 'record_count': 'Number of demo deferral records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-manage-deferrals-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic manage deferrals data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for manage deferrals. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-manage-deferrals-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic manage deferrals records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo deferral records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo manage-deferrals records in sandbox USMF, stage them in Excel, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Number of demo deferral records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-manage-deferrals-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo or training data for manage deferrals in a sandbox tenant. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataManageDeferrals(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageDeferrals'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo deferral records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-manage-deferrals-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataManageDeferrals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
