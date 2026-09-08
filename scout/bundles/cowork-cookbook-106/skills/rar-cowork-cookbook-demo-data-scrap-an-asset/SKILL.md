---
name: "rar-cowork-cookbook-demo-data-scrap-an-asset"
description: "Generates 25 realistic demo records for scrapping an asset in a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_scrap_an_asset", "rar_sha256": "9ab9e8408914ff446712185c99e59e660c940281bc9a7571872ec16c55d19acb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_scrap_an_asset`. The original RAPP
agent is preserved byte-for-byte in `demo_data_scrap_an_asset_agent.py` and in the RCI capsule.

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

Scrap an asset Demo Data Generator — Generates 25 realistic demo records for scrapping an asset in a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-scrap-an-asset
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
      "description": "Sandbox D365 legal entity to target (default USMF); never a production entity.",
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
      "description": "Excel staging file name, e.g. demo-data-scrap-an-asset-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_scrap_an_asset_agent.py` and embedded as the fenced Python below (sha256 9ab9e8408914ff44…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_scrap_an_asset_agent.py` first:

```bash
python3 demo_data_scrap_an_asset_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_scrap_an_asset_agent.py   # or on stdin
python3 demo_data_scrap_an_asset_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Scrap an asset Demo Data Generator — Generates 25 realistic demo records for scrapping an asset in a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-scrap-an-asset
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_scrap_an_asset',
    "version": '3.0.3',
    "display_name": 'Scrap an asset Demo Data Generator',
    "description": "Generates 25 realistic demo records for scrapping an asset in a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-scrap-an-asset',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-scrap-an-asset',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '33400ac728e46c9e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/scrap-an-asset'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-scrap-an-asset', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); never a production entity.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-scrap-an-asset-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic scrap an asset data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for scrap an asset. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-scrap-an-asset-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic scrap an asset records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for scrapping an asset in a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo scrap-an-asset records in USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); never a production entity.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-scrap-an-asset-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo or training data for asset scrapping in a D365 sandbox tenant. Sandbox only — it writes records and must never target production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataScrapAnAsset(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataScrapAnAsset'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); never a production entity.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-scrap-an-asset-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataScrapAnAsset().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
