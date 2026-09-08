---
name: "rar-cowork-cookbook-scheduled-brief-analyze-rebates-and-incentives"
description: "Builds a rebates and incentives morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, plus an email draft (not sent) and"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_rebates_and_incentives", "rar_sha256": "a7f9bb96e4f9b38dedb92c5fff01d767c5ea534541b1b1a0032129aa3a90a105", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
