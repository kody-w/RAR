---
name: "rar-cowork-cookbook-demo-data-develop-brand-kit"
description: "Generates 25 realistic demo records for 'develop brand kit' in a Dynamics 365 F&SCM sandbox legal entity (default USMF), staging them in an Excel workbook first, then creating them and returning each new record's primary"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_brand_kit", "rar_sha256": "ef8dd01739a0f258cbea4c4fd13a496ec924b68fe6bf214371c895bf6744136e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_brand_kit`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_brand_kit_agent.py` and in the RCI capsule.

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

Develop brand kit Demo Data Generator — Generates 25 realistic demo records for 'develop brand kit' in a Dynamics 365 F&SCM sandbox legal entity (default USMF), staging them in an Excel workbook first, then creating them and returning each new record's primary

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-brand-kit
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
      "description": "How many demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-develop-brand-kit-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_brand_kit_agent.py` and embedded as the fenced Python below (sha256 ef8dd01739a0f258…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_brand_kit_agent.py` first:

```bash
python3 demo_data_develop_brand_kit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_brand_kit_agent.py   # or on stdin
python3 demo_data_develop_brand_kit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop brand kit Demo Data Generator — Generates 25 realistic demo records for 'develop brand kit' in a Dynamics 365 F&SCM sandbox legal entity (default USMF), staging them in an Excel workbook first, then creating them and returning each new record's primary

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-brand-kit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_brand_kit',
    "version": '3.0.3',
    "display_name": 'Develop brand kit Demo Data Generator',
    "description": "Generates 25 realistic demo records for 'develop brand kit' in a Dynamics 365 F&SCM sandbox legal entity (default USMF), staging them in an Excel workbook first, then creating them and returning each new record's primary",
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
        "upstream_slug": 'demo-data-develop-brand-kit',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-brand-kit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '07356e9f79a659db',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/develop-brand-kit'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/demo-data-develop-brand-kit', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-develop-brand-kit-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic develop brand kit data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for develop brand kit. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-develop-brand-kit-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic develop brand kit records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for 'develop brand kit' in a Dynamics 365 F&SCM sandbox legal entity (default USMF), staging them in an Excel workbook first, then creating them and returning each new record's primary", 'example_request': 'Generate 25 demo brand kit records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-develop-brand-kit-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data for develop brand kit created in a D365 sandbox tenant — never against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDevelopBrandKit(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopBrandKit'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-develop-brand-kit-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDevelopBrandKit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
