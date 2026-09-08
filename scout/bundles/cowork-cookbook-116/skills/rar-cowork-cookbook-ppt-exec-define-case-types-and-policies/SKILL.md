---
name: "rar-cowork-cookbook-ppt-exec-define-case-types-and-policies"
description: "Builds a read-only executive PowerPoint deck on case types and policies from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_case_types_and_policies", "rar_sha256": "5619336784d46c6600dccf70da7d39d4921b916dd8f0693577dfa325418fbe88", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_case_types_and_policies`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_case_types_and_policies_agent.py` and in the RCI capsule.

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

Define case types and policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on case types and policies from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-case-types-and-policies
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
      "description": "D365 legal entity to pull from, e.g. USMF.",
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
      "description": "Target .pptx filename, e.g. ppt-exec-define-case-types-and-policies-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Intended briefing length, e.g. 15-minute monthly review, to size the deck.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period to compare against for the trend chart.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_case_types_and_policies_agent.py` and embedded as the fenced Python below (sha256 5619336784d46c66…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_case_types_and_policies_agent.py` first:

```bash
python3 ppt_exec_define_case_types_and_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_case_types_and_policies_agent.py   # or on stdin
python3 ppt_exec_define_case_types_and_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define case types and policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on case types and policies from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-case-types-and-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_case_types_and_policies',
    "version": '3.0.3',
    "display_name": 'Define case types and policies Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on case types and policies from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-define-case-types-and-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-case-types-and-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '10f5e2afec633f1c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-case-types-and-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/ppt-exec-define-case-types-and-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull from, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-define-case-types-and-policies-2026-05-24.pptx.', 'review_length': 'Intended briefing length, e.g. 15-minute monthly review, to size the deck.', 'review_period': 'Reporting period and prior period to compare against for the trend chart.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for define case types and policies reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on define case types and policies for a 15-minute monthly review. Produce 'ppt-exec-define-case-types-and-policies-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define case types and policies data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on case types and policies from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on case types and policies from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to pull from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-define-case-types-and-policies-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period to compare against for the trend chart.', 'name': 'review_period'}, {'description': 'Intended briefing length, e.g. 15-minute monthly review, to size the deck.', 'name': 'review_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready PPTX summarizing define-case-types-and-policies status from D365 ERP for a short monthly review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDefineCaseTypesAndPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineCaseTypesAndPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-define-case-types-and-policies-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Intended briefing length, e.g. 15-minute monthly review, to size the deck.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period to compare against for the trend chart.', 'type': 'string'}},
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
    print(PptExecDefineCaseTypesAndPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
