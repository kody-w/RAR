---
name: "rar-cowork-cookbook-audit-create-production-plan"
description: "Audits create production plan records in a Dynamics 365 F&SCM legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel audit"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_create_production_plan", "rar_sha256": "63e4fb3884f7a9edd58bbe30409e01baf592fccceb19cffcab616eb8a6f3e127", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_create_production_plan`. The original RAPP
agent is preserved byte-for-byte in `audit_create_production_plan_agent.py` and in the RCI capsule.

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

Create production plan Completeness Audit — Audits create production plan records in a Dynamics 365 F&SCM legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel audit

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-create-production-plan
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
    "date_window": {
      "description": "Date range used to judge stale dates; adjust for demo data (USMF data is mostly FY2017).",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to audit, e.g. USMF.",
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
    "output_filename": {
      "description": "Name of the Excel workbook to produce, e.g. audit-create-production-plan-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_create_production_plan_agent.py` and embedded as the fenced Python below (sha256 63e4fb3884f7a9ed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_create_production_plan_agent.py` first:

```bash
python3 audit_create_production_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_create_production_plan_agent.py   # or on stdin
python3 audit_create_production_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create production plan Completeness Audit — Audits create production plan records in a Dynamics 365 F&SCM legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel audit

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-create-production-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_create_production_plan',
    "version": '3.0.2',
    "display_name": 'Create production plan Completeness Audit',
    "description": 'Audits create production plan records in a Dynamics 365 F&SCM legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel audit',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-create-production-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-create-production-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4966be86be830303',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/create-production-plan'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/audit-create-production-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; adjust for demo data (USMF data is mostly FY2017).', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-create-production-plan-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit create production plan records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to create production plan. Output an Excel workbook 'audit-create-production-plan-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no create production plan data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads create production plan records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits create production plan records in a Dynamics 365 F&SCM legal entity for completeness and policy compliance (missing fields, stale dates, blank descriptions, inactive references) and returns a read-only Excel audit', 'example_request': 'Audit create production plan records in USMF for completeness and give me the Excel audit workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; adjust for demo data (USMF data is mostly FY2017).', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-create-production-plan-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness/policy audit of create production plan records in D365 F&SCM, delivered as an Excel workbook with per-category and summary sheets.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditCreateProductionPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditCreateProductionPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; adjust for demo data (USMF data is mostly FY2017).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-create-production-plan-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditCreateProductionPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916eZOjSJbnV9HGmG1VjTIDEKeyrc0WAQIkEPchVbZlcYM4xSGBauq7ryNFZGZ1Z/dMm+1fq7AIgeP+7vd7z8P5/cUb+rRuXz69GJFXLXivKLI0ahdeFS6Y+la3Ofiqcx/8LoK66tvMH/q67V4+vIRRF7RZ02d1BZbTQ5j13SJoI6+PFk1bh0MwP1o0BaDbRkHdht0iqxbegp0qr8yCboES+GL7vw1GXhRR4hWLqOqzflrEdQt4lU0R9VEVdd1DmKYusmB6jmdeFUSLn8us67IqWcRZVITdh0XXe0W0CAF/cOMDtvniOxnBWFZ5QKZrBMSJozYCRLpfHsTbqB/aCjACV174sa6KacGNQVQsvFktoGw0erNA3cunX//24SUD1y+ffn8JCq/r3pVnHqqrXzVXgQRgJfibgCnNBOw83zdRCxQswVAYxYu3u5+7qIg/LP7zP/Ob1ybdL58+V4u3z+eX+UcfqkWfRou+9ro+CheB13h+VgBzvS7o4uZN3XdKdMBNVfL6XPmNUt0s/jo/+/nJ5DWJ+p8/v9RABG+W9/PLLwtg+c8v7TBfv85Ump9/eS3qW9T+/Ms3Ot3gn6Ogn4kBqV+/vN2/kQUTv03N4sUXQ+WYN14gDLImAsS/02/+PEV/I/dmki/PyT/XzYfFjynP+vwVyPt0sg/o/pgssAFY+fJ6rrPq5zcebX2NqjmMfv7ln5EN0ijIi6zr/0d0f30STkH8AGu9meSXDw/3/W2xfNPtK81/znbOl39HEzD9nd1XQ/0z2g/P/h3pIgM59tWXPyT3owXLvy5+/ae6/asFHxbx5xc2KkAetp5fRJ8Wvz9C5Nefwm+DP/3tD0D6vyVj1EMbPCh8Kb0qi6Ou//Ll15+6x/BPf/v1p6EBURx55ZehLX5E80d2ffD5kwXfZv3857WAv1XlVX2rFl9zaPF73fyv9o/Xhe0VWfhtvPu0+D4T589yMSvxzvRpgu+ysQOyfmfHX17+ALBTAW2e4DKjzn/8x0LOgrbu6rhfGEE99Avg4D4ro1l4M80A3nYP1GgjYNcuA4Z9mwfif/bwLHEdL377P8ED6j8Gb1APPWDvyxPMv3wD80d4/Pa6MAHNus0SAKjFQqdV9XPlJQC9Z35NG3VRewUY5U999BGk8sf5Yob+3/4V2S8PCq/N9NsDkrMn3umMOGNdNxTR66yVk0bVmw4BqCvRGAUDIF7UAZAkzooZ+oEAdQFQvp8t0OVZUSzCDKAJqFvTE+6H6tNM7LfffvO9Lv1cPcEZXTyLRQeBCV/FWXz8CFSKiyxJ+89VFKT14qff//hp8V+Lf7XqQXzmoYIK8eYDIOHOUA4LkFNDCabN5RCAuRc+fPD7H2+GBWQqUIGBxzJQ2Z6LQUzmUfhuZUOgP65wYuFHwLrAsmVTt/1cCbP+dSHGi6/yAqbzo7kmpHXXg3LYRFUICt8EqHpAna+WrOp+0YHA6+Lpw2LoogfX3/zWe4hYguT2+t8WMqOCClQX4M8s5mMSWFxXGTD/1xh4jgMi7U/dYvNO4nVxmKNw0Xit16St98Yj9p5+AZXnfTkg7i2q6Pa5mutsNJvqkRJP84BJwDLBm0s/zj6fuwKQ/8/+on+f48110nzUy/Zz1b2Fu9dGj24EiDItkiEL5yLwl7eQ6tJ6KMKH/YCkM6U3L4RvXnnEIPPjHof5vmV5dASLz8MKRrDF/8+90WwQmud1jqdNjl1wB1M/Ph01t4uzQ58d5rvwj6T81r28I9Q7UH+uigxEXTv95Tnz4d63OU/wG1rgDZ3WH/RBbAFHzXQfoT+HctvOSeN9rt4rwgcg+gP+gMEBToA8msP3neH89F3SFIDBfP+tO3hzzmwIEN6LZvCBpRdxFIW+F+RAqtkm724GeRDNqXxLsyD9k1az90C4AfoLIMQcC6BqvH5F6efTd9H/tPDZBM1LHg3iALK3fRAAcsxOerjolvUAxLz+2Z0DPT89iAA1yqafdfdB/gBNn4PAu5ch67JHKDztGjUAoz/O309N59FobEDKAGOBxGgGYN1HKs0xVYIWB8gAAghkVplVoOQDo7wZ4UHQK2dcALj7FjxPio/hN4WiR/7Ntep94azIvGYu/4sYiA5Gpu/hw/xRmAB65TzjwffvI+0rt5n2DKEdgEHA8f3ps094fZb6Zy+xeKf76R+2Pz//ezukR/G2/hwAnxZp3zfdJwh6Ftz3evsKUhd6yto9a+/HJ1h8/AYWHx+N4fc0n+p+Wvx7cv2JxFtefFogr/ArPD+S3uLq7QPMwHzcHD9i89PPlR59g1bAvi5BYM1Om0Cx/1oH36eAYpi0ALzA5Gdd7OZyegMV/FEIgAc+V98H+pxooM5UyRyYXf0dADwaAhD0T4d9rVfgUdUD3uHcNibR67zbmsXvopdP1VAUH14AmEb/zf5srkflHMndvKMD9gYdWJ9Fj7sHMIz9fPnn3a7yuPCK1wUbARAquu+j7a2KzFX0u6R4KggUCwCHD08onqseUHBmPieU14EIBcE5K9JPzSz5cys3N3/zgi+3rArr2z/Kw86FpZ1NN7N9ANx5CJPoe9z/y8ILzwPoAubwD6Oynoe9xc+WIW+fl8DcJWgTgEW3RyA3+csPBXnUoy/PevQDSebC9aeSNZfz2f4fFtFr8rqY2f2Q7tfW9x+JOqD7mOmE9ae5EH94g7YPjwL6YfF15/Fh8b4XnDlE1QC22b/Ou57Zz48l88XT718Xff1Xhh+9/O1Hcj3w78sciM9w+nvpDjOuAdyfvfysjHP2PRIPyPzM4OhN+3+V3B9X8Ir4COMfV9jrWHTjD6wExHmgN6iBs2bfTPZN8Pqxd5sFBzT7578afn8BEe7NPn6L8bfmH0wHYPexm5sfCEAAYAjun8kKnv1b24K3tV3qgdYULCbQCIt9lKKwmPTWURjilO9HKIzB6whGfC/G16s4CILIR9ZBHAeeTyBE5FMeEaMRsiIBvWe6f5m7u2yWZxYGmOEjQIzo22MwFL4p8hR8ttLXXcis8Js+v7/4BAZmClgn0s8PA60RH3JIf5JcyIWpsbg5Q7P1QFiU6rpsrtLZG3PYoXfllVvpR8lG6DrItLHJkyEltTNP+wQnoIyaFxBO3WTF0+oVlWfR+nrYTJMur2KlkqFYMdWVyq9vVpclBSNeu0uyn+6ppJ8w7mKed2GVZwZe7JvANPd1I1HBEoLgA2RlUlchpigzXbaLdtZG2cHVzSOVrZlNq+Vym0HLJXTPC+uc7/KMM+UBQ8Ueseuz5hq2KOLbytDvwzqWMYOTG73tj4BfmAlWl8PpIWUurC7WIrFUJQbU2SzPLp2Y3o+JqWJnjTaRwCD3YyFaW+58KjAxGC6GxGlq4uoHbjCv7nkpnowdw6d+QgkmSa4hCrqTzWoZV1hbtevlchnkrk8Gxn1vJp1sJEHT2cXVnnhYVjSd6LDaiDB72N1sZzAKNmZPO8zWzC1UdOtgs2JPd5mjJwa+NIweqSrMnmQVKzTHZI9DHPPTRuGzjLGPQjQxhy0u2RZJrxur29I5OQU76c4Q9+hcEB5UBZuykVCCD/d4OXGSnRl0wqr7tcNJu6Mxln1ypQ11x2GOhDRFftHbwEUOCYG28UpD6noN66ck4W/JAJPrW0T3pEVA3X1Cm1IolF0Aa4bfZt7ZMDZHSjAmzSuSEUF5XND0wgkMABoadhrbJMYjt1cK25L9Y11hYhHjwWg0JeT0+FRNxCqHmt1qqQtdrQ7aKDFM2U7txFiHdZkY7e5cnTa6eqc9rjmRigiPg6KFFMQlKQwLmbHrT6cNFOqdftynV23D5lmgQ3dt6XAC65GMvEOvYytu9rdwo5QI6+7zTavfDtjk4SFidDph6IqEu8dTcT5cC/tkHzWjS+OsYqm9gVpKT6JKll+picHdJbPm8XG3XJoolpGBpm6Fjs34+zHYVql+YfF63Z8DaNtn4/1wgg5agx3LKl/GglHytnVfN8vmnLTmLmvkvXHBdqrt4EvpPAhiw2+iYzZBlA5h56ta3jtDvW8mEStBpHlxbbsJGU00whgjrwkO2/h0QIoF2o9OfQ3lVJPvfc47t9VGE63NIJ8PF4iK6bV647vOaMR42J4OUKoPCaqzp0syjRTSKCszdXLqdj6bB+Mi3PbZagxFU7P5KVFvkB6Sm8BJwljqLDMwlcR0kwsq7+irVN2yjFUb6q6w7HW1u9Zr8QJwY7lFnSw0L6PRZ3vbGaWdPu5ESzYN86ylDdQEGlaqpCrWdjqs3OKasTJ8ONR0xR7UJVox165o7Q28wqD7xewhVjru5WnJy6fGlnlsnQ/2Tr+x6SiP7tY9sv5JKhO9yhqyuXBZzDIHLBXhfqLutbPen5W9m+wu8tEh4/hAbibtnkxUgTNo3p9wWdliRswtOcQh+UK4N5OH4ss2kaSwq28FObYMilhN1ScbYXeTLqfjdPX2B8lp/Ymxs3isM229uZP3YSIP+cUS+BoN4LuGUtV9aDn82KO7S9fXYxbZLcF6w3bSbYIeqINFY1eiKGCHLTORtBgJZKGZHrtSKpktoZvRtiCYcENX5eBdskYRuQKxRuVqHGByByX3sj8B74bBSFNQvG2c4KBA8JK3As/iEUGwMWWPrwbSP63FCTS9Go+mvItahaMC+9mbwQuR6EY2CAahtTppyrrZIceRFkIh0ETNKU+r3TmicLweBRYTEjgZT4e94disMl5Gh8Z05wDVAt9vOOKe4ZxGLeEi4cytsSJYLTEnkS5pjc7ODG0khF7rp1HxYWKwfReW8QTb5LRq5CcTYHwXykPPbDGxVk6bVWdlSpSs7EPdbOk4oe/FwRQDS9d5Q9vkxqlEnXV6W5WWIcGM1pAc2QanxrOm1SFUMHQQN8URhlVVg2OZvyBBi1zWTHAYjiv2SHpRAfX5ZUKOd+2u3FUJXkbXOw6ZCV/mQsnHxt6IN41dFxwvkCK8GhGNkDhIV9Pk1MUkOToZukfOmyV81BIfQeI1RVHIHqqrZQzlYowhYWkVkXBEgOUiQ9KSlJXEwr0FqITtOON4ySm3DlPEYRg2AaHd7ZCt6QM8Ce6B3Wr8RK1sqzh5VhFEhAai/ixrq1aDNEt0m71ot0Kc1+w07VmxjqxDl41Naa16bwthxylDDyLqyX4sRJAclBUDKZNITPixcXTXwLs0reSKxgsUN7EKRXeTraB1BIJhaTtCQXbnTZLUDFeEY14wEZmf0n4j9Wk/ndItO/HC1lmaViuE150Lsu82Hbd5Zx4LLAstXTobCXxBAwkSjhmZ0TqHUNAOinVHZPfWtqcndhfdrtDeuAq1WGQuUmygEbOYvoAZUhktF9ram445JHs30+1bzdCo04Qoid/qgtGthEMAYl/5ft8ZWabS9rhvc3cf0pB0jTaZm9hOcR6zY2ndgjTU0By7bttk649WpoOQOPnabbmqDK7FXY45CH2klctTuS01eVQr0RNd0PENgrVqIhI9cAkuUdx502gbHbukW0yqm9iONRXj+21gh3Ybn+RJhqj9srTPOif1k1dt71IGC9YFz/jTMBiBZxa2fxA5JVzJm4wmdveKKJoDjcJCWqdYsQq3+xOp10QMn5hN6nIJ066YIHOnsDCoKT34lX7c7tOsaHRTM/HKBY2W7km7qJaPwqCTNdOcNYgz+3x33tcAmx2op7UK9pLtno7TCep1eroJJNf45m21v+thdixqJmMs9bAOT/12GZ2RM21ACMXtrgD11TTIWS44n5xrHN1aUrE9lRU2ZVVLGqWi/TIYhAYLycyZzif5guuh2x2aA5eux1ONsJ5kHiwph3XlnlmiVXXM8qrrOteUXhASnM05ydnmITzNlDHtqCvAQY8lvDSxNKFbWbs8YPWwYPZnFj+VZrMMQVuTa1Z1t1enXFpubtEm1/cnC9skU0j4hsQbMLEbrzJ6gncCy09hxXoZZUI1IlL77WmqIx/G4ZvReCiVbLS66PYTR+SZpyK7s0dTEbzMvGRPMEvC76DlWulI1ss93pfYq6nx6urck8tcbk261Sm2Wd8m15aVHZrTcMrvPfzkddn2foFU/ugSSl6Oeb3BV72jmXrWTbSWnsHOSbqenF1G8bpP3x3LqMKwVVjktt/U+dU8217IdjeNu9lMwuW132yafSeLoOcUOAT2jTyhVzf5fjHqbjRqA7ano483N1X0PEMhm8FWVlZW+9bGGo4xeq3rFZwhNmaoerTU8KKE8xAvkvMIrSOVvKQxJl7WeJG19U5CcQJSMknFcHxvECfzKJ374Bw4lQXbg8Ipo2CgUMYwfJt2veE2m9teuZv4wbLS5abtHcCh2VDDiRO2Db9mcQLL1QqlCJVDYTiMzXEN4e5aROgopi4Noh72W+nCI3bRbw/M0Es1f00uejb2uOgUVaN7eXBW2HuTHbSJ6aZdZzDE2ijNujWztFvaPqdoJbZZt8edyYXZ7aIluVOuqqaOaMqqs5wQ90nhx5RAu7hjXaTEZnZlh90gmMnLIlR7eLddStQu9GB1qfqlZu7a7e1ENjmOivtt76u7m89GlBTX1Tbf8keoKy+izXfICSFuWHS6rEhzV2Qxv1fwRnEdEpQkK+L30uHqD6G+6/DWCcv9iV+rzNLqD4rYDfUA3xzFqf0a9kbZZ1qF6+EQ9GP0RiUPS1HKp9WtwfCWPUP89hh63tq820jXGLhgikd9tee3I1Qbudmz3fXQ9he57FJoJ2sszphLERbX4y4zUwBbhb/d2xRl74UzvvcU9zYkjiAUnHzflaJ0OmeDpW1PBdveg5vtn9r8qpegeIE2HYcl4Xavl2GtZOWhxoY6qLrW49hOz/stfe+bqoNM3r5tJ7nDKiiXrxZe9iHOyCldudHpxHBhqx52jRDIk3THUlsfis09gdDhLG2cacnt4pY0XWgM1xx5JoBHqLShXQSdWjae9hf/Wh58LC49W1hX68DAjN0Wa8Sxasw9UZyrtmeuYhmOkFNoKTocSoEUZAayhgRh0rNJxYzm6jGBehl/ozZxpk9Mkh5gSbWbg9OkRRcoq3p7JEgeLu81Uqa9XrNF4nN2M+E0kV2MC3drDzFCONKy5NnY6t1z7wdqHO+HE5WHtMDADceVfe8FauaaR9nsdyRxXIE2VFHSItKpNS+tb1h6gRvXwtFUxW8Rz426NiSBUIW7OD/Bp21xS+wcJAelDuxZPnBbV4rz7pjF8lAicdk0FhbE2kVAd6i2nBx0SBSD87JQnMjjZggvER+rNtGB4GsjD17X5C71dpbU62tPC+6JKQpbxZddgwIws4UzYsCSFd13wpWl2Yp1MRTqlilxD45n20GihBIHbmKKkB+lnCNOJFbqFwrbXFSuPhJbP1versvuPPgHz1+F2opIG3WXDskQ4uW+J3lcIfYrVmly+346CI0EFZR4qPweAPGWJ6RjlVmXSEicQ5w1vWt2THQ6hPZuibqVeRDXko/UV2SET+RREe+dWblxGNm3Au4tGjHb5hKuTQKjldNZdZp7gAucgNmjV6hDOnnUirVUBfdgyMf7zZqL/U14rojLzU+EEiO2UXc1WG49KmCzqEPFddzfNhJXl6Mil6ZRHSQ2yryMZDaHNLplRM4NLerFKwFqjuo+I+M1AiO82/RdFICOim1IDzGlfolRE+W7E3S7svqKh7bcgJakn9yE5uxQLARRbkxxyHDCeVNbDj00slQVNM3RHy/LYh1uOnurbBjg2JNOGq18vmPjlo3EEdmL6tBBaoUwZooQlRFMIcfpxp5f5VncHdVEAklvsffxSjbymjrw+CFbhwR+HelRv9BEG7H37uAYfcK4OZNGxZIPsAC/lygHsoXNg4p0cZ06kPUOjDAZ0k0cvbnw8SpGEAQlw2JX0Zjbo/ShqvxWLvWMuG93GOJsVHXkXOZOAJz3YLK+Egxauq6gd0yo6vvVWaMqfVltvSlYtgIJH1Tq3DCdJeYJ1+RJoF4hl3fDqqGOxHFSId8ZOt3Od+tDI9rRyus9Qi1Gb6utzayl88MV40fhvLpfdQKaNtP9nB/5mDgUd38SliJDOlVKo6sN1xqn/f4gVltMPsPyvb2c9w2T5KzK748uCrVZmjJFrV/bGo3Kc3lWZB7PTZHf7OC9v5Slkyz4zJbM4J2I9/h9c1uXDNu7Ie/IhBZd9yjR8+cRW6/RdRDv98w137VIZ9nDmjriJpqA2Goc2OQE6t5RknQpb9eJZEvnbo/xqow5F+0VjamyIYmdU+YpJENy2oHg9WCZYeWGbCTdG6zQQ2MaS06pwFwPF+1uT0tHnzyCoPscvzrXPS9xRpWd9xhBU7fDVrr5IWbadsSysqNXWF+DfQ22o+6Ccz2cjsF42+LtXem32ztfHNSAxutVdkPrMlfysDdwls2FXTEpUlPzbrvuulj2NSbD6t1AB0uw/5OZaQOt10gZnMs6wyAhEfIA3x5c6bATY1MqM5vMNmrAwCXSGyv1vOlVr0fcfH33US5UAiq623aojKx6XwarwQ3qW0/LpnJlM0II8GXEVLsBvqq9JayopYGeh9aPiHWvY1fSvw3HrL9sIvci6NV1T66lTGzaAi7thNtDSTjq+pHG8XIqRj+ssS66oBeZl6xAhnHpSDbAEVUtnDNUUQdUui2zi9qdT4pqQqKThEl+0rcnE5cubHQNz3wn3LwzvLvHrZrqOqReUzo7JG6gBflqvbE8fZ0J1DEVO8lElJQXKG7vmtby2NEaBgeEw6h3cTWEwZDdc9eMUJbLY71yBH2Q3dHw20Y6HWKf5Zf+cVvVF35UNAeR8RTq7WC0MUwGiKAk1z7BtlCQa0PdaMIRxcSIqFl4XJ/pkLCFskyyQlhD1KaTKLQ8+9N1mmpVTxoe7aSug+DrcZ+zu2uvZb54E/vx1PsI6U2VxFNdCBI0LDx8tWwsq5WOIkLyii9ez7dVtz4myMrkMZLYJgFoW/pDWQmtUsDCzlXWuoN7+3K5z5TgtD1GpogzZyr0N1ceShwd3lxbJJEJizI1Gu7PcLWJJn9TE/og+XaeHwYCPuyYiPavgrAP6FWNUk1mn501YvZLcu3qasGWhYxsL50Mja2NRcFARbis8ioBYlKF6kxOYFkLRWGlKUvRcBJXYQIVWiJrPCZcZhO3IIsTMkrkZkvc7tnxcB2sBmUv7eA6aK8inrORq5RyDMhV4z0RwMXauFr06BN5vuzy2jw2qzF3wvomO4ay5DeNW0Ky248D2m1JDk8CgO2NIHnrdbS006RfmjvheGN1rQzuHnFPV8fNugmqO7ppj6RQ02ADJUjS7ZZyydVRsoBeOz7u0wJbIwO7Fe3K9TsSngK4xkk5UC9QQ7FO5FEE4feBD4vLDdvGW0sNajUjarRVGYkYanLyluuc8CNYPyBREYHJQkwg7UaNcaqA5PVR9CCnY/1ivSW26M07jJQh03AOx+EqI9bmPscuzdXBMl+CiIEmr6C/EgRLFaO493nFocCm0YzYq+XcgzYcW2N5x5vUza7LY9q6m+PNE6GYRDd3VhaYzLm6kUw4rQdiwb2fYT4+3WkcK50N7ST+4J4rxq+Z+sxYCMwtrWJleoHATuQFFc5uUluyIEfrXF7nMHtMQo+tMWW7W2qZGEqHu0QW50HJaLdan/sUTcsrHkIrcb1XtSO6vt3JypCiVR6ZU4NabONhkDuc3I07VaOYbq+B4XHDsa9P1i5kb5SdurFyA3l95U4UDzq9YIxy9LznrqvSCKQm5L14aou9ekZuV/5aw+pa36n9PlI2EMUgYW1frC1D0/RfXz68fDsUe/kfvds1n9r8Pzsgep7zvL+q8Tjpi7zw04PXp/+ZOH/78NIGGRDmefjVFUPydpT0d0dfH//Vwd28cnq+JvV+YPw8fu69ZH5j+CWrwqHr2+lLVxePFzTACn/o5hcNu1m4AHx/f0T5/tbxQ9i+fpN/PvPKqvmdiyjMgBhvt8nbEeCHl/Dt5aEvKIF/idpmVu/thB9ohb7Cr6uXP/4vUdEwlPMtAAA= -->
