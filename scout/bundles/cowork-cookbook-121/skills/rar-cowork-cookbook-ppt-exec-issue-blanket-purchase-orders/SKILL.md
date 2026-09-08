---
name: "rar-cowork-cookbook-ppt-exec-issue-blanket-purchase-orders"
description: "Builds a read-only executive PowerPoint deck on blanket purchase order issues from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_issue_blanket_purchase_orders", "rar_sha256": "d583c6976fbf36aaf794112e3f099ec7722caf6ca6c9121fef6e7e3403641dc9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_issue_blanket_purchase_orders`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_issue_blanket_purchase_orders_agent.py` and in the RCI capsule.

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

Issue blanket purchase orders Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on blanket purchase order issues from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-issue-blanket-purchase-orders
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
      "description": "Dynamics 365 legal entity to report on (e.g. USMF).",
      "type": "string"
    },
    "meeting_length": {
      "description": "Length of the review the deck must fit, e.g. 15 minutes.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-issue-blanket-purchase-orders-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and comparison prior period for the trend chart (e.g. monthly review as of 2026-05-24).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_issue_blanket_purchase_orders_agent.py` and embedded as the fenced Python below (sha256 d583c6976fbf36aa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_issue_blanket_purchase_orders_agent.py` first:

```bash
python3 ppt_exec_issue_blanket_purchase_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_issue_blanket_purchase_orders_agent.py   # or on stdin
python3 ppt_exec_issue_blanket_purchase_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue blanket purchase orders Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on blanket purchase order issues from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-issue-blanket-purchase-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_issue_blanket_purchase_orders',
    "version": '3.0.3',
    "display_name": 'Issue blanket purchase orders Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on blanket purchase order issues from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-issue-blanket-purchase-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-issue-blanket-purchase-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e7e61084b3ac3dcc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/issue-blanket-purchase-orders'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/ppt-exec-issue-blanket-purchase-orders', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'meeting_length': 'Length of the review the deck must fit, e.g. 15 minutes.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-issue-blanket-purchase-orders-2026-05-24.pptx.', 'review_period': 'Reporting period and comparison prior period for the trend chart (e.g. monthly review as of 2026-05-24).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for issue blanket purchase orders reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on issue blanket purchase orders for a 15-minute monthly review. Produce 'ppt-exec-issue-blanket-purchase-orders-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads issue blanket purchase orders data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on blanket purchase order issues from Dynamics 365 ERP data for a given legal entity, with KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on issue blanket purchase orders for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-issue-blanket-purchase-orders-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and comparison prior period for the trend chart (e.g. monthly review as of 2026-05-24).', 'name': 'review_period'}, {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'name': 'meeting_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX on issue blanket purchase orders status for a short monthly review, sourced from D365 F&SCM without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecIssueBlanketPurchaseOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecIssueBlanketPurchaseOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'meeting_length': {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-issue-blanket-purchase-orders-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and comparison prior period for the trend chart (e.g. monthly review as of 2026-05-24).', 'type': 'string'}},
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
    print(PptExecIssueBlanketPurchaseOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
