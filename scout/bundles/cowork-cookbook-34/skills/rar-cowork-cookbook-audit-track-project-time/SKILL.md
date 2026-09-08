---
name: "rar-cowork-cookbook-audit-track-project-time"
description: "Read-only audit of track project time records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returned as an Excel workbo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_track_project_time", "rar_sha256": "fffedb237939aa0e71655ee35988762bb03a32645d4cf88db26f448439a68d34", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_track_project_time`. The original RAPP
agent is preserved byte-for-byte in `audit_track_project_time_agent.py` and in the RCI capsule.

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

Track project time Completeness Audit — Read-only audit of track project time records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returned as an Excel workbo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-track-project-time
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
      "description": "Date range for records and staleness checks (USMF demo data is mostly FY2017).",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-track-project-time-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_track_project_time_agent.py` and embedded as the fenced Python below (sha256 fffedb237939aa0e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_track_project_time_agent.py` first:

```bash
python3 audit_track_project_time_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_track_project_time_agent.py   # or on stdin
python3 audit_track_project_time_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track project time Completeness Audit — Read-only audit of track project time records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returned as an Excel workbo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-track-project-time
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_track_project_time',
    "version": '3.0.3',
    "display_name": 'Track project time Completeness Audit',
    "description": 'Read-only audit of track project time records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returned as an Excel workbo',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-track-project-time',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-track-project-time',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '80db46306334dfe5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/track-project-time'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/audit-track-project-time', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range for records and staleness checks (USMF demo data is mostly FY2017).', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-track-project-time-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit track project time records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to track project time. Output an Excel workbook 'audit-track-project-time-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no track project time data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads track project time records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Read-only audit of track project time records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, returned as an Excel workbo', 'example_request': 'Audit track project time in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range for records and staleness checks (USMF demo data is mostly FY2017).', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-track-project-time-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants track project time records checked for completeness and policy compliance in D365 F&SCM, with no data changes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditTrackProjectTime(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditTrackProjectTime'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range for records and staleness checks (USMF demo data is mostly FY2017).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-track-project-time-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditTrackProjectTime().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
