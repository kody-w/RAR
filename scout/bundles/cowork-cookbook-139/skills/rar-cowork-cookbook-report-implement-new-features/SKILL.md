---
name: "rar-cowork-cookbook-report-implement-new-features"
description: "Builds a read-only summary report of implement-new-features activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_implement_new_features", "rar_sha256": "46d5fcd18dea819928a4210aaf752d76c79da7bf880fa77165784967c80ca307", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_implement_new_features`. The original RAPP
agent is preserved byte-for-byte in `report_implement_new_features_agent.py` and in the RCI capsule.

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

Implement new features Summary Report — Builds a read-only summary report of implement-new-features activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-implement-new-features
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
      "description": "D365 legal entity to report on (e.g. USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. report-implement-new-features-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_implement_new_features_agent.py` and embedded as the fenced Python below (sha256 46d5fcd18dea8199…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_implement_new_features_agent.py` first:

```bash
python3 report_implement_new_features_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_implement_new_features_agent.py   # or on stdin
python3 report_implement_new_features_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement new features Summary Report — Builds a read-only summary report of implement-new-features activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-implement-new-features
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_implement_new_features',
    "version": '3.0.3',
    "display_name": 'Implement new features Summary Report',
    "description": 'Builds a read-only summary report of implement-new-features activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-implement-new-features',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-implement-new-features',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4cb989916ae11003',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/implement-new-features'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-implement-new-features', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-implement-new-features-2026-05-24.xlsx.', 'period': 'Posted period to report; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where implement new features stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of implement new features for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-implement-new-features-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads implement new features records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of implement-new-features activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build the implement new features summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to report; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-implement-new-features-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP summary report of implement-new-features activity with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportImplementNewFeatures(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportImplementNewFeatures'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-implement-new-features-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportImplementNewFeatures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
