---
name: "rar-cowork-cookbook-scheduled-brief-conduct-competitive-analysis"
description: "Builds a competitive-analysis morning brief from Dynamics 365 ERP data for a legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, plus a saved email draft and a Teams-ready summa"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_conduct_competitive_analysis", "rar_sha256": "8bcadea32e12d1329cac9f39afacb7ef8637b0f58df92be96807c13d10208c46", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
