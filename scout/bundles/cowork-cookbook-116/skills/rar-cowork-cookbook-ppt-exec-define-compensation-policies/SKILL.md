---
name: "rar-cowork-cookbook-ppt-exec-define-compensation-policies"
description: "Builds a read-only executive PowerPoint deck on compensation policy status from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_compensation_policies", "rar_sha256": "3177f0fcbe4cf6a30660fc9e9a33cb4f4be42e1b93adbdc391db875717e30fb6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
