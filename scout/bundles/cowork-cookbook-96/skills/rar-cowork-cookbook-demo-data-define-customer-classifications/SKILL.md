---
name: "rar-cowork-cookbook-demo-data-define-customer-classifications"
description: "Generates 25 realistic demo customer classification records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_customer_classifications", "rar_sha256": "60480007a7b20ad7bba755c3b42a7e2fbed31e5288a4c2eed2ae2d9276224293", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_customer_classifications`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_customer_classifications_agent.py` and in the RCI capsule.

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

Define customer classifications Demo Data Generator — Generates 25 realistic demo customer classification records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-customer-classifications
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
      "description": "Sandbox D365 legal entity to target (default USMF); must not be production.",
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
      "description": "Excel staging file name, e.g. demo-data-define-customer-classifications-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_customer_classifications_agent.py` and embedded as the fenced Python below (sha256 60480007a7b20ad7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_customer_classifications_agent.py` first:

```bash
python3 demo_data_define_customer_classifications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_customer_classifications_agent.py   # or on stdin
python3 demo_data_define_customer_classifications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define customer classifications Demo Data Generator — Generates 25 realistic demo customer classification records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-customer-classifications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_customer_classifications',
    "version": '3.0.3',
    "display_name": 'Define customer classifications Demo Data Generator',
    "description": "Generates 25 realistic demo customer classification records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-define-customer-classifications',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-customer-classifications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd5105f35417d74ee',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-customer-classifications'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-define-customer-classifications', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-define-customer-classifications-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic define customer classifications data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for define customer classifications. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-define-customer-classifications-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic define customer classifications records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo customer classification records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo customer classification records in the USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-define-customer-classifications-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training customer classification data created in a D365 sandbox legal entity. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDefineCustomerClassifications(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineCustomerClassifications'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-define-customer-classifications-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDefineCustomerClassifications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
