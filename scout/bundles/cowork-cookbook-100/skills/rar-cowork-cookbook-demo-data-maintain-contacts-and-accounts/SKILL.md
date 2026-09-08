---
name: "rar-cowork-cookbook-demo-data-maintain-contacts-and-accounts"
description: "Generates 25 realistic demo contact and account records for a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns a confirmation list with primary keys."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_maintain_contacts_and_accounts", "rar_sha256": "a6db0393d023ec6d2baf7295f4d2d2450a22acf73a748ac42a4b23d0c26f81b7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_maintain_contacts_and_accounts`. The original RAPP
agent is preserved byte-for-byte in `demo_data_maintain_contacts_and_accounts_agent.py` and in the RCI capsule.

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

Maintain contacts and accounts Demo Data Generator — Generates 25 realistic demo contact and account records for a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns a confirmation list with primary keys.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-maintain-contacts-and-accounts
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
      "description": "Excel staging file name, e.g. demo-data-maintain-contacts-and-accounts-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_maintain_contacts_and_accounts_agent.py` and embedded as the fenced Python below (sha256 a6db0393d023ec6d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_maintain_contacts_and_accounts_agent.py` first:

```bash
python3 demo_data_maintain_contacts_and_accounts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_maintain_contacts_and_accounts_agent.py   # or on stdin
python3 demo_data_maintain_contacts_and_accounts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain contacts and accounts Demo Data Generator — Generates 25 realistic demo contact and account records for a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns a confirmation list with primary keys.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-maintain-contacts-and-accounts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_maintain_contacts_and_accounts',
    "version": '3.0.3',
    "display_name": 'Maintain contacts and accounts Demo Data Generator',
    "description": 'Generates 25 realistic demo contact and account records for a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns a confirmation list with primary keys.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-maintain-contacts-and-accounts',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-maintain-contacts-and-accounts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b55a0081d89987e0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/maintain-contacts-and-accounts'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/demo-data-maintain-contacts-and-accounts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF).', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-maintain-contacts-and-accounts-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic maintain contacts and accounts data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for maintain contacts and accounts. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-maintain-contacts-and-accounts-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic maintain contacts and accounts records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates 25 realistic demo contact and account records for a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns a confirmation list with primary keys.', 'example_request': 'Generate 25 demo contacts and accounts in the USMF sandbox, stage them in Excel, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-maintain-contacts-and-accounts-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo contact/account data in a D365 F&SCM sandbox for training or pilot scenarios, never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataMaintainContactsAndAccounts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMaintainContactsAndAccounts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-maintain-contacts-and-accounts-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataMaintainContactsAndAccounts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
