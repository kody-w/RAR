---
name: "rar-cowork-cookbook-demo-data-develop-loyalty-programs"
description: "Generates 25 realistic demo loyalty program records in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_loyalty_programs", "rar_sha256": "aba9418230c5e0378fb8b06bad38e98b4bd399e6eb73baaf412c5eed202d1a52", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_loyalty_programs`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_loyalty_programs_agent.py` and in the RCI capsule.

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

Develop loyalty programs Demo Data Generator — Generates 25 realistic demo loyalty program records in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-loyalty-programs
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
      "description": "Sandbox D365 legal entity to write into (default USMF).",
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
      "description": "Excel staging file name, e.g. demo-data-develop-loyalty-programs-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_loyalty_programs_agent.py` and embedded as the fenced Python below (sha256 aba9418230c5e037…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_loyalty_programs_agent.py` first:

```bash
python3 demo_data_develop_loyalty_programs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_loyalty_programs_agent.py   # or on stdin
python3 demo_data_develop_loyalty_programs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop loyalty programs Demo Data Generator — Generates 25 realistic demo loyalty program records in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-loyalty-programs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_loyalty_programs',
    "version": '3.0.3',
    "display_name": 'Develop loyalty programs Demo Data Generator',
    "description": "Generates 25 realistic demo loyalty program records in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-loyalty-programs',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-loyalty-programs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f68b2f71e2474eb7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/develop-loyalty-programs'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/demo-data-develop-loyalty-programs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write into (default USMF).', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-develop-loyalty-programs-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic develop loyalty programs data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for develop loyalty programs. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-develop-loyalty-programs-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic develop loyalty programs records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo loyalty program records in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo loyalty program records in USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to write into (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-develop-loyalty-programs-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo loyalty program data in a D365 F&SCM sandbox for training or pilot scenarios. Sandbox only — never a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDevelopLoyaltyPrograms(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopLoyaltyPrograms'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write into (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-develop-loyalty-programs-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDevelopLoyaltyPrograms().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
