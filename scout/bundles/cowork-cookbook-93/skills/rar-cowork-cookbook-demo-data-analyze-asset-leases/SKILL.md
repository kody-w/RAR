---
name: "rar-cowork-cookbook-demo-data-analyze-asset-leases"
description: "Generates 25 realistic asset-lease demo records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_asset_leases", "rar_sha256": "cf6631bf1c89fb1569fd5d28f1dbf7d2442363202c64095333eb0c127974f833", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_analyze_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `demo_data_analyze_asset_leases_agent.py` and in the RCI capsule.

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

Analyze asset leases Demo Data Generator — Generates 25 realistic asset-lease demo records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-asset-leases
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
      "description": "Sandbox legal entity to create records in (default USMF).",
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
      "description": "How many demo lease records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-analyze-asset-leases-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_asset_leases_agent.py` and embedded as the fenced Python below (sha256 cf6631bf1c89fb15…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_asset_leases_agent.py` first:

```bash
python3 demo_data_analyze_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_analyze_asset_leases_agent.py   # or on stdin
python3 demo_data_analyze_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze asset leases Demo Data Generator — Generates 25 realistic asset-lease demo records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_analyze_asset_leases',
    "version": '3.0.3',
    "display_name": 'Analyze asset leases Demo Data Generator',
    "description": "Generates 25 realistic asset-lease demo records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-analyze-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-analyze-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '137519612feff733',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-asset-leases'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-analyze-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox legal entity to create records in (default USMF).', 'record_count': 'How many demo lease records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-analyze-asset-leases-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic analyze asset leases data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for analyze asset leases. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-analyze-asset-leases-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic analyze asset leases records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic asset-lease demo records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.", 'example_request': 'Generate 25 demo asset lease records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox legal entity to create records in (default USMF).', 'name': 'legal_entity'}, {'description': 'How many demo lease records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-analyze-asset-leases-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need sample asset lease data in a D365 F&SCM sandbox for training or pilot demos. Sandbox only - never a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataAnalyzeAssetLeases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAnalyzeAssetLeases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox legal entity to create records in (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo lease records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-analyze-asset-leases-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataAnalyzeAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
