---
name: "rar-cowork-cookbook-demo-data-analyze-asset-leases"
description: "Generates 25 realistic asset-lease demo records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_asset_leases", "rar_sha256": "cf6631bf1c89fb1569fd5d28f1dbf7d2442363202c64095333eb0c127974f833", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
