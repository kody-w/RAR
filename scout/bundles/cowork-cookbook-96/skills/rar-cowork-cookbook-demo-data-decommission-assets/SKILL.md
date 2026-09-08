---
name: "rar-cowork-cookbook-demo-data-decommission-assets"
description: "Generates 25 realistic demo decommission-asset records via the Dynamics 365 ERP plugin, stages them in a dated Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_decommission_assets", "rar_sha256": "07435c877dba885c6932b79f301f0a60896339403a228fa04d207ddd265bf183", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_decommission_assets`. The original RAPP
agent is preserved byte-for-byte in `demo_data_decommission_assets_agent.py` and in the RCI capsule.

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

Decommission assets Demo Data Generator — Generates 25 realistic demo decommission-asset records via the Dynamics 365 ERP plugin, stages them in a dated Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-decommission-assets
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
      "description": "Sandbox D365 legal entity to target (default USMF).",
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
      "description": "Number of demo decommission asset records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-decommission-assets-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_decommission_assets_agent.py` and embedded as the fenced Python below (sha256 07435c877dba885c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_decommission_assets_agent.py` first:

```bash
python3 demo_data_decommission_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_decommission_assets_agent.py   # or on stdin
python3 demo_data_decommission_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Decommission assets Demo Data Generator — Generates 25 realistic demo decommission-asset records via the Dynamics 365 ERP plugin, stages them in a dated Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-decommission-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_decommission_assets',
    "version": '3.0.3',
    "display_name": 'Decommission assets Demo Data Generator',
    "description": "Generates 25 realistic demo decommission-asset records via the Dynamics 365 ERP plugin, stages them in a dated Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-decommission-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-decommission-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0a17f0a93d664ae1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/decommission-assets'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-decommission-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF).', 'record_count': 'Number of demo decommission asset records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-decommission-assets-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic decommission assets data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for decommission assets. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-decommission-assets-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic decommission assets records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo decommission-asset records via the Dynamics 365 ERP plugin, stages them in a dated Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.", 'example_request': 'Generate 25 demo decommission asset records in USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo decommission asset records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-decommission-assets-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/training decommission asset data created in a D365 F&SCM sandbox legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDecommissionAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDecommissionAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo decommission asset records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-decommission-assets-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDecommissionAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
