---
name: "rar-cowork-cookbook-demo-data-revalue-and-adjust-assets"
description: "Generates 25 realistic demo asset revaluation/adjustment records for a sandbox Dynamics 365 F&SCM legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_revalue_and_adjust_assets", "rar_sha256": "bbaf72049877692dd462d03696d5c2062bea5333b1d9c68881b1d163f1bc05d7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
