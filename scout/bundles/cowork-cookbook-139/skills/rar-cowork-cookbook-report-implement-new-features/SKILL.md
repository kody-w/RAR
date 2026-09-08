---
name: "rar-cowork-cookbook-report-implement-new-features"
description: "Builds a read-only summary report of implement-new-features activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_implement_new_features", "rar_sha256": "46d5fcd18dea819928a4210aaf752d76c79da7bf880fa77165784967c80ca307", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
