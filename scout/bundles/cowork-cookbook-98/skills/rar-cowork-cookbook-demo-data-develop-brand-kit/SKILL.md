---
name: "rar-cowork-cookbook-demo-data-develop-brand-kit"
description: "Generates 25 realistic demo records for 'develop brand kit' in a Dynamics 365 F&SCM sandbox legal entity (default USMF), staging them in an Excel workbook first, then creating them and returning each new record's primary"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_brand_kit", "rar_sha256": "ef8dd01739a0f258cbea4c4fd13a496ec924b68fe6bf214371c895bf6744136e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
