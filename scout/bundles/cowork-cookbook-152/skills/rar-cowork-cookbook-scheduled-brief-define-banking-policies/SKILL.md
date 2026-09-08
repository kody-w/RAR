---
name: "rar-cowork-cookbook-scheduled-brief-define-banking-policies"
description: "Builds a morning brief on define banking policies from Dynamics 365 ERP data for legal entity USMF, covering top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_banking_policies", "rar_sha256": "0f90f7fd3dd39cb619fc016951930bd56c22fe74affe2f30b3b73f5d3c6b31a0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_banking_policies`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_banking_policies_agent.py` and in the RCI capsule.

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

Define banking policies Scheduled Email Brief — Builds a morning brief on define banking policies from Dynamics 365 ERP data for legal entity USMF, covering top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-banking-policies
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
      "description": "Dynamics 365 F&SCM legal entity to query; defaults to USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_banking_policies_agent.py` and embedded as the fenced Python below (sha256 0f90f7fd3dd39cb6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_banking_policies_agent.py` first:

```bash
python3 scheduled_brief_define_banking_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_banking_policies_agent.py   # or on stdin
python3 scheduled_brief_define_banking_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define banking policies Scheduled Email Brief — Builds a morning brief on define banking policies from Dynamics 365 ERP data for legal entity USMF, covering top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-banking-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_banking_policies',
    "version": '3.0.3',
    "display_name": 'Define banking policies Scheduled Email Brief',
    "description": 'Builds a morning brief on define banking policies from Dynamics 365 ERP data for legal entity USMF, covering top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-define-banking-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-banking-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0c02bd34dceb8766',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/define-banking-policies'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-define-banking-policies', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where define banking policies stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on define banking policies for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads define banking policies, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on define banking policies from Dynamics 365 ERP data for legal entity USMF, covering top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to', 'example_request': 'Draft my weekday 7am banking policies brief from D365 USMF and save the email to drafts.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a recurring (daily/weekly, e.g. weekday 7am) banking-policy brief for the responsible owner as an unsent email draft and Teams post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDefineBankingPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineBankingPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefDefineBankingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
