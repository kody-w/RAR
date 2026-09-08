---
name: "rar-cowork-cookbook-scheduled-brief-define-accounts-receivable-strategy"
description: "Builds a morning brief on accounts receivable strategy from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_accounts_receivable_strategy", "rar_sha256": "3158b4ac6329ac358eda2ad5a2fadc314b8717f9156275117e4f2aab1d9a2ba0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_accounts_receivable_strategy`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_accounts_receivable_strategy_agent.py` and in the RCI capsule.

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

Define accounts receivable strategy Scheduled Email Brief — Builds a morning brief on accounts receivable strategy from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-accounts-receivable-strategy
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
      "description": "Dynamics 365 legal entity to pull data from (e.g. USMF).",
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
    "responsible_owner": {
      "description": "Person the brief is addressed to and whose email draft is created.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence for running as a scheduled task, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_accounts_receivable_strategy_agent.py` and embedded as the fenced Python below (sha256 3158b4ac6329ac35…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_accounts_receivable_strategy_agent.py` first:

```bash
python3 scheduled_brief_define_accounts_receivable_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_accounts_receivable_strategy_agent.py   # or on stdin
python3 scheduled_brief_define_accounts_receivable_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define accounts receivable strategy Scheduled Email Brief — Builds a morning brief on accounts receivable strategy from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-accounts-receivable-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_accounts_receivable_strategy',
    "version": '3.0.3',
    "display_name": 'Define accounts receivable strategy Scheduled Email Brief',
    "description": 'Builds a morning brief on accounts receivable strategy from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to',
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
        "upstream_slug": 'scheduled-brief-define-accounts-receivable-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-accounts-receivable-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9317f9f47a77b6fb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-accounts-receivable-strategy'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/scheduled-brief-define-accounts-receivable-strategy', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'responsible_owner': 'Person the brief is addressed to and whose email draft is created.', 'schedule': 'Optional cadence for running as a scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where define accounts receivable strategy stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on define accounts receivable strategy for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define accounts receivable strategy, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on accounts receivable strategy from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to', 'example_request': 'Give me the AR strategy morning brief for USMF and draft it to the owner, plus a Teams summary.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Person the brief is addressed to and whose email draft is created.', 'name': 'responsible_owner'}, {'description': 'Optional cadence for running as a scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when an AR owner wants a daily or weekly morning brief on accounts receivable strategy drafted as an unsent email plus a Teams channel post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDefineAccountsReceivableStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineAccountsReceivableStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'responsible_owner': {'description': 'Person the brief is addressed to and whose email draft is created.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for running as a scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefDefineAccountsReceivableStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
