---
name: "rar-cowork-cookbook-ppt-exec-define-product-policies"
description: "Builds a read-only executive PowerPoint deck on define product policies from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_product_policies", "rar_sha256": "5ba8943fa2beee0e32c5d3b10b3b982de98bbf33fab41ad9e497cdb1216d5add", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_product_policies`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_product_policies_agent.py` and in the RCI capsule.

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

Define product policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on define product policies from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-product-policies
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
      "description": "Prior period to compare against for the trend chart.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to report on (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-define-product-policies-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. a 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_product_policies_agent.py` and embedded as the fenced Python below (sha256 5ba8943fa2beee0e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_product_policies_agent.py` first:

```bash
python3 ppt_exec_define_product_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_product_policies_agent.py   # or on stdin
python3 ppt_exec_define_product_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define product policies Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on define product policies from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-product-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_product_policies',
    "version": '3.0.3',
    "display_name": 'Define product policies Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on define product policies from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-define-product-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-product-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ab6d8a95ebca75f0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/define-product-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/ppt-exec-define-product-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against for the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-define-product-policies-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for define product policies reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on define product policies for a 15-minute monthly review. Produce 'ppt-exec-define-product-policies-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define product policies data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on define product policies from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build the executive PowerPoint deck on define product policies for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-define-product-policies-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare against for the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX summarizing define product policies status for a short monthly review, without modifying any ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDefineProductPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineProductPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against for the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-define-product-policies-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. a 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecDefineProductPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
