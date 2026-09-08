---
name: "rar-cowork-cookbook-demo-data-nurture-opportunities-and-finalize-the-sale"
description: "Generates 25 realistic demo records for nurture-opportunities-and-finalize-the-sale in a SANDBOX D365 legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_nurture_opportunities_and_finalize_the_sale", "rar_sha256": "98765d583af85c3863f2e867af7dea26f5cdb0d306afe1ab52e761153aa5d391", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
