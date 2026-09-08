---
name: "rar-cowork-cookbook-demo-data-track-project-time"
description: "Generates 25 realistic demo project time-tracking records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_track_project_time", "rar_sha256": "ad0fc61f9cd8a15e226835a47e1d3b65b7609d9669e18466217134bf9eef4578", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_track_project_time`. The original RAPP
agent is preserved byte-for-byte in `demo_data_track_project_time_agent.py` and in the RCI capsule.

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

Track project time Demo Data Generator — Generates 25 realistic demo project time-tracking records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-project-time
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
      "description": "Sandbox D365 legal entity to target (default USMF); must not be production.",
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
      "description": "Excel staging file name, e.g. demo-data-track-project-time-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_track_project_time_agent.py` and embedded as the fenced Python below (sha256 ad0fc61f9cd8a15e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_track_project_time_agent.py` first:

```bash
python3 demo_data_track_project_time_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_track_project_time_agent.py   # or on stdin
python3 demo_data_track_project_time_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track project time Demo Data Generator — Generates 25 realistic demo project time-tracking records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-project-time
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_track_project_time',
    "version": '3.0.3',
    "display_name": 'Track project time Demo Data Generator',
    "description": "Generates 25 realistic demo project time-tracking records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-track-project-time',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-track-project-time',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c165db4fa89128ce',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/track-project-time'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/demo-data-track-project-time', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-track-project-time-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic track project time data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for track project time. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-track-project-time-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic track project time records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo project time-tracking records for a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo project time records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-track-project-time-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo or training project time entries created in a D365 sandbox legal entity. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataTrackProjectTime(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTrackProjectTime'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-track-project-time-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataTrackProjectTime().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
