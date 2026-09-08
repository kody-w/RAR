---
name: "rar-cowork-cookbook-scheduled-brief-define-accounts-payable-policies"
description: "Builds a morning brief on accounts payable policies from Dynamics 365 ERP for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an unsent email draft"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_accounts_payable_policies", "rar_sha256": "74d53b52565dec20cc340fb9ffdac520669c949dfb7ec7086bc1d413bf97cca1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
