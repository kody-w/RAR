---
name: "rar-cowork-cookbook-demo-data-nurture-opportunities-and-finalize-the-sale"
description: "Generates 25 realistic demo records for nurture-opportunities-and-finalize-the-sale in a SANDBOX D365 legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_nurture_opportunities_and_finalize_the_sale", "rar_sha256": "98765d583af85c3863f2e867af7dea26f5cdb0d306afe1ab52e761153aa5d391", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_nurture_opportunities_and_finalize_the_sale`. The original RAPP
agent is preserved byte-for-byte in `demo_data_nurture_opportunities_and_finalize_the_sale_agent.py` and in the RCI capsule.

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

Nurture opportunities and finalize the sale Demo Data Generator — Generates 25 realistic demo records for nurture-opportunities-and-finalize-the-sale in a SANDBOX D365 legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-nurture-opportunities-and-finalize-the-sale
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
      "description": "Sandbox D365 legal entity to write into; defaults to USMF.",
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
      "description": "How many demo records to generate; defaults to 25.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-nurture-opportunities-and-finalize-the-sale-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_nurture_opportunities_and_finalize_the_sale_agent.py` and embedded as the fenced Python below (sha256 98765d583af85c38…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_nurture_opportunities_and_finalize_the_sale_agent.py` first:

```bash
python3 demo_data_nurture_opportunities_and_finalize_the_sale_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_nurture_opportunities_and_finalize_the_sale_agent.py   # or on stdin
python3 demo_data_nurture_opportunities_and_finalize_the_sale_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Nurture opportunities and finalize the sale Demo Data Generator — Generates 25 realistic demo records for nurture-opportunities-and-finalize-the-sale in a SANDBOX D365 legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-nurture-opportunities-and-finalize-the-sale
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_nurture_opportunities_and_finalize_the_sale',
    "version": '3.0.3',
    "display_name": 'Nurture opportunities and finalize the sale Demo Data Generator',
    "description": "Generates 25 realistic demo records for nurture-opportunities-and-finalize-the-sale in a SANDBOX D365 legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key",
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
        "upstream_slug": 'demo-data-nurture-opportunities-and-finalize-the-sale',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-nurture-opportunities-and-finalize-the-sale',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e0afa326f4da6588',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/nurture-opportunities-and-finalize-the-sale'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/demo-data-nurture-opportunities-and-finalize-the-sale', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write into; defaults to USMF.', 'record_count': 'How many demo records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-nurture-opportunities-and-finalize-the-sale-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic nurture opportunities and finalize the sale data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for nurture opportunities and finalize the sale. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-nurture-opportunities-and-finalize-the-sale-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic nurture opportunities and finalize the sale records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for nurture-opportunities-and-finalize-the-sale in a SANDBOX D365 legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key", 'example_request': 'Generate 25 demo nurture opportunity records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to write into; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-nurture-opportunities-and-finalize-the-sale-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data for nurture opportunity and sale-closing scenarios in a D365 F&SCM sandbox. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataNurtureOpportunitiesAndFinalizeTheSale(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataNurtureOpportunitiesAndFinalizeTheSale'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write into; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-nurture-opportunities-and-finalize-the-sale-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataNurtureOpportunitiesAndFinalizeTheSale().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
