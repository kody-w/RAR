---
name: "rar-cowork-cookbook-ppt-exec-establish-support-procedures-and-policies"
description: "Builds a read-only executive PowerPoint deck on support procedures and policies status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_establish_support_procedures_and_policies", "rar_sha256": "f5d26b0c88c62c5b753b9522c921b44bc8c338676ee404d5a5008bebb189e152", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
