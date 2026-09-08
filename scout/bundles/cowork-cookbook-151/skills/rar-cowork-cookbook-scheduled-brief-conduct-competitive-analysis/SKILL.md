---
name: "rar-cowork-cookbook-scheduled-brief-conduct-competitive-analysis"
description: "Builds a competitive-analysis morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, plus a saved email draft and a Teams-ready summa"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_conduct_competitive_analysis", "rar_sha256": "8bcadea32e12d1329cac9f39afacb7ef8637b0f58df92be96807c13d10208c46", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_conduct_competitive_analysis`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_conduct_competitive_analysis_agent.py` and in the RCI capsule.

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

Conduct competitive analysis Scheduled Email Brief — Builds a competitive-analysis morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, plus a saved email draft and a Teams-ready summa

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-conduct-competitive-analysis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_conduct_competitive_analysis_agent.py` and embedded as the fenced Python below (sha256 8bcadea32e12d132…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_conduct_competitive_analysis_agent.py` first:

```bash
python3 scheduled_brief_conduct_competitive_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_conduct_competitive_analysis_agent.py   # or on stdin
python3 scheduled_brief_conduct_competitive_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct competitive analysis Scheduled Email Brief — Builds a competitive-analysis morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, plus a saved email draft and a Teams-ready summa

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-conduct-competitive-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_conduct_competitive_analysis',
    "version": '3.0.3',
    "display_name": 'Conduct competitive analysis Scheduled Email Brief',
    "description": 'Builds a competitive-analysis morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, plus a saved email draft and a Teams-ready summa',
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
        "upstream_slug": 'scheduled-brief-conduct-competitive-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-conduct-competitive-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '319001cc13b0f472',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/conduct-competitive-analysis'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/scheduled-brief-conduct-competitive-analysis', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where conduct competitive analysis stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on conduct competitive analysis for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads conduct competitive analysis, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a competitive-analysis morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, plus a saved email draft and a Teams-ready summa', 'example_request': 'Draft my weekday 7am competitive analysis brief from D365 USMF and email it to the owner.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly competitive-analysis brief for the responsible owner from D365 ERP, delivered as an unsent email draft and Teams post text.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefConductCompetitiveAnalysis(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefConductCompetitiveAnalysis'
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
    print(ScheduledBriefConductCompetitiveAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
