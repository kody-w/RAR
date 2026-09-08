---
name: "rar-cowork-cookbook-scheduled-brief-conduct-research"
description: "Builds a morning brief on conduct research from Dynamics 365 ERP data for a given legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (saved, n"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_conduct_research", "rar_sha256": "9eda8a52cff78bc401d8b8aa87803c3d810a6efeb63057aa77076a0c9d4b4df6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
