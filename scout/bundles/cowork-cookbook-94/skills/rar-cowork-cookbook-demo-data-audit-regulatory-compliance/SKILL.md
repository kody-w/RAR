---
name: "rar-cowork-cookbook-demo-data-audit-regulatory-compliance"
description: "Generates 25 realistic demo records for audit regulatory compliance in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, then creates them and returns each record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_audit_regulatory_compliance", "rar_sha256": "35eb6e29ac75052c1aad969ed072aba5dcdc5d5ed546c740a70302744bf3ab63", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
