---
name: "rar-cowork-cookbook-demo-data-analyze-asset-utilization"
description: "Generates 25 realistic demo records for asset utilization analysis in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_asset_utilization", "rar_sha256": "0dd27687e0d63309417adc680e583691870e1045f89f479e64443156a1356701", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_analyze_asset_utilization`. The original RAPP
agent is preserved byte-for-byte in `demo_data_analyze_asset_utilization_agent.py` and in the RCI capsule.

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

Analyze asset utilization Demo Data Generator — Generates 25 realistic demo records for asset utilization analysis in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-asset-utilization
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
      "description": "Sandbox D365 legal entity to write to (default USMF); must not be production.",
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
      "description": "Excel staging file name, e.g. demo-data-analyze-asset-utilization-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_asset_utilization_agent.py` and embedded as the fenced Python below (sha256 0dd27687e0d63309…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_asset_utilization_agent.py` first:

```bash
python3 demo_data_analyze_asset_utilization_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_analyze_asset_utilization_agent.py   # or on stdin
python3 demo_data_analyze_asset_utilization_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze asset utilization Demo Data Generator — Generates 25 realistic demo records for asset utilization analysis in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-asset-utilization
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_analyze_asset_utilization',
    "version": '3.0.3',
    "display_name": 'Analyze asset utilization Demo Data Generator',
    "description": "Generates 25 realistic demo records for asset utilization analysis in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-analyze-asset-utilization',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-analyze-asset-utilization',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '462323a66eb8de84',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-asset-utilization'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-analyze-asset-utilization', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-analyze-asset-utilization-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic analyze asset utilization data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for analyze asset utilization. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-analyze-asset-utilization-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic analyze asset utilization records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for asset utilization analysis in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo asset utilization records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-analyze-asset-utilization-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/training asset utilization data created in a D365 sandbox legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataAnalyzeAssetUtilization(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAnalyzeAssetUtilization'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-analyze-asset-utilization-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataAnalyzeAssetUtilization().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
