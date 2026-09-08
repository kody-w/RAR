---
name: "rar-cowork-cookbook-report-identify-continuous-improvement-opportunities"
description: "Builds a read-only summary report of continuous improvement opportunities from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_identify_continuous_improvement_opportunities", "rar_sha256": "b9620c1e4cd488307ade6b19701a3676c86e25b2c45f698c03f71b7f573452d3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_identify_continuous_improvement_opportunities`. The original RAPP
agent is preserved byte-for-byte in `report_identify_continuous_improvement_opportunities_agent.py` and in the RCI capsule.

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

Identify continuous improvement opportunities Summary Report — Builds a read-only summary report of continuous improvement opportunities from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-identify-continuous-improvement-opportunities
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
      "description": "Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on (default USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. report-identify-continuous-improvement-opportunities-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to cover; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_identify_continuous_improvement_opportunities_agent.py` and embedded as the fenced Python below (sha256 b9620c1e4cd48830…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_identify_continuous_improvement_opportunities_agent.py` first:

```bash
python3 report_identify_continuous_improvement_opportunities_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_identify_continuous_improvement_opportunities_agent.py   # or on stdin
python3 report_identify_continuous_improvement_opportunities_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify continuous improvement opportunities Summary Report — Builds a read-only summary report of continuous improvement opportunities from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-identify-continuous-improvement-opportunities
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_identify_continuous_improvement_opportunities',
    "version": '3.0.3',
    "display_name": 'Identify continuous improvement opportunities Summary Report',
    "description": 'Builds a read-only summary report of continuous improvement opportunities from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-identify-continuous-improvement-opportunities',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-identify-continuous-improvement-opportunities',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7296d869eb565a3d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/identify-continuous-improvement-opportunities'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/report-identify-continuous-improvement-opportunities', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (default USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-identify-continuous-improvement-opportunities-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where identify continuous improvement opportunities stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of identify continuous improvement opportunities for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-identify-continuous-improvement-opportunities-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads identify continuous improvement opportunities records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of continuous improvement opportunities from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a continuous improvement opportunities summary report from D365 USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on (default USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-identify-continuous-improvement-opportunities-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals/trends/breakdown report of continuous improvement opportunities from D365 ERP data, delivered as an Excel workbook. No data is modified.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportIdentifyContinuousImprovementOpportunities(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportIdentifyContinuousImprovementOpportunities'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-identify-continuous-improvement-opportunities-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportIdentifyContinuousImprovementOpportunities().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOjSJblX9G8NpvMbEU8QCCWaGuzYRFaAbFIIDLKItn3fRGQU/99HEmxZFVWT3f1fBqlZUiA+/W7nnP9Ob+/WV0bFvXbpzfVs/LF1krTKPTqhZW7C7a4F3UCvorEBv8vnCJv68ju2qJu3j68uV7j1FHZRkUOpjNdlLrNwlrUnuV+LPJ0XDRdlln1CO6URd0uCv8hIcq7omsWUVbWRe9lXg6elPOALo/ayGsWfl1kC27MrSxymgWKrxf8/1RZYfFz6gVWugATonZcXFSB/2XhF/WiDb1FVjQtWMeZpZXgt+cuSq+OCvcDuNt2dR7lAbBpsRkcL13MZj0sukdtuFCfan5YcF5rRemHh+1aUSLwogk9r23egbHeYGVl6jVvn379y4c3oHz69un3Nye1GnDrTXlYuHdn3fyR/Wbl/ruR0o82AoGplQdgZjkC9+fgGqgLjMnALdfzF6+rnxsv9T8s/vVfk7tVB80vnz7ni9fn89v8n9LlD/vbwnoY7VilZUcpcND7gk7v1ti87J8j04Do5cH7c+Z3SUW5+Pf52c/PRd4Dr/3581sBVLDm2H5++2UBvPz5re7m3++zlPLnX97T4u7VP//yXU7T2bHntLMwoPX7l9f1SywY+H1o5C++qOcN+1oLBC4qPSD8B/vmz1P1l7iXS748B/9clB8Wfy55tuffgb7P/LSB3D8XC3wAZr69x0WU//xaY45WbuWO9/Mv/0isE3pOkkZN+5+S++tTcAiKAnjr5ZJfPjzC95fF8mXbN5n/eNkSJMx/xRIw/Oty3xz1j2Q/Ivs3otMoB7X4NZZ/Ku7PJiz/ffHrP7TtP5rwYeF/fuO8NOpB3tmp92nx+yNFfv3J/X7zp7/8FYj+v4pRi652HhK+ZFYe+V7Tfvny60/N4/ZPf/n1p64EWexZ2ZeuTv9M5p/59bHOHzz4GvXzH+eC9S95khf3fPGthha/F+X/qP/6vrhaaeR+v998WvxYifNnuZiN+Lro0wU/VGMDdP3Bj7+8/RWgUQ6s6ZzHY4Af//IvCyFy6qIp/HahOkUHkLEDiJR5s/JaGAHwbR6oUXvAr00EHPsaB/J/jvCsMUDr3/6X82CAj86LAaAnkn+JXkD35Tuef/kBz7/8Ac9/e19oYK2ijoIoB/it0Ofz59wKZqgGepS113h1D7DLHlvvIyjxj/OPRZQvfvtnlvvykPxejr89cDx64qPC7mdsbLrUe5+9oIde/rLZAbTgDZ7TgUXTwgEa+hEA+pk4miLtAbbOHmuSKE0XbgTQB9Df+JANvPppFvbbb7/ZVhN+zp9gji6evNhAYMA3dRYfPwJT/TQKwvZz7jlhsfjp97/+tPjfi/9o1kP4vMYZEM0rZkDDgyqJC1CD3Ww/CCdIAAAwj5j9/teXw4GYHBA5iHDkz7Q6TwY5nHjuV++rO/rjao0vbA943ZsZGbhxJsqofV/s/cU3fV8MPnNIOBOt65VeDoLijECqBcz55sm8aBcNSNTGB3zaNd5j1d/s2nqomAEwsNrfFgJ7BoxVpOCfWc3HIDC5yCPg/m+58bwPhNQ/NQvmq4j3hThn7aK0aqsMa+u1hm894wKY6ut0INxa5N79cz7T9SNVHiX0dA8YBDzjvEL6cY45aE9AJ5C7zde1H2OsmVe1B7/Wn/PmVR5WPYfCASkIFg26yJ1J499eKdWERZe6D/95z/7kFQX3FZVHDn5tF/5zXdGrS1k8W43F524FI9ji/+eua/YRvd0qmy2tbbjFRtSU2zN2s0Hzms/eddbrqRGo0+8N0FeQ+4r1n/M0AolYj//2HPmI+GvMEz+7Ghig0MpDPkg3ELtZ7qMa5uyu69lR1uf8K6kApRcPBAUJAaADlNac0V8XnJ9+1TQE+DBff28wHtlTu7PZIOMXZWenIBt9z3Nty0mAVnNEv4YZlIY3R/IeRk74B6vmwIBgA/kLoEQEahQQz/s3oH8+/ar6HyY++6h5yqPH7EBB1w8BQA9vVnAOyBwqoF777PuBnZ8eQoAZWdnOttugpIClz5te7VVd1ETtDJ9Pv3olgPOP8/fT0vmuN5SgioCzQK2UHfDuo7rmXMlAlwR0AAADii2LctA1AKe8nPAQaGUzVAAofrW1T4mP2y+DvEdJznT3deJsyDxn7iCeeW7l44+Iov1ZmgB52Tzise7fZtq31WbZM6o2ABnBil+fPluN92e38GxHFl/lfvq7jdXP/7W914P/L39MgE+LsG3L5hMEPTn7K2W/A0yDnro2L/r++JVPP34Hho8/AMPHPwDDH9Z6uuHT4r+m7x9EvOrl0wJ5h9/h+dHplW+vD3AP+5G5fcTmp59zxfuOwmD5IgMJNwdzBP3CN8r8OgTwZlADvAKDnxTazMx7B2T/4AwQmc/5jwUwFyCgpDyYE7YpfgCGR+8AiuEZyG/UBh7lLVjbnTvSwJt3ho9yaby3T3mXph/eAIB6/9yOcGa0bE78Zt5agmEASx+PwJUNNE5cUNpfXJDYefNs9X7/mz049+3ZIxG/TZqN6wBwAJAA1G3V7bz8B2BU6wXFjMFgMOh2SjDx0QyCKV79YfYbYDmrLIGJc+3M1rZjOZv33ErOzecD4Yb275WRHj+s9P2F8M2PZfNiyLlD+KG6nxEByjrA9g8LF+jXzLqBiMxumZHBapKHcX+qy4Oqvjyp6k+8M5PaH9hsbj9eLAnaeLDvtrq0fXLcn8r/1oX/vXAdNDazPLf4NHP8hxdEgm+wcwKu/roJAla9tqWPvyrkHdjx/zpvwOYEeEyZf4A54OvbpG9/bLG9t7/8mV4PHP0yJ+4z/f5WO3HGR8Afs5P/hoyBzmBdt3OAw7334H3xz4DExxW8wj/C648r7H1Im+FPvfdsDf5eufOPncOsz6Or+rfFKx7NfOs/7DYWVg/y6x9kKFj4wUqA22dPfw/hd0cWj23tQ8XUap9/hfn9DZSiBTLQehXja18EhgMQ/9jMfR4EIAwsCK6fYAOe/T/ZMb1kNqEFunMg1KbwFewgHua4GEmiMAFYErcRioARC8UJ3CFxb7W2Vw629nGKdGDUJxCb8NcEiq1XLgrkPWHsy9zgRrOes5LAPR8BEnrfH4Nb7svAp0Gz975t0GZHvOwEgIRjYOQOa/b088NCFGJDN8LuTgaEwhBT3U+Gm/Un1TYP+tLPbqVkHpgoUGXLtPc9j+yYIrItZA+31sWpNzt5ksNloFFJjkuYl5yEfPS3CtpRjUgX9za5ebv1UkTPSUjkrUOw16uqCF3L8idScyoYYU+WuctxVUfvSqWYaWfy2UXhy5OMHSfHznSI9+DrebChJXmBhqKYogvdlE5kcI5Zb3R811biKKili+4JQoAxGEMjc9zcr5Z/NpLGiJF+5e5sUg6uUWOyy+O02pf91OLktijTrGij2pEzRDZ09hZaYUNW/CE/FpPsYHqqrJPsUu8VYRD6c3CredMs/ZN4guV02A5u2ZqRKl3VbeztlaHwI9kMSJ89IXrVMssa8knK69ETQkIQxI36aSCXyx3VEgQW8NdSItTotG+RLBSNsKT2EcxkTrjjKXryI+Eywvdr0ixzHlZPOy+BxPv2cgE+2dBkQaP7E0GRkC+giXlQy7xJd2G0FtjwLDklqxDbdbpR8ctJYO/L6jrsLPUUiaeYJthjm1YSGjdLBNn2+FQeziazL5I0s0JCS3clbkRTcBz4Y+mwW46FmM2YacgBpKC6lwx8DG8iZHJssVXla0cHVkznZLPZ9y3dTed+JyxF6xqsx1ARL2d+PAhFcuXSM3PvjjorIMn+gDdRPFr8Rl9J7MW6cZB2teUy9MboxPAkwqV434xwug0pIT5eVkY8GKbgo9mJ4hlqShWaKY+6cjXZiqHUSu7GGIOFSCGVKjml2RgdSC4OUE0YuttuayqDHVFHCq9yNwoOnH7fbvkNGUFZRhobjrNFeVzdCkO6yscwtrehWOr0tbC3DXNqu1WlF+l+QPixcC74oNddfSFOZ56Ve4XJIX6DVak4pIfTFYOpSttR97KjzzXJ++3eDiL9QLCHRGQnQqQUGu5XaeWzta6YwMu6rJKCRk+9xLmcMMRSdSB9ZDAlPu03Eu3IMDME8KZiqVTh6Cu1lFZas8WHVCYpBsI4iMsmyloS3HK/zmISa/uBgLYjheAtzwxSkiMBbsjccty7dnNhPcZOLle7iJRmTPH2yiUTe9tNG7FWfdvbhN4e4VVVorpa1/L7tc6saX/eXS0HhSwuzZawshQOSa7KWUSqQdHsLregxQ7eWWYQe1qjcbz0o5UfVYlnkzv1HnY8dlnuUqHpt5OAbSTI3K5jVL5KfAuturgieC1NDRll06JPz3J/BCB1ERn/0l+i0i78wAj9TvfC9U661ZnbwVdI3bGlxRaxD3CtnnKnY2F7hfsu2kA46g9sHStZDnnxgR3CkOrWWiZtYX+9pxgvVbIJ9KQEw5zD03Qf73DlO2wInW9lLkRrdRvqeoDz28tmw1bC/lR2S7L29mq648twinZC51QT1NxHfsuRx2aFtkfDyvd1SMDtYWMIUu+zK1qV7Ut71jmdpae17lVLWSP0Qd9evGzDLVWartI1RRhrWtdCV1Fu/KQ1sAjtYbzGJO8UT7dxaoS9kaZkyPXs2RcaBrACJhcSdNDcLbmuIh2hI0wUT+Ypl+4Tw3bCcOYkjN4mxYpinERC1IaeJovPMaTYmRS5JR09jGlGX2LnbNfzaoxqzbTL1zUjXu94TywlyTue7L7c8nkmyCuSdvs6WQ/kOi6666T16p2FkiXX+udR3orS2qTRs8THFwbl9aKABcOeCm9DwkVmXEp7K0Mm2pB43SvBOb8qywByiY1resX9Vklxo57s+0XfyBKV1slhA0p83DU3JSsPsMsm2yzfr3s/W+/FHga55KrZIRbQfVUB2IyVqoS7yz7LMpiszlU01DaS2AOjjpqTyOMey8j2kJ0GprRFl2LL9nxPI5OXuYStW78ctJGtszYXJjRg1pIoMlCP2xB/vfU8PqCcpji6xjo7zmhu9XEPk/pGqOJDDi8lo8Yob5nT3LnZkPndvFoHZRSoMsmI1XGn3Uw1OEnGLoY8Er6ct7gZuOIE8HPZSPF5gg8QFCfaqh6WQhovr9eCcEqJjGpsXWY+S9wCmVknKhXQdkocdLZl0Sxax/v9yGQHiVpt8LAsquV65Co8xSJC9uzJTAONx7VyMsatccdv0fZq0kumUs+sexCbI4sJDqUdT4ezczPZwQ73w7i+TNsqPjIhwpkzq9l2P/ZELt9PeVU25iF2JjzN6+04dqfsJPpIeTZjMyUvqz3h1YPdHOnpYNbn9BqRcE8PiYyUbN0XcZSdTAiRl8GYa9p6SafLkHODymCz217JmDMObPabeLjRAOx24qbMD91m2E6hGSJuTMrigT1FONRjYlhMFwl0Yff0dkAlzOb5aleiJ9Pjm+XkOhPMNIx9TGIPrzZydxCZ2yHOg+vaLm7MxOyDe+yneORUG8wqXAZujKtC17i8Zb2Nfi1FzdR4iOyQ00Zt2MCZKiwiaUyDD/Y+jhEyDodbvi/NdFPd27MdclHDGoq2VXFCirijeNH4eyQqfE7L9JneypXBd4qBE1p22AhacedP7GUrNTXiDgYuNxkLtxte1vR6tcTNS3OjIakbNveVwlK3FcH7I5ZorXZROHhlMJ4FVLCZve4qSE05HKzmZ1HV00prq0zG067UoL5idtMyPWjkFttwvnc/HGJKu7VGdaWxtbuOm+PxqKQ8wZrCkaCPyPUkrMeIv+h3QTvyUuYoe5vhhPHIbjtiB8eYjYn08cr6qOkvk+xWcES0gU0M3TKm6JDbW+qeb7cjIXUnURyl0+g02Ckx87Jtl8vjujluYoZLjaSFLB+P2dWKhurN7XAU0LOWkl5utFnHuQQbXYghQV34eucS2z+fFNpqL2tOn870gdlthbvOIhudOefopRVKfYPLxsa6MfrxfAwsC1OCzu5FKj5VsYOTjcNaF05geh2zjo6pVJuzteKpLDUsVeCCTNbgU35OhB2XnBV2Yo+7uyJRh3BXHxx3gy0N4rLayDTS5OUdKSGu004WEzCRi+sZKlFZVfGBrrLYXtV5UzBVVNwtg7ClvfPKyywnS0QKRm/QRHolzB/IY9neDvgN3Wpj4uJLlVIGLi2W99F1nCQJdiZDJsJVuYr3FvHcCI+h8/bCU7yr3NRLpGXhxWDM4ZhomyC+NGWdF4ZYakdjuxZ4kGohS7E6k40sO/YnN186vi5SyEUs7mMfcsgh9laMlmzIGJNPSSQxdyuqhWQUKn7FH9UiP/HyOrs7ZLTUmC3BmyyLonHXDlu/W2WigRzCi9ozB4QLDgFyESZFUTBWZcVEDkrcYtP9Vcaays4ySjYmrukHVcdiIyLP9hFSUlhSdz7iR/ttwHYHQnAvOGxX9R5bWzf0Hu0j8mBE7GY4cLW8d5HtSO7ueVqj03C48hAkxUwx+jGDQbsYJXofIxBzaXMt7RZLV8R7jNG5DZ36Y9EQ68JD3TDenPeaskUvzhVNxe1dLzMx4I6TIqw4olLrpTbtO11R+5t5v5vRlVN3pGs67Kq0VEnoLTEQLHeEl0oXq65BHHmcx9vdUT6ql5A6efcu2g/upeASLWoubaKsgmJvHhUfHUn2PlVReMdgedpjN42P6DoazS2GLuM90cixNTjbM232Xne9Zk0aLTcY0tDeyeI2qaqhq+i4T9SquZZtng4Dj9QNZYfbNm5CiSpLijpTtb0ac2WlRadMLk9rYS/bG/akoqDZztkgYhRaDalWR+MBIyFavHjmfuMoqTqkbHANdtoK3fAhZ1w2dyHhtJ6W13YONgw+BTEdt8S3ZZzkik9xWZHtuDHgBRvnjL09WSl0606+T0g9tBVjpV/15wsz5ilXaqdkYxWlsE1CxED4yW6gLTUiWnSr83KrMrd9JFHjVS428NqokHAYsQruEvS0o0/yYTutIv58vA9Vpx7zUoHOPIrJvuZhrSLvi+ONu5+ljrplUWhpXa8dYKxy82EHGu/N2BQOez2GagFf3PWNLSpSw+jSaZTl1brehTXerqZVHmSsxHGmsJK9QWC4LG/NZh86DSdflltWaRpozawV1ucPqWqWem7KNgrD5sFKJBFyCjzegD3j5jYwGWbsxEoOSCm4yfA9Bm7DY32AY5DfrQERPVQtKXJDoUdt0EsJP2bCMaVut1Npr7fJ8b4aVbHxb1h/Uy7348jALZ6jht+estDT4Ypc33CiXN667Zgk3uE+uFgEWeeMJXTevthq62nnJNqs+7Yw9cHjICyBEWinZXrpb+4BYyGGg9strG6Y/NCEFO7DSq7U0/22TVwG5EZkOyeNCy3syPLbXC35uhyR6YZpdgg1QXpeVvT51qGUR1tChlm6eFLYMKNO1z3WmpMeY5dbM0Scj11DxfROxMDd1hCtV0iqAYqT0NXqrhv0XVaQna3kmjzxedrhJImHKtqkkruEqirsmyzCV8nysN4lkdU3eIEX8Q2/i5E7ni54ha59znZWNgBNHWwDzHzpG3lL3THEqTDLVtYokt5bMauWdglLCLmcpnXTm8uVGWvnAGk0q4Nu5KmcykvhdvmRuhJ4ZsuJnx/13t8uV+dirzjr22UNdo43vycbSbpasmWiA4uTFcWh0rkqj9BNstOSh/akLE2NXtlFbag9mbplv2eq7DJV3raDpfuVW8re2GHwsbD8oj0E7mFsVgbgCFwXh1rx7yOdkbsK0VEs8s9KW50M1MHyCUU4KE165ACvyLYWcApV+Wu03HKFeOeUgN9rw+1GrageQiYICnwqqr2jQIgtCVkQZmAitCXdZoCI6NLdakNuuHBzMaykTSmSnW7IpvDKKYADd7oIkg9H92PPW0a+agOMwy9izG18+e4Hkio3wm4KY6IUhkbYUlJUmskavUrDUamFFULUN1Xqaju9mr6bShY5DOjW3nJivz1GJAS3qqPr+PII02eiyej71qp6Dup9C1dJSsRSGuqwG0qetFpKBN0KqMO2osbgfJ8cjagT0DfrEysaOrmyAcKEMUIcosIlLr3k1Shu+de47TYxCdJ3d6HH/cYYMWlnoDXdSpO0PEQ3djraulTI1wvqqaage7qXW1aerU6IPE1VTsNdf20zcSv2bnztEzftd/v7HhKIY4JuCFJbw+05YvsmOhgbX025W3sjhPPqEtc+J6ROAHPbLX4xjL6OIlvM1dgZEBa3pI0glHjDWnTkXwPOHpqTGRJ7uWeY8rATa+mcMyuTO5yItTZeN321cqEjcye9s3+gUPQeUPx6ox5Oa7DHnbxBckyjcYdj6eHjZkciDTmJVXbvJ2PnVDyoqM5qPN8jSU5q0GRF9hl87LIOFYYN4jGpIcrOtJngshfxxDRRWbPH9XmiJfuqcVzLWKjZ1/kqi49rq5lqZBItuZyYkrrR3rLZExiw2r5cvbMntNN1wBW0JarzJHkqDLdxd2Z2gmchZUAhgx7roducdHOX5FkLt8HxdtnezMqkMEFZOqKMU55bRmt6ZKtEilZLW13dkIBeWmfIUIo0wOq9I0bEcN2tFENXQ6maajsX2NS7M+t4RUQ3V6wxtDYSwktLsUKookO3XrcsGr03w7yjzrZx7mBL76NDbngTxWJbQcKreNjKvi/Gdg7D5NrQ+6q3C+WwwqFUx3qIbqtOsjOoIFYrSMVkhxbbMVpvdnumH0Uh0AzQStYt5ccW75tSRZW7mC3dakBRBdVwdLdTz3hNGRWD3CEq2HVGt2lhaDw1wkBfynTNI8wxlfQttTM4B2xsLkvEOneGJh0NZO3d6GtzrFqObOCDYlaocDYZiYNQjjHYJS2ZctK55zEMK+6wk0I5cnDJZ62IjBIj1qHjnl7uzqBpIML+wDdekiXXVXchJjfQr91FzLyd1grrGBKv3kBRJ5hqaSnonDvO285GzopB3pkGtnfxnoFv3bCUJjYkJsxn4xUF4dqR4nXYTq5QyjN40x5Rt3QTylbJ3dHv9WjHoOZWSrzd1W1xGMaQydOzXBvSsSUJf3OsrmEj3qjTTkyMAbd1XZRRXd3ecZxPbiJhWLboeYVp3OnMIRDe1pOo7k8TqiYYW0mWRuNZTxhOu86xdeCpaIIPunjwDwVdtdo9YbwlTxfLo9TuLgf40Fi4p58KI18f4LBEraUBO15HnJDatdPQuFHobTMOkEJIUzFm0sFutSlBa2xHKz101I0sS4udsrX2iHIqeydg8okeq8PqgJ4IqPRdQ4rwEJ126uSQ9YVL+/xYN7bdLa9SfycBM6TtevJ1XgMt/bICW94dvPO6o7zeEiN3S6ACyjHnQnkXAuydEewuXFQBJ5DWyKCj4QVit67H/SRTQpdfznpKTFMDucyJTFV9CLZRKJTZANdmC3ZG6vqUd6wOQLfgmg23O518WY7uRrVTeBqCasqkd1wxdJx5bjMcNUfrgqfM0LkXn7GvWNZgojkiqAU2sTSZ7vyLLlN63DHLAq1PLId3hT1aS2oPeJVgVlfdp7Tu1i6z3qHsWEwhKiIw5rKyyQGTTCpxMJ5bnjJD5jQtxGGL6JN9tYuqbWlFeAMv16TT9d0pPop3ahiWSDMgeKs3vB92DefbtTt0xqG3RybPeO8IlRnfktPWjs7oqkXbMuPg60kr+sg9i33SrREP360MZR3fSG3Jc5dEpWkrdZatK2wu941y5q98wizzFFVwR/Kiulijsa3KG9INTbLM96tg2lurtKhXBLO8cCqwXso9VVrLBuHuaru5rzY6YfTL1qtZ4XR2ZJTCBhv1DlJWeKAFXl241sRyoy9RRR4J7HBvhqa8bq6CcD9aThVAK5yqidCE/CHHEFZEMTaUeiTa9VmkXbSjr+PGMK3gHUVguODLrs3L9XkSpLM0UVsI3+s0qik0Tb99ePt+2Pf233pNbj79+X920PQ8L/r6isvjZNOz3E+PtT7999T8y4e32omAks9DtybtgtdR1d8cuX38Zw4wZ4nj8w21r+fZz+P81grmd77fotztmrYevzRF+ngRBsywu2Z+J7SZXxt2wPePR7hPJV5nuV/a4svrkPVtfl1zfrkF7N6t9utl8DqT/PDmvt7A+oLi6y9eXc52v16ZAOai7/A78PL/AfCtOXO2LwAA -->
