---
name: "rar-cowork-cookbook-scheduled-brief-use-and-track-project-materials"
description: "Builds a morning brief on project materials usage from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions; drafts an email to the owner (unsent) plus a Teams"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_use_and_track_project_materials", "rar_sha256": "a40b73c74de00f07a853c57264db8fb5cde1800dfc6f6e46ebacfcabdda2318a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_use_and_track_project_materials`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_use_and_track_project_materials_agent.py` and in the RCI capsule.

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

Use and track project materials Scheduled Email Brief — Builds a morning brief on project materials usage from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions; drafts an email to the owner (unsent) plus a Teams

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-use-and-track-project-materials
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
      "description": "When to run, e.g. weekday mornings at 7am (daily or weekly).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_use_and_track_project_materials_agent.py` and embedded as the fenced Python below (sha256 a40b73c74de00f07…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_use_and_track_project_materials_agent.py` first:

```bash
python3 scheduled_brief_use_and_track_project_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_use_and_track_project_materials_agent.py   # or on stdin
python3 scheduled_brief_use_and_track_project_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Use and track project materials Scheduled Email Brief — Builds a morning brief on project materials usage from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions; drafts an email to the owner (unsent) plus a Teams

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-use-and-track-project-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_use_and_track_project_materials',
    "version": '3.0.3',
    "display_name": 'Use and track project materials Scheduled Email Brief',
    "description": 'Builds a morning brief on project materials usage from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions; drafts an email to the owner (unsent) plus a Teams',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-use-and-track-project-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-use-and-track-project-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '626a475c3fefc7fd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/use-and-track-project-materials'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/scheduled-brief-use-and-track-project-materials', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run, e.g. weekday mornings at 7am (daily or weekly).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where use and track project materials stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on use and track project materials for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads use and track project materials, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on project materials usage from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions; drafts an email to the owner (unsent) plus a Teams', 'example_request': 'Send me the project materials morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run, e.g. weekday mornings at 7am (daily or weekly).', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly project-materials brief for the responsible owner from D365 F&SCM, drafted as email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefUseAndTrackProjectMaterials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefUseAndTrackProjectMaterials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run, e.g. weekday mornings at 7am (daily or weekly).', 'type': 'string'}},
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
    print(ScheduledBriefUseAndTrackProjectMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
