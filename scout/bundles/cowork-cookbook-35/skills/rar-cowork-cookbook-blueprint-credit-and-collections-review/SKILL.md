---
name: "rar-cowork-cookbook-blueprint-credit-and-collections-review"
description: "Runs a read-only credit and collections review in Dynamics 365 F&SCM via the Cowork ERP plugin, producing a workbook with At-risk, On-hold, Aging, and Worklist sheets plus an emailed worklist."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/blueprint_credit_and_collections_review", "rar_sha256": "c7ba24d5ddb12a26de0335d4ada83b97b1f39ecd7e8f2b4fc302122db51fc631", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_blueprint", "blueprint", "order_to_cash", "advanced", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/blueprint_credit_and_collections_review`. The original RAPP
agent is preserved byte-for-byte in `blueprint_credit_and_collections_review_agent.py` and in the RCI capsule.

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

Credit & Collections Review Blueprint — Runs a read-only credit and collections review in Dynamics 365 F&SCM via the Cowork ERP plugin, producing a workbook with At-risk, On-hold, Aging, and Worklist sheets plus an emailed worklist.

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
  Upstream entry : https://coworkcookbook.com/recipes/blueprint-credit-and-collections-review
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
    "asofdate": {
      "description": "As-of date for balances and aging buckets, e.g. 2023-11-30.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legalentity": {
      "description": "D365 legal entity to review, e.g. USMF.",
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
    "riskthreshold": {
      "description": "Numeric risk score threshold used to flag at-risk customers, e.g. 80.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `blueprint_credit_and_collections_review_agent.py` and embedded as the fenced Python below (sha256 c7ba24d5ddb12a26…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `blueprint_credit_and_collections_review_agent.py` first:

```bash
python3 blueprint_credit_and_collections_review_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 blueprint_credit_and_collections_review_agent.py   # or on stdin
python3 blueprint_credit_and_collections_review_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Credit & Collections Review Blueprint — Runs a read-only credit and collections review in Dynamics 365 F&SCM via the Cowork ERP plugin, producing a workbook with At-risk, On-hold, Aging, and Worklist sheets plus an emailed worklist.

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
  Upstream entry : https://coworkcookbook.com/recipes/blueprint-credit-and-collections-review
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/blueprint_credit_and_collections_review',
    "version": '3.0.3',
    "display_name": 'Credit & Collections Review Blueprint',
    "description": 'Runs a read-only credit and collections review in Dynamics 365 F&SCM via the Cowork ERP plugin, producing a workbook with At-risk, On-hold, Aging, and Worklist sheets plus an emailed worklist.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_blueprint', 'blueprint', 'order_to_cash', 'advanced', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'blueprint-credit-and-collections-review',
        "upstream_url": 'https://coworkcookbook.com/recipes/blueprint-credit-and-collections-review',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '177afcd17edb7b5a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': '2026-08-20', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections'], 'recipe_category': 'blueprint', 'recipe_type': 'prompt+blueprint', 'upstream_path': 'order-to-cash/blueprint-credit-and-collections-review', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the Accounts receivable role', 'Prerequisite: Cowork D365 ERP plugin toggled on in the session', 'Output matches: One workbook in `Documents/Cowork/output/` with At-risk, On-hold, Aging, and Worklist sheets, plus an emailed summary. Cowork also turns the trigger node into a real recurring scheduled task, which it creates paused for you to enable.'], 'confidence': 1.0, 'deliverable': 'One workbook in `Documents/Cowork/output/` with At-risk, On-hold, Aging, and Worklist sheets, plus an emailed summary. Cowork also turns the trigger node into a real recurring scheduled task, which it creates paused for you to enable.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'asofdate': 'As-of date for balances and aging buckets, e.g. 2023-11-30.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legalentity': 'D365 legal entity to review, e.g. USMF.', 'riskthreshold': 'Numeric risk score threshold used to flag at-risk customers, e.g. 80.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Points the collections team at the handful of accounts carrying real exposure instead of working the aging report top to bottom, which shortens days sales outstanding.', 'expected_output': 'One workbook in `Documents/Cowork/output/` with At-risk, On-hold, Aging, and Worklist sheets, plus an emailed summary. Cowork also turns the trigger node into a real recurring scheduled task, which it creates paused for you to enable.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the Accounts receivable role', 'Cowork D365 ERP plugin toggled on in the session'], 'prompt': 'The attached image is a workflow blueprint. Build and run it as an automated task using the Dynamics 365 ERP plugin. Follow the diagram exactly: execute each phase in the order shown, honour every decision diamond, and stop at a red halt node if its condition is met.\n\nDo not ask me clarifying questions — every input is bound below.\n\n## Input variables\n\n- legalEntity: USMF\n- asOfDate: 2023-11-30\n- riskThreshold: 80\n\n## Trigger\n\nTrigger: weekly, Monday morning\n\n## Outputs\n\n- credit-collections-review.xlsx — At-risk, On-hold, Aging, and Worklist sheets\n\n## Notification\n\nEmail the collections worklist to me\n\n## Guardrails\n\n- Read only. Do not place or release credit holds, do not post interest, do not contact customers.\n- Produce the workbook in this run — do not return a plan or a methodology document instead.\n- Rank and recommend; leave every collections decision to me.\n\nIf credit limits or aging buckets are not available from the plugin, report exactly which check you could not run and why, list what you did complete, and stop. Do not estimate balances you could not read.', 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': "Validated end-to-end against a live Cowork tenant on 2026-08-20 with USMF demo data. Cowork read the blueprint image and ran all four phases with ZERO clarifying questions — every input was bound by the prompt. The 'Open AR balances found?' gateway passed, so no halt node was reached, and it produced 'credit-collections-review.xlsx' with At-risk, On-hold, Aging, and Worklist sheets. Findings: 27 customers carry 3,623,949.93 in open receivables, all of it past due, with 3,287,971.43 sitting in the 120+ day bucket; 9 customers scored at or above the riskThreshold of 80, the worst being US-008 Sparrow Retail at 920% credit utilisation with an item 2,535 days past due; 3 customers already on hold had no open balance as of the as-of date. Cowork surfaced two data caveats unprompted: an item counts as fully open unless D365 marked it closed, so a partially settled invoice shows at full value; and balances are in accounting currency while credit limits are held per-customer, which only affects DE-001 (no open items). The read-only guardrails held — no holds placed or released, no interest posted, no customer contacted. Notably, Cowork converted the diagram's trigger node into a genuine recurring scheduled task (weekly, Monday 08:00), created in a paused state, and required explicit approval before sending the email and before creating that schedule.", 'verified_against': 'm365.cloud.microsoft 2026-08-20', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only credit and collections review in Dynamics 365 F&SCM via the Cowork ERP plugin, producing a workbook with At-risk, On-hold, Aging, and Worklist sheets plus an emailed worklist.', 'example_request': 'Run the credit and collections review for USMF as of 2023-11-30 with a risk threshold of 80.', 'inputs': [{'description': 'D365 legal entity to review, e.g. USMF.', 'name': 'legalEntity'}, {'description': 'As-of date for balances and aging buckets, e.g. 2023-11-30.', 'name': 'asOfDate'}, {'description': 'Numeric risk score threshold used to flag at-risk customers, e.g. 80.', 'name': 'riskThreshold'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants customers ranked by credit exposure and overdue balance for a legal entity as of a date, with a proposed collections worklist.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BlueprintCreditAndCollectionsReview(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BlueprintCreditAndCollectionsReview'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'asofdate': {'description': 'As-of date for balances and aging buckets, e.g. 2023-11-30.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legalentity': {'description': 'D365 legal entity to review, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'riskthreshold': {'description': 'Numeric risk score threshold used to flag at-risk customers, e.g. 80.', 'type': 'string'}},
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
    print(BlueprintCreditAndCollectionsReview().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
