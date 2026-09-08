---
name: "rar-cowork-cookbook-demo-data-plan-asset-leases"
description: "Generates 25 realistic demo plan asset lease records, stages them in a dated Excel workbook, then creates them in a Dynamics 365 sandbox legal entity and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_asset_leases", "rar_sha256": "66b684564127ec18b426f34dc9760138281d7d9ddf4726367ad5bce4dcfd29c6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
