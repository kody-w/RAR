---
name: "rar-cowork-cookbook-demo-data-define-customer-classifications"
description: "Generates 25 realistic demo customer classification records for a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_customer_classifications", "rar_sha256": "60480007a7b20ad7bba755c3b42a7e2fbed31e5288a4c2eed2ae2d9276224293", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
