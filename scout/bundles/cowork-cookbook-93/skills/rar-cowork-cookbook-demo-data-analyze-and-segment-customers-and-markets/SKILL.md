---
name: "rar-cowork-cookbook-demo-data-analyze-and-segment-customers-and-markets"
description: "Generates 25 realistic demo customer/market-segmentation records in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_and_segment_customers_and_markets", "rar_sha256": "a3654d4070644ec6d15bd924c332f39627cf17ec49a3311b2c2876a0d258efc2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_analyze_and_segment_customers_and_markets`. The original RAPP
agent is preserved byte-for-byte in `demo_data_analyze_and_segment_customers_and_markets_agent.py` and in the RCI capsule.

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

Analyze and segment customers and markets Demo Data Generator — Generates 25 realistic demo customer/market-segmentation records in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-and-segment-customers-and-markets
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
      "description": "Excel staging file name, e.g. demo-data-analyze-and-segment-customers-and-markets-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_and_segment_customers_and_markets_agent.py` and embedded as the fenced Python below (sha256 a3654d4070644ec6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_and_segment_customers_and_markets_agent.py` first:

```bash
python3 demo_data_analyze_and_segment_customers_and_markets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_analyze_and_segment_customers_and_markets_agent.py   # or on stdin
python3 demo_data_analyze_and_segment_customers_and_markets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze and segment customers and markets Demo Data Generator — Generates 25 realistic demo customer/market-segmentation records in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-and-segment-customers-and-markets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_analyze_and_segment_customers_and_markets',
    "version": '3.0.3',
    "display_name": 'Analyze and segment customers and markets Demo Data Generator',
    "description": "Generates 25 realistic demo customer/market-segmentation records in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-analyze-and-segment-customers-and-markets',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-analyze-and-segment-customers-and-markets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6fdd96512442ee27',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/analyze-and-segment-customers-and-markets'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/demo-data-analyze-and-segment-customers-and-markets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF).', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-analyze-and-segment-customers-and-markets-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic analyze and segment customers and markets data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for analyze and segment customers and markets. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-analyze-and-segment-customers-and-markets-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic analyze and segment customers and markets records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo customer/market-segmentation records in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo customer segmentation records in the USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-analyze-and-segment-customers-and-markets-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need seeded demo data for customer/market segmentation in a D365 sandbox for training or pilot scenarios. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataAnalyzeAndSegmentCustomersAndMarkets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAnalyzeAndSegmentCustomersAndMarkets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-analyze-and-segment-customers-and-markets-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataAnalyzeAndSegmentCustomersAndMarkets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
