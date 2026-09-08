---
name: "rar-cowork-cookbook-scheduled-brief-conduct-research"
description: "Builds a morning brief on conduct research from Dynamics 365 ERP data for a given legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (saved, n"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_conduct_research", "rar_sha256": "9eda8a52cff78bc401d8b8aa87803c3d810a6efeb63057aa77076a0c9d4b4df6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_conduct_research`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_conduct_research_agent.py` and in the RCI capsule.

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

Conduct research Scheduled Email Brief — Builds a morning brief on conduct research from Dynamics 365 ERP data for a given legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (saved, n

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-conduct-research
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
    "responsible_owner": {
      "description": "Person the brief is addressed to; the draft email recipient.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence for the scheduled task, e.g. weekdays at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_conduct_research_agent.py` and embedded as the fenced Python below (sha256 9eda8a52cff78bc4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_conduct_research_agent.py` first:

```bash
python3 scheduled_brief_conduct_research_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_conduct_research_agent.py   # or on stdin
python3 scheduled_brief_conduct_research_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct research Scheduled Email Brief — Builds a morning brief on conduct research from Dynamics 365 ERP data for a given legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (saved, n

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-conduct-research
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_conduct_research',
    "version": '3.0.3',
    "display_name": 'Conduct research Scheduled Email Brief',
    "description": 'Builds a morning brief on conduct research from Dynamics 365 ERP data for a given legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (saved, n',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-conduct-research',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-conduct-research',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2ebda6b1e7533a7a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/conduct-research'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/scheduled-brief-conduct-research', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to query, e.g. USMF.', 'responsible_owner': 'Person the brief is addressed to; the draft email recipient.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekdays at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where conduct research stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on conduct research for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads conduct research, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on conduct research from Dynamics 365 ERP data for a given legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (saved, n', 'example_request': 'Draft my daily conduct research brief for USMF and email it to the owner as a draft.', 'inputs': [{'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Person the brief is addressed to; the draft email recipient.', 'name': 'responsible_owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekdays at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly conduct-research brief emailed to the responsible owner, or wants it scheduled for weekday mornings.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefConductResearch(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefConductResearch'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'responsible_owner': {'description': 'Person the brief is addressed to; the draft email recipient.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekdays at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefConductResearch().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
