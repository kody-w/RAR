---
name: "rar-cowork-cookbook-scheduled-brief-settle-customer-transactions"
description: "Builds a morning brief on settle customer transactions from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft emai"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_settle_customer_transactions", "rar_sha256": "c9a34abdaea8d6415af4848c6765b3f2ccf141ea5bc5c3254665737a841b4e8c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_settle_customer_transactions`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_settle_customer_transactions_agent.py` and in the RCI capsule.

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

Settle customer transactions Scheduled Email Brief — Builds a morning brief on settle customer transactions from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft emai

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-settle-customer-transactions
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
      "description": "Dynamics 365 legal entity to query; defaults to USMF.",
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
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "When the brief should run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_settle_customer_transactions_agent.py` and embedded as the fenced Python below (sha256 c9a34abdaea8d641…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_settle_customer_transactions_agent.py` first:

```bash
python3 scheduled_brief_settle_customer_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_settle_customer_transactions_agent.py   # or on stdin
python3 scheduled_brief_settle_customer_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Settle customer transactions Scheduled Email Brief — Builds a morning brief on settle customer transactions from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft emai

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-settle-customer-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_settle_customer_transactions',
    "version": '3.0.3',
    "display_name": 'Settle customer transactions Scheduled Email Brief',
    "description": 'Builds a morning brief on settle customer transactions from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft emai',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-settle-customer-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-settle-customer-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd5f18b2f6871dba3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/settle-customer-transactions'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/scheduled-brief-settle-customer-transactions', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where settle customer transactions stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on settle customer transactions for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads settle customer transactions, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on settle customer transactions from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft emai', 'example_request': 'Give me the 7am morning brief on settle customer transactions in USMF and draft it to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly settle-customer-transactions brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefSettleCustomerTransactions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefSettleCustomerTransactions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefSettleCustomerTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
