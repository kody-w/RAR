---
name: "rar-cowork-cookbook-ppt-exec-establish-support-procedures-and-policies"
description: "Builds a read-only executive PowerPoint deck on support procedures and policies status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_establish_support_procedures_and_policies", "rar_sha256": "f5d26b0c88c62c5b753b9522c921b44bc8c338676ee404d5a5008bebb189e152", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_establish_support_procedures_and_policies`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_establish_support_procedures_and_policies_agent.py` and in the RCI capsule.

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

Establish support procedures and policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on support procedures and policies status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-establish-support-procedures-and-policies
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
      "description": "Prior period to trend the current numbers against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to pull from, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-establish-support-procedures-and-policies-2026-05-24.pptx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_establish_support_procedures_and_policies_agent.py` and embedded as the fenced Python below (sha256 f5d26b0c88c62c5b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_establish_support_procedures_and_policies_agent.py` first:

```bash
python3 ppt_exec_establish_support_procedures_and_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_establish_support_procedures_and_policies_agent.py   # or on stdin
python3 ppt_exec_establish_support_procedures_and_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish support procedures and policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on support procedures and policies status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-establish-support-procedures-and-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_establish_support_procedures_and_policies',
    "version": '3.0.3',
    "display_name": 'Establish support procedures and policies Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on support procedures and policies status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-establish-support-procedures-and-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-establish-support-procedures-and-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ea92b3c678178ffb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/establish-support-procedures-and-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-establish-support-procedures-and-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to trend the current numbers against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull from, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-establish-support-procedures-and-policies-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for establish support procedures and policies reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on establish support procedures and policies for a 15-minute monthly review. Produce 'ppt-exec-establish-support-procedures-and-policies-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads establish support procedures and policies data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on support procedures and policies status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.', 'example_request': 'Build the executive PowerPoint deck on support procedures and policies for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-establish-support-procedures-and-policies-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to trend the current numbers against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX on establish support procedures and policies status for a short monthly review, sourced from D365 ERP without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecEstablishSupportProceduresAndPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecEstablishSupportProceduresAndPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to trend the current numbers against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-establish-support-procedures-and-policies-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecEstablishSupportProceduresAndPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
