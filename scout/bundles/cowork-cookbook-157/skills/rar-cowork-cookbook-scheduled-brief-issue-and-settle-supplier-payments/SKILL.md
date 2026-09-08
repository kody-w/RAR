---
name: "rar-cowork-cookbook-scheduled-brief-issue-and-settle-supplier-payments"
description: "Builds a morning brief on issuing and settling supplier payments from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day average, next actions, an email draft, and a Teams-ready summa"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_issue_and_settle_supplier_payments", "rar_sha256": "ec60a0eff83ab658e32c80cd134f74ade5ccba33cb21ddbedd477c9923a8285c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_issue_and_settle_supplier_payments`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_issue_and_settle_supplier_payments_agent.py` and in the RCI capsule.

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

Issue and settle supplier payments Scheduled Email Brief — Builds a morning brief on issuing and settling supplier payments from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day average, next actions, an email draft, and a Teams-ready summa

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-issue-and-settle-supplier-payments
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
      "description": "D365 legal entity to run against, e.g. USMF.",
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
      "description": "Optional cadence for the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_issue_and_settle_supplier_payments_agent.py` and embedded as the fenced Python below (sha256 ec60a0eff83ab658…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_issue_and_settle_supplier_payments_agent.py` first:

```bash
python3 scheduled_brief_issue_and_settle_supplier_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_issue_and_settle_supplier_payments_agent.py   # or on stdin
python3 scheduled_brief_issue_and_settle_supplier_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue and settle supplier payments Scheduled Email Brief — Builds a morning brief on issuing and settling supplier payments from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day average, next actions, an email draft, and a Teams-ready summa

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-issue-and-settle-supplier-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_issue_and_settle_supplier_payments',
    "version": '3.0.3',
    "display_name": 'Issue and settle supplier payments Scheduled Email Brief',
    "description": 'Builds a morning brief on issuing and settling supplier payments from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day average, next actions, an email draft, and a Teams-ready summa',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-issue-and-settle-supplier-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-issue-and-settle-supplier-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a944e50b29469cb4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/issue-and-settle-supplier-payments'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-issue-and-settle-supplier-payments', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where issue and settle supplier payments stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on issue and settle supplier payments for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads issue and settle supplier payments, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on issuing and settling supplier payments from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day average, next actions, an email draft, and a Teams-ready summa', 'example_request': 'Give me the 7am supplier payment brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly supplier payment brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefIssueAndSettleSupplierPayments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefIssueAndSettleSupplierPayments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefIssueAndSettleSupplierPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObWJbmX9G8/SEzW7bZJBZ3VMQgQGKVECCQlK5wsoPYN7Fk53+fi6TXzqzK6pmM7k8jhy0B9579POccX359s7s2Kuq3z2+6b+eLnZ2mceTXCzv3FkzRF3UCvorEAX8XbpG3dex0bVE3bx/ePL9x67hs4yIH2zddnHrNwl5kRZ3Hebhw6tgPFkW+iJumm2/MJBu/bdP5ounKMo0Bo9IeMz9vm0VQF9mCHXM7i91mgeHrBaepi6AAsixSP7TTBVgWt+OHRR+30aItysV6Ebd+1iyccRFnpe22HwCTIrMB4WZxbxZt5C+Ij549Luy7X9uh/2GR+0O7ACuB0M28euFndpwuvNoOHrs9wM3w7az5WPu2NwI5s8wGyvqDnZWp37x9/vnvH94At/Tt869vbmo3zWw7N/K9LvW9zay0ABT26dzTZ2V9/aWp+lIUEEvtPAS7yhGYPgfXpV8DPTNwywMme1392Php8GHx7/+e9HYdNj99/pIvXp8vb/MfrcsfGraF3bS+t3Dt0nbiFJjo04JOe3tsFrXfdnU+e6UBnsvDT8+d3ykBI/5tfvbjk8mn0G9//PJWABHs2URf3n5aAAd8eau7+fenmUr540+f0qL36x9/+k6n6Zyb77YzMSD1p6+v6xdZsPD70jhYfNVVjnnxqn03Ln1A/Hf6zZ+n6C9yL5N8fS7+sSg/LP6c8qzP34C8z9h0AN0/JwtsAHa+fboVcf7ji0dd3P3czl3/x5/+FVngZjdJ46b9f6L785NwBAIJWOtlkp8+PNz398Xypds3mv+abQkC5q9oApa/s/tmqH9F++HZfyANMhQk0Lsv/5Tcn21Y/m3x87/U7b/a8GERfHlj/TSes9RJ/c+LXx8h8vMP3vebP/z9N0D6/0pGL7rafVD4mtl5HPhN+/Xrzz80j9s//P3nH7oSRDHI8K9dnf4ZzT+z64PPHyz4WvXjH/cC/qc8yYs+X3zLocWvRfm/6t8+LUyAS973+83nxe8zcf4sF7MS70yfJvhdNjZA1t/Z8ae33wAS5UCb7olnAD/+7d8WSuzWRVME7UJ3i65dAAe3cebPwhtR3AA4fqBG7QO7NjEw7GsdiP/Zw7PERbD45X+7D/T/6L7QH2reMe7rA9m/zrDufwWI+fUB6v7Xd0j/+g7pv3xaGIBTUcdhnAP81mhV/ZIDGM7bWYqy9hu/vgPkcsbW/wgS/OP8YxHni1/+OrOvD7qfyvGXB4rHT2zUGGHGxQaQ+jRbwIr8/KWvO4P/4LsdYJkWLpAviAHAfwCWaYr0DnB1tlaTxCkoDzFAHlD2xgdtYNHPM7FffvnFsZvoS/4EcmzxrIcNBBZ8E2fx8SNQNEjjMGq/5L4bFYsffv3th8V/Lv6rXQ/iMw8VFJiXv4CEon7YL0D+dc+SOTsfgMvDX7/+9jI3IJODugq8GwdzHZw3g/hNfO/d9jpPf0TX+MLxgc39uXQWdTsX5bj9tBCCxTd5AdP50Vw/oqJpF55f+rnn5+4IqNpAnW+WzIt20YAgbQJQn7vGf3D9xanth4gZAAK7/WWhMCqoVkUK/pnFfCwCm4s8Bub/FhnP+4BI/UOz2LyT+LTYzxEL+oXaLqPafvEI7Kdf5jbhtR0Qt0Gd77/kc5n2Z1M90udpHrAIWMZ9ufTj7HPQ2IAin3vNO+/HGnuuqcajttZf8uaVGnY9u8IFpQIwDbvYmwvGf7xCqomKLvUe9gOSzpReXvBeXnnE4KM9+N4N+X/SC33rJxbcoz15tBWLLx0KI6vF/8+d1mwferfTuB1tcOyC2xva5em3ufmc/fvsV4F0D4EfOfq98XkHt3eM/5KnMQjCevyP58qHt19rnrjZ1cDIGq096INQA3aa6T4yYY7sup41BHK9FxMg+uKBnMDeADZAWs3R/M5wfvouaQSwYb7+3lg8Iqf2ZuVBtC/KzklBJAa+7zm2mwCpZku8uxmkhT9ndh/FbvQHrWb3gOgD9B9OBx4FBefTN4B/Pn0X/Q8bn/3TvOXRW3YgmesHASCHPws4u2V2OhCvffb6QM/PDyJAjaxsZ90dkE5A0+dNv/arLm5AeDQfXnb1SwDkH+fvp6bzXX8oQQYBY4E8KTtg3UdmzfGZge4IyADABSRaFuegWwBGeRnhQdDOZpgAMPxqZ58UH7dfCvmPdJzL3PvGWZF5z9w5PAPezsffo4nxZ2EC6GXzigfff4y0b9xm2jOiNgAVAcf3p88W49OzS3i2IYt3up//aZj68a/NW4+6f/pjAHxeRG1bNp8h6Fmr30v1J4Bn0FPW5nvZ/viAiY+PSvoRsPv4RJ+P7/jw8R0f/sDpaYTPi78m7R9IvLLl8wL5BH+C50fyK9peH2Ac5uPm8nE1P/2Sa/53/AXsAcq0c31Ixxl93ovl+xJQMcMaYBZY/CyezVxze1DmH9UC+OVL/vvwn9MPFKM8nMO1KX4HC4+uAaTC043fihp4lLeAtzf3oaH/aR7fZvEb/+1z3qXphzeAo/5fnwHnOpbNId/MgyRILtDltbH/uHogyNDOP/84ZB8eP+z004L1AVqlze/D8lV95ur7u+x56gx0dQGHDwsPWKqZqyXQeWY+Z57dgFAGUTzr1o7lrMxzXJwbzEdB+PosCP8sEDtXj9/XjPfSboePTPuw8D+FnxYnXdn+KfVvve0/k7ZAyzBT84rPM8UPLwAC32Ae+bD4NloAnV7D3szBzzswR/88jzWzkR9b5h9gD/j6tunbf184/tvf/0yuHoTXP8uk+U0Jytmja34sAZFWzCb2QXQ8nfGobyByn9XukXN/qvl7Xv5rJ4MQ9B5p8g4wD2Ivi/a+n8zl9tUDgBLVLgg7+xNWgNcDokGhmw3z3eLf9S4es90sFbBT+/yviF/fQHTaIFzsV3y+hgOwHCDax2ZueCCQ0YAhuH7mHnj2PzA2vCg2kQ2aVEDSd3HYhv0gIDHbwdekj6EuCbsegq0CYgVstHZdx8Yw10ERz3N8z1sRhEtRKGaTKLl2Ab1nTn+d+7x4lnIWERjnI4AF//tjcMt7qfdUZ7bdtyllNsNLy1/fHHwFVvKrRqCfHwaiEAdHV87o8MsJDwpD2LBKvOVvbeBfDvntskOu+3DiupWcGM7mGPPbqUzyg52tCNU6XDnaSIRA4vyrSJoeMq1N+nzA2kNTXJTEUD3EMxHIrvC1cTvgEmaVmjAyF83SNK4s3KaJYcmM4am7lKeTVU6ENVin5Fhzuj6xujwpR+JkQdBEqKQhK0XPyLYuwFMvJivkQtoNzOm8ABcHW+Gxq0hgBxiJSTQ+jWwOt/d7jVdGuD4M53pPB3t9hyQiSzcyf5lc7WRZyC7JzmHVJ/LWqgZUKPoJ19xJFuUdV+jIUoq2jXmOb9CeJgqDrHhpfTIOWsUtt70S9oah77dFjXG+Nk6Owtbq1R/Nm+qOFssHsXKZEvt+vk3rbkqmyx0TcYgbz8F9wtbwcL4fqfaQ0Ns9kzYndHI5p0Ha5jgiZOam5m6/m2B2o1/rgp7O4Qmgiruu2/za0XgksS1H9wVky4rg4dMW9ZRzcREjTkt6UjCdvjlOYATLo2mrhPlZj1SHbu8GKkrC6U7qzaqDzwXhm/nQlR6hU+OgqnjJifVK7wLZUCVmf4MY8sxZkUxdpY1+L88rIedCqd7DiSF6EtLtqx1U2xOPiPI9Vu16NxRKjUjYni9UHzvcpXZFJBM7ZrvMFiQJue01seAl3ygvJ+VoS5f9Sb2K2+Ti10muo5dNHarkSkLvmrSNd6i9wauzirhRVKCF5Vl5XDk1dp2WDeKUQlCdcIekE1EaR6EWPAOrvOMWtY4NvRT5jVQefa3PBI0g7nyTidm+OHMX7SD4B+6GVjlVtRLLwBy6EUjdiHPSkbeGoSAxavBGv5NCk22MXXRPLdpMetZXsuXZO9Wcla1g+2Shg16bFoVYnb0Mu3F7OPhqUUk4pwSleS2DVerhnStCipGeG3WFrRjIPd43XGMsuUm4bPPlFWfKAvJYa8ntu3hUjRhXbnns4N4aKstgd7wgJx9nomi6hd7EhNfq1p4zsXGUCqb7uhc3/sjdQsFc7SSqZdrLsO0ElYhVjPMIEjWrM3QMNrxCBdAtgsLSvymEqbmsJyLFLuVOaUhvI0Qbtrslll22QVXsOlmc9Ct/VsQwYIwDZvU8RG5qmavxnWy2uTMpGFkmR9Iu4bUzwZgjEAWGXlhRTKIrs0JM/XJIwo2c7NtDEWoCSdaYSEwgtIbAEvbd7pju1FIWdGMcR0eZWh6VuUlZkpq5Ofu3mkSysjxXWX1aEVtc3drqZrUiiwG/nwrqXFleo5v1hmutu7Cv7lXnbSp5LxD1UI0utZduJ+p61O4IVCDlOq1G0qlsx1UbqK2CmMN2tXIfMk5PZZbO7cCIFTX3GWdXIcKtRG+tcKnxJYepBsekxoSyK85rUgTXkhA7hhMTLaWY4eRrEHgQLfo9E2pWt1lucamBdjrZnW/QztnvIW1Ky8mu15Acn1JDWtJ9FirRJuuOg3kipoxcwyUh3VNhidwtsRTKqwBx0UQUXaC0vstrelcf9zhRotIO2toegufqdrNuzned4czhEqyEdT9Nk3ycpFNQSww9UTdqdUGsnTDY/K6y/fNwF5LI2nHLaJoofc3sliG234JA3lkjjQG5PYuxlGuIsRmmFMLq7qurpUxZjW95CNdKtesuywG636QsaCwXokdWUu0D3SYOTFVXSS3x/XiEFJ/vVvzoYfvBD/KU5LYWtVM42CS4g6I5vnZeX6oNhazT+n636YoOqeseHyizGPgQ0UCmKkNGhVncF4f9jQxEPjydOW1HpU4h5SxzPLIrP9lGo70rGW2TDThB4UuvR/qWj2TdohEBz4a2ikok9KSNsILhZRIVQxkQOlJz64jxaA0uMk00YmeEO8GKWX3EJ5y9696mVHqJOZykjlpm6WElbZRBom2c7bc7cdMWQUvoUO/XaVxbHXcksX3U+/zZb1ZZaJZ2c+uTNR9gayJQZW95zLdFOqRSYIuFul+bQroTjGXKqB6xpe1GKZmtKtW7bqLKjaI7aYTAqx6+puqUjZqKUHu+Ig1Pvd+J3XlCBy875YfziV6vs4CpL2HE3oW0E5iOT1oBhwtccGrPj88nh3Nk6HLz6COCBE4Z6p3iB1NBesGkwVB+W0N6LIeNsr0SraBY6HFY8oHcS1Wtct453+7NPVrRyqo7lVu2ym67QzzKgzB68HEpNkMqGmgEbyLmMuRyDkOyv3MpYerJlqMg/iYu49ONxGtFaVfq0d9npszL48G0UZtAIbi3rDXhXvz1FIadYDeRdl5dNW3TLfl7e7xolXqwdqJy0pHLLemRih8GNHHTPqPLJNuNhHORcYLfJFbPVLTDTklF0gOnaB1+PjWYgnFyfKVXkJHhMXnRzV2P7tMBd/d4XIIuQA+qTK+3JySkmW2zOTXaqtoeG1GlQSezxflOJzK1moxI8AN90I4lv6IrWZOaqtGb0GOMOKZt59Tj2gUykfZKy4JputM1OhwrQdLvtHhxgxDuZQ+XdNEW78QZXm2aUsloS0vY6xo+XSMpWVU5a3IuXRTRMk70FHas7bI9wTc2u/c2M4TSmT8JFBtsD0UtHlumHDsJRXvWa0gO9DQ923dYEW9HqHUyCAFAvr/7kXGEz5qvGGPrs5eOK7P1rhh2gpzHXaUPe9qTGJXWTJjoj/Iy1xisGE8lRUYAeuXYcqB41YLClIalQmqr8zYV+jgLM/mQC9twH/vRqriYbsAhh4aTrEusZZdbti7QyzIJ2PO23HDFaVmfoaasBNozeUcpLsbaNLOIkAxW3+5MdtWuvbIR24B3drRqKOSeatHh2EYkHNKgvUmDzHWKZo0kEOzuRjtci2iQR0Nw2NmrBht24iVKA3GVVfsDbo/0/kYkxrE6oLa1qT0xTNy8yo4iY0sek8dL0VJOzYDDJ646QlbFx5FkWlB0wnze4M6m6u+vFyI0uROcLdWoPPaYYdOU45/XmhMkfgBDazK4n0TqeJWvCFufHCUPLzADcTIvXNQ9X3P11ierosrg6djvHdE+KjZEoBu2it3+kvqI2E3ytcNP/S45ehyXRqYWnO6TiBUS4W5vuxQ2qv21x1YGBZGHGmHI9bQvmsDS6bHleP/eUkVKpMXBHDeCKdfJoWJO4TLk9ZNQdgBdBgfyqEm7c9AJOV+PcMFcu8K6CCGn25jAMLu9PhZdmAaSSPvXAqPhyj3TdFsfKKSPRzI0636yHdWXQzmSthtMMPgTMSJH+MgLy4NYiaEsQSE99ooRG+UNvyCib68VkXRRpOH6ZTtMzlEu4xIHkCNstCFEmyyV22E4QjmB4E5gUhuPNQbjkChdvywl8qJKTqEf+iJW0mHKjn2U4dLVxSFHTghnuTrzzbWsN4HYd1BlnkrvlFJtRuviJIBK13Jp2ZwFO6kOZScgu8PthDHE2GUsJFVbLWMRxjBw2grDewQJ9CBt15G6NQ44jugkrwgbe133oLmkxH0z9IKQ5a4KrVWtdFNplAo6ELNj4ifSmXHK7fHEmCK6XoUOz1/hk1htrmZkXahVn0I3yg7EsxOD1loZ7sTRbtDL2SSv7YgLiNDu1iRrTlSR3CQNzRoFPedWJTc7g7hQDWSR4oZiuwhpdAqNWtteo5CimMSwh6RQ4fgkd2+1G5OiYamRYmyvBhGTAc4NG7ntj9XUnjgMkhSdOVRnV/fY0ooZPglPWFDd2DTP+XMM0NRvtC4Oi1GnTUzmdkJ9tDPWS3ZicO41LfDatvUOAXxgKMVfQyvHI/WVvq4KXdqMxZIggaWrdTXSPE2IimvuwsPIJJJk5RaYgJI9WnADJfkOQq/3e5Y8sUy8Pm0IVQyuy7KUxBzP7gkXMgC6Ri7cSTjqscyJrdr2pJT0NS3w+N7TlcudpuKgK7c2hPJ4aDie64+JyfNbTD00CnQaysPygtzjWPY2+8uSzpGNm92YfXwhQLlOYF2WboZp0/gyjC56cVnmN4vGHAU1XOpGKA5SEEcFk28ovMM3Os/aNLSST/lVAWMR7fVQnSdbUrne0ssuJQfuWlwmHEmuGYoLe/OsmOOWPZ/ag+FuGFou11lu2XlukAFiL8XcYeqiq1wSas9YyiTmyMZyCoY/U8u2d3jbb24CMvb0loK8RDttnIK58QifRHnNBdvtZGxWtt/aqe2P4lLaVmFR8Jln0jxCCFSfLmmxKhCWFa7CfZ3upAOi0YjrNGFLB5q538U5ssUz7dbRuxqGyna/c255vd9eYTpv0gQXN7xhx5pzdyjWv1iWjZg74xZasIMn14i6cZ4T0zKDNGuBIW10V3iJoh7qidHxXEa4JXPakplpXpENVqOspbWBiY7Xo3o9VWJXdTfitmqUVo00IjkaOc8aah2IB8cYr3vGWtV24w1TeruSu5tlwgE67VNY608UW7RyRF7ZyOnri0Sd7VHlSTn3eb0oZajbqpNJWgcKliaiy70EZYn4foiXZ/Wae+GK94e9Q0D11Al6fMII73CWSgzZe4btl5J19zIfVQVFL8lGcg/ySW4u+81adKtJKvxwl9iNFKB2fbrfmgurU1pKbFjqjkhB2G/iLmbGZukUtH9iaW5ropmItTWNiKdWH0rK2dLLwWbuhwAFZWkbZ+bVWC6HvRAQqEObB3jAhQ2PYZbf5U6wu2eGf8DEy1Uts1W+34RnIqhhb6cR+R0iBwoaBOJSjU14mbwAikvKEmRDw/jLKONUcm93bchFUpceCSk75rcIq6dDCIudajU7xUbVXtza052SqwBjrvRWMHSxsFfxkjMScdSF6X5AGJO6lvvyilSr/U05+2OBbleEgiL8/aIHjNPzZLFlJpls1/EEWsxGv/juXhuCPBA353NZ3686pspZX543PDUuu67LrUIHU1zKumNQUiCtHHEgr0xC6iVf5nAnl1cWrl3KpNTeLW35XoOBXVXzonW0e6cVkEGXiL6seULZm+gVZlGOGS/0abwceGy6GfcOjICifZHkNdIal7AWYvvEHGuqGWwEceQRQ6Ms35lMPFInqyGumYapqG1iqHKN+olElQEM9ffBx3aDV+iroVhf9Et5unJho/V+llNyeUbYjAmPu+HGUKRyMZEVKPMedsy5ZPKsI7fJCsPuC0XWeHvYUPaOvB46lQpFflscoG7jjsy9XiPGMessRD1A6YX01TPRdBWxPrJpuz0KlXsjlxV0yXa7BqdJo0LaItpge0JlJqJsgMUHtBqLDbXdBfx5Cu8BW6crt/PWNyYsnUZuNON8L60Jw4RBocSr3LY7y1ya6OmgdEdowhuh9Vf7tLOWXYGvlfp2n4YMIcEMn5M1h/VbYt/LbWkgESjCqwCCTlldYrc1gKycJBu7gJH1OIRTl+6zyeBZ1eKQJmXTpbnbK1hpb32JF672dcW5t3iFRykO8Sw7SeFGq0/M2dX8lncVZtxAXk4JfeZpXNmqGn/BQfxWmG7TS9Sv2Zqn9z5+O1B6QxEJVp+jtYfsVdvD1l1uBt5GO1HLiVUpPEAP56C4JpMwHTrqQNWuXwlZbOUFzJuKixLY7bC1zSWEtPp2oHDT8wfK5qQxGyk0u3vVbUBP42SfiDsY407tPoiMc2jbdUv4vMV61KaiKnXHmq49oGyUH6s9RjOHrPXK5doLWVwo8NrZ9pRKRiemuoqnyAWI0WohgKMc2xXHm1KSdhZ4y1GSoGlwL7TZMNWWJRu4jHNNLSGfdXki2jHFadWTYXRd4fc+7BEl1g7lkDi5rlqdichlHYS6cihZSL507Qqq9yOMwnGB1L2vt5d1fKnQUWWk2Jnq5aqi2rrDIgJnPNZdbjvhMAgRdVTCDr33RwITQy0mcpDXEn+HwOir2hB5vPDbvD0gSVCaBnCD3ub2+Rou4bs2JsQWzKvVRXZwbRV4B7Q2tJu8W4IIa2+mjU0teaxK69AjN7hxUS1gy/YKumDnKjlGcbE2/RWOYNR2/QbHRCV1CWTjZMWthiRhTXFahIiyeAxuAODX3kpsAlpG2Uu9S1SYpPfOkRTpc14eJTW+VwPGwFI84XDN0GSIuYeDjd0w3kkavXWwZeWZQVDjF64gV5WzMjtTVpkWxNBIDBTRk1dIv6amaoescFM5K9ngMqbS4qpXrAqDOsiHvPtaKnsZviJrWFiubJMBsdx7BIqu7ojRqF2Orttgz5yRoghJ/0ydZeqEm046afwR8o7EtsPXm2GLHMTkQKqMrO9ZBDSYQ+uY2/uYYuetY6YEtw7drMJOqpUSmN0E1EYmb7p77FntmDGTjWOhpfkgphMW29RHgi/4JmF5WYaOERfmp0Nsb6iG7wj6wB5zl5cDR2y7KUGu08G4cVS95PRsoDz4YtzqjkLCI0tyh7Zoo7rkSYcJ/caVzshVw+A1SThD5bQwbFoBUbeFt+wal2yhdMSWQwSRyPLm7jAZBgB3C3snWuerTSnCEN6aCLNfDyHo8AwrHXPUokb8sLorYcWubwBWhBZBW6vZnsMJ3SaoBLkOsrSta3FdR0F8t83IUXf2Bj1Qy7YPWAKMlApwVloRyVnJvPq+7hBz7BlR2fM9ZYlMSFN6FyBZxlQXulD35jbZdKmJabh7WMZ1hN0PNXMM/T3MqfKV3RfbkoGLQ11Cp9uKFtr71b+yrmCOsIYuV4rX7V3QHDuglaQ1DY93ULcLfHy4KDA7+qY1hl6tcjtqknDZOvsiKbQObh63E++xu5tUBNvxjuPrM0RQ0ypSBUzgp06GRQI7blF4NNhJlQoM4nN+LOiGOxGutAusalphk5EEEJ1W9jRh1fFI028f3ubj2Neh6n/jPbD5XOd/7AjpeRL0/h7H44DRt73PD16f/ztC/v3DG5hZgIjPo7Qm7cLXEdQ/HKR9/OsH+TO98fn61fuB8vPEurXD+UXmtzj3uqatx69NkT7e9AA7nK6ZX3Zs5vdhAVA1vz9F/QdFv5+ctcWs2tv8OuL8EofvxXbrvy7D13Hjhzfv9crRVwxff/Xrclb+9XIA0Bn7BH/C3n77P4GrzrCSLgAA -->
