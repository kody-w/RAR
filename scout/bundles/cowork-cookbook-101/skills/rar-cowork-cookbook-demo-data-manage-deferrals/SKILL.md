---
name: "rar-cowork-cookbook-demo-data-manage-deferrals"
description: "Generates 25 realistic demo deferral records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_deferrals", "rar_sha256": "ede42e3897f3550d98653bb449fc127ab36cedd810622e682dd139bb83a4d733", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
