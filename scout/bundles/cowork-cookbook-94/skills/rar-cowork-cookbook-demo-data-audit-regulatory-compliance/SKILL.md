---
name: "rar-cowork-cookbook-demo-data-audit-regulatory-compliance"
description: "Generates 25 realistic demo records for audit regulatory compliance in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, then creates them and returns each record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_audit_regulatory_compliance", "rar_sha256": "35eb6e29ac75052c1aad969ed072aba5dcdc5d5ed546c740a70302744bf3ab63", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_audit_regulatory_compliance`. The original RAPP
agent is preserved byte-for-byte in `demo_data_audit_regulatory_compliance_agent.py` and in the RCI capsule.

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

Audit regulatory compliance Demo Data Generator — Generates 25 realistic demo records for audit regulatory compliance in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, then creates them and returns each record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-audit-regulatory-compliance
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
      "description": "Excel staging file name, e.g. demo-data-audit-regulatory-compliance-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_audit_regulatory_compliance_agent.py` and embedded as the fenced Python below (sha256 35eb6e29ac75052c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_audit_regulatory_compliance_agent.py` first:

```bash
python3 demo_data_audit_regulatory_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_audit_regulatory_compliance_agent.py   # or on stdin
python3 demo_data_audit_regulatory_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit regulatory compliance Demo Data Generator — Generates 25 realistic demo records for audit regulatory compliance in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, then creates them and returns each record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-audit-regulatory-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_audit_regulatory_compliance',
    "version": '3.0.3',
    "display_name": 'Audit regulatory compliance Demo Data Generator',
    "description": "Generates 25 realistic demo records for audit regulatory compliance in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, then creates them and returns each record's primary key.",
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
        "upstream_slug": 'demo-data-audit-regulatory-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-audit-regulatory-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4d399419b0f9e8a8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/audit-regulatory-compliance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/demo-data-audit-regulatory-compliance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write into (default USMF).', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-audit-regulatory-compliance-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic audit regulatory compliance data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for audit regulatory compliance. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-audit-regulatory-compliance-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic audit regulatory compliance records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for audit regulatory compliance in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, then creates them and returns each record's primary key.", 'example_request': 'Generate 25 demo audit regulatory compliance records in USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to write into (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-audit-regulatory-compliance-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training/pilot data for audit regulatory compliance in a D365 F&SCM sandbox — never against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataAuditRegulatoryCompliance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAuditRegulatoryCompliance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write into (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-audit-regulatory-compliance-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataAuditRegulatoryCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
