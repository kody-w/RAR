---
name: "rar-cowork-cookbook-report-analyze-safety-achievement"
description: "Builds a read-only safety achievement summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_safety_achievement", "rar_sha256": "2ccd8615c0926441e69f777a059f3bb36a7ec680f850cc659b3c8c40b69439f6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_analyze_safety_achievement`. The original RAPP
agent is preserved byte-for-byte in `report_analyze_safety_achievement_agent.py` and in the RCI capsule.

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

Analyze safety achievement Summary Report — Builds a read-only safety achievement summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-safety-achievement
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
      "description": "D365 legal entity to report on (defaults to USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. report-analyze-safety-achievement-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_analyze_safety_achievement_agent.py` and embedded as the fenced Python below (sha256 2ccd8615c0926441…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_analyze_safety_achievement_agent.py` first:

```bash
python3 report_analyze_safety_achievement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_analyze_safety_achievement_agent.py   # or on stdin
python3 report_analyze_safety_achievement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze safety achievement Summary Report — Builds a read-only safety achievement summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-safety-achievement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_analyze_safety_achievement',
    "version": '3.0.3',
    "display_name": 'Analyze safety achievement Summary Report',
    "description": 'Builds a read-only safety achievement summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-analyze-safety-achievement',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-analyze-safety-achievement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd057518b72616955',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/analyze-safety-achievement'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-analyze-safety-achievement', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (defaults to USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-analyze-safety-achievement-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where analyze safety achievement stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of analyze safety achievement for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-analyze-safety-achievement-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads analyze safety achievement records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only safety achievement summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a safety achievement summary report from D365 USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on (defaults to USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-analyze-safety-achievement-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary of safety achievement activity in D365 F&SCM with totals, by-dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportAnalyzeSafetyAchievement(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportAnalyzeSafetyAchievement'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (defaults to USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-analyze-safety-achievement-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportAnalyzeSafetyAchievement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
