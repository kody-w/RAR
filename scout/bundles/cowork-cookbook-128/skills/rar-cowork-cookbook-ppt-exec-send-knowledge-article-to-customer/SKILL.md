---
name: "rar-cowork-cookbook-ppt-exec-send-knowledge-article-to-customer"
description: "Builds a read-only executive PowerPoint deck on send-knowledge-article-to-customer status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_send_knowledge_article_to_customer", "rar_sha256": "8844d4c0fbcffee3d6aae5468c5aca2c107acb1f513aae03026871d5317f4c74", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_send_knowledge_article_to_customer`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_send_knowledge_article_to_customer_agent.py` and in the RCI capsule.

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

Send knowledge article to customer Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on send-knowledge-article-to-customer status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-send-knowledge-article-to-customer
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
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-send-knowledge-article-to-customer-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period for the trend comparison (e.g. monthly review dated 2026-05-24).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_send_knowledge_article_to_customer_agent.py` and embedded as the fenced Python below (sha256 8844d4c0fbcffee3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_send_knowledge_article_to_customer_agent.py` first:

```bash
python3 ppt_exec_send_knowledge_article_to_customer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_send_knowledge_article_to_customer_agent.py   # or on stdin
python3 ppt_exec_send_knowledge_article_to_customer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Send knowledge article to customer Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on send-knowledge-article-to-customer status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-send-knowledge-article-to-customer
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_send_knowledge_article_to_customer',
    "version": '3.0.3',
    "display_name": 'Send knowledge article to customer Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on send-knowledge-article-to-customer status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-send-knowledge-article-to-customer',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-send-knowledge-article-to-customer',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '667357f098491939',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/send-knowledge-article-to-customer'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/ppt-exec-send-knowledge-article-to-customer', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-send-knowledge-article-to-customer-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period for the trend comparison (e.g. monthly review dated 2026-05-24).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for send knowledge article to customer reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on send knowledge article to customer for a 15-minute monthly review. Produce 'ppt-exec-send-knowledge-article-to-customer-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads send knowledge article to customer data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on send-knowledge-article-to-customer status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': "Build the executive PowerPoint deck on send knowledge article to customer for USMF for this month's review.", 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-send-knowledge-article-to-customer-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period for the trend comparison (e.g. monthly review dated 2026-05-24).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs a 15-minute monthly review deck on send knowledge article to customer built from Dynamics 365 F&SCM data, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecSendKnowledgeArticleToCustomer(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecSendKnowledgeArticleToCustomer'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-send-knowledge-article-to-customer-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period for the trend comparison (e.g. monthly review dated 2026-05-24).', 'type': 'string'}},
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
    print(PptExecSendKnowledgeArticleToCustomer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
