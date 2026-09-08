---
name: "rar-cowork-cookbook-report-set-strategic-goals-and-incentives"
description: "Builds a read-only summary report of set strategic goals and incentives activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_set_strategic_goals_and_incentives", "rar_sha256": "601ef4e08a305ed0281b789d2d779a95535dbde0ba1ae4a891417bcbd6fb7749", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_set_strategic_goals_and_incentives`. The original RAPP
agent is preserved byte-for-byte in `report_set_strategic_goals_and_incentives_agent.py` and in the RCI capsule.

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

Set strategic goals and incentives Summary Report — Builds a read-only summary report of set strategic goals and incentives activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-set-strategic-goals-and-incentives
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
      "description": "Dimensions for breakdowns, e.g. department, category, responsible owner.",
      "type": "string"
    },
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
      "description": "Excel workbook filename, e.g. report-set-strategic-goals-and-incentives-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_set_strategic_goals_and_incentives_agent.py` and embedded as the fenced Python below (sha256 601ef4e08a305ed0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_set_strategic_goals_and_incentives_agent.py` first:

```bash
python3 report_set_strategic_goals_and_incentives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_set_strategic_goals_and_incentives_agent.py   # or on stdin
python3 report_set_strategic_goals_and_incentives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set strategic goals and incentives Summary Report — Builds a read-only summary report of set strategic goals and incentives activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-set-strategic-goals-and-incentives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_set_strategic_goals_and_incentives',
    "version": '3.0.3',
    "display_name": 'Set strategic goals and incentives Summary Report',
    "description": 'Builds a read-only summary report of set strategic goals and incentives activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-set-strategic-goals-and-incentives',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-set-strategic-goals-and-incentives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f2d1605e3b7230d2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/set-strategic-goals-and-incentives'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-set-strategic-goals-and-incentives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Excel workbook filename, e.g. report-set-strategic-goals-and-incentives-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where set strategic goals and incentives stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of set strategic goals and incentives for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-set-strategic-goals-and-incentives-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads set strategic goals and incentives records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of set strategic goals and incentives activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a strategic goals and incentives summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook filename, e.g. report-set-strategic-goals-and-incentives-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP summary of strategic goals and incentives activity with totals, dimension breakdowns, and a top-10-by-value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportSetStrategicGoalsAndIncentives(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportSetStrategicGoalsAndIncentives'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook filename, e.g. report-set-strategic-goals-and-incentives-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportSetStrategicGoalsAndIncentives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adPiVpbmX2HejhjbrcyUkISW7KiIQQsItAESCHA60tr3fZfb/32ugMy0XVndVR3zafACSPee/TzPua/47c1smyCv3j6+aa6ZLbZmkoSBWy3MzFmweZ9XMXjLYwv8t7DzrKlCq23yqn579+a4tV2FRRPmGdjOtGHi1AtzUbmm8z7PknFRt2lqViO4UuRVs8i9Re02i7qpzMb1Q3vh52ZSPzSFme1mTdi54KsN3sNmXHhVni64MTPT0K4XGLFabP63xsoLLwfWLXywOFskrm8mi3kr2DALKvK6ccGbW4W5827huAlYV4Er5qxowQ+2myxmrx4O9WETLLSnle8WnNuYYfLuIUfPiyWyqAPXbeoPwFd3MNMiceu3jz//8u4tBJ/fPv72ZidmDS69nR4Oam6jffFtO7u2zpzdV8eAkMTMfLC6GEHEM/AdWAmcScElx/UWr28/1m7ivVv8+7/HvVn59U8fP2WL1+vT2/zPqc0WTeAumtx8+GqbhWmFCYjAh8U66c2xBgFv2iqbkwGCHWb+h+fOb5LyYvG3+d6PTyUffLf58dNbDkww53R+evtpAaL86a1q588fZinFjz99SPLerX786ZucurUi125mYcDqD59f319iwcJvS0Nv8Vk78OxLV+XaYeEC4X/wb349TX+Je4Xk83Pxj3nxbvF9ybM/fwP2PkvSAnK/LxbEAOx8+xDlYfbjS0eVg0oyQZ5+/OkfibUD146TsG7+Kbk/PwUHoA9AtF4h+endI32/LKCXb19l/mO1BSiYf8UTsPyLuq+B+keyH5n9i+gkzEADfsnld8V9bwP0t8XP/9C3/2rDu4X36Y17tqhpJe7HxW+PEvn5B+fbxR9++R2I/m/FaHlb2Q8Jn1MzCz23bj5//vmH+nH5h19+/qEtQBW7Zvq5rZLvyfxeXB96/hTB16of/7wX6D9ncZb32eJrDy1+y4v/Vf3+YXExk9D5dr3+uPhjJ84vaDE78UXpMwR/6MYa2PqHOP709jtAoAx409qP2wA//u3fFnJoV3mde81Cs/O2WYAEN2HqzsbrQVgvwL8zalQuiGsdgsC+1oH6nzM8WwwA+tf/Yz9A/739An34Cd6fAXJ//orcnx/I/RkA5edvyP3rh4UOFORV6IcZQOXT+nD4lJk+uD0rLyq3dqsOAJY1Nu570Nfv5w8A+he//tM6Pj/EfSjGX1+08fDpxO5mFKzbxP0w+2sEgBqe3tkA9N3BtVugKcltYJYXAhh/B+JQ50kHUHSOTR2HSbJwQoAzgNueTALi93EW9uuvv1pmHXzKnrCNLZ6kV8NgwVdzFu/fA/+8JPSD5lPm2kG++OG3339Y/Ofiv9r1ED7rOAAaeWUHWLjXVGUBuq1NwTKQOJBqACWP7Pz2+yvKQEwGWBrkMvRC97kZVGvsOl9Crgnr9+iKWFguCDUIczqHGHDBImw+LHbe4qu9L3qe2SIA7Ak4s3Azx83sEUg1gTtfI5nlgL1BSdYeYMu2dh9af7Uq82FiCtrebH5dyOwBcFOegP/NZj4Wgc15FoLwfy2I53UgpPqhXjBfRHxYKHN9LgqzMougMl86PPOZl5n5X9uBcHORuf2nbCZjdw7Vo1me4QGLQGTsV0rfzzkH0wvg+cypv+h+rDFnBtUfTFp9yupXI5jVnAobEANQ6rehM9PDf7xKqg7yNnEe8QOWzpJeWXBeWXnUoPbfTzqvwWPxnB4Wn1oUWeKL/4/nqDku6+32xG/XOs8teEU/3Z75mifLOa/PYfRhdV49e/PbePMFwr4g+acsCUHxVeN/PFc+svxa80THdrb4tD495IMSA/ma5T46YK7oqpp7x/yUfaEMYPTigY+gCABcgHaaq/iLwvnuF0sDgAnz92/jw6NiKmd2G1T5omitBOTGc13HMu0YWDUn9EuWQTu4cyL7ILSDP3k1ZwHkGshfACNC0JeAVj58hfHn3S+m/2njc0qatzwmyBY0cfUQAOxwZwPnhMypAuY1z0Ee+PnxIQS4kRbN7LsF2gh4+rwIUl62YR02M2Q+4+oWALffz+9PT+er7lCAzgHBAv1RtCC6j46awSYFMxCwARQQaLA0zMBMAILyCsJDoJnO8ADg9zW0PiU+Lr8cch9tOJPZl42zI/OeeT541reZjX9EEf17ZQLkpfOKh96/VtpXbbPsGUlrgIZA45e7z0Hiw3MWeA4biy9yP/7dSenHf+0w9WD3858L4OMiaJqi/gjDT0b+QsgfAI7BT1vrFzm/B3Dw/iscvH/AwXug8/03OPiTgqfvHxf/mpF/EvFqko+L5QfkAzLfkl5F9nqBmLDvmdt7fL77KTu53+AWqM9TUGVzBkcwDXzlxi9LAEH6FUAksPjJlfVMsT1g9Qc5gHR8yv5Y9XPXAe7J/LlK6/wPaPDARNABz+x95TBwK2uAbmcGNd+dD3iPHqndt49ZmyTv3gBauv/8wW6mq3Su8Ho+FYJeArjZhO7jmwWsjB3Qw58dUMFZ/ZzYfvvL6Zn7eu9RcV83AYfcD/6HmZTNqplZ7h3wAliSz0gLhpgCbHlMc2AxoB5gTDMWs+nPk988Kz4ga2j+Xqn6+GAmH16QXf+xD140N9P8H9r1GW0QZRv4CHgBmFLPtAyiPbs/t7pZxw8nvmvLg2g+P4nmO1GY2elPXDTPEE/WM/1Hd7/icdbkzXcVfJ2a/166AcaTWaCTf5yZ+t0L9MA7OOmAsH45tMx09zxGPk7+WQtO6D/PB6Y5048t8wewB7x93fT17yGW+/bL9+x6IOPnuSqftfVX6/5CqV8Wvvz9pxv9PYqgxHtk9R7FPwxJPXw3SE9a/3sbDn9k/TlUz8kjnMDw47ie2Sagl5r8UQnpPCuCcpjJ8E/TwsLsQC3N0Pwd3UD5g1IAMc9B/ZatbzHLHyfOh5mJ2Tz/QPLbG2gvE1Sb+Wqw15EFLAcI/L6eBzMYQBFQCL4/QQPc+58fZl6C6sAEMzSQRCBL18NdhDIxZOU6CEotLZKiHdQhSdqkVyts5ViOi1jm0nRxk6KX+JK0bMshPIskcRrIe2LQ53kMDWfjZstATN4DGHO/3QaXnJdXTy/mkH09O83ev5wDyELgYKWA17v188XC9NKCcdJqpSuEITBT9tLVSZtqHycYO0XKoN0m7cT66BEZ0ZMplaaw49PldBrMJVRs9+oQ+hzNZ+T+gKi4G0tyNkZ7paWrm8VI6ya+ucIKcjAuSt1Vj7R3NhVln5bai3gy1LgXz9ptiMUkPg8SfeYNvJRMS95TIk2KuuomkOp58Lh1L1q5ly9cLOdjpsYomldsZEeKKCGX4QDFfV/aZYOKdwJHcIywglNsbNyDvrxA0gZeEnZ3ukuZoV42RzPbFdtKZnhkc1J3Z9GUzu2eW8WVwA+CxKjKeFgnxc4TqNt41G0Tm0r8alygvZkYLZbgMZ6gRh77me6a7sQQbmjwzX3TrXzqoCcj6R2u04qm4cE+HGAUc2rPO2xa6WzEyLCvQnJdLqciy+qN1V7MTSjv6qsY8lm7uYb25hLkmGRzym7JSoKbw0ovXsSCadn15XK+1HqLEk6XXsf8XMSTcbkSeHLe91naavzI6fewLLRBlNmxH5B9MfKKcFkFDpHlK7ft8OvO26TZKmtvVn+sfbvME0RoVIPBAlc6ifldS5JuHUYizPBtqjdFVF4KmauaW2VUHnqkxU2EMHf/uL/iLY8HdeYiKnxQKWc0g+Jy2acpq+9v+tk0hkmICWPP8dsyZTbccTdO+2tIVDyTOvIaHrq62KHdMZACDTUDmpv01bm8sKkU3o1sAjkh70fIvXXIWSDlO39E87Iey5E7O1Nea4XRDqwphyfqpmvZFJ3zixC7lDveDKvkBpnP1upVO2/yA1E6qMjwirW+3WJ9lCDzOuL+zrqnsoKIKzI5s/ENDXydSPKNuV3moCPu4FhI7DXRKQ9ayW9bZelM1jFxVnt2Q+40Ei8x5nyH9nJMX6Pj0OnCcrmDZEWiRM/gueFErkFsUIEhyP7mQxZm3bDDIOV1je5RO5CGQY5UalRpVd/Km9Db0qbXQ2jW0MsDCo2pkakk1cWZRwp1esixzd6/Vtx0GHoOXuqwkOq0mZMcvMPRiSB3XkHCm5HamO1e6uu9eFgjWc7lo7Sx7DMra5N4udyMPbra8eLKUM2dyrRylbIwZa1brN/WtZbmN4VH7YxtzABKRUuSjtwdzuq1MylIyRWmVpwyji9JnUciYVOdjDOh8SGHS2v3Wh9D1gvvMWtRuyLnjG6415LUj6MlR3WGSjwmu9RJDa8uV1EDW+QEd0kbRmHE87ZObiLC39juZhqXXLwkK77aCLHqR/Q0GKe7yaMU29ByWuTjLY5MrtlVcHhX96i1m2xWXeqTMoHAKxffSa/H1XW7sbWeO5aOvV/ben3qz6frTuDPp93mvoXEU7ZPJ62hJ/Hqj4M3xAHsGwlXMvusbLQwo8ZLwdYQibIpixUonw8+c+RSw+Na95zvYiz3+IY067FQPaJgwzhgSkPrtjAfntELDiijP/Bkgpx9pIeQ5po0wj7h3diP9syGILMlR2fEyK7bm3Rp6TvuQadqLOxV3WFNx2+oowgnLhRAB4b35JrBPBI9hi1U+M7WWBWhsVyHmLLfLYWsRUNmY951aMsgjCMdm3K72iltcmUiMJ5lxDK53kdqS9mXZbS+nuPeUzBXO2ct5qSeyIQ7IjSgnsSGKYOJIVAnyi91NPIFc0uqdrbfj6Fmxtcpysmsu+jtFR51CrE6NV/2wzH11VsUnIxtvLru1xPWhvndLPXJHtrpfsdr7BidrTqJZR6v7PSodzxzrVfqcDh4AXM77UbRuYdWz8Db3XEtn/B+2waxNYlMpFT6taLJFeM7JsSeuCNLRfl2ExwdNg6xekes/B5d84RymUyDvqV7P7ttBWl9W9maa1wCltdMVDh7PVnp6n6TAm116KCdAjBJbiaDbE9kyCiqsuGIWhSQzcXsNuVUr/NNd3cP7njJpC2PG+GFsHnmSECOWtWQ512jAbOPHXnaTauDWPB538NEcuroMEK2W9lO2u1+C8GwwXIQplt1ziydUWQNDpKF64qG9ieqgTuuR4yMQpTykrn6Jb4XmRdOdz/gbHF94siWS5njYJ/z4TIShlj62mBbNy9mZBGVcWiNrZc8TbEZdFCKMB8KP9xRvbniFKIyN77TifYOS2QRC2/deZfvbH+5AaeEpBX7XvKMc02JlHzrNR2C8njwj6KyXWOctVIVz8mCKRiwgyENyR1npL2t3OWLd09aG9shQ3WvBIuU2OlKb8tDfYZ2+5C5HnfcJjnnGtpairyTVHpr7aCzL+9MeUOuiKkbtnIMkcl0X6+DydQCP2f3+x6XdxErCwQmp3iG+7gWdhEhWulhCIZzUN+IXUyueyEIjNOZUn3oWuiHEMPWm7W/vfBKmBJiV47B+rYRmU23Wa9WTMZQ+VTBSy1YloJ4zyUNEa/S6XbGT14o+Ykc3Mf7gHfwUg17pkLyq740RWzN8mFa+0JOe+uelS7jbl9OJ9PAyt7Fl3ZSxvx4CMNqKybDLeZOoxfu4n18JI6DYqZNbsJXtd0eGQPerIubdpqOLFG1phsKXBxwqZ/uxpLu2lRjAuZASOVJVuJbZyjF4UqlUk9fqtNZQurtRSauPioxu6FlcJkJ5RVehTGrO8JxzdKsdYq0Q6kIOpTtj7KIxyzjEmQgriSX8ET+5BRwppp5WKTHc32v+5JQNJDBcL3bX0vmtC2qY2pz69MWPTZyGQ1WONH5yEPRmbkfTzAp0UueExiv1pLowK4iUskdnuSrIllD3lVNcDAZQvlxI+yjoHVSVFrhYjoqYSwoG1pCHH8qD5FnTQVSMKIV4BQ81Uh04DoviUQlHqy43NNBsavPSms0bN7cVo16RPWTRKr7daBh/YGgN9ujlt6LHstP9Y1cb6szoKqiiixuD/UHEMtyebv73I4s+7snY9e9xuR4GltDvvKU+7XIj6fgQuitFU+xLHD+FuS8EDh8l7gpHi3jTA0pb2q2KB8y1V3Vg06HVEqWeHbJIoRoWMgKXaJF2hdr/nQSr4eEoxBvs1XAQAENiO6xuH9oRli7uhnU5mjBBmg/UKAsduO1IaAlUk7Y4UhFCdWHxjVs1vR4dPrIkTyrjIMNEsKHrX0mokMhBoHGd8yxxYuRPu0qOd7scKjcsXS6UfZxMMlgCNV2UnpgLhxbc1eZGwPtTB5EGpA2Wd5uzIgk8Apl2l0i6/1JCil1B5iTSVNxC8JrcXJq8JKIR7WzHMQATzqW3oaojrO3sjnmIXdaOkhzhqk1e7ZuyrlwjgHPwjyD20rIouk+sO0zRSV7W6Q7eWhqX0XrC7KOnCY5Hi70NNZBR8CttGRHxU2yZk2Uwvq4PBIb60LejfnvOkbGIZTnRQgNGxVBHTxoIHR8lNu7WKwM15FrMLwekGVx9HqVOnm+vLZq0U17qtOCvcpoqQEha/5KrA05iz2+sqaS3i9Nc1QQSy9b7L5vKxHm1dtFmqqEHktte7wd6X2VaBtXOqvaZjLlvXyl+54Wr0UHlcQJca5wtp5iODJTMmCXmzHwb3e9aO1wt5R8fjrLPStfhSub9MZWv1gt3zLorYzWcaduTiKDOBGcIy6B8XWN7ZMVeqYs5yRUeHSIiAg9ORIhsWYEdyGVCye2WKal4jo3C61XrB5th+x26Kll4ei+IxjstE/cmjYL7XyLteqIni1Jjw47nD/xmi5uJoo6CFjPQFF3OeXJ5TytulrXcOFIVrZy26Hmnr9IkJTumJxMj4FJk7JdmzJ6VLc8Q0VnlJQYnQMzs84h+P7I+J1/BLjpdey9xGi66fqaOnCUEhmZHl0D4VbAZpckTbfac2zrVFl7jw6kVKiFRkJpFjvQGg+pcfR3nVqBg4lgq+z+YmXG5UbbG+0eNHC/ZIqVpfP3grIwEk/hkPbtNtAYvtD8UwWGCcNuNd/UOxhBiO1yF+G8ayis152X8ZhE20vNV/LALU+RMLCbUTW2jiEwkwGhN9i1ZaFfI0xS0dGtFjYS3jp0Cw5ijG4KIZPY57acVmc6Y+8Tk05hdb0crU7Mh3S1M4kVeXa2KkoauzFktb5VuTMjUgpSTGUVgtGph/Pl1o2OG5VZEliGmyhFn6f1QVnG4RovwSgcdemxJmlUOzeBtvOOuC11azAEZugtxg8tuSrE+HAPtNRUhwrn2ClY80cpydZLzBRoMEdAQ7szbt6xgTA1PEiODcqlNmBwOggrQWcAsF126+N9PGsmJZ2L1omCfn10M3p7Qiu7ren9RhMnhk2v+zFzs9LZ4UJXl9B0zCR2N2DHu+BarVdpSVyThU2kHEIWwz6copCRrXEv5pfbGiFv6k08YuaKSG0pCtJDXOlrZdN4/gnV3XV/aZo0EiN7DJqYUll/osW9W1ApZ25UNyVj1dic6UBCGk9XhNXFRFuEQK83Jr9mrsZEaGjobbMB24QN2Y4xQkojZI1IMxw0QuiRdiC5G+xbnE8uT9uVKZwUbJXknbxNYTIYb0pNLyW67lY0eq9OB22q9W0L4VQVC8UpPpzUDC2xpRL5OXFUjO6eQuNhx/s1Re/sLkDru0Tnk3BweFppb3fP3lgNKWJwgVeukCI4DQuHuNmvLkS+4rFhD+f326WU78QptbGYRva8ljehEizFY6CkDLFZH09F42U2HN+8EGsusAaZEZbjpd/B1/4oO0yKk1c+dyncoZYJWjlqu5ruKdYSoY5fg5wUPDbtU0Q6RggW+AYNw7DsedQFqu938STdWw8ervAWFexVyFmIRBBcp1yQY5RtNlC72lslWmyygdjl1BDESOBMUS14jngLK1rmFSiDWG0rxprQgrju9rJ9ZqahI/cyVNNbXDkjzWRP9yyvlI0uTE7DrFC5OJgQSaDC8j4FnWzbeDLUvcXFIEhLubHiUW9Xqr0inXjHhtndG+Br5jmFa6f2vXQxahe5StHEI29dfHq/LekR38kZnknuHsMsN3JoHaUgAi+lIFqudmnukOdWXSZOsbeg2qt7FObYKBzPkbY2Y40BY4Nysxz0kg2Rx5+k7VBZZ/emXc8Eq9xrwzPa6m5mLSUtb8MkVhzC5FiT7oUGvgcXL3eSAyf18qSQqxrbkJSeIMEhZKIm3F+FaFixN65fyR6iZp2wvWgDl29tQD8i0ll+VBhVJV65xidqP+VYWlgGxxvPqkh4dBUOEJCnZIqmSkenu3H3niIMQCjsVjHPMQwZBeoesimHSHJ1bDZkfmR66OKDaqr1aA+EpfslA6tHH44dob07Z1SA0p5M6tS++nQ1JDSph2uShLiyVU9KSagrbZIvyl092+CcI0cHPaWI+2mZuR7dMa1Qbym05E7XODXJVVflLKqntEndTmpyro93z/XlWnI6akva/OV+9W03QmWSL64u2qKcMmDaZKQqiU+3foUZaXQ1M90z+MHfnFPIcEzBFFZbpLCDALB6MqlSUW/BqayuPfl6ZEMtd1udokwVv21iDiYOaHmJ0jzEYcEXYu++oY1K2d88y13GlypkDjaLOJgn1IctbbpY1VUKYXQyulxhE8ZdXMTiDxQ2wGYB6nrEYdEwIVRqLhN1hhxLwlc7pkPAKIhStrykC6JCoW3otZ3h1Ba52/nqBROKXtqStBThBWFdw2LjWuC4tNzIvn71S42sPRfeZu7glnR52HIX21yNW3EqbVKPd9l0bHvBbSsG5s8uwU6mnbk3Z32dT8Fin2mesaUNcuvcFP+i3i3QVW44RhCFsczGWhe5T+4Vws6RiohrBuIppDucRf7m9evCUfSV1W+32yjTymN73y5RJsFSJyQsDN/5HGFDIyqFCXVJV4RGnK4mtQS4wd4NIqwjdOvo2/uBLiuU7W4u1uX7mJnKqwxAOOWXPLEmt+SaIy+Bi0q1F+VjDvXLLZ/DXYfpkZPSiGVeIOOiEvZGROkSBJg80Zl4rFNIYQVw0D+bokI6Ckrv7jcsqQoDsWzyql6XapXsLcbo3H7ab2jXGNLqvAHTfHqAhtuW6TxC3zcD4V+8gL1M3dlp1OCMQe61tZh0cz7LKQNtujXcogDwoPVBR8Pa0OCoZ5YKN8aMRt1XUntMdtf0UrDjdumYauwfdsr8t2LlDCvpSuIrgJXldZ3ly0amz65pwzkrG10/wWJ5DeiRbPrGx5e0di9XsHNm4iDxOU2lE64L+fgsRJx6gABe0x3NDUy3DIQElbv19jLSt2JUCDRFmiXXYu01JYsDOMlKe53BiYZoXfKErZZS2qmr3aCTYUsM+z5Zakqm1gLHjfv1cqlej21Tyt6kWbZwyE7GAN0UsXFpbkQbJ4uCA5WE2uAbqS/v0wG5nlv8NBQ2hqGMZBPCTlUBXcZJV5/CtV4Jpz1DERFt+cI6v7TcCm7iFLOmoejzSN9BN2g/FeuVh6+yoFIbtDsKNK8GeRNEpVAbGeNcyEsXYWJbkiHwmaKxpEiwC2qNo7sDONXZJdkdkgPdkZvoSii9ZXdFd2ohDoBKIveSpp9ozJSqpVjqYZnSVnhKPThGFMzrcX3jQm5PwaYhOvfpUjJkfyeBDhGzzWVrjtbtghdwWpvLwDwYGoeiNNz2OkO2SYZi5TaFMOmKW/feQ5OaTM3ckQ0hxXGeMZl25ci4rq8v/M7IWj8aeUDwRe8IG+yquIrLBsfeHkj0OKHWUQmZ5qgIDHXOVutdUN9bx7Vzp0dOBA2DA7BKSQ2UeXQIGz7CK5RNQTgyYm1xjfHSGRjCYJUl2V77C1JQK3+nkJB+TDC+4VRfvLlbCkaJVRVR0Io6Zb0Vc8W0IUxoyDUAUXzJ9WypwBQ4CijaMiCF7hgbNBocokY9MF3P6aKL1REvr9frv/3t7d3btwd4b//6r9bmxzz/z54oPR8Mffn1yeMRpWs6Hx+6Pv4PbPvl3Vtlh8Cy53O0Omn914OovzxFe/9PP4ycxYzPn4Z9eQb9fLzemP78U+q3MHNaIGL8XOfJ49coYIfV1vPPLuv5l7k2eP/jU9en5jkNeeXaZt18bvLPr0exYTb/xMR1QmDQ66v/erj47s15/f7pM0asPrtVMXv7+g0DcBL7gHzA3n7/v9vbdhANLwAA -->
