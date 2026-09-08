---
name: "rar-cowork-cookbook-demo-data-decommission-assets"
description: "Generates 25 realistic demo decommission-asset records via the Dynamics 365 ERP plugin, stages them in a dated Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_decommission_assets", "rar_sha256": "07435c877dba885c6932b79f301f0a60896339403a228fa04d207ddd265bf183", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
