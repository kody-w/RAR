---
name: "rar-cowork-cookbook-ppt-exec-define-product-attributes"
description: "Builds a read-only executive PowerPoint deck on define product attributes from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_product_attributes", "rar_sha256": "126e457527ef8dfd501652fe44103193c0bf35c2b26a8d32115a326f847fafa1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
