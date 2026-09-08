---
name: "rar-cowork-cookbook-ppt-exec-develop-new-products"
description: "Builds a read-only executive PowerPoint deck on develop-new-products status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_new_products", "rar_sha256": "023dacae02b9c1b51415c534059e4563c0fb0ae9d75bca10fb7b436cf77a6c79", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_new_products`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_new_products_agent.py` and in the RCI capsule.

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

Develop new products Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on develop-new-products status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-new-products
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
      "description": "Dynamics 365 legal entity to pull data from, e.g. USMF.",
      "type": "string"
    },
    "meeting_length": {
      "description": "Target briefing length the deck should fit, e.g. 15-minute monthly review.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-develop-new-products-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend comparison, e.g. monthly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_new_products_agent.py` and embedded as the fenced Python below (sha256 023dacae02b9c1b5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_new_products_agent.py` first:

```bash
python3 ppt_exec_develop_new_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_new_products_agent.py   # or on stdin
python3 ppt_exec_develop_new_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop new products Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on develop-new-products status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-new-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_new_products',
    "version": '3.0.3',
    "display_name": 'Develop new products Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on develop-new-products status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-develop-new-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-new-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cd76853de0f4540d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/develop-new-products'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/ppt-exec-develop-new-products', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'meeting_length': 'Target briefing length the deck should fit, e.g. 15-minute monthly review.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-new-products-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend comparison, e.g. monthly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for develop new products reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on develop new products for a 15-minute monthly review. Produce 'ppt-exec-develop-new-products-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop new products data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on develop-new-products status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.', 'example_request': "Build a 15-minute exec PowerPoint on develop new products from D365 USMF for this month's review.", 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-new-products-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend comparison, e.g. monthly.', 'name': 'review_period'}, {'description': 'Target briefing length the deck should fit, e.g. 15-minute monthly review.', 'name': 'meeting_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX summarizing develop new products status from D365 ERP for a monthly or periodic review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDevelopNewProducts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopNewProducts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'meeting_length': {'description': 'Target briefing length the deck should fit, e.g. 15-minute monthly review.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-new-products-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend comparison, e.g. monthly.', 'type': 'string'}},
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
    print(PptExecDevelopNewProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
