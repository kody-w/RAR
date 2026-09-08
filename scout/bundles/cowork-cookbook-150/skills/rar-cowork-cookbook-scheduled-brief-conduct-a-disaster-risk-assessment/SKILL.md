---
name: "rar-cowork-cookbook-scheduled-brief-conduct-a-disaster-risk-assessment"
description: "Builds a morning brief on disaster risk assessment from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an email to the owner (s"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_conduct_a_disaster_risk_assessment", "rar_sha256": "bbdc6f73921c423613d93727ecf90ec57beb1c98bd4a12270ddd6b4e2ada8038", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_conduct_a_disaster_risk_assessment`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_conduct_a_disaster_risk_assessment_agent.py` and in the RCI capsule.

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

Conduct a disaster risk assessment Scheduled Email Brief — Builds a morning brief on disaster risk assessment from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an email to the owner (s

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-conduct-a-disaster-risk-assessment
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
      "description": "When the brief should run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_conduct_a_disaster_risk_assessment_agent.py` and embedded as the fenced Python below (sha256 bbdc6f73921c4236…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_conduct_a_disaster_risk_assessment_agent.py` first:

```bash
python3 scheduled_brief_conduct_a_disaster_risk_assessment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_conduct_a_disaster_risk_assessment_agent.py   # or on stdin
python3 scheduled_brief_conduct_a_disaster_risk_assessment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct a disaster risk assessment Scheduled Email Brief — Builds a morning brief on disaster risk assessment from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an email to the owner (s

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-conduct-a-disaster-risk-assessment
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_conduct_a_disaster_risk_assessment',
    "version": '3.0.3',
    "display_name": 'Conduct a disaster risk assessment Scheduled Email Brief',
    "description": 'Builds a morning brief on disaster risk assessment from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an email to the owner (s',
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
        "upstream_slug": 'scheduled-brief-conduct-a-disaster-risk-assessment',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-conduct-a-disaster-risk-assessment',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '90ddf5148fc693e7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/conduct-a-disaster-risk-assessment'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-conduct-a-disaster-risk-assessment', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where conduct a disaster risk assessment stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on conduct a disaster risk assessment for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads conduct a disaster risk assessment, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on disaster risk assessment from Dynamics 365 ERP data for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an email to the owner (s', 'example_request': 'Send me the 7am disaster risk assessment brief for USMF and draft it to the owner.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a responsible owner needs a recurring daily or weekly disaster-risk-assessment brief from D365 F&SCM, drafted as an email and a Teams post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefConductADisasterRiskAssessment(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefConductADisasterRiskAssessment'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefConductADisasterRiskAssessment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
