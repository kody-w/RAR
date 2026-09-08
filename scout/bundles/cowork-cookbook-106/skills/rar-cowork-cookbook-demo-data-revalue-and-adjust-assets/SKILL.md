---
name: "rar-cowork-cookbook-demo-data-revalue-and-adjust-assets"
description: "Generates 25 realistic demo asset revaluation/adjustment records for a sandbox Dynamics 365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_revalue_and_adjust_assets", "rar_sha256": "bbaf72049877692dd462d03696d5c2062bea5333b1d9c68881b1d163f1bc05d7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_revalue_and_adjust_assets`. The original RAPP
agent is preserved byte-for-byte in `demo_data_revalue_and_adjust_assets_agent.py` and in the RCI capsule.

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

Revalue and adjust assets Demo Data Generator — Generates 25 realistic demo asset revaluation/adjustment records for a sandbox Dynamics 365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-revalue-and-adjust-assets
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
      "description": "Number of demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-revalue-and-adjust-assets-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_revalue_and_adjust_assets_agent.py` and embedded as the fenced Python below (sha256 bbaf72049877692d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_revalue_and_adjust_assets_agent.py` first:

```bash
python3 demo_data_revalue_and_adjust_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_revalue_and_adjust_assets_agent.py   # or on stdin
python3 demo_data_revalue_and_adjust_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revalue and adjust assets Demo Data Generator — Generates 25 realistic demo asset revaluation/adjustment records for a sandbox Dynamics 365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-revalue-and-adjust-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_revalue_and_adjust_assets',
    "version": '3.0.3',
    "display_name": 'Revalue and adjust assets Demo Data Generator',
    "description": "Generates 25 realistic demo asset revaluation/adjustment records for a sandbox Dynamics 365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-revalue-and-adjust-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-revalue-and-adjust-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '28e5ab64892fd4eb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/revalue-and-adjust-assets'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-revalue-and-adjust-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF).', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-revalue-and-adjust-assets-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic revalue and adjust assets data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for revalue and adjust assets. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-revalue-and-adjust-assets-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic revalue and adjust assets records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo asset revaluation/adjustment records for a sandbox Dynamics 365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo revalue and adjust assets records in USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-revalue-and-adjust-assets-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo or training data for revalue and adjust assets in a D365 sandbox tenant. Sandbox only — never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataRevalueAndAdjustAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataRevalueAndAdjustAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-revalue-and-adjust-assets-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataRevalueAndAdjustAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
