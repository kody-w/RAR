---
name: "rar-cowork-cookbook-audit-define-extensions-approach"
description: "Read-only audit of 'define extensions approach' records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category (missing fields, stale dates, blank descriptions, inac"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_extensions_approach", "rar_sha256": "23ee964442794ce21cb75ac0a7930a5435a14dee49bb57f2c270c3144860cbab", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_extensions_approach`. The original RAPP
agent is preserved byte-for-byte in `audit_define_extensions_approach_agent.py` and in the RCI capsule.

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

Define extensions approach Completeness Audit — Read-only audit of 'define extensions approach' records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category (missing fields, stale dates, blank descriptions, inac

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-extensions-approach
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
      "description": "Date range used to judge stale dates; note USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-define-extensions-approach-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_extensions_approach_agent.py` and embedded as the fenced Python below (sha256 23ee964442794ce2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_extensions_approach_agent.py` first:

```bash
python3 audit_define_extensions_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_extensions_approach_agent.py   # or on stdin
python3 audit_define_extensions_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define extensions approach Completeness Audit — Read-only audit of 'define extensions approach' records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category (missing fields, stale dates, blank descriptions, inac

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-extensions-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_extensions_approach',
    "version": '3.0.2',
    "display_name": 'Define extensions approach Completeness Audit',
    "description": "Read-only audit of 'define extensions approach' records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category (missing fields, stale dates, blank descriptions, inac",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-define-extensions-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-extensions-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0b1ed1be4daad592',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-extensions-approach'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-define-extensions-approach', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; note USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-define-extensions-approach-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit define extensions approach records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to define extensions approach. Output an Excel workbook 'audit-define-extensions-approach-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no define extensions approach data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-03', 'what_it_does': 'Reads define extensions approach records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Read-only audit of 'define extensions approach' records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category (missing fields, stale dates, blank descriptions, inac", 'example_request': 'Audit define extensions approach records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; note USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-define-extensions-approach-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a completeness and policy-compliance check of define extensions approach records in D365 ERP, with findings exported to Excel and no data changes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDefineExtensionsApproach(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineExtensionsApproach'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; note USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-define-extensions-approach-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDefineExtensionsApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebOiWLbvV/GdG3Er65J5VATU7OiIByIIAiqzVlZkMWwGmeehbn33u9GTQ3Vn3+6OeH89KyqVzd5rXr+11oHfX6ymDrLy5eOLAqx0xlpxHAagnFmpO9tlXVZG8CuLbPj/zMnSugztps7K6uX9iwsqpwzzOsxSeFwGlvshS+NhZjVuWM8yb/aTC7wwBTPQ1yCt4LZqZuV5mVlO8NOsBE5WutUsTGf0kFpJ6FSzFYHPmP9UduLMy6AIMz9sQTqLgW/FM5DWYT28h+fqpkzD1Icizva9A+LZJOVDwC6sA3isCgCoZznUArJ3p62OVQM/K4fZuySsqmnFC0HsVu9nVW3FYObC+/DCjq00mn2nF1wLU8uByoLeSvIYVC8ff/n1/UsIf798/P3Fia0KLr2Qk8r0Q9v9V2XJN13haUjXh9vyAdo6hddQNqhhApegiWZvV+8qEHvvZ//1X1FnlX7188dP6ezt8+ll+k9u0lkdgFmdWVUNXKhVbtlhDM3yOiPjzhqqN+tUkxGgq1L/9XnyG6Usn/11uvfuyeTVB/W7Ty8ZFMGaFP708vMMmv7TS9lMv18nKvm7n1/jrAPlu5+/0aka+w6ceiIGpX79/Hb9RhZu/LY19GaflfN+98YLOj7MAST+nX7T5yn6G7k3k3x+bn6X5e9nP6Y86fNXKO/TaTak+2Oy0Abw5MvrPQvTd288ygyGl5U64N3P/4isEwAnisOq/pfo/vIkHMBUgNZ6M8nP7x/u+3WGvOn2leY/ZpvDgPl3NIHbv7D7aqh/RPvh2b8hHcPArb768ofkfnQA+evsl3+o2/924P3M+/RCgxjmd2nZMfg4+/0RIr9AyPi6+NOvf0DS/5SMkjWl86DwObHS0ANV/fnzLz9Vj+Wffv3lpyaHUQys5HNTxj+i+SO7Pvj8yYJvu979+Szkr6VRmnXp7GsOzX7P8v9T/vE60604dL+tVx9n32fi9EFmkxJfmD5N8F02VlDW7+z488sfEHpSqE3jPG5D/PiP/5iJoVNmVebVM8XJmnoGHVyHCZiEV4MQImz1QI0SQLtWITTs2z4Y/5OHJ4khWP/2f50H3H9w3uB+/sDxz08M//wNwz9/wfDfXmcqpJuVoQ9BMp7J5Pn8KbV8iNQTz7wEFShbiFP2UIMPMJ0/TD8mwP/tn5H+/KDymg+/PQpR+MQ9ecdNmFc1MXidtDMCWB2eujiwGIAeOA1kEGcOlMYL4wnSoRBZ3ELMnCxRRWEcz9wQoko9VYOJNrTWx4nYb7/9ZltV8Cl9gvRq9iwC1Rxu+CrO7MMHqJYXh35Qf0qBE2Szn37/46fZf8/+t1MP4hOPM6wWb76AEvLKSZrB3GoSuG0qhBDULffhi9//eDMuJJPCOgY9F8KK9TwMYzMC7hdLKwfyA4oTMxtAC0PrJnlW1lOFC+vXGefNvsoLmU63ptoQZFUNy1wOUhekzgCpWlCdr5ZMs3pWwQCsPFhvmwo8uP5ml9ZDxAQmuVX/NhN3Z1iJshj+M4n52AQPZ2kIzf81Dp7rkEj5UzWjvpB4nUlTNM5yq7TyoLTeeHjW0y9T8X87DolbsxR0n9Kp5oLJVI/UeJoHboKWcd5c+mHyOexSEogDz86i/rLHmuql+qib5ae0egt7qwSPPgSKMsz8JnSnYvCXt5CqgqyJ3Yf9oKQTpTcvuG9eecQg/Q9bHNg3TRLDdQC9/ugQZp8adLHEZv8/90qTUUiWlfcsqe7p2V5S5evTWVP7ODn12XFCAR+SPxLzWyfzBa2+gPanNA5h5JXDX547Hy5+2/MEwqaEHpFJ+UEfxtekCqT7CP8pnMtyShzrU/qlOryHaj+gEEYAxAqYS1MIf2E43f0iaQABYbr+1im8uWJCDhjis7yxYxh+HgCubTkRlKqcUvjNzTAXwOTbLghhOHyv1eQhaGFIfwaFCGFSwgry+hWxn3e/iP6ng8+GaDryaBYbmMHlgwCUA0wCTpg2+RaKVz+7dajnxwcRqEaS15PuNswhqOlzEZSgaMIqfLj1aVeQQ6z+MH0/NZ1WQZ/DtIHGgsmRN9C6j3Sa4iOB7Q6UAQYDzK4kTGH5h0Z5M8KDoJVM2ACx960/fVJ8LL8pBB45ONWtLwcnRaYzUysw86DocGX4HkLUH4UJpJdMOx58/zbSvnKbaE8wWkEohBy/3H32DK/Psv/sK2Zf6H78u3Ho3b83MT0KufbnAPg4C+o6rz7O58/i+6X2vkIQmz9lrZ51+MMTHz58w4cPX/DhT3SfKn+c/Xuy/YnEW258nC1fF6+L6ZbwFltvH2iK3Qfq+gGb7n5KZfANYiH7LIHBNTlugIX/az38sgUWRb+EIAU3P+tjNZXVDlbyR0GAXviUfh/sU7LBepP6U3BW2Xcg8GgMYOA/nfa1bsFbaQ15u1Mb6YPXafqaxK/Ay8e0ieP3LxBAwb8ws021KZkiupomPbgMQbIOwePqARB9Pf388xR8evyw4tcZDSAYxdX3UfdWUaaK+l1yPJWEyjmQw/snvE4VECo5MZ8Sy6pgpMIgnZSph3yS/jneTQ3hdOBzB8E76/5eHhrenJWT+Sa2D6C7N64Pvsfyv0Cggrs0RWRgCifZtGpNGJvANgFakrlCWdc/5P0oN5+f5eYHzKca9X1Fmtg/ovn9DLz6rw+WP6T7tQP+e6IGbD4mOm72carD799QDX7DgvR+9nUAeT/7MhJOHEDawGn7l2n4mVz7ODL9gGfg19dDX/+qYYOXX38k1wP6Pk/x94yiv5VOmiANQv7k2L8puFBmyNdtHPCm/T/L6w/oAiU+LPAPKPbax1X/A0tBkR7gDUvgpN03s30TPnuMcZPwUNn6+VeH319gYFuTm99C+20OgNsh1n2opv5nDrMfMoTXzzyF9/7tCeHtfBVYsEOFBNAVAFsCwzB0vcUcgC4de41bzsJab1cLC8dWuLXEXACwrW3jaw910PXCWS0xbEMsHNuyIb1ntn+emrxwkmkSCJriAwQM8O02XHLflHkKP1nq60AyKf2m0+8vNoHBnQes4sjnZzffLm0CXdsKbyMlATL8wpWWZoVRqq4Exr4JUtGnmkWqqXPJUe+yIX1Rvl2jPlDyW870lHgmz+Jlg6kj7zWuxuhJdJRqXkVs5XKh+Jtk5BriDanW6GdnY6dirEdRFJzx66AtEnCUD40baUAO6j5JtqvCkcfidsEKcIyYw3w9LOcM26fsYuyF7SBEt3l8pE+nu85BGRkG9PssStS7fUP2aHhTMcKfeyHlzV3zQCjFOFwyOUzN4ZJo9/gUDcwoFtFqv+lKYjgKYmpw1bhHHJfLG44QCMIAJhaXuTT4aFxwqJa7JXcxaCLJdOY6pDpYi3qWDAGjLi1eZcXl3spEbYBjvAjONzlP9OFoHMNCMbVIVDeUx5ILlt/CD2JvGvy0wlEvnHNgZa/WaO82EsOw4Go4sRv3zcYXKtGdx3zMXB3ZaSJcAZgO+M7VT/FVE2tMXBjyLahMpKAITClZhL3uSf1qVgOTbE+rO43vSa5K2F5BGj7eOTwTaQHnlKRUoZdYV1Mqvs85379Ui/tAdE03lDi417h9Vi0f3VIV4bM0LfA8S9+o+CzSo5VHSaQHPKvMaYLMNr4miES1HI4UR7QuFlUkszoTl5tCWQtKDjgl7Z3bHPc3/A3Nt9tbGrdqdTgO0ShTedHwhcBfmXvnCvsgpNWhl303MGSbr8IjM/IRi0jzRqnLhRh2qs3s5zFnbnIt17qy1Da5siZMbp5rc8DdUe2wcoZjyEbtLl8xV5WQ/K2uqFZPG+eQ6m6XITnaNzIC8rpf88Gtybx9p14XfBEdtku2Z/yC3ZL7k8L3h7lE486lEsuK61IwZzf+vqQWjGVrklNc2FogV3e+jFf6sT/kkpg0sXSPDBFFdDPWZeo4MMhx13a54F6IFa96lEzg25t5CTCN9nx7G5GbvdoD7CIGleExRCYad2Qp2ZjJjken8JJqme73gziO2HxYa91YJFeRikWJkkR2d7waO2YYYEkeN0biNLIispuRuc4Red4FbXsH6O2MU/TRU/Fxe243ttDJDU5lvs650S6uiFW1M5XlEqu2C572+fLGaSxmBg7J+SOrdwGJ2NW2Jdm2UgLeQyhLamOtJpNRuiXhECzNHIEBZNRup+0GYYcwXdFUvcT13HF7vUB40w7+hZJs3l9ATUeHRjMlzXxU7PlKKDHymm/GE023KN9m2wWjhmuPsssbyPVrb8jFTt+r6nHH5prkQ924lNV7OtrPq41aXxraA5QJdmoWyVLOMSZa8e3JwK+Bcaf5LN4mSWxHNzMwkgOKy1Slq7vBs+ghPjPdiTrQt4t54k5XksvKTnE2i0t9XGliBUyUkyyb44b7yLnoaGx3Ar874VFKh/PlKsgH0WUHn40OYhBKy+5aFn1nMfNTypelSRQXLN5e+FxY0UV95IT1tU3AQigux9vZotwSZLRxSfeXYdjtWDpNWy/K03NcMEeuWa7TICVShF8enHizcYh9o1An7GDHp60Qsn5nXk9Yt612XFoK0MWVVCnLzAFy16WC7JOykezXAaj3usK5fJFETTEo0tETGJRZ5Wy3jfHOHtHktNy7F9Jv3DZc5KckdQmPpy8FejhYGDhgxDh3jSG9obKe02pHFxTKL1Oc2hX18q6251ZtUnOcJ/5GostVdDCpMD44BwcUfs121eIMNjTR5Yck21W3raYQmY3We9Ki46g4Cb61FnND9PLCvCPVhgyvxQW9Wgf5fO1pfudYGl6KN2scfbVPqlW53BRo64yDykbRTlVQM1M5fiwUe7EkYWEKTjyW5BoBoUlbLSLN5yOgX/KdeNhHeqz5AyfRZnnOtPq22hfbS0mKWeraq+NRNwysxFeHbUce9bt62bq0vJWLUl+0RnURlPKyuowabkt3ys7beJCT9LQ+NzDmnbnJd+oYyEOMnjySV8/ZIlsMLXVPG9Mmu2wr+feMTly0PW8BCfrmoNbZtYtuy+M5vvbR3KyKFht3YjuPPLZXJf6IsLd8jVfGRSBzmaobdcRONybZ5bzPF5UexVoOdOREb/erXi6KZjGSjHPdIKocjVvxgBzm+iiHBq5pri9YviahFL6VgBAw6110AYuCKy/irr9a/nA8XDjHUPgAF4dVX2Cbw47V6gCf3y+GxsmeXwWqsVhopbj2Dil1Cm/0Dh0jViRchFXhzF25p1uldkZ5XmFmHBTeokrFecLtNL8eNf12TGqBta8XRcfdKqD6TR+wodEy2xO9vmQlQ7Y2dgv6HStT5MhT+OVO0cV6sR+98nq2Qzuk5T2/md8EIKMidQytkxz0FbkOEsNlkqSlCAsT70vZ45YLmP16q+vrk87pvHQThFDWj5kTlNS2VMf58hhEBUvcrsJuxOzD7WJEYZj2frTT01NNht7cTNbUvo51S2aiFCd9Pz8SMn64b9g0acAuVSoxw/DBJapz51QG9P8+JIVFkQm9MybdXOr32t4mzwbBlaou3s1k7OMFd5xffYYOVVbatGxyjdfH/XnYX6MkG6lsBYirKF6EuZXkzAVRwvs1dWq7w1arQl9I1EY3j0fLTHWB4YBLV1d6Ty3GVFqGlluSg3vbezu13d0ZZ5UvLtGG3bcWsz/viztRa/N8ZworjlyvYjk7B4ESZ/J4lfG7VnV2v99XB0yjdpJ7YsRBpBi736FDYe7HuF1Ds2/Z7FD4983JdEOORaEaMX0F7HiybtVtL9GaWhRyW8557LxGQXUl6bM9XtC5zYQqJXP+FTcGwUM7JOO2aSZyXMIqPsMQ87M6bLZnt7fPnKEI4ETck7D1FXKN89f93S2jSkmM6+3IoXTF+7Wq+zS+XfKoYrjFYEaKI6M7KVrhYnVdnKU0nndMf1HUq7hDlD1T6iLFAdMpjhnmQXzbmKmn6wJLHQBR3yVX3VJMyxsh7HzEQxguh1vYnhTR4oc5UBYLi6VLXLj0d28r8901syqWT2pgi2tUbRKDPHMC7FotXWtifrNwC/q0oq597mpjUWECdkPmyLoah2J3TvTQ2Y/p1RZX9cE+jBKuZztj7PxjvOziWERVj9912oWqYlhKVE8549h4SRuRhaU84ll5v3Y4XuFpPYw6ytI70bmiK+mwHwTxWO+UC0FIEuo1l6O477eOdRsV2+391VBcyoQ8MeoqNi+1f+9qMnJUUz8eU7a8MCIRFbu9XoQ14yQsYmlUd3dC2dxKww3toiUb+UU9EgD21RYSG8V+w/eWiRFA0HeLAMZ5jQLmPkixp7mHe7/BpcN9jtiFeZZtkbOiwRGcoc6NjKLXmsx5yGLUlOWZSWUSCXdR5kTz/ZkmWyO00xtn6zu6aLgiykzJQ/h1wZ9Cm7id2vkVyZEmUGXBROSwvMj2zbgVrXiDPZbsHQ/iEb02KlD0GCRrgyy8YIVEgrzlqGpHMX0qJZxy3tUNrZvMMRuwq3u3GZp0Qz9R/VhJEKMgBoxl2DzjYpJMjnK97VyDPIYR4gDx4sRRfEAi/RqludvqXH+3a3qtdHMsBVdEjCqTSmNW8Zwiuy6rbXptyG0huNmc8nQ0Qio2FHSjQm8MQeCMW6H2WkghBhyxFZo1/oohrqpKLLgmUMDAqpxcjLIzorUt6ugZObFuvj82nICINmUaFxON93F2kZK55kZWfTOk6IBzm6VDGwa5Tw41IgqLoTudBpFW57pwdS1/JVuOMLhSuJe0ww3VDHS15NfGZRUl1R0/ZnBKUwuKqdTgtjbjNcUUCDimQX5UGphu2VUK3LDgb/v1nrp0/VJnNTioYWQjdvUGX7RyslmergKPmAvsaF2zjYvcnYBag92tVGFDwIcndigPuntCzoW2TsJ8Kc0r4I7seF3mCxJiZZSunNtxZ2wRs3CVBOsiK+3DMAgt/lwFxCbHYRCRrBGs55ez1zfzBRqjR5rH72bvmR5bSXPYrJSbvnTY3YrKKfvsHTgtuYRHA/YNHd3k141V+mdFOPDzK1Dz1ufu+7m8GZYotnBzEw5KdWRxbhgLucaQAkgc32C40aCX8MImyBsbcltNzZlKw4XCzXsJdhnGcLOttUrVqamNZ6P1pOx+ASnb4Vx4wIXmyDvlUYnQOeta7U62Dk1htal5xhJk62kbn1csjMJuthbel/iRDsI70gvmjYpal0x63bbtYLllN3rH9SVaHNR+dbMJnrjE0CU5r96c+8Hl5+lCPdpNkxDrpeDVsTMoh8jAETdqT/Qh1C1rrmto49B+5u9W+VzxgbfaYWdFHbJgc4RY2dEtyDLpZKa726Z3upsEVsN1cO/duWZQ063YKNiS9dYS4+BSx30UJ5KIrt19YSgiLWHRNsfuI1/uV+sK97dBu78ttXo1SDwt8Z2lK6WFn0+szVNrxaSFJPOsxMxa/7Sux7V1IjZL1+A0CebhvrB17BABvGnZnpAb9nYf7Zp1QKpYsPvxnLONQpIgqJs5K6159EB15XHZL9CcQKWznLTHaG7nY98koGMI1BwIQlxWhwRH+bFsm/MOuxNOQVnB4roESF4vyDRX03J5q5x7QYmGbMXncDuG2z1dn1Olt9LaR+7szqtD2IpvFyVtd4tdmp8XemUpByAtGeJ43vCbbDh65gnHlU7l8/FwUZ3Q8tc7GCZIB/Glaoo18FD+nF/Pu7s4nzNUIbaGfd3o6KbgxlVfwjbR7W8xjq6DTQDYe+Uiuz1YubbqX+nFKCDsdj6/tEiILUUXVQ9IA+a9uTlI5EpLFna3NPVryWt06quYvuLPomlGic1whDqeCiQU1u18lHq1jlw3P6SnkiLJY35dLBx5TssDifP+2LUCc0bqQeqLZT5o5TmlkMw4gQ5pUH+zJnVavXFFwVxaOOM3jugE4y1UhW1wOQsIg6fk3cBOLir4WA5nUgi89/P8TBDEetN00T2zBGPtH9R1vWTV4wVEowIYzafpjRpjFULcGqMGmAmyGteX3WItRaMG2kw7HBdezuubqi1kdE4HgycIFE6JIcVsGjqotwR2HKvtKthDxSXbGlc7pYhkec2HI9EvbVvZnCilOCSufj35UnpaZRFYbQlGR+6othFbSj2bbSM4atsD87hHOPaEcrGiH2UY09cDnyJJhu8xOMdxEjkGTRTXawLLrqqy2K8WvrpUKYIfmbsz5BWF8wQlnQ9X9M6vOlMl69A426eLekpz2cdtNNFF4gJaOyVq9s4vtpvV1vV2kmKG4p04sVK63dx6deVv+1OGLO77w2asNoJQJF07rOlEuxu0dxcRsW1vJ25ojcRndqd1uGYudb+XK0LGUJ7IBffa7G+3Vb8nhh0h7E62PtaquLytmMyOTuj9OP2B0W6KKOCcdXZBAdnYYOcip1MlZEfvcC9QPsE2EWFbG3fT0kYruVdHw/Z4OUr1kh+VJXVyfLxCB2yZJdU5roPLDbYv09/b7gNuBcthux6lbgerju4eY2zddFcmohFCmJ8jtNf2fXKm5g42FGxmJlY/Z/2CsVc7GnRUXq+cyhFYmrCWwuZwItC02VrOGt/Gdlnw98O8xDH30uA97rKL4gpMvVvCQRbxbiBojkLeltfNkKZugm6XK1D0Z9S8b9CtHR2ks11Eaph4K8I8SKoq5XbLc/G4W3eBeiWXWBLW426b4QskXBYRbKAlcYn3FzzTYIvpn6PQFOv2cJIR1Ac32Bh5hwKaPuFonUM5pOK1Eu1WGYq5wU5U0u2YITgtYvm8tUdyx/imWHmR0e+ONTlf0QsWa86XBeMIGIfHOxlH58eEzcSFQyCKNGZ9G1ZFcF94CjifeA6hxepUOvY5rNCVYgzEAj3V3fLKBIU+qmzeGypiHbdwXKo8OF3AEURfDkKC8T2lHDt2aLr9fHmeV517p52jfEhAdWcO+GbTOdJm1cp1YOI37RB02t1GGRRBFqp9XNDHVtJCm8T2NSW3dryyhxQ4Q1+VtttcS9NEUiqJa3I0Gs4N7s0oXEeppE04e93Hxuh9vJHcFM2H1GxJXbsLJtgqxg05Jg0cIoC+v55UDk9ajGiMzXqjoCdeQLfXOxudFxvSNXJcJUvgdBHgVb0sFJRGpZskGIvjuInWFwwf/WYBS2h6Qxg7BQJuq3Pgj1Tkxgxve1fc23oQb+YgOow2wht6AhbBQT5a/OmaLi5AIVXUv51ODrtFtnMcwvQ9ULNxa2aXZi8VzICqAXaqm0WzVBOrSRs8NkFYRl3hb1xzawouSWDreCsfNH97We8rYoxwlciIITWYoN/4l2kIzUx2efK23WnFCQQsH15CK2Xaapu6NI0etgT0kr/6rXph98ONOJcmz+OZuFqi8tkh7j57Vig/YirABSS/vFcJ2ToVYmBUd2RsvweHG4OugbU429F1fa7KAMOzk4nAklSMpVuipBeOucNUonudh4sFvUwDHTE1fSvNWd3d3hyJLQq1BcVqXBEWrHSNiJhz9N6wW/XWjra/rdH9yjfOWHOjSUkSD6leNrC4Zcgxs+NCSODBQ6dDRHM6FQjJyRuqFDTY0upkQJ+vxngp3b41kVwo6VY6boy5WtE2nuzTvdeCtT+qYrozjNYEZwKsLdcOzG2zbQnnSh8Gr9MsLr5caK00B2fRyS4p7zdLzbikiG26h7LDjsKpt2vDqEIeW/srXBXlmkcvpyLNsBNDIZqvEJqdmqlwgCWXBi0qoaq9kzx0Pa90oqqpu3c4nxtJrNeFjp+Pd+cC4uzugnW8YVzOE4OdALBowbu9cLlnO+IQZC3dNLdg47keiW9YnMScHiTn2Nq3aKIo1JWR2XYT4M29QTv9vkL5fet0sOtZ3TtvQ9MDkSm3YEeS5F9f3r98e4D28i+/CjY93fl/9iDp+Tzoy1sdjyeDwHI/Pnh9/NdF+vX9S+mEUKDnw7Iqbvy3x05/86jswz972DedHp5vV315tvx8Wl1b/vTS8UuYuk1Vl8PnKosf73TAE3ZTTe8pVtOrrA78/v7R5oPh9O0+38gA5ec6+/x8Qjg9KQvT6WUN4IbfLv23h4fvX9y3t4w+rwj8MyjzSdG31wKgfqvXxSv68sf/APnEQIM8LgAA -->
