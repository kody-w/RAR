---
name: "rar-cowork-cookbook-demo-data-manage-service-pricing"
description: "Generates 25 realistic demo records for manage service pricing in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_service_pricing", "rar_sha256": "a5a0059693bf6ad18c6c75ea62e728742f410f5994f9ccca61ce92e6fbcd2a72", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_service_pricing`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_service_pricing_agent.py` and in the RCI capsule.

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

Manage service pricing Demo Data Generator — Generates 25 realistic demo records for manage service pricing in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-service-pricing
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
      "description": "How many demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-manage-service-pricing-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_service_pricing_agent.py` and embedded as the fenced Python below (sha256 a5a0059693bf6ad1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_service_pricing_agent.py` first:

```bash
python3 demo_data_manage_service_pricing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_service_pricing_agent.py   # or on stdin
python3 demo_data_manage_service_pricing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service pricing Demo Data Generator — Generates 25 realistic demo records for manage service pricing in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-service-pricing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_service_pricing',
    "version": '3.0.3',
    "display_name": 'Manage service pricing Demo Data Generator',
    "description": "Generates 25 realistic demo records for manage service pricing in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-manage-service-pricing',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-service-pricing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2cab39c809f0534e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings/manage-service-pricing'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/demo-data-manage-service-pricing', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF).', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-manage-service-pricing-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic manage service pricing data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for manage service pricing. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-manage-service-pricing-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic manage service pricing records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for manage service pricing in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo manage service pricing records in USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF).', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-manage-service-pricing-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data for manage service pricing in a sandbox D365 tenant. Never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataManageServicePricing(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageServicePricing'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-manage-service-pricing-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataManageServicePricing().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
