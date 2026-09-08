---
name: "rar-cowork-cookbook-scheduled-brief-perform-license-requirements-analysis"
description: "Builds a morning brief on license requirements analysis from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, plus a saved email draft and a Teams-ready"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_perform_license_requirements_analysis", "rar_sha256": "a8a73fe0149e13c819a9fb1b04d087c27f513c3968e45c6cb21b07d8f75f9f25", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
