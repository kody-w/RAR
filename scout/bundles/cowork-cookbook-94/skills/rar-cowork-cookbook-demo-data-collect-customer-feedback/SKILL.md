---
name: "rar-cowork-cookbook-demo-data-collect-customer-feedback"
description: "Generates 25 realistic customer-feedback demo records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_collect_customer_feedback", "rar_sha256": "b95b716385bc39d7eae26bb4cc7bfcdab7387baf935c05837d2f148daa619b84", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_collect_customer_feedback`. The original RAPP
agent is preserved byte-for-byte in `demo_data_collect_customer_feedback_agent.py` and in the RCI capsule.

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

Collect customer feedback Demo Data Generator — Generates 25 realistic customer-feedback demo records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-collect-customer-feedback
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
      "description": "Number of demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-collect-customer-feedback-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_collect_customer_feedback_agent.py` and embedded as the fenced Python below (sha256 b95b716385bc39d7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_collect_customer_feedback_agent.py` first:

```bash
python3 demo_data_collect_customer_feedback_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_collect_customer_feedback_agent.py   # or on stdin
python3 demo_data_collect_customer_feedback_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Collect customer feedback Demo Data Generator — Generates 25 realistic customer-feedback demo records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-collect-customer-feedback
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_collect_customer_feedback',
    "version": '3.0.3',
    "display_name": 'Collect customer feedback Demo Data Generator',
    "description": "Generates 25 realistic customer-feedback demo records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-collect-customer-feedback',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-collect-customer-feedback',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6f7dcb0487ee102a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/collect-customer-feedback'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/demo-data-collect-customer-feedback', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-collect-customer-feedback-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic collect customer feedback data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for collect customer feedback. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-collect-customer-feedback-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic collect customer feedback records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic customer-feedback demo records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo customer feedback records in USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-collect-customer-feedback-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training or pilot customer feedback data created in a D365 sandbox legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataCollectCustomerFeedback(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataCollectCustomerFeedback'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-collect-customer-feedback-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataCollectCustomerFeedback().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
