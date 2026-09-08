---
name: "rar-cowork-cookbook-demo-data-manage-service-pricing"
description: "Generates 25 realistic demo records for manage service pricing in a sandbox D365 F&SCM legal entity, stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_service_pricing", "rar_sha256": "a5a0059693bf6ad18c6c75ea62e728742f410f5994f9ccca61ce92e6fbcd2a72", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
