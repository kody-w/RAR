---
name: "rar-cowork-cookbook-scheduled-brief-manage-accruals"
description: "Builds a morning brief on manage accruals from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email to the owner"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_accruals", "rar_sha256": "f3075ff25d372038623b09cdd2f558eb17c78bcfeb2076a0b30cd044889624b9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_accruals`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_accruals_agent.py` and in the RCI capsule.

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

Manage accruals Scheduled Email Brief — Builds a morning brief on manage accruals from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email to the owner

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-accruals
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
      "description": "Dynamics 365 legal entity to run against (recipe default: USMF).",
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
      "description": "Person the brief is written for and whose draft email is addressed to.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_accruals_agent.py` and embedded as the fenced Python below (sha256 f3075ff25d372038…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_accruals_agent.py` first:

```bash
python3 scheduled_brief_manage_accruals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_accruals_agent.py   # or on stdin
python3 scheduled_brief_manage_accruals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage accruals Scheduled Email Brief — Builds a morning brief on manage accruals from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email to the owner

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-accruals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_accruals',
    "version": '3.0.3',
    "display_name": 'Manage accruals Scheduled Email Brief',
    "description": 'Builds a morning brief on manage accruals from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email to the owner',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-manage-accruals',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-accruals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f7224d7755dae695',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/manage-accruals'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-manage-accruals', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against (recipe default: USMF).', 'responsible_owner': 'Person the brief is written for and whose draft email is addressed to.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where manage accruals stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on manage accruals for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads manage accruals, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on manage accruals from Dynamics 365 F&SCM (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then drafts an email to the owner', 'example_request': 'Give me the manage accruals morning brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to run against (recipe default: USMF).', 'name': 'legal_entity'}, {'description': 'Person the brief is written for and whose draft email is addressed to.', 'name': 'responsible_owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a responsible owner needs a daily or weekly accruals brief with an unsent draft email and a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefManageAccruals(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageAccruals'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against (recipe default: USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'responsible_owner': {'description': 'Person the brief is written for and whose draft email is addressed to.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefManageAccruals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOjSJblX9G8NpvMbEWEJEAs0VZmwyYBYpMQIMgoi2QHsYpFLNn538eR9CIyq7K6qszm0ygsTALcr9/1nOvP+fXN6dq4rN8+v2mBUyz2TpYlcVAvnMJf0GVf1in4KlMX/F94ZdHWidu1Zd28fXjzg8ark6pNygJMp7ok85uFs8jLukiKaOHWSRAuymKRO4UTBQvH8+rOyZpFWJf5ghkLJ0+8ZgGj28Xuf2u0tPgxCyInWwRFm7TjQtek3U+fF21ZLbaLpA3yZuGOiySvHK8Fd31n/ACULHMnS4JmcW8WbRwssI/g/qIugRFAA+ce1GDlDw9j6sAr8zwo/MBfFMHQAn1mzZsP88Ri4ddO2AL1i0WQO0kGVngILPsiqIGtweDkVRY0b59//uuHN6BF9vb51zcvc5pmdp0XB36XBT412yw97CVf5oLJmVNEYFQ1Ak8X4LoK6rCsc3DLBx56Xf3YBFn4YfGf/5n2Th01P33+Uixeny9v879TVzxUakunaYERnlM5bpIBX31akFnvjA2wse3qYg5CAwJVRJ+eM79LAs78y/zsx+cin6Kg/fHLWwlUcGZnfHn7aVHWYL26m39/mqVUP/70KSv7oP7xp+9yms69BiAOQBjQ+tPX1/VLLBj4fWgSLr5qKku/1gJhSKoACP+dffPnqfpL3MslX5+DfyyrD4s/lzzb8xeg7zMVXSD3z8UCH4CZb5+uZVL8+FqjLu9B4RRe8ONP/0gsCKuXZknT/ktyf34KjgPHB956ueSnD4/w/XWxfNn2TeY/XrYCCfPvWAKGvy/3zVH/SPYjsn8jGhQLKKH3WP6puD+bsPzL4ud/aNv/NOHDIvzyxgRZMtenmwWfF78+UuTnH/zvN3/4629A9D8Vo5Vd7T0kfAU4k4RB0379+vMPzeP2D3/9+YeuAlkcOPnXrs7+TOaf+fWxzh88+Br14x/ngvX1Ii0ASCy+1dDi17L6X/VvnxYGQCb/+/3m8+L3lTh/lovZiPdFny74XTU2QNff+fGnt98A8hTAmu6JXAA//uM/FlLi1WVThu1C88quXYAAt0kezMqf46RZJE9krAPg1yYBjn2NA/k/R3jWuAwXv/wf7wH2H70X2K+ad0z7+gDyr08U//qO4r98WpxnfKyTKCkAap9IVf0yjyjaecmqDpqgvgOYcsc2+Aiq+eP8Y5EUi1/+ieSvDyGfqvGXB24nT9Q70fyMeA2Y92m2zZxB+2mJN4P2EHgdkJ+VHlAmTABUfwA2N2V2B4g5+6FJkyxb+AnAFMBf45MTuuLzLOyXX35xnSb+UjwhGl48ia1ZgQHf1Fl8/AisCrMkitsvReDF5eKHX3/7YfHfi/9p1kP4vIYKqOIVCaChoCnyAlRWBxgJ0M4cVgAbj0j8+tvLt0AMIJ8FiFsSzhw3TwaZmQb+u6M1jvwIbdGFGwAHBzM5lnU7M1/Sflrw4eKbvmDR+dHMDHHZtAs/qGYmLLwRSHWAOd88WZTtogHp14SAX7smeKz6i1s7DxVzUOJO+8tColXAQ+WDJusXL4HJZZEA939Lg+d9IKT+oVlQ7yI+LeQ5FxeVUztVXDuvNULnGRfAP+/TgXAHcHX/pZgJN5hd9SiMp3vAIOAZ7xXSj3PMFzPFg8A272s/xjgzW54frFl/KZpX0jt18OgJgCrjIuoSf6aC/3qlVBOXXeY//Ac0nSW9ouC/ovLIQelvGptvbcCCffQQj25g8aWD1htk8f9xfzT7gtzvT+yePLPMgpXPJ+sZo7ljnGP5bDJntUGiPuvxe/vyDlHvSP2lyBKQcPX4X8+Rj8i+xjzRr6uBkify9JAP0grEaJb7yPo5i+t6ttn5UrxTAjBx8cA/4G4AEaCEZgPeF5yfvmsaAxyYr7+3Bw/P1P7sJJDZi6pzM5B1YRD4ruOlQKt6rtxXlEEJBHMV93HixX+wao4byDQgf455AnwJfPfpG0w/n76r/oeJzy5onvLoEDsQovohAOgRzArO4euTFuCX0z4bdGDn54cQYEZetbPtLiid/MPrZlAHty5pQNo84wv8GlQAoT/O309L57vBUIFqAc4CNVF1wLuPKppTJwc9DtABAAkoqjwpAOcDp7yc8BDo5DMkAMh9NaVPiY/bL4OCR+nNZPU+cTZknjPz/7MMnGL8PXKc/yxNgLx8HvFY928z7dtqs+wZPRuAgGDF96fPRuHTk+ufzcTiXe7nv9sB/fjvbZIe7K3/MQE+L+K2rZrPq9WTcd8J9xMov9VT1+Y7+X58oMTHJ0R8fIeIP4h9Wvx58e+p9gcRr9L4vNh8Wn9az4/EV2q9PsAT9EfK+ojMT78Up+A7sILlAci0M/Bn4wxB7yz4PgRQYVQD5AKDn6zYzGTaA1B50AAIwpfi97k+1xpgmSKac7Mpf4cBj3YA5P0zZt/YCjwqWrC2P7eOUfBp3nHN6jfB2+eiy7IPbwBKg3++TZsJKZ/zuZn3dqByQCPWJsHj6gEPQzv//OO2V3n8cLJPCyYAUJQ1v8+5F43MNPq70njaCGzzwAofFj7wTDPTHrBxXnwuK6cBeQpSdLalHatZ+eeObu4BHzTw9UkDf6/QH4jjD4zx4monepTT4seXkmAP6nRZ+/nJKH+64reW9O+XM0E/MEv2y8+z9A8vxAHfYBvxYfFtRwDsfO3R5hWCogPb35/n3cjs+MeU+QeYA76+Tfr2RwY3ePvrn+gFGrwKUNTc1X597tT/Tj8VeLR8NgNPwgXJ1AN8AGD/wIAHdoKeKHgy3IvdwCDH94H45sEUf+qU9xr9M58A4b/rjB4Lf1gEn6JPiz4I0pmDX10AWKddYE7+Jys87AMoDbhudtX3GHz3RPnYpM3KAM+1z78p/PoGctgBSeW8svjV5YPhANQ+NnN/swJ1DhYE18+KBM/+3f7/Nb2JHdCAgvkhvMa2YQhtfRiD1jCOQrC7Jjzfh8LtFg/cDeZhuOuFgQutMdRZu/Da89cIguMECiEuAeQ9y/rr3IYks0qzPsATHwEyBN8fg1v+y5an7rOjvm03ZptfJv365qIIGMkhDU8+P/SK2LiYibmjfFnWaGc1KZm1p4NhV418u553QomcqX0MMVroWh17mPjI04zhLAg+M8SsRGIQf8n390rCt9JqzF069O/7JZaMQ+JBrlIwaTitcisJJKScvDHLmqxSiCK2xnWg3O/GjmIPMQ36q2yPFKl5K2FkM62WBxu5WKdTyXv6cgz4Hi7LDTOaA8T5pSsKqbhBPKtO1VCDlsv77RSouduO/n2gT5o5pMIu8OMwZsI7DE9gO6gH9uFwGkVpY6Aioe/Z5eaMKi6yx6/kWUoxSIpuxi5erkfOP6gCdu3wRDvQvLIlA8MyA2eHxNLSy5b1kifvUniz+u0Sv9ICYfXmkIj8lra4JbY7hiKJW5YoGM4IDLzat01YVOgyuJ9bgtfRVXgJl9F4DyyfUpF48uisSLvxeK2uvhDnZryrt9L2fJPQXVuadKsVpn/AUv/USdvUL+JEyDFaE4yzdOB6fOSZeBmqU5XjjMiu0n4zGdikHM9XEZWokRL3+z1qTBy7ikrqxrEGl1wgfpPTS7gk9tq0hXVlVRKTzauHyhnqTXQzdZLedzussbb0BRp1unW1e39SS4ru/U5K4ysJIXkJkuVuBnocQtauTNEtM1Lk6AGDffiISht3hHe3feHJ+vrIG67pJNGeHy8RYu7E3V6rmwNObPgtiHcd3bVNJVSRShB5q8SbiVeJScV083KrRlFvKPNqSPG5CtWNpW9X+MBV5epmHa5LLhX45Nw3PGGsE1/H8qbyKFyTaFD5DYdbsXpv8SCxcoKgERCqnonhXZCdiFb3T5YSRb3AJCfvuJpsgHRC3F4ai1PIQadLFxpKDTWinRNsa9KE3fbW3gRNUmkRu1iCn7ScbAhpmB6aOEzEEC+1WyV6tuAJfpqt0rLbrOLwLCM3SC1rnAo7nksSSNjQdqPQ54knKA++Q0MFGA4KKvi2NdUEX4thfVGvdn+lbzusZpOpYHp/iHp3YqPENjzili2Z8z6PtWY3TjuMWHNYpEgryXTS+1rVr4mtroh4FXnStcEMo9nDgpDSbeQcj/LdInSyL1fr5swpxOHgI159lyMWta4UMYQdlFNTxMQ1W9GXlS7vh/FwwQtk3NhlijhFinG8JsG3UiAGbq/RCBQrUmgej/FootcjGTqKelitPQ8/n/HLJiGxOGWv8DpLD8JWrpTch3bXZJAm9drvzN06ZOFTAk96styI18mMTYB9tonu5fvGKCsWSe487tzHYGBussBzNXpa1QR1FA17XwluL06xldEetE1HbnXWGLENC+/WDcuc94aUpdZThShlalGSN0kGctlXO8rpCQtV5Psyt6P0gt0coVzunfsab86iIVSpSkMSHcQ6Kx26kVjCEhdgJ4jOsJS7FU2t4d5t3ObqUm5SxReve8BYmwIlt450EY+4Tkf7M3N2EtqrhkHJVEdfsZzSHW5SddBPFIbplED4GBLTm2VTHbcEAjtKEVa1Z7g7aRfgbc8p9FpALioC2jb3MhI8cJd5ZZpzH+/Wlzg/CJi+F32/4cddLjNEHKulz6/07hjXiDydL7YkZE0kq1ldGAqRN727nQyTPey48LoUk7teU8iEY9Axbiw/HmB4uzWXm2kfRXa227Uca4402jmJfkWDq5Xea6xh2t41YBcu1BtD8ffjTmSUlazZ/ejQis12LDfUsMaqLXqU+mKwxWTojIYXJYeEXPXsk20zXq2hyYVARZmetgH1eqOEkR2J5GnM8Obai60qsVSN5KHbNbjDWJq3mFSltsBXyGANoJ+Wa7kTU3WbQBZaBFqmlTsUIm592VPyuEfKQeCw5DD2t6PB7tuMKHBaQ0ZKs6OQbCWx8vt0dztNiEnXpH8khcpMIrTYMRvj3lxugz2cqqjFDKud4ir3qITTLjXl6HCCLXH1WhBEB1WkY637c0oJW4LLzGuK5xLtK8RpzzDUUbFH3dvCIaGRXdXtOVc7xeRww1fXuJ9w9jrgqyA+8USoh9wmxwB3e3S12W69wBOPMUm1uTYgipthVHm6kI57deLL+ry13KmxIJyVjQuEWmw9cQWCKNwF7wN1G+Hh2hqI1FQ6ootYxuUrlXFTVDOCCeEuHi7U7CCVKhfbZGkqB7u3KGEqRr/fR5lx3Uem3xupuOw5nm562T6fVWnI6v1gXS5HP8itiEFX4sFiuK7Eb0hR6aF+P2xO0VhzzNJYWug+SCY/0fioTNg+PGV79gTXQTcwBp4tJ2bHXen9WbaXJjs4Togcygt+5sn1GjenSxbALCE3fmbqksCVx1NAW4x0DJDLaQ1LMCsmNomstBxNcOtg7AdSNgYUlw94qaiGFzr5VRB0K6GqccPGmGocIdsWK+HO281FlGR1C/OevY8n5KaTwxG9iIxohHstvFBHTaYYK69k4eZofL7KptamkSSzw6iJAGSuKf4ycpl3iazO2SKiJtiDiinrUjoLZJw4pyimL6i7W++thDVtToOO+lHMSabLUfG0w1u9S07JChFrq98JSXBQvDuNOpt1pV0T16RkqiFXrmTQ2BbZrVSNYI/KhSiOcJSJOArI+biW/SItuM68U6V50Pbo3trsebFOW8c9SCuD4qEuPlHH/WGLnSsoXNvOcbmM6hOSbmjqPrRpTUiRtC9My6ITOrVP/lHMYoOlvOSsHlfGwbrRiZP7B62zkvOG3suF3gpbcUWwegaBDeqNXi1LNTumfRniWnxV9zriqJ2ND+zl7MXDCsulKFVwtNnRRDStJ3lydx7OTnZE0dTFaDK4jbRbybgVRUg9lVzumF9Uo2WAXqerhc2JMyW30Kx+vNVrDukgqxv4tbP12DZD95omIFVfsjeXpUL3Vqonc2r3AZHQzNCfKoPCNMBIUD+6zXVbioem5qSIPWZRm0VMssquMkeiRnot6SU3xjm5uzOXmGO7lSEje0qwEiG97Q7uRcgPxJa8nBRmvWJ7a+1xpxEqmTyE/JGiNAhhj/cbrtpEWhiyTh2OZkSPyK1cHc4bdoJ2REcOrYNUImH38PZKrFaQONAryFYiiKMJ6VQLyBlVwyEABJSVHT/GnhfLmpmuxmOw3TcuEzhNb6zvOGEj59VNK+sdst2e/L4rEZL1nAtPC8zeOO0uTQ6MK1VpK6P7Xayu0PM19Ox1zW8CXNqDzhoOmM2hImGL4Q3RNM/7EzN2DlNuU/4g9eJIklw0yRWaZkLoZILY9HCGIRAuU0vx0t42nkka2/6QSidZmPaDSlKMQB1OlZO7wEOcf6yomKIHe1lZLIMxWErZdeEgRzooJ5z3Die+Tox2rayPtD5wrhMnZ5uiyVKxzUruGo0vbjB6hZpqMKq9T3dGe7nQ2UYzzC127Eg9QQJ+lafILkd3aeEasr93URjNW0MzPC+0d+e+6LzDeD9WA2IgxzXJppGe0mdycArA0YZAkkgkMfmWFFDUPd7dRjvEtgQS8kpvZYwVm1OIXug4PeWWglwFqY6iTs/6CIUNZD8RVnOdDicCGYbVFUePp6JLQPsaDRB2ukmd5WcroQKMZqA1FMHUJgycE3sDTWyz2VQXCA4aYTJHQ2yKluW5u3v1javvHjhrMi8hixI3KSFVQdmqZ+jcyqkaGAEGdonnWF4F9flKkUO8GepGdjicojjUZiqt57esx0qnWI5ZSzwe7R11VDfQuiG6rWRkPqaGOt/au1xoTfmcQwEfkLWYC3un5UtWu57vubIcD7m7XnaxQlsIzfAYfzjqUte1/q3FCznNw0qbDo0qVGWAwyeaHisEctGlhrBGViFVRe3EVGR8O4L0A+26ogl5e6FHBVbfgy3LjVfJvb3V8lYcZakO4W3swxzWw1gCxUlyzwuwZ771eLyytlkbqLbWDmuS27KhuYs4PpGHY32TWbavINu45nVJEoLWdPVQs5ilmneS4CB1jcXLjNKoDl15jbEW9Gvd8iEusnebxkmdR7f1yIiiE03qHvwjdnmEwfr9jIdDGgJwvJK3/bLsvUSgN32q5ppRl0tHHmQd8Apjbzxf33H3ldbhNItfDiFf9ZpN367wzicvphYLTdgUIttSAo8XlmdL/t5wUQJVsDz3+lZ2Nkrql2fcG4+cwXjH2nCTPjAaG1NCEWLLdjkVgq5iYWYf1n6SaSnRjbvgtHLaci2glav3hL8/3WVuS28QztMql0gkrruMnre7i72OGgOP8iM8xkcB3ZkusOfo6Mxwcu7X8A52Pnfxtq/tIweLSgFt7k3R433LGjuoCddHZasbo+samXRnFNspdtBZZ4SzgB/aWPaNjW+qOzlzCyXI7Y2EZqK7aVUF2U5Ti9JnTLmJtQt3N7HDLx4q0li4JdcmVm7ou5GnV2h1daYeNeoqbPsaw2On569DzcBeh29L+HoCtw0DtoMmrzGll3zbH1Bdg52p3nQbXtaxjbTZ3ITbYNiEEx7NPB0LYVL8Y9NxVY8fdLERRVPG1xTRnJQzQAKLiyMIvbGcX08ucb6WyrE3fd5sVtWSvOg0aBLGWjIF19jVTqUgEEd0x/NEIhmVLY/Abz3JXQNxspHGg81NR0WTCRfSPhR823Hqem9BhowZ8G4bLXO3bHuGVmDVxVEvho7qajPBq+hKJNWBNs+yu1qeV0PVH9SdL98vd3HUIMOCLYFvEIP3b7zjK5zTSagMKvPoDta2sleyethtiYqQxO3FIhtKOOTDNRFvtnrkhAPWIYi+Dde5jua1eYmH2+AR2akpooO9NrjC6u+wv76eSoOaxKbdRlOuWJ5m7U2u8UJEF5aiQzAl1pvbzbEHXU65llfdsCaINbLVeCVAG9dk1vcOSkdb5qb8cBwymgvUWL/cRq6CerRxLvj2BhmXC3NuUUM+oU50V/xydSXvGzs0rteOO2QUYp5p0k5pYYurR9cmbkZhFyFLSfEla2sSPxxucsY2uajW3Klt3elGExfpsDEi1Fo7wwRYdOkN3apXoClOEdrPCV+wE38pJMj6CjpJZWArrQIkaF11tLmPknsfaT4D7Q1Dc6ilw3Wd5JPMaYy3MeSdzF0Vau2aghydZOko3JEwUEmFzGAe6dNrDBXMtmfWl9W12HGKnabE6nIfEIljYhSr8xjnex9sSKITvCXU0eX56ZwHpCkbhrK0I7cMOMP3dbANzI9bfWjsuwuF6YUpeCQLXByTBY85n9b+uDOR9gZ7d8sVcztXbq2xHpO6HZeEyoiTZWBtJfVLzSg20+WiZ022cQgIyY+6hqT90qddazekVg477Ma4RCtXZafmIHsbflUpFzfPzawJa5Py+m0BqH7ZHmKzpZEYSqYL3+X3pG217S6+cew0ctR6fRbXTsGQE9uQJWjuiibt9mOwp2xy1V3x3DqPVcKORTk1XqUtbxt4H6ntzRmUoWcuHen4/j2GmR6uRajBAY4707buQtMPQHb4+4FZKcQdO4udLqlWKuSXux+cYRmoUZagmc/brZrvOlyooLa9G8E99s7+BBUtKBRKO3tEN7nyJkIIsbIr0YWg3eXg53ukrsldeDjds+VtNRCFe7zdb7zuGPVVv59SBSupbsvYoLqnCipGPZxuqtgOjsctzzxzsGQ9t1mZAllqKsQe5njtKtX4hh9RAl+Xq/t9JJM20ofSTyFif5APy9sSZTzOjff0jcV1b4wtBF2hClt6pXc7+4dt6qhFZpiDI265S8GmIQXcP3ibgjBdsZLtw3Ul7W6MbdpHyEB2WXWVQoAjjU4MARSWVMpM6z1eYVHCbhiTxA4Yxaz0hJpoiEMwSVQbJ2oOqrNdleKSYKGNmxpDvqPGtnVgX1iWOZQhe50760kt39ensr7Ia9jVMlHZOpDR5hBohS9LLuuylpzMrvSzazeJ1lmuz+bNmbgj2jK70duHfMtkauh1Ko9nHrahXLYE+/3DYYmtT/FGYIR1qMFp2EEssWo0mccOlC0u7xKrH4DF6DlSd2GkG7tLFje25W9l0Wv0opLhuJr2ZxM5B8GkbGoP3RBnPyhK0jawozpoSXaPtPvm4h6XmL+HVtZSCHTTzw0l4ccjOp401UsoeKLHA3PCsRW2orrCpSODYLBunx07s/b2d1OC2yX4IUNL2LO3VUK0h1JVM8KA4EtXmJi3ltchrCtDHbSNB/Y/vH2+M0O0vh6JIy/irrmxXVzD1FOb3ADXrtWz4GJcbeJErCjLvlgeBdHqp9MxpycbZUoV9OuVt1YhSvTQa8rBoKtMs2LN8g2LDuvz8a44xOVI9agMYmYTzRrClImEZUHRsT2GXtCQ3FxOtdLlCEwrVy4tt3mCcjf90js3GR16mDB1n1BCRcFv1Mrb7IwCX14cLqzqS1iEW69dtTpO3bop3HMMBnlMFKf+gE8o6Zx8tasN/0wvbUvcZetN5QnL/C51YLM18YdoVWKrw+ijk1ab2r0P6sN0K8JOvmFyjq91FBYHlVD69g6gwDstl0Qb7HP7zoQqVWFn0EH4B644b8V1LdNI38P3Q2bpOU0eYnd5PnXsut+dVErf6bsu200nzNsTCVbmcH3RjiniVYhUFQgUYZa2Tq2bAto5/TpqpymIcE3ZWpdWu8rEaLma7MEu7sJ5H9ETvAedsaQQcHK0ay7CyzbjMTPg5WLvr02pWzLeoXUPYHN0Zho6L4TyroB6CAPxvsL9JXMENEKW5/tqubvfkiPiDNtNnuFnvC/kCb3umVsWUycsFHVFadfEHj8kWnW1WJYkyb/85e3D23zK+jor/Vdf0poPZv6fnQE9j3LeX7x4HBAGjv/5sdbnf1mjv354q70E6PM85WqyLnodGP3NGdfHf3LMPk8en289vR//Ps+TWwBas3ZJ4XdNW49fmzJ7vHQBZrhdM7892MwvmHrg+/fnm39jwnyG9jgL/tqWX59vaL3Nr/jNr1QEfuK0wesyep38fXjzX6e7X2F0+zWoq9nY1+k9sBH+tP4Ev/32fwGFCldU1S0AAA== -->
