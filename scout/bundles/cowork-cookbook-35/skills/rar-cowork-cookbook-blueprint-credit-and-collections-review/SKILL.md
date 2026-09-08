---
name: "rar-cowork-cookbook-blueprint-credit-and-collections-review"
description: "Runs a read-only credit and collections review in Dynamics 365 F&SCM via the Cowork ERP plugin, producing a workbook with At-risk, On-hold, Aging, and Worklist sheets plus an emailed worklist."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/blueprint_credit_and_collections_review", "rar_sha256": "c7ba24d5ddb12a26de0335d4ada83b97b1f39ecd7e8f2b4fc302122db51fc631", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_blueprint", "blueprint", "order_to_cash", "advanced", "integration", "dynamics_365_erp"]}
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
