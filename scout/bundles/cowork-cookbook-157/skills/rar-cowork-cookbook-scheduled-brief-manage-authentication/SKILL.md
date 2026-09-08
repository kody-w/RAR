---
name: "rar-cowork-cookbook-scheduled-brief-manage-authentication"
description: "Builds a manage-authentication morning brief from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, next actions, an email saved to drafts, and a Teams-rea"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_authentication", "rar_sha256": "bb02830b03cdee5f51dac349051b3d9c0ebd9e588df41c639d116fe076b4d533", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
