---
name: "rar-cowork-cookbook-ppt-exec-develop-new-products"
description: "Builds a read-only executive PowerPoint deck on develop-new-products status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_new_products", "rar_sha256": "023dacae02b9c1b51415c534059e4563c0fb0ae9d75bca10fb7b436cf77a6c79", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
