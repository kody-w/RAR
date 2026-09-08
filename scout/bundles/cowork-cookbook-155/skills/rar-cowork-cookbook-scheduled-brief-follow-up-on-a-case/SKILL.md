---
name: "rar-cowork-cookbook-scheduled-brief-follow-up-on-a-case"
description: "Builds a morning brief on case follow-ups for the responsible owner from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day average, next actions, plus a saved email draft and Teams-ready sum"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_follow_up_on_a_case", "rar_sha256": "fb977e81e3bffb0b91581c72e0c36b910e72df57424945fe8995705ef6cbc16a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_follow_up_on_a_case`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_follow_up_on_a_case_agent.py` and in the RCI capsule.

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

Follow up on a case Scheduled Email Brief — Builds a morning brief on case follow-ups for the responsible owner from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day average, next actions, plus a saved email draft and Teams-ready sum

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-follow-up-on-a-case
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
      "description": "D365 legal entity to query; defaults to USMF.",
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
      "description": "The responsible owner the brief is written for and whose email draft is created.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence for the recurring run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_follow_up_on_a_case_agent.py` and embedded as the fenced Python below (sha256 fb977e81e3bffb0b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_follow_up_on_a_case_agent.py` first:

```bash
python3 scheduled_brief_follow_up_on_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_follow_up_on_a_case_agent.py   # or on stdin
python3 scheduled_brief_follow_up_on_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Follow up on a case Scheduled Email Brief — Builds a morning brief on case follow-ups for the responsible owner from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day average, next actions, plus a saved email draft and Teams-ready sum

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-follow-up-on-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_follow_up_on_a_case',
    "version": '3.0.3',
    "display_name": 'Follow up on a case Scheduled Email Brief',
    "description": 'Builds a morning brief on case follow-ups for the responsible owner from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day average, next actions, plus a saved email draft and Teams-ready sum',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-follow-up-on-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-follow-up-on-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2c1e209a6e82095c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/follow-up-on-a-case'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/scheduled-brief-follow-up-on-a-case', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'owner': 'The responsible owner the brief is written for and whose email draft is created.', 'schedule': 'Optional cadence for the recurring run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where follow up on a case stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on follow up on a case for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads follow up on a case, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on case follow-ups for the responsible owner from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day average, next actions, plus a saved email draft and Teams-ready sum', 'example_request': 'Give me the 7am case follow-up brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'The responsible owner the brief is written for and whose email draft is created.', 'name': 'owner'}, {'description': 'Optional cadence for the recurring run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly case follow-up brief for an owner, drafted as an email and a Teams channel post, from D365 F&SCM data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefFollowUpOnACase(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefFollowUpOnACase'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'The responsible owner the brief is written for and whose email draft is created.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the recurring run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefFollowUpOnACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
