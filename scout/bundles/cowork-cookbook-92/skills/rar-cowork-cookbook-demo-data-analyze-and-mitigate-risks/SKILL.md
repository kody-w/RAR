---
name: "rar-cowork-cookbook-demo-data-analyze-and-mitigate-risks"
description: "Generates 25 realistic demo records for risk analysis and mitigation in a sandbox D365 legal entity, staged in an Excel workbook first, then created in D365 with a confirmation list of primary keys."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_and_mitigate_risks", "rar_sha256": "97723700b68646db9dbb0b25c58b7468f5919cdcebc2e2e4a368096b80c7e39f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_analyze_and_mitigate_risks`. The original RAPP
agent is preserved byte-for-byte in `demo_data_analyze_and_mitigate_risks_agent.py` and in the RCI capsule.

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

Analyze and mitigate risks Demo Data Generator — Generates 25 realistic demo records for risk analysis and mitigation in a sandbox D365 legal entity, staged in an Excel workbook first, then created in D365 with a confirmation list of primary keys.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-and-mitigate-risks
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
      "description": "Sandbox D365 legal entity to create records in (default USMF); must not be production.",
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
      "description": "How many demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-analyze-and-mitigate-risks-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_and_mitigate_risks_agent.py` and embedded as the fenced Python below (sha256 97723700b68646db…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_and_mitigate_risks_agent.py` first:

```bash
python3 demo_data_analyze_and_mitigate_risks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_analyze_and_mitigate_risks_agent.py   # or on stdin
python3 demo_data_analyze_and_mitigate_risks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and mitigate risks Demo Data Generator — Generates 25 realistic demo records for risk analysis and mitigation in a sandbox D365 legal entity, staged in an Excel workbook first, then created in D365 with a confirmation list of primary keys.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-and-mitigate-risks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_analyze_and_mitigate_risks',
    "version": '3.0.3',
    "display_name": 'Analyze and mitigate risks Demo Data Generator',
    "description": 'Generates 25 realistic demo records for risk analysis and mitigation in a sandbox D365 legal entity, staged in an Excel workbook first, then created in D365 with a confirmation list of primary keys.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-analyze-and-mitigate-risks',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-analyze-and-mitigate-risks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7a079169926af4f6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/analyze-and-mitigate-risks'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/demo-data-analyze-and-mitigate-risks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-analyze-and-mitigate-risks-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic analyze and mitigate risks data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for analyze and mitigate risks. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-analyze-and-mitigate-risks-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic analyze and mitigate risks records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates 25 realistic demo records for risk analysis and mitigation in a sandbox D365 legal entity, staged in an Excel workbook first, then created in D365 with a confirmation list of primary keys.', 'example_request': 'Generate 25 demo risk mitigation records in USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-analyze-and-mitigate-risks-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need seeded demo data for analyze-and-mitigate-risks training or pilot scenarios in a sandbox D365 tenant — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataAnalyzeAndMitigateRisks(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAnalyzeAndMitigateRisks'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-analyze-and-mitigate-risks-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataAnalyzeAndMitigateRisks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
