---
name: "rar-cowork-cookbook-demo-data-maintain-contacts-and-accounts"
description: "Generates 25 realistic demo contact and account records for a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns a confirmation list with primary keys."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_maintain_contacts_and_accounts", "rar_sha256": "a6db0393d023ec6d2baf7295f4d2d2450a22acf73a748ac42a4b23d0c26f81b7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
