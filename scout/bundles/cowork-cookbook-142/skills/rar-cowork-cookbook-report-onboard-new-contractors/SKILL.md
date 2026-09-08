---
name: "rar-cowork-cookbook-report-onboard-new-contractors"
description: "Builds a read-only summary report of onboard new contractors activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_onboard_new_contractors", "rar_sha256": "6f836d4bf291d42110050f010c83f6a4c1611399a71da1350be464aba651609a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_onboard_new_contractors`. The original RAPP
agent is preserved byte-for-byte in `report_onboard_new_contractors_agent.py` and in the RCI capsule.

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

Onboard new contractors Summary Report — Builds a read-only summary report of onboard new contractors activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-onboard-new-contractors
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
      "description": "D365 legal entity to report against, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-onboard-new-contractors-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to cover; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_onboard_new_contractors_agent.py` and embedded as the fenced Python below (sha256 6f836d4bf291d421…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_onboard_new_contractors_agent.py` first:

```bash
python3 report_onboard_new_contractors_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_onboard_new_contractors_agent.py   # or on stdin
python3 report_onboard_new_contractors_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new contractors Summary Report — Builds a read-only summary report of onboard new contractors activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-onboard-new-contractors
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_onboard_new_contractors',
    "version": '3.0.3',
    "display_name": 'Onboard new contractors Summary Report',
    "description": 'Builds a read-only summary report of onboard new contractors activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-onboard-new-contractors',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-onboard-new-contractors',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0bf3267f44adfdd2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/onboard-new-contractors'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-onboard-new-contractors', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-onboard-new-contractors-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where onboard new contractors stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of onboard new contractors for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-onboard-new-contractors-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads onboard new contractors records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of onboard new contractors activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build an onboard new contractors summary report for USMF from the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-onboard-new-contractors-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary report of onboard new contractors activity from D365 ERP data, with totals, by-dimension breakdowns, and a Top 10 by value section.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportOnboardNewContractors(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportOnboardNewContractors'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-onboard-new-contractors-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportOnboardNewContractors().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
