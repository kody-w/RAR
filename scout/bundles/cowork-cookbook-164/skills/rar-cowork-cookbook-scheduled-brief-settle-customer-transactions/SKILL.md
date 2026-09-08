---
name: "rar-cowork-cookbook-scheduled-brief-settle-customer-transactions"
description: "Builds a morning brief on settle customer transactions from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft emai"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_settle_customer_transactions", "rar_sha256": "c9a34abdaea8d6415af4848c6765b3f2ccf141ea5bc5c3254665737a841b4e8c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
