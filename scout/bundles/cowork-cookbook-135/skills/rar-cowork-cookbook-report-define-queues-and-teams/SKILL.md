---
name: "rar-cowork-cookbook-report-define-queues-and-teams"
description: "Generates a read-only summary report of queues and teams activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_queues_and_teams", "rar_sha256": "c19ad6a4191396a8b0da1c1d958b1c775de7cfb16ca6de57d516d6fc13d03551", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_queues_and_teams`. The original RAPP
agent is preserved byte-for-byte in `report_define_queues_and_teams_agent.py` and in the RCI capsule.

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

Define queues and teams Summary Report — Generates a read-only summary report of queues and teams activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-queues-and-teams
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
      "description": "Dynamics 365 legal entity to report against, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-define-queues-and-teams-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_queues_and_teams_agent.py` and embedded as the fenced Python below (sha256 c19ad6a4191396a8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_queues_and_teams_agent.py` first:

```bash
python3 report_define_queues_and_teams_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_queues_and_teams_agent.py   # or on stdin
python3 report_define_queues_and_teams_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define queues and teams Summary Report — Generates a read-only summary report of queues and teams activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-queues-and-teams
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_queues_and_teams',
    "version": '3.0.3',
    "display_name": 'Define queues and teams Summary Report',
    "description": 'Generates a read-only summary report of queues and teams activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-define-queues-and-teams',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-queues-and-teams',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7544ec186fab0c0d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-queues-and-teams'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/report-define-queues-and-teams', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-define-queues-and-teams-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where define queues and teams stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of define queues and teams for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-define-queues-and-teams-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define queues and teams records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only summary report of queues and teams activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build a queues and teams summary report for USMF's latest posted period as an Excel workbook with a Top 10 sheet.", 'inputs': [{'description': 'Dynamics 365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-define-queues-and-teams-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-modify Dynamics 365 ERP summary report of queues and teams with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDefineQueuesAndTeams(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineQueuesAndTeams'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-define-queues-and-teams-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportDefineQueuesAndTeams().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOiWLbuX/G+J+JW1SHzZRKE7OiIC6IMioCoIJUdWcyDTDJDnfrvd6NmVlV3dp/TEffTNQcV9l57jc+ztptf3+y2iYrq7dOb7tv5grfTNI78amHn3mJd9EV1A2/FzQH/Fm6RN1XstE1R1W8f3jy/dqu4bOIiB9N5P/cru/Hrhb2ofNv7WOTpuKjbLLOrEVwpi6pZFMHi3vrtPAjIb3w7A5/cJu7iZlwEVZEtuDG3s9itFzhJLLb/W1/Li6AA6izCuPPzReqHdrrw82aeMMsoi7rxwZtfxYX3YeH5KRhXxXkI7i42g+uni9mIh/593EQL/anRhwXnN3acfnhIORUliizqyPeb+h2Y5g92VqZ+/fbp5799eIvB57dPv765qV2DS2/HhzGcH8S5rz3MYXLvNBsDpqZ2HoIx5QjcmoPvQDNgQAYueX6weH37sfbT4MPiP//z1ttVWP/06XO+eL0+v81/jm2+aCJ/0RT2wz7XLm0nToHV7wsm7e2xBi5t2iqf3V03s8Hvz5m/SyrKxV/nez8+F3kP/ebHz29FOYcJxOzz208L4NnPb1U7f36fpZQ//vSeFr1f/fjT73Lq1kl8t5mFAa3fv7y+v8SCgb8PjYPFF13drF9rVb4blz4Q/gf75tdT9Ze4l0u+PAf/WJQfFt+XPNvzV6DvM+8cIPf7YoEPwMy396SI8x9fa1QFyB47d/0ff/pnYt3Id29pXDf/I7k/PwVHINOBt14u+enDI3x/W0Av277J/OfLliBh/h1LwPCvy31z1D+T/Yjs34lOQdLW32L5XXHfmwD9dfHzP7XtX034sAg+v3HPsrSd1P+0+PWRIj//4P1+8Ye//QZE/7di9KKt3IeEL5mdx4FfN1++/PxD/bj8w99+/qEtQRaDQvzSVun3ZH7Pr491/uTB16gf/zwXrH/Ob3nR54tvNbT4tSj/V/Xb++Jip7H3+/X60+KPlTi/oMVsxNdFny74QzXWQNc/+PGnt98A7uTAmtZ93Ab48R//sZBjtyrqImgWulu0zQIEuIkzf1b+FMX1AvydUaPygV/rGDj2NQ7k/xzhWWMAwb/8H/eB7B/dF7LDT3j+4j0g7csTor8AYPzygOhf3hcnILWo4jDOAfweGVX9nNshgOF5xbLya7/qAEo5Y+N/BMX8cf6wiPPFL/9a8JeHjPdy/OWBwvET845rcca7uk3999kyIwLA/7TDBaDuD77bAvFp4QJdghjA9AdgcV2kHcDL2Qv1LU7ThRcDRAFU9eQJ4KlPs7BffvnFsevoc/4EaHzx5LAaBgO+qbP4+BEYFaRxGDWfc9+NisUPv/72w+K/Fv9q1kP4vIYKaOIVB6ChpCuHBairNgPDQIhAUAFoPOLw628v1wIxgD0XM3MFsf+cDPLy5ntf/awLzEeMIBeOD/wLfJvNfp1pLm7eF2Kw+Kbvi2pnXogANwJGLP3c83N3BFJtYM43T+ZFs6hB8tUBYMO29h+r/uJU9kPFDBS43fyykNcqYKEiBf/Naj4GgclFHgP3f8uC53UgpPqhXrBfRbwvDnMmLkq7ssuosl9rBPYzLjOvv6YD4fYi9/vP+Uy2/uyqR1k83RPOvUXsvkL6cY45aEYAj+de/XXt8NV/zGQ+c2b1Oa9fKW9XcyhcQAFg0bCNvZkI/vJKqToq2tR7+A9oOkt6RcF7ReWRg0+y/8fm5dVNLJ4tweJziyHocvH/Ty80287w/HHDM6cNt9gcTsfrMyZzMzjH7tk/PnQuqmf9/d6sfAWkr7j8OU9jkGDV+JfnyEckX2OeWNdWwIIjc3zIB2kEYjLLfWT5nLVVNdeH/Tn/SgBA6cUD7UCgASSAkpkz9euC892vmkag7ufvvzcDj6yovNlskMmLsnVSkGWB73uO7d6AVnPwvgYVpLw/B62PYjf6k1VzDEBcgfwFUCIGtQdI4v0bKD/vflX9TxOfPc885dEPtqBQq4cAoIc/KzgHZA4VUK959t7Azk8PIcCMrGxm2x1QKsDS50W/8u9tXMfNDItPv/olAOSP8/vT0vmqP5SgOoCzQA2ULfDuo2rmXMlARwN0AOkDiiiLc8DwwCkvJzwE2tkMAQBiXy3oU+Lj8ssg/1FqMzV9nTgbMs+Z2f6Z3XY+/hEpTt9LEyAvm0c81v37TPu22ix7RssaIB5Y8evdZ1vw/mT2Z+uw+Cr30z9sbn789/Y/D64+/zkBPi2ipinrTzD85Nev9PoOsAp+6lq/qPbjkxE/PhHgI1jt4wMB/iT1afCnxb+n2Z9EvCrj0wJ9R96R+db+lVmvF3DE+iN7/bic737Oj/7vOAqWLzKQWnPYRsDt30jv6xDAfGEFQAgMfpJgPXNnD+j6gfogBp/zP6b6XGqAVPJwTs26+AMEPNgfpP0zZN/ICdzKG7C2N+NY6M87s0dh1P7bp7xN0w9vACD9/25HNrNPNidzPW/iQNkAgGxi//HNAbrdPFCuXzyQrHn9bLV+/bu9Lfft3iO5vk2azWgBGIDCBzRrV83MWx+A+o0fFjOugsGgMynBxEczBqb41YfZQ4CR7LIExsz1MNvVjOVsyHMrNzd/D9Qamn9URnl8sNP3F2rXfyyFF5vNbP6Hin36HijrAtsBMTyoCegGfD+7Za52u749jPuuLg+m+fJkmu9454809SdSmluGJ9nZ4aPQPyz89/B9cdbl7XcX+tYO/+MqBuhGZoFe8Wkm5g8v/APvYAsDfP51NzLz3nN/+NjI5y3Yev8874TmTHhMmT+AOeDt26Rvv2Y4/tvfvqfXAyS/zLn6zLi/1+4wgx8gh9nbf8e0QGewrte6/sv6f40AHzEEIz8ixEds+T6k9fBdPz0p/h/VUP/YAcwrP5qevwCXBHabggJrioeK2dwZgqyYafFPXcPC7kBKPUD61Vc1M1U239ECqPGgGkDYs4d/D93vDiwe+8qHwqndPH8G+fUN1KINUtB+VeNrYwKGA2T+WM9NGQzQCiwIvj9xBdz7N7csr9l1ZIOmGUx3Udr2SHuJ0ihOkzblIJ6NuqhHE5SDuqsV4fkrN3BQ0rVJzydWHoGSHhm4KO4hOEGgQN4Tm77MfWc8azSrAxzxEcCb//ttcMl7mfJUffbTtx3SbPLLIoA95BKMFJa1yDxfa5hGHRJbObrkQBXpF4TGVPYZVI56TLd1mSHXvGGZTWYbcJ3fBE6cmLNh7a/lLcTilZbwjJOJ/lUikBxTSP++OxA3BUoPE9ILjK4fL7an5G6D79MLJvBeL6beUaxNtdTHdJMv9fi2J43RVEYINyY8iDt30juWg6FDFwxGa42HvrOlRCyPtIKMJ39tnHkiL8O2rXSqkOO2IHf5JUnJi+2uWAnm+8suUM3mAO0vAbEMusGoDkxw8Eyt2QzCvjlS++yoIaER3e56cVMzDexWtpuI2/MtN+zQPKxOCcXL0RW3TRI9HeTKPcoXnurIozSJfQHH64tC6Hs5PyJSU67HszLElK/iJOzn1XbwcwnaI7hrrgQUHWprE+uSvN71LbznrHKKRq7GxNPuKCwzB5Kv+Z03+zOfEre7KDqNKJKG4lmrMvTbIk1s8Rhp7M2wQhjH9/Ry8o+wPpVpfdkn8UkT1v6RPLaM5ajL1DhHl9Dg18LuVkTJSV/2bR9Xlp00hKMmNoXRXLc/LxPl1IvSQTuWQrMzWDzy961cbNZ12ZPnwBQ3ORLVlYxkkacnlRXJ24yyIF11NAkL9zLLXKB9JIl7cY+VKGThaXuS1d1Zt8qwGMwNuskKdyCUNNYG9l6GwNeUWMcJYaWhhiuZ5ixx7Lp1zKrcDjx2Z+GdqRLuMb4DT2Kyyp8x0yczWk6dUgzG63jl6nKN7PeirlWoGFwMLTAm+qbG7HjURhyxpEh22RVBStClKXCRTlxm6UlGqamni3Mz2EKi1hqxyTfqEsdTmumz1S5Yyae9sC62Gto0WoZVzA4BZM6kGG5dqrN+W44xcc52p2tiri73SyrcEtEsogmOixp1bstTnd8pa3tHBsjT4YSzYcZ0dHZZNKGvZQ4X3ujpoDkHgSjsfNkczsbxrpb1VuU2PUX3Ie4ukQK7Z7jZ23I2yGDvqdZefDYdVLnwNLZPyEM1Fdtlf5woV6PdAu6JG8zf6h5eK9sl1O0F0vOWihl2aG8HWlqQuLvT9W29qrWjyJrZeWuUWYQnkF8inM0xV3O1pQnjuoIYyb+ivA7bbItCx2PvWiqa6eLujhBKhgnOdqjWrX2U+Fu03S5T1roqa7sykB3D3Vl0meeXYRpUdfAx5tDyxZWRT67vrMcAqbNJXMnQdM38BNc2rdRQatds7ewSo/zWIgClepfldRMl6Hk4HJTDRszXl4FLLrBF8LtbTee+LwXQUttyhzS936JO6qTpdOWMqiodlM463IauBnwpI1q5jnotaunqNF6GcCD65e26v9Xbq96lTHBbBwdx4q57ZH/y422tMhdarM4xZNJeetTyMOv7UG9WsLnZ04RwBGxSrmMJPtQtx1DsMYZPneyt7AIroT1B0LucUdzLzde9HoJw6yrmXsglspkMliAdMrQ5oyUr9QKii+tEcyF3JbemhQC8K1R8L58PsESRd0Mxdtxoa76x2aBjAfW7ILziN357dDySEbtAvkLrgpqGvR0ODh9t82RSj2wY+bfzKrq44emEVMatHcdQ2Tn21ne0u6ko25XMhiZoUJtis5NUjhJjOLVUWklgPz4z7X1p5dwqAfWs4yfymFpEsjl0jL8jCaUOuP6SYq3tTRREIwTty6YQmlRHHStKFiuTxbdxsT+6e4nDu7VrI3p1R5C96Nx6zJtapABQ74YhEtg0d6ewy5XNhQHap0m/28eSYIOPvDPByM0seqU5jbeKV+gsF6XOxKarUclTfII2YaBbijGma4vmTX1Kw0Knt1cUKY/3m57X5CjtI1HKKVgb6mVCNeJtw7Klc7BoNmmUvonDncder53vpLx0XPrUfcA3niiKF+6k0RWfkoln7iWjuTL+yWDbQzb0yD5b44nHZYnEO1g5BUIJwcppRPmrRTM3Ckr0RNvBmGKXh1qJjss9p+LrnM6H1Y3a6YJn1ks5S0qWhQPeqVaQ0VsqDOVOul+CMNLcNbXy22WXyPJEGc6GZ2Q3NmAWdztVSiQtPRT0+b6ui+uOSzoto+TDxcTIK1+1ZixMbNk12YVlvE0yZd1N7qLyKMv3TFquy7u7QaaCP3NJT0X6TtjulwUT9ntPKveaWNuhXE5sfz1MoEKzdaKvy8lLdWLyJQQA5XkMevuSbA8ylsW9MmrGSF9x4zjlBRL2+I3Wy8wc9GUykPW2DoutXMFXZFf7+wheb7fscbNTyLjdXZu8WKFsbbtdD5A+uo/HfejvoO0Vu1D+qb2xa/VCFddYXfe6n9w5RJ38ititYicWjpsjBR97+MjL7O52aMSe32OFImzvZow4Gby79yW8XFZr/piyzm7+maEawyIg9ZO+VTf3MT0PnMHCfMiErTAIqXvblBZySKhat8Xz5qDz4jnftcxoQjg2UUybnq+XbSpYmymU1qR2XQGm7251uzvEKjKuTzYv3IE+/rQrokha5ekxSjd3K7l6WZFPjBry3WGDlnbGOhPgcpnZ5tR5HUX7hG9NFyLK5S7A1lTtpuJJqTBotM41w8C7ttxq2HENYNFNg3GZnyrnfOQQ1GQV+5RenIMYe5x35RgGOeUqejbcqaOr8XoXm3Lsu/tR2EMgXeTdcrN2/DLbWCPulZRebCFplSla4ZZ37VJbVF+tGCmKEYqjzvkNtCz7Ail5Kxb3hmjy3nGpEg6EHNfm8c6uCxFu9ak+MtBgOhvQOS8RB8Kd7VGZKjE9rnEUS5cGQcqYzPp4uayqoImjYH0UC43g+yPMc1sTMabzyd8dw1vh+15eUr6ZRKt2LxHsaFmDqYcIiqxDwdyfwrPVIM363E+sdFRQOYw5dG+z6nZlpJZkYxXrHstwey3gMSibxGDLllIwAF5Kb0NJOmpFY0hFeapvmARa8lONFrcc9i+SSTDUrksOaIDxp1729W6zF8SrethWm2QLNlwicmqgYH1FrhhXEM45STo6kBitNN3dPkN9S/bI430dr01xHQ+EtjoI5G1oGF/F/NZGss2WRvArPEFuueEJ6SyD9i7OzoRgsXi1CnRJdRt25E8r0FS2Yp1nOkeI2LrYr8qr5W46nMxZ4XxZ8bv0qtf37Q1ntEzXy80gilgl2sQ5RSWBTaC82EhHi7mdurCMrHNo1/t+tEQ3R3Vg6GTImwrAYqtVDkMj61YixGzY5EwoH9NkL3N8zEZ8Nkpjf1asWuiY+hZ63bDWvOYw4eZGXdVGszunl2498sEO5e8iwxqm3njskjeZg8SMbrM9EDZ/VgQxbkqvq8oYz29lVaaHQVEb1MCI84XhsBsWre4g40/nI5Jiq2URTA0JIdD21gn3TA3FrOh0xQ0TV7dIlOQhPcwcRi532ykg14GaoCTU4ggpdSVCwl6yEshx3YGKXxrKvTGhm7bSFMNUxwNCW7yzM++38MxcpPVhTZ0tXFMT87Ym8VXGGjkvnbaX+3KryM1aYj1SlgIDjROad7l7WOH2RLWGpndXC+utNhM2KpWNIdvuCGgTwUhcdPwOJXgKcVFDLpxe27lb47zRz3EtiUtJzEZuq2VEIuZxexPjsNuc74OO3OvddbQrqyf63SRS18O27BuFG5sah+KJrorTenJ5orNuWIduxi6UCQFn7MFbbTec54tqHIr8zbjXl7LJ4Z1Q7lvN2NCHPSU0tnn1EYcx4dG63o+VdiN54tT7m8C9YqIokBDUCSViybCWpd0tZloNKbh1ozlXnsIrb92woOOKNkOYYJKI66O8NGph4IrrobFoGaXkPS3JKpfFoFJWzCCeT6XlXa+S1fQUDnOay3Mk5uqecq5Lanc0xEvStJOlnFt1leplfyC7RpaS65nsi6DWlhJh4vcS0TDTppPxjCRIQ7V781BfLEAFbqXuRPTesl6aAodzuOsEzbqsR0pnNhs2VCxrNZ45BsEdHy3v7NlvYovWyCwuylV80tl8d2a80jnKxbhbsnJ7dHuyAqFZYgY50Kcuo6JeQ06HrKs5VluS6y0ZMRyJCBF3cfopLXBUR6l4txMqWEEmhaH0e8M599vJzFKXpPN4NyIX/9Yq2jk2rrZWqOcahQ3r2unWSVAKsuOLlsPpZDKMtRVRaKtqIqnr1SikpbbTnI1VriThKjFLezNIrMBOyVn0LOoKelPe4IOY3ReX9ha3utkDuEowWQ9vptVvPdRe9jVPs4UjFUJxhThzVOWaX2GEFdEnc4qDuhsReXVbaZHGlMthhVsHcpVru/A0nvEIPmV6ji9NdHc6bgJY1Cp61D2+OzWacku67UXwWGUJ3XdGcro3xVouENrtC1JEz1l6Ekx2dyCh4J4wvGxWEAjGele6sBhEpMtkyTFFb41I2icrurpRxDBnk94cMAphPAqKkj5Ab8Se2Pdhqk1Y56Knvbp2j4OM3rGT7l0QGZh+zekWycqgNXsZa+rL3bywZIRpS4Nvo+LAmZbgHGt4I9xZwwJdO0pioE8oopVhToQt0jW+EbGyvPq07w/oucDPqZYESkYmGCq1IaXwxkEp1Xa9KQnrsiqWK5tr/B5mg0NtImf82oQNDV3aiJQ7M1hh7kG5xyoFFyis2qmpFhlUdih7WqMnztsQuSqptH4U73s3CehkU0A063ESupYUE3OnGjSqA0Z2ZaCMK1TeGhcYeJwAFUfYKwGi+sGXIwG3jDWGEX6GZ3hEFnqPeEmz3NJ8adgyd/WzzYpQ4RV0gHuTH9LcUjiSWMFbeKj0DGJvUEObB5yELom5kaY1eUsafaDC4UrwiVKOCRJ59EoWAiTud/nWUU3FZScog/BzePKmLcVKUsKEgcA77W3CesS5jftLXmUdaHUC/SB3A4YIibXGRGelZlYQdbLtDqMcnwQ6KoUd5FO3reOTEk3usKJeyRHH3LUJHrCsa/E9AMZVEE/dEmi6uk+HW63aWgl6MpYq4C3h79U2c04VCha/7/1LA1w+ES4qlKDZJYyE3oEtWkrbCr7U96Dx0lztJIbHYB8uzUBp18hKdZaZFO53ZWOREXs53Zf0bbAIi/TKwvc2l3tE5BeDK8C+0EF0xYFovoIZYa/wp3DAKwzfZqK6TPaprm72oLvRsx2FxJoR9uppgiKQ5cO01kT6SkS+p/g7A7mznIeKOHoJyTBscsFXknXal+FQbBD6zlOWAkl3J631aGXqbD36F+OU5qnQ2+caho1o6akAA9v7CtLSGEp20abYKu6kEAdXqWqaXVdYmQmCPDSUwxZZX00m7hY8Ujm2XVgBlFFrJapvPByQsXLL2mU7nPcue3MUzcW39CbKQVPvWOYZvZeyTvSCfCfSKIuafUySBFcWY2vgMk9bJ+O2cxHzUoV7QHN4kKQVZ6/zgRqb1m6FnULDfgldjh3AvjqYCoEoJ6M5CJC7u9tnru3sakdtKRw67cHm62pHWHgbe3qb9vS6Sic0c0JejGOe3J+wbnUMDU1dFXB55Ec7jOVoqQr5+lzdE1/aCZQtF1Xnis2K4bPOoe2oQPEyuXQ0RVZ2cFmZcKDUg7c8ujVEq2qLck7ONdg1LiMCddLNNLoSyiTJtdchjWxUn6CHY+OcfdzwTtxA3enSNVj/nNNq45MlhnNXuurKcp9i5LZb6sHNvzJZxyAoaENoDN3RMX1pLttkXXr3AfOPuG5g+KFV77nnYbB35qDrkU4rRaJ8gkf4a6GcJzciAb51FQCEKkI2Bb0PyFTA62O+7VACLKDXO7LkqBoBzVuJ81UR5luKzEAPB4tbubBNxSS0/iLdkoPriLiSjC01VgZ3pEWRWm7UpRyvLnvBoi4ZtDxhLpINXk0bytVOXZSt5MsNzuL22hKFBzsayHpSaiNXZRnx7roM5mFrAaoOdMbWh2Eqz75jcOI5QOExHbqBbXh0E5Tpyec4/ZDbplXShT+lYuZ4dqQ201bHt9iqJR37bBHwntfLGrOy1utGi99pGHfwiShbqyu3SWS+UO9SIvv0iMnCYSplDFfOFEzQ8WiR/eGuD4chQ+GWI0BCHC43N+HoyjegydVwleAQuqi2N3VJMRe9JPRNqayp1JdOZ/PuQBtecpSVgexOfb7qe6LRVUTpdtf0inaNvxQapSuFUiMKhzIL0oHBpuhO6AJOp2cOU2MzldLGihDQWVuGTmqrmyZDhXHRFPqy9FWqIkYaWW62cIQE+A4wLuFIw77ZW16OlWiZB7DbNjkb3Me7NvrCcNl7LqQ4A66bGEX3yba7C/sVvpWdi4LJ4+DKk7RJ/Gi0t0MzJfB95cRbWhcxFWzc0QktfBfZH0TqBIvLW329lKBDs2qaR6t2QyGtQ66YtPWOMSdEm35cY6v1Rl97GgnagKUdrChmeVgf+mvdYk7l5UqWlKnARwhN9YdTbE+Tme9Nr4oCjRvPHn20ONRWl4ctS1/FS3BJheCET2muDJ3SYtXUFYehDxB0FZGUxXQwnbqjHY8BhjOTXzudVvuDjAvMzrZUvjK9Or1o9eWIOprRYDkmTClCYy6c1HvahSNLpv3ysjrwS7Vjp2wHu1UzVD6MWWVkxgLkRJUpDUgf010XeLTYuz1r01uSKOtmOsCEgp2ouuyaKJAmhiAgg2W2Wgvvylx3inWRhHf9vsa5mC48hTsOHuo5Q1WKhquIxOo8LU+aVUu2jlyEUw/tWFBGbXdsrcAtnLHQSAiWvWbTCjhc5dCQxxOyOcCujBFojDelEC7vNMqQhqKiq+zSm1REcTLAqPtF256Ew3qX7Aufjw3apfbdCrIh7hQeRraYElo4OcjRauVNTU16q8DqgHvuQMer7Z25H6xllaKoqoZwcyHRPXoBO3rmr28f3n4/xnv7Hz6fNp/v/D87SnqeCH19BuVxOunb3qfHWp/+pwr97cNb5cZAnedRWZ224evY6e8Oyj7+6+PGee74fNzr64Hz82S9scP58ee3OPfauqnGL3WRPp4+ATOctp4fmqzn52pd8P7Ho9XncvPhql37X5riy+PRvK8z43x+qMT3YrvxX1/D17HhhzfvdZD8BSeJL35Vzka+HmAAtuHvyDv+9tv/BYD21PKyLgAA -->
