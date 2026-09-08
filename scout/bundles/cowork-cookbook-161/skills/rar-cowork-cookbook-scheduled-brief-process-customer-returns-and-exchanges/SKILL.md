---
name: "rar-cowork-cookbook-scheduled-brief-process-customer-returns-and-exchanges"
description: "Builds a morning brief on customer returns and exchanges from Dynamics 365 ERP data for a given legal entity, drafts an email to the owner (saved to drafts, not sent), and returns a Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_process_customer_returns_and_exchanges", "rar_sha256": "6785bb1f5c23db6c97b563d52d4d7a7641663c94452c87ff3660ab3770e61f4c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_process_customer_returns_and_exchanges`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_process_customer_returns_and_exchanges_agent.py` and in the RCI capsule.

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

Process customer returns and exchanges Scheduled Email Brief — Builds a morning brief on customer returns and exchanges from Dynamics 365 ERP data for a given legal entity, drafts an email to the owner (saved to drafts, not sent), and returns a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-process-customer-returns-and-exchanges
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
      "description": "D365 legal entity to query, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_process_customer_returns_and_exchanges_agent.py` and embedded as the fenced Python below (sha256 6785bb1f5c23db6c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_process_customer_returns_and_exchanges_agent.py` first:

```bash
python3 scheduled_brief_process_customer_returns_and_exchanges_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_process_customer_returns_and_exchanges_agent.py   # or on stdin
python3 scheduled_brief_process_customer_returns_and_exchanges_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer returns and exchanges Scheduled Email Brief — Builds a morning brief on customer returns and exchanges from Dynamics 365 ERP data for a given legal entity, drafts an email to the owner (saved to drafts, not sent), and returns a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-process-customer-returns-and-exchanges
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_process_customer_returns_and_exchanges',
    "version": '3.0.3',
    "display_name": 'Process customer returns and exchanges Scheduled Email Brief',
    "description": 'Builds a morning brief on customer returns and exchanges from Dynamics 365 ERP data for a given legal entity, drafts an email to the owner (saved to drafts, not sent), and returns a Teams-ready summary.',
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
        "upstream_slug": 'scheduled-brief-process-customer-returns-and-exchanges',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-process-customer-returns-and-exchanges',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b621ea25fcb00d78',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/process-customer-returns-and-exchanges'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/scheduled-brief-process-customer-returns-and-exchanges', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where process customer returns and exchanges stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on process customer returns and exchanges for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads process customer returns and exchanges, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on customer returns and exchanges from Dynamics 365 ERP data for a given legal entity, drafts an email to the owner (saved to drafts, not sent), and returns a Teams-ready summary.', 'example_request': 'Draft my daily returns and exchanges brief for USMF and email it to the owner as a draft.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call for a daily or weekly returns/exchanges brief covering top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefProcessCustomerReturnsAndExchanges(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefProcessCustomerReturnsAndExchanges'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefProcessCustomerReturnsAndExchanges().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
