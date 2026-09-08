---
name: "rar-cowork-cookbook-scheduled-brief-drive-app-value"
description: "Builds a morning brief on drive app value from Dynamics 365 ERP data for legal entity USMF, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an owner email (saved, not"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_drive_app_value", "rar_sha256": "e82c05b7c763b504c4b2a6469b48f0b0f51d7cbe071b72ae6ca768b7b6afe8af", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_drive_app_value`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_drive_app_value_agent.py` and in the RCI capsule.

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

Drive app value Scheduled Email Brief — Builds a morning brief on drive app value from Dynamics 365 ERP data for legal entity USMF, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an owner email (saved, not

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-drive-app-value
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
    "responsible_owner": {
      "description": "Person the brief is addressed to and whose email draft is created.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_drive_app_value_agent.py` and embedded as the fenced Python below (sha256 e82c05b7c763b504…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_drive_app_value_agent.py` first:

```bash
python3 scheduled_brief_drive_app_value_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_drive_app_value_agent.py   # or on stdin
python3 scheduled_brief_drive_app_value_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Drive app value Scheduled Email Brief — Builds a morning brief on drive app value from Dynamics 365 ERP data for legal entity USMF, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an owner email (saved, not

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-drive-app-value
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_drive_app_value',
    "version": '3.0.3',
    "display_name": 'Drive app value Scheduled Email Brief',
    "description": 'Builds a morning brief on drive app value from Dynamics 365 ERP data for legal entity USMF, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an owner email (saved, not',
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
        "upstream_slug": 'scheduled-brief-drive-app-value',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-drive-app-value',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '95e4f1a9f78d504e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/drive-app-value'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-drive-app-value', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'responsible_owner': 'Person the brief is addressed to and whose email draft is created.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where drive app value stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on drive app value for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads drive app value, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on drive app value from Dynamics 365 ERP data for legal entity USMF, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an owner email (saved, not', 'example_request': 'Give me the drive app value morning brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Person the brief is addressed to and whose email draft is created.', 'name': 'responsible_owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when an owner needs a daily or weekly drive-app-value brief from D365 F&SCM, delivered as an unsent email draft and a Teams channel post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDriveAppValue(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDriveAppValue'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'responsible_owner': {'description': 'Person the brief is addressed to and whose email draft is created.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefDriveAppValue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObWJbmX9G8/SEzG9uITQh3dMQgQEhC7GIR6Qon+74vEsqp/z4X6bUzsyqrqypiPo0ctgTcs5/znHN9+fXNHYek7t4+v+mhW614tyjSJOxWbhWsmPpWdzn4qnMP/F35dTV0qTcOdde/fXgLwt7v0mZI6wqQ78a0CPqVuyrrrkqreOV1aRit6moVdOkUrtymWU1uMYarqKvLFTtXbpn6/QrbECtOU1aBO7irqO5WRRi7xSqshnSYV4Yu7j8AwVPYLTyHulkRq3QIy37lzau0bFx/+ACUrUu3SMN+NfWrIQlX5MfAnVddDYwBVC6gduPww9OoKrwPK0AFtO4/LIsXBd1oAKpXq/pWAdvD0k2L1Y89oAs+rKp6AMaGd7dsirB/+/zzXz68AcHF2+df3/zC7fvFd34SBmMRBrvFaHYxmG4aczEX0BZuFYNFzQw8XYHrJuyAoSW4FQAPvV/92IdF9GH1n/+Z39wu7n/6/KVavX++vC1/tLF62jbUbj+Ewcp3G9dLC+ClTyu6uLlzv+rCYeyqJQj9sPjr04vyN07Aff+9PPvxJeRTHA4/fnmrgQru4pAvbz+tQAS+vHXj8vvTwqX58adPRX0Lux9/+o1PP3pZ6A8LM6D1p6/v1+9swcLflqbR6quucMy7rC700yYEzH9n3/J5qf7O7t0lX1+Lf6ybD6s/57zY899A31cqeoDvn7MFPgCUb5+yOq1+fJfRgaSq3MoPf/zpH7EFUfXzIu2Hf4nvzy/GSegGwFvvLvnpwzN8f1lB77Z95/mPxTYgYf4dS8Dyb+K+O+of8X5G9m9YgyIBpfMtln/K7s8IoP9e/fwPbfufCD6soi9vbFikS116Rfh59eszRX7+Ifjt5g9/+Stg/U/Z6PXY+U8OX0u3SqOwH75+/fmH/nn7h7/8/MPYgCwO3fLr2BV/xvPP/PqU8wcPvq/68Y+0QL5R5RVAjdX3Glr9Wjf/q/vrpxWo/jT47X7/efX7Slw+0Gox4pvQlwt+V4090PV3fvzp7a8AeCpgzfhCL4Af//EfKzH1u7qvo2Gl+/U4rECAh7QMF+UvSdqv0hcidiHwa58Cx76vA/m/RHjRuI5Wv/xv/wn2H/13sIf7b5D29QnkX58o/hWg+Ncniv/yaXUBbOsujdMK4LVGK8qXCqBsNSwimy7sww7gJ4DpIfwIqvnj8mOVVqtf/gnnr08mn5r5lydepy/U05jjgng9oPu02GYtwP2yxAfAHd5DfwT8i9oHykQpQOoPwOa+LkDrGRY/9HlaFKsgBZgC+tf85A189Xlh9ssvv3hun3ypXhCNrV6NrYfBgu/qrD5+BFZFRRonw5cq9JN69cOvf/1h9X9W/xPVk/kiQwGd4j0SQMOTLksrUFljCZaBIIGwAth4RuLXv777FrBZutHS+qKlty3EIDPzMPjmaP1Af0SJzcoLgYPDpR3W3bB0vHT4tDpGq+/6AqHLo6UzJHU/rIKwCasgrPwZcHWBOd89Cbrdqgfp10fzh9XYh0+pv3id+1SxBCXuDr+sREYBfaguwD+Lms9FgLiuUuD+72nwug+YdD/0q903Fp9W0pKLq8bt3Cbp3HcZkfuKC+g/38gBcxf069uXaum34eKqZ2G83AMWAc/47yH9uMQcDAolQIGg/yb7ucZduuXl2TW7L1X/nvRut4TiOVnMq3hMg6UV/Nd7SvVJPRbB039A04XTexSC96g8c5D9m8Hm+xSw4p4TxHMYWH0Z0TWCr/5/no8WZ9A8r3E8feHYFSddtOsrSMvIuATzNWUuGi8mPAvyt/nlG0Z9g+ovVZGCjOvm/3qtfIb2fc0L/sYOOFmjtSd/kFdAqYXvM+2XNO66xVj3S/WtJwDbVk8ABP4GGAFqaEndbwKXp980TQAQLNe/zQfPNOmCxTsgtVfN6BUg7aIwDDzXz4FW3VK672EGNRAuZXxLUj/5g1VLyECqAf5L0FPgUODNT99x+vX0m+p/IHyNQQvJc0QcQeV2TwZAj3BRcInbLR0AgLnDa0IHdn5+MgFmlM2w2O6B2ik/vN8Mu7Ad0x5kyivIwK9hAyD64/L9snS5G94bUC7AWaAomhF491lGS86UYMgBOgAkAVVVphVo+sAp7054MnTLBRMA5r5PpS+Oz9vvBoXP2lu61TfCxZCFZhkAXnXgVvPvoePyZ2kC+JXLiqfcv82079IW3gt89gACgcRvT1+TwqdXs39NE6tvfD//3Rbox39vl/Rs38YfE+DzKhmGpv8Mw6+W+63jfgLgBb907X/rvh+fMPHxiREfAUZ8fGLEH9i+LP68+vdU+wOL99L4vEI+rT+tl0fn99R6/wBPMB9314/48vRLpYW/ISsQD9BlWJC/mBfU+dYGvy0BvTDuAGiBxa+22C/d9AaQ5dkHQBC+VL/P9aXWQJup4iU3+/p3GPCcB0Dev2L2vV2BR9UAZAfL7BiHn5Yt16J+H759rsai+PAGsDT8p9u0pSGVSzr3y9YOFA4YxIY0fF490eE+LD//uO2Vnz/c4tOKDQESFf3vU+69jSxt9HeV8TIRmOYDCR8WYAcFD7IRmLgIX6rK7UGaggxdTBnmZtH9taNbZsBnA/j6agB/r9AfGscfegUAvHYMF1QF2053LIAjwa2lg/ypmO9z6N/LsMAQsNAG9eelH354RxnwDfYOoB192wYA4943ZouEsBrBnvfnZQuyePtJsvwANODrO9H3/1nwwre//IleYKprQG9aRtmvz3709/opwI31awJ4dVmQQG4QAMr+BfxPwASTUPjey54dblnlgyQEefqnDvlWk/84CUBGBs+q+Q4u3yeCAYT0wyr8FH9a3cIwX9rv+yAAVBtWpFv+icyntQCnQbdbHPdbRH7zS/3cpy3qAT8Or/9W+PUNpLG7DAzvifw+6IPlANY+9suIA4NKBwLB9asmwbN/dwvwTt4nLphBAX24Rf014ZE+ucE8Yo37uIe6G3xDefg2WnvriEAC0vfCNYl4JOqGG98lN1uP9DZuFG7dCPB7FfbXZYxLF5UWfYAnPgJsCH97DG4F77a8dF8c9X3Hsdj8btKvb94GBysPeH+kXx8GphAPxknv3tmQvd7ei5s1NnvQPhhntKZqc5y8ze72MFKLI4WrMKhH+Jj7aq9djv66HJLeoCPgm+sJKrBH/DgdDXvoBgzHMndHQ5AuokH5qOEpkn2RtKtww+XahAQM0RX4mZCE9BIll9w06/R8Dxg409jbeO0MDYYzD9vamZDj6dm9XJ214TbIeCeKwBFaIcw4VCN966LOHea72b7AIMBvA0UpUNVo77Paaq2AiAnXnUd2PpIUtI3Y6+UaOeFe1x+Pw+lub/UCLce7Uid4tR1vFV06TjU6d649U0hryLMFVXk0H491r1updednwryoI9dWG4PuxLSTjAca3zxzN+rljdoHRdHGbQLx8SWzK+0iaI6s1VQ4kVsqUKqMwqFIF8JomlDqCkHhcShu6W3oTS5pMcHee1ok5wyRksbR0UnbN87KtZMrYQiKOtSgQrx0auIedqgXn3LCUFSVbTumZ9oMo1zFPu9JfmBEnSdCKNzvGX9/UPXQrM+UhNcPPbAhhuNTX9c1J7weXEfyJw3F2kjeFBh1GEJV4JsLJxZMYpaaobt8uCcGg0wNfjbS4TpPIhMemX263ThOm+so54SkLN2RRy6XQoznJX4LVOKg1tnWnVz7UtoRUmXTpT8IvkC0cd4josmXOdNs5LOeuXxRAScS2BEpLc2bx5nXzkV9oEhY1tkOtRxvjtBr2BosZfdXh+TFganmNupu1ANqRkWnYTNB5v3J0Q3TMkPVLSZxU5y3jUxlfAwfC6EQJufOj9J9FoLqah+VdNvnN59IakRXyjZCBbr25DjpdYXL0QySCmji5A4RWTy+ljvVQ5Pe3lT93pGRBlSLQ22G8qQdJYQk1WsTJEPUDo+2Tk2JoTgexjVkf7av7YNkj9152tlBd+Bh9Dxr/SGpUAneqhvhhFfUMVTRTkn79V45wmei27r2tbCsscCH/byTWHm7VXoYY7y9OgX0+upvXVa+KrsDT9+cx+7WON3l3NsHz5/NqyDFgkfeSLjCtrKnII3dRxTLoNHjnsHytD2c11a5Nq/5qAvorjnSaZ+ZhpIwt81ZFrbIcdjoDIOhtzOdiAecCyM7qghalGlkn9pFhjwOTUMLweMc5GnUPo7FWo5xYrxwJsyI+ylOJRMtT40u1Q2VMcmOpIO7ygXX2yG2YwBazpo5UsbYRKFRxfuNw2P9ljlNTkGw6M4M2Qm6N0lhD6ALGzY9xNl1H+/zHT+feweZBiNOp1oNp80caeRB5rD86E4FNseY5PCm4cY2XHbSPrIu2QO7uBms1GGFN8O9fTy2wZ0v7FtnyHGPa5rP3i44ZhW51q7ZmOGP0aZ0bld744ZhG5ZaRs95q4OCn9kz6sKN5tx0TMjroCIjvDUD4Sxs2A1LqjubCHkb26PnrZT2csCdqkunwNU8nCB9W1+3pkszj769a8om5kQEt/XY6KL1em9nLpwzQx6zFpeFI0Gp+AayuD5IZm+jsNNagk5mvm22W58sR50RODsr5LXqHzv2iKuPwo9Ou4wlY+boHix+T8788SFjJeHyHCNsH5XB33E64G5jwxOnIkSrrm8ibcwOEnmdjoWD37ZSIrMEujnpPewGvAZzubk3Tih5uENKy8kzsfbZY5snNU4jR9LYtJSm1I3U6ROIdoixI2lMoXjJRb2K1NQ8hAf/IqraJCEcDW9PRH4/DfhME0fY0q7iMOOHGlXNUo5Ja7yEaD/vgi0u32UlumvXnczDOW7ugntx8ndieu6PybmQ2B0pHMFAU6RkCNV2avF6fjJL2xAH18K2j01xdOqMvxKKSl5Egc8cC0MNf8fku4cQ7FSobuP+hu8EjpxGGktmPrWFjmbWZpZR51byTfUYujcFP4CUNWNEVGxHnHy7RRxgKb0nLHzAU1KWmflh6Z4TcuLgwEq1RwNpwh63omQKoxp5/3aSlHxdz/qUJzQZR7qW3FSjjlOs3cKEyCPFmoyG3Z6rhFqhENtGUSg/wG6kYIeNsqE6tKuGk7zdtRJB1KGuqAm9GxD9zovYA9XTfbhvJqniro5B74jogJ8m+nJE4N0Aqri6nTf1GoM2HcfvMPWRIHdZPyJNyUmGuN0hB5FxG1ET2JzTVIfN0tIZ+CK2S+8hx2hfnXkjWOOKrTPSqawVwn90gaDasL8LeuNwavHjRsdnZW1d/CytFdm3rvmWd2ORKkZXsm/kSOyNY6wbUgelJ5nLOgu5pFztnalyJ8s8J97dBz7k96sbod5s8ukD9RtzO1UmeqZ3Zhb3nM4etOMhOUBXQ6KmPEydkdsdLpeKkr1GvseNfvc14THf6MQqXFe7i1RrY4SE3LP4bJk415CKqWOFdtpymGYpx/5s+wQrC7tdfNp2JisZIxHr6DHxTIqeef4u8IJtrkdNgM+VP2unvBPuiaMNF4lj1Cm+FNsoRmaBwI/ayWnCgzzXCumskyh0ZnrnbZt2zuS7cCq126DqMe3TYmBUniNMw71gdNGOk+vZ4nLR4y4CummITlc1yeNKl78eet4v8SRJYawJW9zjksvoTbuBEqNhwweK6u3FGXIfmNs5R1tONtKu2W1O56rMzsqejmV7PoylZhUhNyuHgb/kUa0Ko34q7gVBkoED6TcWyvCBKTT6LObXukFvnkg3dMHJdK8ybS2cBGdzYrcP7tCX5wPfuVlrw+4xUY7Ijlnv4cMZGk/8noVTTnSITX7RqEktjyXq08IAj9c0vZEgHkYnsyzLYFJvP266VJgctw/t2YvQ3alZSwC2aowTdJ/3zDWsPLL1A9v3VM2dGa+aw8ZNs7Hs4zW+Ic4Gn4HxKWdQFz9JJ7RLGVVOxluDw6kB8xZV3mzOMpIhdwraQJvyDvfbaXMM1nsENWMrFjj3ht5cDY9n86Fdob45Ef4wKpHSTxTkT4auqeGu47LMhrM8ZSXVdFtPT2QTSYK4Ds2zrdHXu39QBRSgSoRGV1pvPJJTp3KrOHBeXaSYcY5MunNm04io8zZ1SCas0ysyeFzK2owE2XgE+zkzDwJN1SVe28mxHjBKcUnzsCc2rLQ9piomavvNOqauPGrvgja/m+sMph59tpX9/pbtFC0GDblxNPUorEVLZXQAQSk3OYOBun2zI0skEIk2yiIx3Hf5HfQJVdW7gKCRk1lbJ9oqm42+ufq0mZ97V3RMz8dZTKfjmb9KrFU0Z1JtdlEoISEljZMaJgi8AZNfvPf5bexzoDx6lRIzodGoHCOQbFAOa36iCf1+CnGjoF3Exw47h60g27jqd3RSAarLGA2THt4ED7ZeM26oMbOO7Gx7DazJJSsWMeUq6jvidiIsivLdytiZdj5kIX03prvkxNXJ327GPEuankabcTRQfnaanEY1miFDAYkfBH08Z6pPzzYq5pbEpFAmtVEoqCYdS1cVvznYurveHdbYST3Sqi0rEKKQnyEtzM+UPx8v3AE4vyzW+rVlUE0iG+oh4QNwC6LfIFEhCfgeHwKwoTgH85V8xJtKELgggk7u4XqOWszVRX2chshfX/m6RjZqpYcYto+DTZw6XIHoBMOdMIqY3aYdLjZ9beEp1bS6NNXLrfKzxj9sTxeIJ8XH3rmQVRRSwbiedV+MHz1FXcjNwQ1pRvSv9u7IYUwhhI1I4413gS/HQLjSB6KKm/TI9deJdt3DsRWEcBzTGSWLu2ViA0WpJVKYflldEZNh9xak5Y8rJpqMwVBagcxY5O9ZngpvdUGIvri78USKHplzNtlW53s4fw4Vlj5Rpp5zGKEO/gRRJjquizZsXUG79KzjTUcerzsnyPvzbSuskZTvmDHhDDik91iyvwjGxTMuIdYUEXzA1o9axxImH8MIBJg0NwdKmUrpylcpxl6iCuag+hxDKu0Zd4vTuXS0pVPl1vop2JM3RiMoL0vAGGc7cThWd6lge/Ze1w+WpXu2hltIHzBZcZzSYJXxYeGUT7UGyQplFVXaru3v+9kQKO1IoFdQv7Gmxqa5AWL9iXFz3hnbAa2QrIKRziQY38hN32Di9vggqkEmqN7FoDrq3foga0aUHJx4PVeBoSEAg7d4fxEQiQ+6yzb1H7RQH3WOORgVY6LFlBQot6fs8+HOS/XDhI7SI+uk9pGX8VE/77cFSGgpsw5tjsvFOuof4xRlTnXI2N3lenas25VzbFlayxqP1NS4LlWfbC8cPsiRe2NyQ2dy0w5UsG2dd/6NNE6XBJlqfX++7kq7mNHd4BzOG0Xsdnst6Owtk6i1PnoOKu3mbYBQ7dX2JJFu5ctska0LefI8Qh1/YigmU6KZZS9B56J3D8w4YJ+TVpOzRhKPp1AtmEKSNK/RmTzzm4dfGV3QBeeDhN47hW3MsaAQZpo2ICs0GRohcsDK0QwlgkLtFgapX5ihtzk/ugxS9NnaWEMYhMShVAJbCYTR6Q2UQiPuiDdMK4goku+HW6Xq8gOxaMSzIFclbgfFaftiK9dqZLljZ9VXG1LrtVTXipMnHdXD1w3tGDu/dIL5fuRLo7NMRmqGCDaEKonTtWwSViQIqtzJW7ty1rcWvlrTDntYdnXio9PBQYV1dBBJcfPwaOE2RxdlLTun5ErGHhzwulcrMA5R8E2D7kbeKHZZwPARxnGaL3aYdwW7PqLoA0M2TgJyHvSdO6QnZxtsRLLdzV5hk6dSliaIwzN7HY6ICrb0ERejIS9zUJIDJM5rjcSKSwXNzmXjBm504B/7W1gGyZZNLy2J5Bv2MR2nm8wm64M0hg+58pE718pSefFFBeykm1OJiyMm253j2Q4Y+nkGW0fUBrYNzM7Q05YiW7460OsNGbBmTiuu2UxMq/o7SNhSlkqV6wtSXehJsuZuxl1qYhKXv687tnCVNd5RdjVccTKJCT45nsCe8b7bQyObINRm3T36B1ZwF9yEbTdWBL3NHO3cpTN/7z0X3cqF2/IgFW4i2IP7/v1ITpXoTlu2H3BC3lXO5OkWXkVpJEunrWpeeo03SjU9okdEzg7UPsBwzbSSI7+LWXE8dxhy14KLNteYpFy0s7Z14ilz711PixxFl1NFy9lJuknbU40P2j2r94+Y3vXTPuDQdq4TDBpArpJwSFHYw4eNM3G9r+MrJrDKhpTufHII4zNTtti1vSmP8FA4lAkdqPG2N51tDI2kkj1I5HA0MXIrhDZReXQfoIR1LLu1XBMBdxYzRbMEym/KGxVlTZJzvkCN3UOMamiWK882TL8yCYS4Ev6RG08iNvk8Km7vW550DcSL4oNfpR164iGoh53UOqOzlfm2m94DACCDVJIXjO3XHDG36QiZlhQiiGuGZ5ZTZEJn2bVdHdbOaNMoARova3KK3pDSkRAvM40PB1i4Thddl3I5wQIuzQ5t1Wra2LKd0YlMEd12ZIJCEKeyFb7uoqEhSMEhKtLwIXkLjZK0jkRlC99xt4KrQ7WWOFgpqYCzEWnetNmWXCsPqjlXx3DLbDtrwohCTPyor4bI6RxjT0lwt0YzzQthAbdal6BEa8jlSQz2U8LaiYCc1E6VIxIFA4mcu2LS4gS1Od7tQJTsYyVXRwhgybaqIE2jVP96IODcvTn6aVO6ubrOW2N/JdHIDxPGn6dH7gwoKdYNrCBEvLduQmMqm7Oa7MchMu8AVyswYDPlYcu4nipCIaztYpfIM8mojhg07Zy9sR7LAWaO602ukMMeDOBQjp0vF71hxWuKncFsumvswbQYaY6AmneblEJS46P6tD48iuGuYyfu1B64HWZSsSLp+EFUrvjBKTSqFo96BkGwcYdDfXKDTICFNKYsHvGm7TRnsE7R7bm3Ngoz1MM0HBKEjBqryGR7QEiX8vgNMhWdW2O6b8beoXIexH4LoKaocrmf11Cl3kY2xppdJ64p6oZQfN5N4bW79nszApP8FKX++bj2ixM0DjdsJu9nY6NiOY9YEh81NcNbDanHU3C9XiEB7c4Gle/HDaKcy/74CK3o6FvEbIf6XaCm66ZALhQ0NbSjEepEXdNzV+jwwzrTEEWh0BYP5chAAySDWm6ub7dkHUeOSnKJxO/8O3KD4BzDCrhuahbiNIc6Vv5eCMOAwa3sSg5nKtxcvIIY8Qem7wlPwJX9vkcesDmCruaj1DpZixB+hDwO1ze1NVfoPrlvS1UKz49eRZFTBKfDQFiBpt8hlL9QXl0pLkwyfhTsD9v4Ej4SPk3EYryvJ5XakWPyUOEN17OtpNoBgCHdut8SLp1MufUZaucRDq1m9WNkzd7MbA/ZOALRnB6Nj0bs4YJSwdq1PYslh53KUnt5uAHAlTOITdTJsvbRBk2nosLv1aRHFXsxG2y8oyOGCtSDsCnvrICEuZk1eqbuuExUNC6eq/4ijTemrC6PBsGuTeTnXLZBPWQ8tjMMdbGMQDmX+4O/1RwEHXHEfZjjYbjysNkN98k+TYpUKaKwNeGLqLjbbH++H0gSnUXXGbfSvOUnN8zZyhiItWLBQmZErnhpinYruXeOUxVMuJOFJO4M9WZKl51SnIK8xHaYP26KebuhdsypJi+q31Qimto52xjB4YI1h5kBvcEJTdYXTGINAA4Xg2E/nh1YIh9Xmu6pwYJHPgo396s4X+bQ5Gc96BSOfzyEjWDZ4S7cW9K6qdMmGXfZpViDerClyD9HMBRC7CUVhV3/yCgeeVzTG+40632c+R48Vrt5jfmcQVJ8yrtaMjtWs5FgOq2Y+6HIVZWm3z68LWeu7yen/+o7W8shzf+z86DXsc631zCeR4ehG3x+yvr8L2v0lw9vnZ8CfV4nXn0xxu+HR39z3vXxnxy6L8Tz6yWob6fBr9PlwY2X94Lf0ioY+6Gbv/Z18XwFA1B4Y7+8TNgv75v64Pv3J59/YwK44wavVynC7utQf32d9y1y02p5yyIM0t8u4/ejwA9vwfuJ71dsQ3wNu2ax+P1AHxiKfVp/wt7++n8BbwD+AektAAA= -->
