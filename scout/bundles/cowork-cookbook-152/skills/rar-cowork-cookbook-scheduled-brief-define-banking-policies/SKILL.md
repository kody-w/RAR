---
name: "rar-cowork-cookbook-scheduled-brief-define-banking-policies"
description: "Builds a morning brief on define banking policies from Dynamics 365 ERP data for legal entity USMF, covering top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_banking_policies", "rar_sha256": "0f90f7fd3dd39cb619fc016951930bd56c22fe74affe2f30b3b73f5d3c6b31a0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
