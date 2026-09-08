---
name: "rar-cowork-cookbook-scheduled-brief-analyze-production-quality-results"
description: "Builds a morning brief on production quality results from Dynamics 365 ERP for a given legal entity and owner: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an emai"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_production_quality_results", "rar_sha256": "47c70c015e52b6cfc6e50787c036ae2ac0162cc3847a4e0e9cc5148c7ddcf1ff", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
