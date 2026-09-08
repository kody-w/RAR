---
name: "rar-cowork-cookbook-scheduled-brief-identify-applicable-regulations-and-compliance-requirements"
description: "Builds a morning brief on applicable regulations and compliance requirements from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_identify_applicable_regulations_and_compliance_requirements", "rar_sha256": "3c1c58825e47c7f5fc37460c729366478f3981f583757eb6f9795e5020e9fa5c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_identify_applicable_regulations_and_compliance_requirements`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_identify_applicable_regulations_and_compliance_requirements_agent.py` and in the RCI capsule.

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

Identify applicable regulations and compliance requirements Scheduled Email Brief — Builds a morning brief on applicable regulations and compliance requirements from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-identify-applicable-regulations-and-compliance-requirements
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
      "description": "D365 legal entity to query; the recipe uses USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_identify_applicable_regulations_and_compliance_requirements_agent.py` and embedded as the fenced Python below (sha256 3c1c58825e47c7f5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_identify_applicable_regulations_and_compliance_requirements_agent.py` first:

```bash
python3 scheduled_brief_identify_applicable_regulations_and_compliance_requirements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_identify_applicable_regulations_and_compliance_requirements_agent.py   # or on stdin
python3 scheduled_brief_identify_applicable_regulations_and_compliance_requirements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify applicable regulations and compliance requirements Scheduled Email Brief — Builds a morning brief on applicable regulations and compliance requirements from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-identify-applicable-regulations-and-compliance-requirements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_identify_applicable_regulations_and_compliance_requirements',
    "version": '3.0.3',
    "display_name": 'Identify applicable regulations and compliance requirements Scheduled Email Brief',
    "description": 'Builds a morning brief on applicable regulations and compliance requirements from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions.',
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
        "upstream_slug": 'scheduled-brief-identify-applicable-regulations-and-compliance-requirements',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-identify-applicable-regulations-and-compliance-requirements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'faafc366181f7afc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/identify-applicable-regulations-and-compliance-requirements'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-identify-applicable-regulations-and-compliance-requirements', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; the recipe uses USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where identify applicable regulations and compliance requirements stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on identify applicable regulations and compliance requirements for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads identify applicable regulations and compliance requirements, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on applicable regulations and compliance requirements from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions.', 'example_request': 'Draft my 7am compliance brief for USMF and save the email to drafts, plus a Teams summary.', 'inputs': [{'description': 'D365 legal entity to query; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a compliance owner wants a daily or weekly D365 ERP compliance brief drafted as an email (saved to drafts) plus a Teams-ready summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefIdentifyApplicableRegulationsAndComplianceRequirements(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefIdentifyApplicableRegulationsAndComplianceRequirements'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefIdentifyApplicableRegulationsAndComplianceRequirements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
