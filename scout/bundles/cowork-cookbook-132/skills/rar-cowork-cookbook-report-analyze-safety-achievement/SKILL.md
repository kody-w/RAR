---
name: "rar-cowork-cookbook-report-analyze-safety-achievement"
description: "Builds a read-only safety achievement summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_safety_achievement", "rar_sha256": "2ccd8615c0926441e69f777a059f3bb36a7ec680f850cc659b3c8c40b69439f6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
