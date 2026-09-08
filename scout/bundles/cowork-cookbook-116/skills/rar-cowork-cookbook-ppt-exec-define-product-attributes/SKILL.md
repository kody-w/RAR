---
name: "rar-cowork-cookbook-ppt-exec-define-product-attributes"
description: "Builds a read-only executive PowerPoint deck on define product attributes from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_product_attributes", "rar_sha256": "126e457527ef8dfd501652fe44103193c0bf35c2b26a8d32115a326f847fafa1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_product_attributes`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_product_attributes_agent.py` and in the RCI capsule.

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

Define product attributes Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on define product attributes from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-product-attributes
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
      "description": "Prior period to trend current results against.",
      "type": "string"
    },
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
      "description": "Target .pptx filename, e.g. ppt-exec-define-product-attributes-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Meeting length the deck is scoped to, e.g. 15-minute monthly review.",
      "type": "string"
    },
    "topic": {
      "description": "Subject area of the deck, e.g. define product attributes.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_product_attributes_agent.py` and embedded as the fenced Python below (sha256 126e457527ef8dfd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_product_attributes_agent.py` first:

```bash
python3 ppt_exec_define_product_attributes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_product_attributes_agent.py   # or on stdin
python3 ppt_exec_define_product_attributes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define product attributes Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on define product attributes from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-product-attributes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_product_attributes',
    "version": '3.0.3',
    "display_name": 'Define product attributes Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on define product attributes from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-define-product-attributes',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-product-attributes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd1849f630fdf3af9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/define-product-attributes'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/ppt-exec-define-product-attributes', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to trend current results against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-define-product-attributes-2026-05-24.pptx.', 'review_length': 'Meeting length the deck is scoped to, e.g. 15-minute monthly review.', 'topic': 'Subject area of the deck, e.g. define product attributes.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for define product attributes reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on define product attributes for a 15-minute monthly review. Produce 'ppt-exec-define-product-attributes-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define product attributes data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on define product attributes from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build a 15-minute exec PowerPoint on define product attributes for USMF from D365, with charts and speaker notes.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Subject area of the deck, e.g. define product attributes.', 'name': 'topic'}, {'description': 'Target .pptx filename, e.g. ppt-exec-define-product-attributes-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Meeting length the deck is scoped to, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to trend current results against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready .pptx status deck on define product attributes for a monthly review, sourced from D365 F&SCM without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDefineProductAttributes(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineProductAttributes'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to trend current results against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-define-product-attributes-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Meeting length the deck is scoped to, e.g. 15-minute monthly review.', 'type': 'string'}, 'topic': {'description': 'Subject area of the deck, e.g. define product attributes.', 'type': 'string'}},
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
    print(PptExecDefineProductAttributes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
