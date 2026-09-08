---
name: "rar-cowork-cookbook-demo-data-plan-asset-leases"
description: "Generates 25 realistic demo plan asset lease records, stages them in a dated Excel workbook, then creates them in a Dynamics 365 sandbox legal entity and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_asset_leases", "rar_sha256": "66b684564127ec18b426f34dc9760138281d7d9ddf4726367ad5bce4dcfd29c6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_plan_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `demo_data_plan_asset_leases_agent.py` and in the RCI capsule.

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

Plan asset leases Demo Data Generator — Generates 25 realistic demo plan asset lease records, stages them in a dated Excel workbook, then creates them in a Dynamics 365 sandbox legal entity and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-asset-leases
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
      "description": "Sandbox D365 legal entity to write into (default USMF).",
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
      "description": "Number of demo lease records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-plan-asset-leases-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_plan_asset_leases_agent.py` and embedded as the fenced Python below (sha256 66b684564127ec18…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_plan_asset_leases_agent.py` first:

```bash
python3 demo_data_plan_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_plan_asset_leases_agent.py   # or on stdin
python3 demo_data_plan_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan asset leases Demo Data Generator — Generates 25 realistic demo plan asset lease records, stages them in a dated Excel workbook, then creates them in a Dynamics 365 sandbox legal entity and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_plan_asset_leases',
    "version": '3.0.3',
    "display_name": 'Plan asset leases Demo Data Generator',
    "description": "Generates 25 realistic demo plan asset lease records, stages them in a dated Excel workbook, then creates them in a Dynamics 365 sandbox legal entity and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-plan-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-plan-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fa55e0863eacc86b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/plan-asset-leases'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-plan-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write into (default USMF).', 'record_count': 'Number of demo lease records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-plan-asset-leases-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic plan asset leases data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for plan asset leases. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-plan-asset-leases-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic plan asset leases records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo plan asset lease records, stages them in a dated Excel workbook, then creates them in a Dynamics 365 sandbox legal entity and returns each new record's primary key.", 'example_request': 'Generate 25 demo plan asset lease records in USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to write into (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo lease records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-plan-asset-leases-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo or pilot plan asset lease data seeded in a D365 F&SCM sandbox legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataPlanAssetLeases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataPlanAssetLeases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write into (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo lease records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-plan-asset-leases-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataPlanAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
