---
name: "rar-cowork-cookbook-scheduled-brief-analyze-rebates-and-incentives"
description: "Builds a rebates and incentives morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft (not sent) and"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_rebates_and_incentives", "rar_sha256": "a7f9bb96e4f9b38dedb92c5fff01d767c5ea534541b1b1a0032129aa3a90a105", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_analyze_rebates_and_incentives`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_analyze_rebates_and_incentives_agent.py` and in the RCI capsule.

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

Analyze rebates and incentives Scheduled Email Brief — Builds a rebates and incentives morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft (not sent) and

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-rebates-and-incentives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_rebates_and_incentives_agent.py` and embedded as the fenced Python below (sha256 a7f9bb96e4f9b38d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_rebates_and_incentives_agent.py` first:

```bash
python3 scheduled_brief_analyze_rebates_and_incentives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_analyze_rebates_and_incentives_agent.py   # or on stdin
python3 scheduled_brief_analyze_rebates_and_incentives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze rebates and incentives Scheduled Email Brief — Builds a rebates and incentives morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft (not sent) and

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-rebates-and-incentives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_analyze_rebates_and_incentives',
    "version": '3.0.3',
    "display_name": 'Analyze rebates and incentives Scheduled Email Brief',
    "description": 'Builds a rebates and incentives morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft (not sent) and',
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
        "upstream_slug": 'scheduled-brief-analyze-rebates-and-incentives',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-analyze-rebates-and-incentives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f5b504ceaef7dcc8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/analyze-rebates-and-incentives'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-analyze-rebates-and-incentives', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where analyze rebates and incentives stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on analyze rebates and incentives for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads analyze rebates and incentives, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a rebates and incentives morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft (not sent) and', 'example_request': 'Give me the rebates and incentives morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a rebates/incentives owner wants a daily or weekly morning brief from D365 F&SCM, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefAnalyzeRebatesAndIncentives(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAnalyzeRebatesAndIncentives'
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
    print(ScheduledBriefAnalyzeRebatesAndIncentives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
