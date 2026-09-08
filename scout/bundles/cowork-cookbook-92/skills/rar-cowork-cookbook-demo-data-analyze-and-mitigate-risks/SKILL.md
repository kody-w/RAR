---
name: "rar-cowork-cookbook-demo-data-analyze-and-mitigate-risks"
description: "Generates 25 realistic demo records for risk analysis and mitigation in a sandbox D365 legal entity, staged in an Excel workbook first, then created in D365 with a confirmation list of primary keys."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_and_mitigate_risks", "rar_sha256": "97723700b68646db9dbb0b25c58b7468f5919cdcebc2e2e4a368096b80c7e39f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
