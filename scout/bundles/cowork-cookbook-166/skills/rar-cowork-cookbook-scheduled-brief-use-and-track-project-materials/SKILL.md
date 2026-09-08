---
name: "rar-cowork-cookbook-scheduled-brief-use-and-track-project-materials"
description: "Builds a morning brief on project materials usage from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions; drafts an email to the owner (unsent) plus a Teams"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_use_and_track_project_materials", "rar_sha256": "a40b73c74de00f07a853c57264db8fb5cde1800dfc6f6e46ebacfcabdda2318a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
