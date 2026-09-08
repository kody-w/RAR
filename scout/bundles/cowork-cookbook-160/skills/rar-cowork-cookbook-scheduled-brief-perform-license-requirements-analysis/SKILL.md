---
name: "rar-cowork-cookbook-scheduled-brief-perform-license-requirements-analysis"
description: "Builds a morning brief on license requirements analysis from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, plus a saved email draft and a Teams-ready"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_perform_license_requirements_analysis", "rar_sha256": "a8a73fe0149e13c819a9fb1b04d087c27f513c3968e45c6cb21b07d8f75f9f25", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_perform_license_requirements_analysis`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_perform_license_requirements_analysis_agent.py` and in the RCI capsule.

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

Perform license requirements analysis Scheduled Email Brief — Builds a morning brief on license requirements analysis from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, plus a saved email draft and a Teams-ready

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-perform-license-requirements-analysis
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
      "description": "D365 legal entity to analyze; defaults to USMF.",
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
      "description": "When to run the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_perform_license_requirements_analysis_agent.py` and embedded as the fenced Python below (sha256 a8a73fe0149e13c8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_perform_license_requirements_analysis_agent.py` first:

```bash
python3 scheduled_brief_perform_license_requirements_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_perform_license_requirements_analysis_agent.py   # or on stdin
python3 scheduled_brief_perform_license_requirements_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform license requirements analysis Scheduled Email Brief — Builds a morning brief on license requirements analysis from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, plus a saved email draft and a Teams-ready

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-perform-license-requirements-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_perform_license_requirements_analysis',
    "version": '3.0.3',
    "display_name": 'Perform license requirements analysis Scheduled Email Brief',
    "description": 'Builds a morning brief on license requirements analysis from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, plus a saved email draft and a Teams-ready',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-perform-license-requirements-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-perform-license-requirements-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4f7ba471010921ca',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/perform-license-requirements-analysis'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-perform-license-requirements-analysis', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to analyze; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where perform license requirements analysis stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on perform license requirements analysis for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads perform license requirements analysis, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on license requirements analysis from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, plus a saved email draft and a Teams-ready', 'example_request': 'Give me the 7am weekday license requirements brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 legal entity to analyze; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when an owner wants a recurring (daily/weekday-morning or weekly) license requirements analysis brief from D365 ERP data, drafted as email and Teams post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefPerformLicenseRequirementsAnalysis(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPerformLicenseRequirementsAnalysis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to analyze; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefPerformLicenseRequirementsAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
