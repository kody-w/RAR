---
name: "rar-cowork-cookbook-demo-data-analyze-asset-utilization"
description: "Generates 25 realistic demo records for asset utilization analysis in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_asset_utilization", "rar_sha256": "0dd27687e0d63309417adc680e583691870e1045f89f479e64443156a1356701", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
