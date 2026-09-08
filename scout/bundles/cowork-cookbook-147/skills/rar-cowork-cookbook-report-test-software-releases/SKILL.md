---
name: "rar-cowork-cookbook-report-test-software-releases"
description: "Builds a read-only summary report of test software releases from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_test_software_releases", "rar_sha256": "6705aa22b932db9a0c7998dc5bf4674850fc96e6df7cc22cf6990242c28d01f5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_test_software_releases`. The original RAPP
agent is preserved byte-for-byte in `report_test_software_releases_agent.py` and in the RCI capsule.

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

Test software releases Summary Report — Builds a read-only summary report of test software releases from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-test-software-releases
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
    "breakdown_dimensions": {
      "description": "Dimensions for breakdowns, such as department, category, or responsible owner.",
      "type": "string"
    },
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
      "description": "Name of the Excel workbook to produce, e.g. report-test-software-releases-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_test_software_releases_agent.py` and embedded as the fenced Python below (sha256 6705aa22b932db9a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_test_software_releases_agent.py` first:

```bash
python3 report_test_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_test_software_releases_agent.py   # or on stdin
python3 report_test_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test software releases Summary Report — Builds a read-only summary report of test software releases from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-test-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_test_software_releases',
    "version": '3.0.3',
    "display_name": 'Test software releases Summary Report',
    "description": 'Builds a read-only summary report of test software releases from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
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
        "upstream_slug": 'report-test-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-test-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5881799500583679',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/test-software-releases'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-test-software-releases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-test-software-releases-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where test software releases stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of test software releases for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-test-software-releases-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads test software releases records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of test software releases from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a test software releases summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-test-software-releases-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary report of test software releases activity from D365 ERP with totals, dimension breakdowns, and a top-10-by-value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportTestSoftwareReleases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTestSoftwareReleases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-test-software-releases-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportTestSoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
