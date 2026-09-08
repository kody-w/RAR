---
name: "rar-cowork-cookbook-scheduled-brief-identify-applicable-regulations-and-compliance-requirements"
description: "Builds a morning brief on applicable regulations and compliance requirements from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_identify_applicable_regulations_and_compliance_requirements", "rar_sha256": "3c1c58825e47c7f5fc37460c729366478f3981f583757eb6f9795e5020e9fa5c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
