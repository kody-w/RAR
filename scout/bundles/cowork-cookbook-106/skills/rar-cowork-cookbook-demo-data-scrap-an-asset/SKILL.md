---
name: "rar-cowork-cookbook-demo-data-scrap-an-asset"
description: "Generates 25 realistic demo records for scrapping an asset in a Dynamics 365 F&SCM sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_scrap_an_asset", "rar_sha256": "9ab9e8408914ff446712185c99e59e660c940281bc9a7571872ec16c55d19acb", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
