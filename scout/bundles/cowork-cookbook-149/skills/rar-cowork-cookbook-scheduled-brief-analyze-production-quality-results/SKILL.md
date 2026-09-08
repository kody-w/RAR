---
name: "rar-cowork-cookbook-scheduled-brief-analyze-production-quality-results"
description: "Builds a morning brief on production quality results from Dynamics 365 ERP for a given legal entity and owner: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an emai"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_production_quality_results", "rar_sha256": "47c70c015e52b6cfc6e50787c036ae2ac0162cc3847a4e0e9cc5148c7ddcf1ff", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_analyze_production_quality_results`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_analyze_production_quality_results_agent.py` and in the RCI capsule.

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

Analyze production quality results Scheduled Email Brief — Builds a morning brief on production quality results from Dynamics 365 ERP for a given legal entity and owner: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an emai

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-production-quality-results
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_production_quality_results_agent.py` and embedded as the fenced Python below (sha256 47c70c015e52b6cf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_production_quality_results_agent.py` first:

```bash
python3 scheduled_brief_analyze_production_quality_results_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_analyze_production_quality_results_agent.py   # or on stdin
python3 scheduled_brief_analyze_production_quality_results_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze production quality results Scheduled Email Brief — Builds a morning brief on production quality results from Dynamics 365 ERP for a given legal entity and owner: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an emai

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-production-quality-results
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_analyze_production_quality_results',
    "version": '3.0.3',
    "display_name": 'Analyze production quality results Scheduled Email Brief',
    "description": 'Builds a morning brief on production quality results from Dynamics 365 ERP for a given legal entity and owner: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an emai',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-analyze-production-quality-results',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-analyze-production-quality-results',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e3795d4d75f29558',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/analyze-production-quality-results'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/scheduled-brief-analyze-production-quality-results', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where analyze production quality results stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on analyze production quality results for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads analyze production quality results, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on production quality results from Dynamics 365 ERP for a given legal entity and owner: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an emai', 'example_request': 'Draft my daily production quality brief for USMF and email it to the line owner — save as a draft.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly production quality brief drafted (not sent) for the responsible owner from D365 F&SCM data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefAnalyzeProductionQualityResults(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAnalyzeProductionQualityResults'
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
    print(ScheduledBriefAnalyzeProductionQualityResults().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
