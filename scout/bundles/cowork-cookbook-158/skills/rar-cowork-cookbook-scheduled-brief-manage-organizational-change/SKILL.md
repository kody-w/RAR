---
name: "rar-cowork-cookbook-scheduled-brief-manage-organizational-change"
description: "Builds a morning brief on organizational change management from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft emai"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_organizational_change", "rar_sha256": "69ed5b47bfb8c17b8aa9f1a52ee79eec0cc83932b48b6bcab0cea148d61228ad", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
