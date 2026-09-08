---
name: "rar-cowork-cookbook-scheduled-brief-manage-organizational-structure"
description: "Builds a morning brief on managing organizational structure from Dynamics 365 ERP data for a legal entity, drafts (not sends) an email to the responsible owner, and produces a Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_organizational_structure", "rar_sha256": "5a3f898e38a8983f54e223f33763e8a6f901c83885aa9b9b8f143b5b759d0886", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_organizational_structure`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_organizational_structure_agent.py` and in the RCI capsule.

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

Manage organizational structure Scheduled Email Brief — Builds a morning brief on managing organizational structure from Dynamics 365 ERP data for a legal entity, drafts (not sends) an email to the responsible owner, and produces a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-organizational-structure
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
      "description": "D365 legal entity to run against, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_organizational_structure_agent.py` and embedded as the fenced Python below (sha256 5a3f898e38a8983f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_organizational_structure_agent.py` first:

```bash
python3 scheduled_brief_manage_organizational_structure_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_organizational_structure_agent.py   # or on stdin
python3 scheduled_brief_manage_organizational_structure_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage organizational structure Scheduled Email Brief — Builds a morning brief on managing organizational structure from Dynamics 365 ERP data for a legal entity, drafts (not sends) an email to the responsible owner, and produces a Teams-ready summary.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-organizational-structure
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_organizational_structure',
    "version": '3.0.3',
    "display_name": 'Manage organizational structure Scheduled Email Brief',
    "description": 'Builds a morning brief on managing organizational structure from Dynamics 365 ERP data for a legal entity, drafts (not sends) an email to the responsible owner, and produces a Teams-ready summary.',
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
        "upstream_slug": 'scheduled-brief-manage-organizational-structure',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-organizational-structure',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7a3013d6a17718c4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/manage-organizational-structure'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-manage-organizational-structure', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where manage organizational structure stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on manage organizational structure for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage organizational structure, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on managing organizational structure from Dynamics 365 ERP data for a legal entity, drafts (not sends) an email to the responsible owner, and produces a Teams-ready summary.', 'example_request': 'Give me the 7am weekday org-structure morning brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly org-structure brief from D365 F&SCM with top items, anomalies vs the 7-day average, next actions, and a draft email.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefManageOrganizationalStructure(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageOrganizationalStructure'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefManageOrganizationalStructure().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
