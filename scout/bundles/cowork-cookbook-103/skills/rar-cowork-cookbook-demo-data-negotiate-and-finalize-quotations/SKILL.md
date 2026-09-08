---
name: "rar-cowork-cookbook-demo-data-negotiate-and-finalize-quotations"
description: "Generates 25 realistic demo sales quotation records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_negotiate_and_finalize_quotations", "rar_sha256": "56e43a27ced3ed2c9ee3beec87d33f8ca90ee2fc26dc42fd45c98fc83e4dd0ed", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_negotiate_and_finalize_quotations`. The original RAPP
agent is preserved byte-for-byte in `demo_data_negotiate_and_finalize_quotations_agent.py` and in the RCI capsule.

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

Negotiate and finalize quotations Demo Data Generator — Generates 25 realistic demo sales quotation records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-negotiate-and-finalize-quotations
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
      "description": "Sandbox D365 legal entity to create records in (default USMF).",
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
      "description": "Number of demo quotation records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-negotiate-and-finalize-quotations-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_negotiate_and_finalize_quotations_agent.py` and embedded as the fenced Python below (sha256 56e43a27ced3ed2c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_negotiate_and_finalize_quotations_agent.py` first:

```bash
python3 demo_data_negotiate_and_finalize_quotations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_negotiate_and_finalize_quotations_agent.py   # or on stdin
python3 demo_data_negotiate_and_finalize_quotations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Negotiate and finalize quotations Demo Data Generator — Generates 25 realistic demo sales quotation records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-negotiate-and-finalize-quotations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_negotiate_and_finalize_quotations',
    "version": '3.0.3',
    "display_name": 'Negotiate and finalize quotations Demo Data Generator',
    "description": "Generates 25 realistic demo sales quotation records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-negotiate-and-finalize-quotations',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-negotiate-and-finalize-quotations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a81675e8de85f47b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/negotiate-and-finalize-quotations'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/demo-data-negotiate-and-finalize-quotations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF).', 'record_count': 'Number of demo quotation records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-negotiate-and-finalize-quotations-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic negotiate and finalize quotations data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for negotiate and finalize quotations. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-negotiate-and-finalize-quotations-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic negotiate and finalize quotations records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo sales quotation records in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo quotation records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo quotation records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-negotiate-and-finalize-quotations-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data for negotiate-and-finalize-quotations in a sandbox D365 tenant. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataNegotiateAndFinalizeQuotations(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataNegotiateAndFinalizeQuotations'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo quotation records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-negotiate-and-finalize-quotations-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataNegotiateAndFinalizeQuotations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
