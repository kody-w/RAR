---
name: "rar-cowork-cookbook-ppt-exec-develop-program-charter"
description: "Builds a read-only executive PowerPoint deck on develop program charter status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_program_charter", "rar_sha256": "16fba68279040220cbab6a12c7f0c35b3af5878585d4214c9c451a264ab54581", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_program_charter`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_program_charter_agent.py` and in the RCI capsule.

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

Develop program charter Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on develop program charter status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-program-charter
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
    "comparison_period": {
      "description": "Prior period to compare against in the trend chart.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to pull data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-develop-program-charter-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. 15-minute monthly review.",
      "type": "string"
    },
    "topic": {
      "description": "Program or subject of the deck, e.g. 'develop program charter'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_program_charter_agent.py` and embedded as the fenced Python below (sha256 16fba68279040220…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_program_charter_agent.py` first:

```bash
python3 ppt_exec_develop_program_charter_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_program_charter_agent.py   # or on stdin
python3 ppt_exec_develop_program_charter_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop program charter Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on develop program charter status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-program-charter
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_program_charter',
    "version": '3.0.3',
    "display_name": 'Develop program charter Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on develop program charter status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-develop-program-charter',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-program-charter',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '474fa672422ff0b7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/develop-project-strategy/develop-program-charter'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/ppt-exec-develop-program-charter', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against in the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-program-charter-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'topic': "Program or subject of the deck, e.g. 'develop program charter'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for develop program charter reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on develop program charter for a 15-minute monthly review. Produce 'ppt-exec-develop-program-charter-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop program charter data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on develop program charter status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions, and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on develop program charter status from D365 legal entity USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': "Program or subject of the deck, e.g. 'develop program charter'.", 'name': 'topic'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-program-charter-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare against in the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready monthly review deck on develop program charter status sourced from Dynamics 365 ERP data, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDevelopProgramCharter(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopProgramCharter'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against in the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-program-charter-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}, 'topic': {'description': "Program or subject of the deck, e.g. 'develop program charter'.", 'type': 'string'}},
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
    print(PptExecDevelopProgramCharter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
