---
name: "rar-cowork-cookbook-scheduled-brief-manage-organizational-change"
description: "Builds a morning brief on organizational change management from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft emai"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_organizational_change", "rar_sha256": "69ed5b47bfb8c17b8aa9f1a52ee79eec0cc83932b48b6bcab0cea148d61228ad", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_organizational_change`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_organizational_change_agent.py` and in the RCI capsule.

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

Manage organizational change Scheduled Email Brief — Builds a morning brief on organizational change management from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft emai

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-organizational-change
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
      "description": "D365 F&SCM legal entity to query; defaults to USMF.",
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
      "description": "Responsible owner who receives the drafted email.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_organizational_change_agent.py` and embedded as the fenced Python below (sha256 69ed5b47bfb8c17b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_organizational_change_agent.py` first:

```bash
python3 scheduled_brief_manage_organizational_change_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_organizational_change_agent.py   # or on stdin
python3 scheduled_brief_manage_organizational_change_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage organizational change Scheduled Email Brief — Builds a morning brief on organizational change management from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft emai

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-organizational-change
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_organizational_change',
    "version": '3.0.3',
    "display_name": 'Manage organizational change Scheduled Email Brief',
    "description": 'Builds a morning brief on organizational change management from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft emai',
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
        "upstream_slug": 'scheduled-brief-manage-organizational-change',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-organizational-change',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '17f39110da193b0c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/manage-organizational-change'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-manage-organizational-change', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where manage organizational change stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on manage organizational change for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage organizational change, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on organizational change management from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft emai', 'example_request': 'Draft my 7am weekday change-management brief from D365 USMF and email a draft to the owner.', 'inputs': [{'description': 'D365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly scheduled change-management brief from D365 ERP data, drafted as an email to the responsible owner plus a Teams post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefManageOrganizationalChange(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageOrganizationalChange'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefManageOrganizationalChange().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
