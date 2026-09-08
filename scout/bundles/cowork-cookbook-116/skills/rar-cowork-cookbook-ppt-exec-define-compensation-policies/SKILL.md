---
name: "rar-cowork-cookbook-ppt-exec-define-compensation-policies"
description: "Builds a read-only executive PowerPoint deck on compensation policy status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_compensation_policies", "rar_sha256": "3177f0fcbe4cf6a30660fc9e9a33cb4f4be42e1b93adbdc391db875717e30fb6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_compensation_policies`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_compensation_policies_agent.py` and in the RCI capsule.

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

Define compensation policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on compensation policy status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-compensation-policies
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-define-compensation-policies-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_compensation_policies_agent.py` and embedded as the fenced Python below (sha256 3177f0fcbe4cf6a3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_compensation_policies_agent.py` first:

```bash
python3 ppt_exec_define_compensation_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_compensation_policies_agent.py   # or on stdin
python3 ppt_exec_define_compensation_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define compensation policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on compensation policy status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-compensation-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_compensation_policies',
    "version": '3.0.3',
    "display_name": 'Define compensation policies Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on compensation policy status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-define-compensation-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-compensation-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '782bd85b45dd4b3d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/define-compensation-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/ppt-exec-define-compensation-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against in the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-define-compensation-policies-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for define compensation policies reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on define compensation policies for a 15-minute monthly review. Produce 'ppt-exec-define-compensation-policies-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define compensation policies data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on compensation policy status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on define compensation policies for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-define-compensation-policies-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare against in the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX summarizing define-compensation-policies status for a short monthly review, sourced from D365 ERP.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDefineCompensationPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineCompensationPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against in the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-define-compensation-policies-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecDefineCompensationPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
