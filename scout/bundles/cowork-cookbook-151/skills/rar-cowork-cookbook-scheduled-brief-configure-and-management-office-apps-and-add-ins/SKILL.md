---
name: "rar-cowork-cookbook-scheduled-brief-configure-and-management-office-apps-and-add-ins"
description: "Builds a morning brief on configure and management of office apps and add-ins from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day average, next actions, plus an email draft and Teams-re"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_configure_and_management_office_apps_and_add_ins", "rar_sha256": "97208fafb9f51599d31d7ad7de38e53795370cf179c71ccb4c76264fdf0508dc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_configure_and_management_office_apps_and_add_ins`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_configure_and_management_office_apps_and_add_ins_agent.py` and in the RCI capsule.

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

Configure and management office apps and add-ins Scheduled Email Brief — Builds a morning brief on configure and management of office apps and add-ins from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day average, next actions, plus an email draft and Teams-re

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-configure-and-management-office-apps-and-add-ins
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
      "description": "D365 legal entity to query; defaults to USMF.",
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
      "description": "Optional run cadence, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_configure_and_management_office_apps_and_add_ins_agent.py` and embedded as the fenced Python below (sha256 97208fafb9f51599…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_configure_and_management_office_apps_and_add_ins_agent.py` first:

```bash
python3 scheduled_brief_configure_and_management_office_apps_and_add_ins_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_configure_and_management_office_apps_and_add_ins_agent.py   # or on stdin
python3 scheduled_brief_configure_and_management_office_apps_and_add_ins_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and management office apps and add-ins Scheduled Email Brief — Builds a morning brief on configure and management of office apps and add-ins from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day average, next actions, plus an email draft and Teams-re

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-configure-and-management-office-apps-and-add-ins
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_configure_and_management_office_apps_and_add_ins',
    "version": '3.0.3',
    "display_name": 'Configure and management office apps and add-ins Scheduled Email Brief',
    "description": 'Builds a morning brief on configure and management of office apps and add-ins from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day average, next actions, plus an email draft and Teams-re',
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
        "upstream_slug": 'scheduled-brief-configure-and-management-office-apps-and-add-ins',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-configure-and-management-office-apps-and-add-ins',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aeaa068e51f25869',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-management-office-apps-and-add-ins'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-configure-and-management-office-apps-and-add-ins', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional run cadence, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where configure and management office apps and add-ins stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on configure and management office apps and add-ins for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads configure and management office apps and add-ins, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on configure and management of office apps and add-ins from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs 7-day average, next actions, plus an email draft and Teams-re', 'example_request': 'Draft my weekday 7am brief on office apps and add-ins config from D365 USMF and email it to the owner.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional run cadence, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Use for a daily or weekly (weekday 7am) owner brief on office apps and add-ins configuration/management in D365 ERP, with a saved email draft rather than a sent message.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefConfigureAndManagementOfficeAppsAndAddIns(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefConfigureAndManagementOfficeAppsAndAddIns'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional run cadence, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefConfigureAndManagementOfficeAppsAndAddIns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
