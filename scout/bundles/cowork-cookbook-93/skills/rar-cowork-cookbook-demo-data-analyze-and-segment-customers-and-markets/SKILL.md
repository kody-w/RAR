---
name: "rar-cowork-cookbook-demo-data-analyze-and-segment-customers-and-markets"
description: "Generates 25 realistic demo customer/market-segmentation records in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_and_segment_customers_and_markets", "rar_sha256": "a3654d4070644ec6d15bd924c332f39627cf17ec49a3311b2c2876a0d258efc2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
