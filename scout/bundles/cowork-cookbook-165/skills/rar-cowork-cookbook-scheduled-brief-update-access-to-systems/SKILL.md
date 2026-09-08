---
name: "rar-cowork-cookbook-scheduled-brief-update-access-to-systems"
description: "Builds a morning brief on update access to systems from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_update_access_to_systems", "rar_sha256": "5c960f07235416e9c9ac1c0a999c6342bb7ea29f4a01aec1789df7befb687043", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_update_access_to_systems`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_update_access_to_systems_agent.py` and in the RCI capsule.

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

Update access to systems Scheduled Email Brief — Builds a morning brief on update access to systems from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-update-access-to-systems
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
      "description": "Dynamics 365 legal entity to query; defaults to USMF.",
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
      "description": "Responsible owner the brief is addressed to in the email draft.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence for the scheduled task, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_update_access_to_systems_agent.py` and embedded as the fenced Python below (sha256 5c960f07235416e9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_update_access_to_systems_agent.py` first:

```bash
python3 scheduled_brief_update_access_to_systems_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_update_access_to_systems_agent.py   # or on stdin
python3 scheduled_brief_update_access_to_systems_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update access to systems Scheduled Email Brief — Builds a morning brief on update access to systems from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-update-access-to-systems
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_update_access_to_systems',
    "version": '3.0.3',
    "display_name": 'Update access to systems Scheduled Email Brief',
    "description": 'Builds a morning brief on update access to systems from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready',
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
        "upstream_slug": 'scheduled-brief-update-access-to-systems',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-update-access-to-systems',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '74fb3b7355c44fcc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/update-access-to-systems'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-update-access-to-systems', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner the brief is addressed to in the email draft.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where update access to systems stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on update access to systems for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads update access to systems, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on update access to systems from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready', 'example_request': 'Give me the morning brief on update access to systems for USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner the brief is addressed to in the email draft.', 'name': 'owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call for a daily or weekly (weekday 7am) access-to-systems brief for the responsible owner, drafted as an unsent email and a Teams channel post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefUpdateAccessToSystems(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefUpdateAccessToSystems'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner the brief is addressed to in the email draft.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefUpdateAccessToSystems().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
