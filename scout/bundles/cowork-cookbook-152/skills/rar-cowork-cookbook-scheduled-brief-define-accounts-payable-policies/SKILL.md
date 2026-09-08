---
name: "rar-cowork-cookbook-scheduled-brief-define-accounts-payable-policies"
description: "Builds a morning brief on accounts payable policies from Dynamics 365 ERP for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an unsent email draft"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_accounts_payable_policies", "rar_sha256": "74d53b52565dec20cc340fb9ffdac520669c949dfb7ec7086bc1d413bf97cca1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_accounts_payable_policies`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_accounts_payable_policies_agent.py` and in the RCI capsule.

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

Define accounts payable policies Scheduled Email Brief — Builds a morning brief on accounts payable policies from Dynamics 365 ERP for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an unsent email draft

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-accounts-payable-policies
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
      "description": "D365 F&SCM legal entity to query, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_accounts_payable_policies_agent.py` and embedded as the fenced Python below (sha256 74d53b52565dec20…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_accounts_payable_policies_agent.py` first:

```bash
python3 scheduled_brief_define_accounts_payable_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_accounts_payable_policies_agent.py   # or on stdin
python3 scheduled_brief_define_accounts_payable_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define accounts payable policies Scheduled Email Brief — Builds a morning brief on accounts payable policies from Dynamics 365 ERP for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an unsent email draft

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-accounts-payable-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_accounts_payable_policies',
    "version": '3.0.3',
    "display_name": 'Define accounts payable policies Scheduled Email Brief',
    "description": 'Builds a morning brief on accounts payable policies from Dynamics 365 ERP for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an unsent email draft',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-define-accounts-payable-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-accounts-payable-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5988529fbfaec994',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/define-accounts-payable-policies'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-define-accounts-payable-policies', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where define accounts payable policies stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on define accounts payable policies for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define accounts payable policies, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on accounts payable policies from Dynamics 365 ERP for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an unsent email draft', 'example_request': 'Give me the AP policy morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly AP-policy brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDefineAccountsPayablePolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineAccountsPayablePolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefDefineAccountsPayablePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
