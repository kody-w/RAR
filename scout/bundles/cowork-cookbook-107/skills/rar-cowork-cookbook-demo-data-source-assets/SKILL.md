---
name: "rar-cowork-cookbook-demo-data-source-assets"
description: "Generates 25 realistic demo source asset records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_source_assets", "rar_sha256": "419f1d9d0866b5f3664821868e71c5c3672639a8b979f6897c693fafe6e005fb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_source_assets`. The original RAPP
agent is preserved byte-for-byte in `demo_data_source_assets_agent.py` and in the RCI capsule.

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

Source assets Demo Data Generator — Generates 25 realistic demo source asset records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-source-assets
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
      "description": "Number of demo source asset records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. 'demo-data-source-assets-2026-05-24.xlsx'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_source_assets_agent.py` and embedded as the fenced Python below (sha256 419f1d9d0866b5f3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_source_assets_agent.py` first:

```bash
python3 demo_data_source_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_source_assets_agent.py   # or on stdin
python3 demo_data_source_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Source assets Demo Data Generator — Generates 25 realistic demo source asset records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-source-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_source_assets',
    "version": '3.0.3',
    "display_name": 'Source assets Demo Data Generator',
    "description": "Generates 25 realistic demo source asset records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-source-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-source-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd678a74e8944eb97',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/source-assets'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-source-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'record_count': 'Number of demo source asset records to generate (default 25).', 'workbook_name': "Excel staging file name, e.g. 'demo-data-source-assets-2026-05-24.xlsx'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic source assets data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for source assets. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-source-assets-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic source assets records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo source asset records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.", 'example_request': 'Generate 25 demo source asset records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo source asset records to generate (default 25).', 'name': 'record_count'}, {'description': "Excel staging file name, e.g. 'demo-data-source-assets-2026-05-24.xlsx'.", 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training source asset data created in a D365 sandbox legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataSourceAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataSourceAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo source asset records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': "Excel staging file name, e.g. 'demo-data-source-assets-2026-05-24.xlsx'.", 'type': 'string'}},
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
    print(DemoDataSourceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
