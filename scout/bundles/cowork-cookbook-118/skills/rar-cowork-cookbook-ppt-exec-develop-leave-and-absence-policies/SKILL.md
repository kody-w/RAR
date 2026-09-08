---
name: "rar-cowork-cookbook-ppt-exec-develop-leave-and-absence-policies"
description: "Builds a read-only executive PowerPoint deck on leave and absence policies from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_leave_and_absence_policies", "rar_sha256": "85a21a6017db2afdf67ceea2a4513b9efb81377e2492e8ccf96f1eefdae79fc2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_leave_and_absence_policies`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_leave_and_absence_policies_agent.py` and in the RCI capsule.

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

Develop leave and absence policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on leave and absence policies from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-leave-and-absence-policies
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
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-develop-leave-and-absence-policies-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend chart, e.g. monthly review as of 2026-05-24.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_leave_and_absence_policies_agent.py` and embedded as the fenced Python below (sha256 85a21a6017db2afd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_leave_and_absence_policies_agent.py` first:

```bash
python3 ppt_exec_develop_leave_and_absence_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_leave_and_absence_policies_agent.py   # or on stdin
python3 ppt_exec_develop_leave_and_absence_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop leave and absence policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on leave and absence policies from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-leave-and-absence-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_leave_and_absence_policies',
    "version": '3.0.3',
    "display_name": 'Develop leave and absence policies Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on leave and absence policies from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-develop-leave-and-absence-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-leave-and-absence-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b255a8c7d399a58e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/develop-leave-and-absence-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/ppt-exec-develop-leave-and-absence-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-leave-and-absence-policies-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend chart, e.g. monthly review as of 2026-05-24.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for develop leave and absence policies reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on develop leave and absence policies for a 15-minute monthly review. Produce 'ppt-exec-develop-leave-and-absence-policies-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop leave and absence policies data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on leave and absence policies from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on leave and absence policies from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-leave-and-absence-policies-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend chart, e.g. monthly review as of 2026-05-24.', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready leave and absence policy deck from D365 F&SCM data for a short monthly review, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDevelopLeaveAndAbsencePolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopLeaveAndAbsencePolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-leave-and-absence-policies-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend chart, e.g. monthly review as of 2026-05-24.', 'type': 'string'}},
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
    print(PptExecDevelopLeaveAndAbsencePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adeb1pbmX1G/9SFJYVuIQQLXums1YhIIEJOY4rscZpCYxCCBUvnvfZD02sm9udWd6v7UshMhOGfP+9l7+/Drmz/0Wd2+fX4zYr9a8H5R5FncLvwqWtD1rW7P4Ks+B+C/RVhXfZsHQ1+33duHtyjuwjZv+ryuwPbtkBdRt/AXbexHH+uqmBbxGIdDn1/jhVrf4lat86pfRHF4XtTVooh98GBm4wddXIXxoqmLPMzjbpG0dblgpsov87BboGt8werqIvJ7f5HUQDSwN/WLRVz1eT99WNzyPluAyyL+sNirwodF38ZV9AEIEn1MCj/9sPDDWcjuya1pwNN8XHRFDjRYNMXQLbom9s9A66ru4+4T0C0e/bIp4u7t889///CWg+u3z7++hYXfgVtvatOzQDcmvsZF3UizJlQVUU891JcagErhVylY3kzAxBX43cQtUKAEt6I4Wbx+/djFRfJh8e//fr75bdr99PlLtXh9vrzNf/ShWvRZvOhrv+vjaBH6jR/kBdD904Iqbv7UAVX7oZ0VXHTAQ1X66bnzO6W6Wfxtfvbjk8mnNO5//PJWAxH82TRf3n5aAMt+eWuH+frTTKX58adPxey3H3/6TqcbglMc9jMxIPWnr6/fL7Jg4felebL4aqgs/eLVxmHexID47/SbP0/RX+ReJvn6XPxj3XxY/DnlWZ+/AXmfMRgAun9OFtgA7Hz7dAKx9+OLR1tf48oHnvrxp39FNsxAlBZ51/8f0f35STgDgQ+s9TLJTx8e7vv7Anrp9o3mv2bbgID5K5qA5e/svhnqX9F+ePYfSBd5BTLg3Zd/Su7PNkB/W/z8L3X7rzZ8WCRf3pi4AJDQ+kERf178+giRn3+Ivt/84e+/AdL/WzJGPbThg8LX0q/yJO76r19//qF73P7h7z//MDQgimO//Dq0xZ/R/DO7Pvj8wYKvVT/+cS/gf6zOVX2rFt9yaPFr3fyP9rdPC8sHyPL9fvd58ftMnD/QYlbinenTBL/Lxg7I+js7/vT2G4CgCmgzPHEM4Me//dtCzsO27uqkXxhhPfQL4OA+L+NZeDPLuwX4O6NGC0Cq7XJg2Nc6EP+zh2eJ62Txy/8MHyj/MXyh/LJp+q8zcn+NnvD29YHUXwF2fn0h9dd3pP7l08IELOo2T/MKILJOqeqXyk8BMs/smzbu4vYKICuY+vgjyOyP88Uirxa//AUuXx8EPzXTLw8Az59oqNPCjITdUMSfZp3tLK5eGoagkD1rT7wo6hAIluQAy+eK0NUFqDr9bJ/unBfFIsoB1oCCNj1oAxt+non98ssvgd9lX6ondKOLZ6XrlmDBN3EWHz8CDZMiT7P+SxWHWb344dffflj85+K/2vUgPvNQQS15eQhIKBoHZQEybijBMuA84G4AJw8P/frby86ATAWKFPBnnsx1ct4MIvYcR+9GN3bURwRfL4IYGBsYumzqtgf1YJH3nxZCsvgmL2A6P5orRlZ3c1WeqyIw+wSo+kCdb5YEJXHRgbDsElBqhy5+cP0laP2HiCVIfb//ZSHTKqhPdQH+N4v5WAQ211UOzP8tJJ73AZH2h26xfSfxaaHMMbpo/NZvstZ/8Uj8p1/miv/aDoj7iyq+fanmihzPpnokzNM8YBGwTPhy6cfZ56BlKQE6RN0778caf66i5qOatl+q7pUMfju7IgTFATBNhzyaS8R/vEKqy+qhiB72A5LOlF5eiF5eecTgqyH4r3ob9s96Imbuib4MCLzCFv8f9VGzSSie11meMllmwSqm7j5dNXeSs0ufzSfg/hDokZbfu5t3BHsH8i9VkYO4a6f/eK58OPi15gmOAxAVgJD+oA+iC0gy030E/xzMbTubxf9SvVcMoNLiAY+zIesQZNIcwO8M56fvkmYADubf37uHR7C00WwMEOCLZgiA2RdJHEeBD1zTZ7MD370KMiGek/mW5WH2B61m84OAA/Rnb+YgJUFV+fQNxZ9P30X/w8ZnkzRveTSQA8jf9kEAyPEIhNlNs1OBeP2zcQd6fn4QAWqUTT/rHoAMApo+b8ZtfBnyLu9ntHzaNW4AaH+cv5+aznfjsQFJA4wFUqMZgHUfyTTjTAlaICADiE6QW2VegZYAGOVlhAdBv5yRASDvq2d9UnzcfikUPzJwrmXvG2dF5j1ze/CMar+afg8g5p+FCaBXzisefP8x0r5xm2nPINoBIAQc358++4hPz1bg2Wss3ul+/qfJ6Me/Njw9ivvxjwHweZH1fdN9Xi6fBfm9Hn8CELZ8ytrNtfnjjAYfX1Xz4yP7PwJ+H1/Z//E9+//A4qn958VfE/MPJF5p8nmx+gR/gudH0ivMXh9gFfrj1v2IzU+/VHr8HWsB+7oEcTb7cALNwLfC+L4EVMe0BWAEFj8LZTfX1xso6Y/KABzypfp93M95BwpPlc5x2tW/w4NHhwBy4Om/bwUMPKp6wDuau8w0nke8R5Z08dvnaiiKD28AJeO/MNrNxaqcg7ybB0OQTqB56+dH85g4Y8bYz5d/nJEPjwu/+AQQH+BT0f0+EF8lZi6xv8uXp7JAyRBw+DCDN4ABEKNA2Zn5nGt+B4IXxO2sVD81sxbPKXDuGx8Q//UJ8f8sEDMXhd9XgUf9frQGAI0+LOJP6afF0ZC5P6X9rWH9Z8I26ApmWlH9eS6QH16AA77BkPFh8W1eABq9JrjH1F0NYDj+eZ5VZhM/tswXYA/4+rbp2789BPHb3/9MrgcqfZ3j4enVf5ROmdEGoPFs4E8gp8Zn7AB5Ac9oCOOX5n8h3T4iMLL+COMfEexB8U8NBnrxPL7NU25eR/8slh6/t2vPFY9gbsBV+34DBEf0DaIe5XlOg7Z/yVuCwMuKGfhmPou5pCSL3wn2zzI9hAKQDwrnbPjvHv1u1/oxEM7iAz/0z3+/+PUNxL4/dxKv6H9NFGA5QMiP3dwzLQFQAIbg9zOlwbP/m1njRarLfNDgAloE7iMrfw2vNlGA+EmUrDdhHPuIj+ErNCDjJCBW6GYTIxiJxEQYJuQ6WcVxEvnxhkxCBNB7YsTXuUfMZ/Fm2YBVPgLDxt8fg1vRS6+nHrPRvo02s/4v9X59C9YYWLnDOoF6fugluQqW7iYYW2fpwMRY3I6Xi2djpwytmnNDsk6P7vRcqVyn76kcoc6ILiDlxMnFbeJgKb85a3aH0mpXkZWpMP450yGITU29P508RyhNpbp3yTWRpw5HS4ZFz815ujm5drs22sm0BU2SIkXIT6Nk7Y0zdwkTzzIs+rJUQZn3Kv54kUJbPNEb9rrcjOaSz4/nstONdM+HgSmxCKJdPSXnC7ro1wgsSYIyiOcScwPOrkZcGCrsavale2LkzJRamTJya+Jyb9tcwrbXuakJc/Qme6xJePHdGhWdO+0VEWha5WszZI66axkXSbHK3rzv7KWlr1mTs+lR3ecrWOpkyXZTeL92kC2mVih6v5NXI8AhUjUJsymX0TVZMhy0OR6Pnm/bnMFaQXWgL3dlI+ptA27jA0eLiSajcC23laConaQIHC8J+YQ4eLk1cEeI05S3OM5Lj8uRvBaBmEEXjr9ptuWsseIo3s7WVk7Pu/K+tYx1IQVsFE5noWVLwXbsLVKajgRHg39H7Xq11EhpI0ql654xWORtnTcFysOcHE7DgD/KxZqF2Qsu9sio9HJXGGKQX4ZVDoaZpce4+YTqYo5c2BYajvWpU2P0cN33eHBGmSm/OArLlhNW1nCR2uoW7jq1EQ++udes3M6s5thIggffmGW5mc6msaSPJS/hF7bDWciC0/pSrjJ8qqY1wm4aBYH0XXdRB3fc03TZTu1EHxWyqg3cGrJ9INMe5Ip8ITHuxXLSkIjXni3l27GTz1ScaEe/3t2tw4ZzUllJB15kiXxZFsQg0DzimkxE9zHHUQ2v1C4LNf7Wznqfoq5IYLdefswr/wRrdb/KeufS3y9tfs5o8rwnMAzKm1NtjmRhWcU9tVB/vO2IMc4TxtoB5XrNT/N4jxrcWcnvWKtsT7A6QW3Ce7YYFW0Z7fSRU0+HG6ESNaJjnp54ZoV7ZphkdaCK5VTC0IgqxhoKdCREQ65bHrx4m5tS6rSsqY5lshQSTEPR1eXeXYn0HKtNPkJlBakFtl+FRpJ5Bu9vm0BW7kJz7EdbaqOtXieisSMtJq3o1T6lMF6Y1LPgIMQEh9QaAoYucmxb44MVw0wvW7bvHHZ7qNp4zJbfOFurkKhTtMUKz3MPqadx+VDDNzlksH1KXsOUlZcs6VIIBhCTca6j1wltyiumN4TCYemW+AlOj5DUE/xwAtDWC6QoabtabDmMXp07qkj3bbFm7IlkjC4TivBMpPCUrIjVqVGpEtUC1L5jZ5Caq6YBAkE3lDtXl93YiU14g+6E00C8j8FeQ6iW3jid5PW1dGBlR8DYUOEancV6CqMKnYPg+4Epr3dx3xBQuzpm6V2QKL7FdJZIDZlOTttjd1XXUDpwAdzylqMx3jaQhAxVpaNrjpf13YWbdXjQ0J0K9o/hIbVECWW8k2vRZbyiZPeaDg2FFzHcB+XJ5DVrz/FrAYrjFWR2OtFrFzjHMD7eJfUmjHxWKUii27HXfGuH7fJGtZjscNV5u7n6DJvc4f3Sy6G9VvQp2zO5dahoHDkKrNUUMubutC184faMDHOIUXuuNdVeXAQqcnS2S5UPMJhTGJrGIUgyzjiyIe6YJlv8kUaTXbxWLyvk6t5TUliDZtrlUUEKNxfPU2tRueiJHFOHmIwOeLzMZFqHyD1TNON2R+1C189OoXkRFOZelflcp01mJbDHU9pEXK6KVyKm6iopsywSV8itjJUTEQu79Oiwxn7J3HLR3NH7neuMI9tMo6EPUymgPelf0ev5zAWaW2iInuhnnQmSQ2qYyap2zB3GsdUKOU9NuyoC2zCm7aQzHHsUpdDQ7eOdBdjcxT201XoVgw2f0xiTbfvEG83dVDHBIJpXyugv8JHpNTjp9+sxlqxTxA802vUZGim3KVsr3DlHDvttt4augUXEZRCtQ1bFHFmGbuZBVRpLKHje2chwOd319W63o8+3neKcljqxklWG71wZuTXbraRjy0QH8ZmsrsuDria3S5LkZe9EhejUqq2qymnSXTYVlI7WKuoedjfYE29Wjjj7S21gB6Xb4Zp52Zfj/bYN76EWNIcM69bF/qSw2zBea9qU+Xu9tSk1PVIMVlBMPKahyB55XcNF4PzO5nyvUAJrcg+YXJOqIad+Y5QycmRL5tRM1pkdZXtHokwex50j7W+1gJ21WzRm7dXBTd9Z7mvRF1AHR3jcqxHk4HRaKdBhdr3D2bE2kCFZyYK07zpE03DB1c6ahF6xgfC3YjMSp1JP8ZUvQNdx7W8EhmMqmM3Z7ejuBKnD0EBx5DsbxNpRNguTKCLl4KfyySjZimOZga4938KjLTtM5CVPiNCinT3ONpWmXyMrtm3htNXEFs0bulgdBDzPbi6f7HsNsg6FvJehEd+6lkZ1oGY1QhM7ss5JhLNHGbYubNtVJaPh1FSkeV1wdi3OHvJVmNN+B9ugyTjvDB4T/Xa7q6Zhs99bhn9Yl/fGkCaJ2h2onXU4IU279hu4OHHkzTHGdG/yxDG6QJcN68j5rRmtm6ZJ6rTxsEZy79QV39h1zk1wdOHJsxdXAkJaJw22cT+0e5/gM7c5bmqPodz0MBzwJk9h0TXMu5avpuCQc/Syhh1lLTfUTTob0mpVhGIiKla7kVOZr0BI+blx9vT4BlqEi5APlrGl+L0daYqwUi7HjXtj9YGVmX1N2Fi39OVMrVfU+cgvyWJps3c+XdaZwseH5kbEw9IEq0lhP0amw61KorKwqHMpRt7cbsgy4EKEZfR0nCKLI71bnNH25bS06cuxoPZog0S7htx4bYoub82+zUq0P+otE5qBYIajr2jrHFnhjKewhIwVNCckW7WFjx6+98qKiTNu5Gp25eeOVkiNdcuDK4On0qWfeNflz53mjjxxz+pmFPmSIsObtG45pL+qd3KAVGfP1EJur1Zag9C77Zoft17OpUe5GvJVbqXXg39ud7XsIkyNB8f76XqXcapsknAvVvfY6/q11cg5XQh0vvUM61hHEnHWcSZe0m7lY40DNEZxk1wSisgVx0CutOBUk7JeSXAa4VBBXEyq1YnsDGE4J+rDeTlpMc53Do2uRKptKmLp3Uxi8EeJLwTjfFEOtmb7J0Mwte3FMVZ30LzdWMbtby6ApTyB4CqGsHsKA1Czbkik6av2otuFXYsjbZTn9XFv+Vp3dlKf3a/2S5fh7e0ppD1F8kfNQXKDXqoK5yPKodXARLIN8GK/PKvCxaXWRdqLCRRLm2hNJmWB3A/U3uAHdss6GUNQVCXwHjEqvgr6IZrT0lObi41v3tINiyUq2hJjYuowVJ3ueJkHkEQ2nuhQoTHIQLGshDzDEW4ENjIMcYvLTagK+xiTtXxY+RV+bAy7viHn63ldT7B/3CbHriBEr8zFYePtzyJIaB5F0HWl295KKRzME0dPwNtsywzUsD3RGHo9bvnYTvWy5lklv/QGt2RddEQbQrsZGW+K1Ni12yzxd1HTW+VtKJTT0g+K2wFvUekG750Vi7Bt3u6H7W1/gq2lcT6UrkFvIt5U3WuzyTLdueW7fr1N1UMkrQ8CtNo4br9puajAMbcOBnu1Ey6Qh2xdqj04ttgfyZ4n1seGICv90q69/GqS8CFsw90qtiJzHKYV7+UkmLwU6SKLR5Rdq5zb8kdX3GzHdYVkXXYj+aA/iAa+mpbdDdvJ8k1cH1eZg6mgwSh9CuKPK+hQBjUY2epyVJ2TeSAgfk+s8VEBvfehp3s5KCs6FL3zZQ1fnYulHzt72lwaZfB7HhtMo+RK1MuoksNuR3Gnn1s69DzfPV56a5rWK8yuT5JFr10kMCBqjFYXxuAOvKCz7SZgBNa429PKyHU0OWaFfadVhy1MCpP6pXs3KtE/sYZHyNySMJP7tpH8zKC4vRjSgbeBQQfhmNEJr/ZoZWpJqmfuWaRuenHxDO1yA1FgOluj0I0CztopRHhT31GBPSBoUuN41G3ZTsPcG+gvSr7bIIekpS/MzZ6EgiGXcoIal44fYwtp4GZizqy9OZWcgmjCNc+GWw9Rt8y72XmDl7FvVyaWKD68d2u/9MtxMxJSYguTf2NOES6kKq2WxZEM9xznRBJJnpWNK2m5E1Fkddas413lYL80tSo4JyrT1SEYVE6FwN3tqDtBA7rflxdusHt1B09QEpxSufcOEY+KuStaclwgW6g3j32YrKtdoHWGibZgsrjYVA3Tq12Ji0FALb0p8rExxI8ml63MLY77HIcopS6r6/5i0ZaohMx+d0Etui77uxfirdf2ROm0m3p0rjArrHon1yE90HRhaLeeMvUEfpcc6srTjAYX250mmvdmWYg6ckSSAxzABRh4VWyIdgGYMUGKbuoetwkw66fust6f127e3xLNrZILfKh6aHeXEaWbQgDgQdWnMQ1KG6YwqKu2Vgll6qXvrCaHHTQ+8BF6h1UVmdAC9Ybu1pmqHkdxNJJHH9UcrXUPAX5CLGJnwmXLx9ewgmi2oT2L98NpQPF+YMoCWm8v94Dx3eUtAIih9UuxZ1BJYY4Tih6XsKtwOi134zmS4RHJxrIWJz+/+PyorPptuaGFyxCZF4iAuGu8R1ZEL6vWbbVeLRMcpla20zVdom0irr/L8f0UrTe7wZGvSplptZPVm12iZTeG4lGWp8gOIHuyXN52SUEHIlN6w7VaO8vdCdsPCtO6RYyyFpdfe4yemg0rDhcw+seO2xmZrbJ3de0y7bikzkUI6SukPYVnjeG18nzSyPuO2HLCKT2XKr/szvfNHQ7SlWmgyl0p47xDCnGpIPCuculsPMrnfeYVkB1iIX6qA7bcVUx5cMhDiLI9CPWok8ql4MoiS2p9Aoav1QpdR7Z5EJhDAFG5ekB5L8zzTc6J2Oq4HVCivA8RCbeJ4pIHnID8e9tmNSIpVd3v9OsAxk7D9IkmsU5kyQfri8QaGnPMNXVXbU6nYJhkSI5AIwb1rQPy6n7ZBnSHMHLgWF1/X8ac3wXWvmXgbYcjd/mEJB1onglt2mUV1nlnkoCC/ASJxForxpOOjOfcaCaRdpkbDuIf9NWb9CJSJ/jEc+t15zor3GDstt1Xe+EeHbXQvI78KtMwS7PhPIRCxparZFdJxkHSoqu/7aaotXdNVagr79gtIee0WpNqPm6W15K62XGm7WWC4GhnIJXwsLmQ+raNq3K3k+9XgmGuZdoCrzTHnc1vJp+NEggjT1CO5TnkloWsAISs3Hw9CNO1mnagAyf3wX2FnIL95r6h7VzXzLufR3eyCZREIcMtgniOlJRMhHZnfVtFytlzacjEFAQT1hMof1DiOG4ptegJ9axMLXNf0dtgp+fbg0/cg0DbSMi5PLBhHXgeWvfniNj4xcQw5x1fTzsRQRlphSO2WiraVqePYj945d1dpRTkq0t3HRjHo3JWt5sQM06burpYwOgrk+NOVpvzakjDERlnncqTfgxLraSUZdWR68jDycA6wgGrEui49JvofoI205734g0Jm/jdXZPOhGUEhmowWhFTf0D7Zh1M2DoPuivTAyh3RT+pzG0FpvmkCeOChOECwqwcpbbXSZFTE/Q6ftDLrnefNifncnX1Gq6cSlVCPYwl9RjjLBTtIyg0yI4lLi02EVcqdZAwjTz6Im/2saAcpTWJCPYNoo9eoQa9QQZwMFZ46NgUH2jDoCVUT58Td4TumMCBkb4+Cm4ybc31/nT3JjC9xJ7A3ZaYSI8yW5zhzs7W+oiPgjp6XLPabBviWCKYiUTH9Y3sInvr8kW8ajwBFZf7gczblXWV4l2QUnA06hVW45ShwPx0wPwlt132VHQiiYPO28drWDAYEcOJQNwHXeltXAy5TAvbwO5RO8EpZOqpqcVWQj9Fgp42Tg9hfeMUldwHewQNbA5tlwyyAg2j1+6O6jTevYKIylXWnstuxFApvIUVfb1vNNxE0R15b0XnQGpgRtmvQd5FxGV/63J9CnfwiihIBCuuocE0G92WxGTVUGVmTLBiEBwuEHTeXOG+FwgDCcrGa5Z0eGXU8+GQ7KSr5Bb+6hppAEqXFswQlxAWSfYYKWRWLhWi2W5I/BYpV1yaLvch1GGtNHalqIibsyZDrm2mFd2G1wQqyHu4DvfUUvEPbRLFadhj64I8BX3bH3H01JKDbaOVQrqW7KkSXhdDF597ZN0wlTnUUe6Q/GpDG9k2bwNe95ATNYIhGlZb/6pAwjUovKvjdGa5nYI20kjfuYLmKYHZ62SJYCyjA5+rgp0RDdMJ7aUzFGNisAv9NL5pctj15JaWtnEdsdgWp9AJow47vSV2U9LyHepBfufh5n2tQQmocRjfEbK3Ar3uzYE1uNwhiFgD0FEp8rixrhnOJU4/ikk8xWv/vt5cInoZoT6/XJUIM6B3vF26ttaoJH9TBnR1qp2ESoMedI0H9HwMYsSYSGNfg7G1tbH7VVrufXpzxXwxrxIVs5PekePeu6BUhB1IyN4UwaD6DpMU8VTl17WXBYk8ltiJxDRy43spGQFoDG478x7wbbi/tlccKSjkCJnD1hzxmqUsGiUq7sDCN05XmSPHcpDWhmklbhFrtauwAm6l2GTDaAqI/iwgZ1yoLB0OVShNaFqM9spd2hRMHLHxNdnwwfaaRVdks+ysdddvmWSnqoMi95uLhR/2p1AbivQUxZuC4HohkSEaTGzFUTRHSQOTS7nLrio5DB5EJOGSwgkep7BwjMtrvmavyEXfpwR1OSVkGVbGkr4Vpyvh7722qMbyukuXxO6MppHBNTRFUX97+/D2/Xjv7b/zMtl8wPP/7CzpeST0/mbI4wgz9qPPD16f/1vS/f3DWxvmQLbnKVpXDOnrEOofztA+/oVDypnQ9Hxr6/2I+nn43fvp/KrzW15FQ9e309cOZOrjQO/DWzB081uR3fzibAi+/3Ay+1INXGZ5G3/t669t3IOrt/mNxfkVkDjK/f79Z/o6XPzwFr3eSvqKrvGvcdvM+r7eMABqop/gT+jbb/8L2mt+R50uAAA= -->
