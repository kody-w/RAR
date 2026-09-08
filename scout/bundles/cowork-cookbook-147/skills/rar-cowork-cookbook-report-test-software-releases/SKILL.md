---
name: "rar-cowork-cookbook-report-test-software-releases"
description: "Builds a read-only summary report of test software releases from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_test_software_releases", "rar_sha256": "6705aa22b932db9a0c7998dc5bf4674850fc96e6df7cc22cf6990242c28d01f5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
