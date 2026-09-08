---
name: "rar-cowork-cookbook-scheduled-brief-update-access-to-systems"
description: "Builds a morning brief on update access to systems from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, saved as an email draft plus a Teams-ready"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_update_access_to_systems", "rar_sha256": "5c960f07235416e9c9ac1c0a999c6342bb7ea29f4a01aec1789df7befb687043", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
