---
name: "rar-cowork-cookbook-ppt-exec-send-knowledge-article-to-customer"
description: "Builds a read-only executive PowerPoint deck on send-knowledge-article-to-customer status from Dynamics 365 ERP data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_send_knowledge_article_to_customer", "rar_sha256": "8844d4c0fbcffee3d6aae5468c5aca2c107acb1f513aae03026871d5317f4c74", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
