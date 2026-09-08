---
name: "rar-cowork-cookbook-demo-data-review-call-center-performance"
description: "Generates 25 realistic demo records for review call center performance in a sandbox Dynamics 365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and returning each new record's primary key"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_review_call_center_performance", "rar_sha256": "2b23f25584b2531edbd73c57d7b17c5997c3374572af290838f3452b43f7dc60", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_review_call_center_performance`. The original RAPP
agent is preserved byte-for-byte in `demo_data_review_call_center_performance_agent.py` and in the RCI capsule.

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

Review call center performance Demo Data Generator — Generates 25 realistic demo records for review call center performance in a sandbox Dynamics 365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and returning each new record's primary key

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-review-call-center-performance
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
      "description": "Sandbox D365 legal entity to write to (default USMF); must not be production.",
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
      "description": "Excel staging file name, e.g. demo-data-review-call-center-performance-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_review_call_center_performance_agent.py` and embedded as the fenced Python below (sha256 2b23f25584b2531e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_review_call_center_performance_agent.py` first:

```bash
python3 demo_data_review_call_center_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_review_call_center_performance_agent.py   # or on stdin
python3 demo_data_review_call_center_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Review call center performance Demo Data Generator — Generates 25 realistic demo records for review call center performance in a sandbox Dynamics 365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and returning each new record's primary key

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-review-call-center-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_review_call_center_performance',
    "version": '3.0.3',
    "display_name": 'Review call center performance Demo Data Generator',
    "description": "Generates 25 realistic demo records for review call center performance in a sandbox Dynamics 365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and returning each new record's primary key",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-review-call-center-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-review-call-center-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '72e8828e2a73d26c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/analyze-case-performance/review-call-center-performance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/demo-data-review-call-center-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-review-call-center-performance-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic review call center performance data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for review call center performance. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-review-call-center-performance-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic review call center performance records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for review call center performance in a sandbox Dynamics 365 F&SCM legal entity, staging them in an Excel workbook first, then creating them and returning each new record's primary key", 'example_request': 'Generate 25 demo call center performance records in USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-review-call-center-performance-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need seeded demo/training data for call center performance review in a D365 sandbox tenant — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataReviewCallCenterPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataReviewCallCenterPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-review-call-center-performance-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataReviewCallCenterPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
