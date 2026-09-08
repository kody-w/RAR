---
name: "rar-cowork-cookbook-scheduled-brief-define-accounts-receivable-strategy"
description: "Builds a morning brief on accounts receivable strategy from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_accounts_receivable_strategy", "rar_sha256": "3158b4ac6329ac358eda2ad5a2fadc314b8717f9156275117e4f2aab1d9a2ba0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
