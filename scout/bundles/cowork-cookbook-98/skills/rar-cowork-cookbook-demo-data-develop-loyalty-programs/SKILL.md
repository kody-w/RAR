---
name: "rar-cowork-cookbook-demo-data-develop-loyalty-programs"
description: "Generates 25 realistic demo loyalty program records in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_loyalty_programs", "rar_sha256": "aba9418230c5e0378fb8b06bad38e98b4bd399e6eb73baaf412c5eed202d1a52", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
