---
name: "rar-cowork-cookbook-scheduled-brief-manage-organizational-structure"
description: "Builds a morning brief on managing organizational structure from Dynamics 365 ERP data for a legal entity, drafts (not sends) an email to the responsible owner, and produces a Teams-ready summary."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_organizational_structure", "rar_sha256": "5a3f898e38a8983f54e223f33763e8a6f901c83885aa9b9b8f143b5b759d0886", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
