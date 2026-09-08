---
name: "rar-cowork-cookbook-scheduled-brief-follow-up-on-a-case"
description: "Builds a morning brief on case follow-ups for the responsible owner from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day average, next actions, plus a saved email draft and Teams-ready sum"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_follow_up_on_a_case", "rar_sha256": "fb977e81e3bffb0b91581c72e0c36b910e72df57424945fe8995705ef6cbc16a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
