---
name: "rar-cowork-cookbook-scheduled-brief-manage-authentication"
description: "Builds a manage-authentication morning brief from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, next actions, an email saved to drafts, and a Teams-rea"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_authentication", "rar_sha256": "bb02830b03cdee5f51dac349051b3d9c0ebd9e588df41c639d116fe076b4d533", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_authentication`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_authentication_agent.py` and in the RCI capsule.

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

Manage authentication Scheduled Email Brief — Builds a manage-authentication morning brief from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, next actions, an email saved to drafts, and a Teams-rea

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-authentication
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
      "description": "Dynamics 365 F&SCM legal entity to query, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_authentication_agent.py` and embedded as the fenced Python below (sha256 bb02830b03cdee5f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_authentication_agent.py` first:

```bash
python3 scheduled_brief_manage_authentication_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_authentication_agent.py   # or on stdin
python3 scheduled_brief_manage_authentication_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage authentication Scheduled Email Brief — Builds a manage-authentication morning brief from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, next actions, an email saved to drafts, and a Teams-rea

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-authentication
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_authentication',
    "version": '3.0.3',
    "display_name": 'Manage authentication Scheduled Email Brief',
    "description": 'Builds a manage-authentication morning brief from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, next actions, an email saved to drafts, and a Teams-rea',
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
        "upstream_slug": 'scheduled-brief-manage-authentication',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-authentication',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '11d42babcb758e17',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-authentication'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-manage-authentication', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where manage authentication stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on manage authentication for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage authentication, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a manage-authentication morning brief from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, next actions, an email saved to drafts, and a Teams-rea', 'example_request': 'Give me the manage authentication morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly manage-authentication brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefManageAuthentication(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageAuthentication'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefManageAuthentication().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
