---
name: "rar-cowork-cookbook-scheduled-brief-drive-app-value"
description: "Builds a morning brief on drive app value from Dynamics 365 ERP data for legal entity USMF, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an owner email (saved, not"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_drive_app_value", "rar_sha256": "e82c05b7c763b504c4b2a6469b48f0b0f51d7cbe071b72ae6ca768b7b6afe8af", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObWJbmX9G8/SEzG9vsINzREYMAIQmxC4RIVzjZ90VsEsqp/z4X6bUzsyqrqypiPo0ctgTcs5/znHN9+fXNG4e06d4+v5mRV69EryyzNOpWXh2uuObWdAX4agof/F0FTT10mT8OTde/fXgLoz7osnbImhqQb8asDPuVt6qars7qZOV3WRSvmnoVdtkUrby2XU1eOUaruGuqFT/XXpUF/QqnyJVgaKvQG7xV3HSrMkq8chXVQzbMK8uUtx+A4CnqFp5D067IVTZEVb/y51VWtV4wfADKNpVXZlG/mvrVkEYr+mPozauuAcYAKg9Qe0n04WlUHd2HFaACWvcflsWLgl48ANXrVXOrge1R5WXl6sce0IUfVnUzAGOju1e1ZdS/ff75Lx/egODy7fOvb0Hp9f3iuyCNwrGMws1iNL8YzLatvZgLaEuvTsCidgaersF1G3XA0ArcCoGH3q9+7KMy/rD6z/8sbl6X9D99/lKv3j9f3pY/xlg/bRsarx+icBV4rednJfDSpxVb3ry5X3XRMHb1EoR+WPz16UX5Gyfgvv9env34EvIpiYYfv7w1QAVvcciXt59WIAJf3rpx+f1p4dL++NOnsrlF3Y8//canH/08CoaFGdD609f363e2YOFvS7N49dXUBO5dVhcFWRsB5r+zb/m8VH9n9+6Sr6/FPzbth9Wfc17s+W+g7ysVfcD3z9kCHwDKt095k9U/vsvoQFLVXh1EP/70j9iCqAZFmfXDv8T35xfjNPJC4K13l/z04Rm+v6ygd9u+8/zHYluQMP+OJWD5N3HfHfWPeD8j+zesQZGA0vkWyz9l92cE0H+vfv6Htv1PBB9W8Zc3PiqzpS79Mvq8+vWZIj//EP5284e//BWw/qdszGbsgieHr5VXZ3HUD1+//vxD/7z9w19+/mFsQRZHXvV17Mo/4/lnfn3K+YMH31f9+EdaIN+qixqgxup7Da1+bdr/1f310wpUfxb+dr//vPp9JS4faLUY8U3oywW/q8Ye6Po7P/709lcAPDWwZnyhF8CP//iPlZwFXdM38bAyg2YcViDAQ1ZFi/KnNOtX2QsRuwj4tc+AY9/XgfxfIrxo3MSrX/538AT7j8E72MP9N0j7+gTyr08U/wpQ/OsTxX/5tDoBtk2XJVkN8NpgNe1LDVC2HhaRbRf1UQfwE8D0EH0E1fxx+bHK6tUv/4Tz1yeTT+38yxOvsxfqGdx+Qbwe0H1abDsvwP2yJADAHd2jYAT8yyYAysQZQOoPwOa+KUHrGRY/9EVWlqswA5gC+tf85A189Xlh9ssvv/hen36pXxCNr16NrYfBgu/qrD5+BFbFZZakw5c6CtJm9cOvf/1h9X9W/xPVk/kiQwOd4j0SQMODqSorUFljBZaBIIGwAth4RuLXv777FrBZutHS+uKlty3EIDOLKPzmaHPHfsRIauVHwMHR0g6bblg6XjZ8Wu3j1Xd9gdDl0dIZ0qYfVmHURnUY1cEMuHrAnO+eBN1u1YP06+P5w2rso6fUX/zOe6pYgRL3hl9WMqeBPtSU4J9FzeciQNzUGXD/9zR43QdMuh/61eYbi08rZcnFVet1Xpt23ruM2HvFBfSfb+SAuQf69e1LvfTbaHHVszBe7gGLgGeC95B+XGIOBoUKoEDYf5P9XOMt3fL07Jrdl7p/T3qvW0LxnCzmVTJm4dIK/us9pfq0Gcvw6T+g6cLpPQrhe1SeOcj/zWDzfQpYCc8J4jkMrL6MGIISq/+f56PFGawoGoLIngR+JSgn4/IK0jIyLsF8TZmLxosJz4L8bX75hlHfoPpLXWYg47r5v14rn6F9X/OCv7EDTjZY48kf5BVQauH7TPsljbtuMdb7Un/rCcC21RMAgb8BRoAaWlL3m8Dl6TdNUwAEy/Vv88EzTbpw8Q5I7VU7+iVIuziKQt8LCqBVt5Tue5hBDURLGd/SLEj/YNUSMpBqgP8S9Aw4FHjz03ecfj39pvofCF9j0ELyHBFHULndkwHQI1oUXOJ2ywYAYN7wmtCBnZ+fTIAZVTsstvugdqoP7zejLrqOWQ8y5RVk4NeoBRD9cfl+Wbrcje4tKBfgLFAU7Qi8+yyjJWcqMOQAHQCSgKqqsho0feCUdyc8GXrVggkAc9+n0hfH5+13g6Jn7S3d6hvhYshCswwArzrw6vn30HH6szQB/KplxVPu32bad2kL7wU+ewCBQOK3p69J4dOr2b+midU3vp//bgv047+3S3q2b+uPCfB5lQ5D23+G4VfL/dZxPwHwgl+69r91349PmPj4xIiPACM+PjHiD2xfFn9e/Xuq/YHFe2l8XqGfkE/I8uj4nlrvH+AJ7uPm8pFYnn6pjeg3ZAXiAboMC/KX84I639rgtyWgFyYdAC2w+NUW+6Wb3gCyPPsACMKX+ve5vtQaaDN1suRm3/wOA57zAMj7V8y+tyvwqB6A7HCZHZPo07LlWtTvo7fP9ViWH94Alkb/dJu2NKRqSed+2dqBwgGD2JBFz6snOtyH5ecft73q84dXflrxEUCisv99yr23kaWN/q4yXiYC0wIg4cMC7KDgQTYCExfhS1V5PUhTkKGLKcPcLrq/dnTLDPhsAF9fDeDvFfpD4/hDrwCAdx2jBVXBttMbS+BIcGvpIH8q5vsc+vcyzmAIWGjD5vPSDz+8owz4BnsH0I6+bQOAce8bs0VCVI9gz/vzsgVZvP0kWX4AGvD1nej7/yz40dtf/kQvMNW1oDcto+zXZz/6e/004MbmNQG8uixIIC8MAWX/Av4nYIJJKHrvZc8Ot6wKQBKCPP1Th3yryX+cBCAjw2fVfAeX7xPBAEL6YRV9Sj6tblFULO33fRAAqg0r2qv+RObTWoDToNstjvstIr/5pXnu0xb1gB+H138r/PoG0thbBob3RH4f9MFyAGsf+2XEgUGlA4Hg+lWT4Nm/uwV4J+9TD8yggD5aYwFC+nRAU7hPIkRA+JhHERTjE+sY8ZGYREM68COERn0a8yIq8Ghq7dM+5cXR2osBv1dhf13GuGxRiWToGGEYLCZQDAlB2mJEGK6pNRWQNIZ4jO+RPsl4/m+kRVaH73a+7Fqc+H03svjj3dxf33yKACt3RL9nXx8OZlAfJmj/3jmQg6zv5e08tlvQWjh3PE81tZ98anN7WNlZoKWLNOh7eF8Eem+c9gFSDWlvsTHw2+UAlfgjeRz2ljN0A07gubdhIciUsbB6NPAUq4FMO3VECYUxoSFHdiVxJBUpO8XpqbDtJjveQw7ODf42XjrLgOHcx9dOLhVEdvROFxexvBYd72QZutJVinIBM+jgfNLnDg+8fFviEOBHQXEGVLWu91m/GlcJlVOhO478vKcZaB3zl9MldqOtaT4eu8PdWZslVo13rUmJej3earZy3Xp078L1yKBXS53PUF3E837f9OY5O9/FmbRP+ihca8piOznrFOuBJTff3oxmdWO2YVlek2sKickpd2rjJBmuajRMNNFrJtTqnCGg2JSieJow5gJB0X4ob9lt6G0hveKSs/WNWC04MqOtvWvSTmAdtUun1tIQlk1kQKV86vTU220wPzkUpKXpOn/tuJ675jjjac5xS4sDJ5siGUHRdssF251uRnZzZBSieZihA3GCmAWmabjRZee5SjAZGH6NVarEmd0Q6ZLYngS55FK7MizTE6MtOVh0ZomzlQ2XeZK5aM9tszXlutfCxAQ3olXljj4KtZISoqiIW6iTO73J197kOafKidE6n079Tgok8poUPSrbYlVwLaUezdwTyxo4kcT3aHU2/HmcReNYNjuGhlWT77Cz688xdomuFs84/cWlRXng6vkadzfmAbWjZrKwnaLz9uCaln22I90rJ5kqj+tWZXIxgfelVEqTexdH5T5LYX1x9lq27otbQKYNamrVNcYktvHVJO1NTSiwHFJKaBLUDpV5IrlUG93H0t6h6n7rqmgLqsVlqKE6GHsFpWn90obpEF+Hx7XJbIVjBBEmDHR7dC7XB83vu+O0ccJuJ8LYcTb6XVpjCrzWKelA1Mw+0rFOy3pkq+3hI9mtPedSns9jSQzbeaPw6nqt9TDO+Vt9ClnkEqw9Xr1om53I3tzH5ta63enYOzs/mO2LpCSST99ouMbXqq+hrdPHDM9h8eOew+q03h2Rc4XYl2I0JWzT7tmsz21LS7kbdVSlNbofKJPjcOx2ZFN5RwhR7MQ1ycoqi24zp8zRx65tWSl8HMMii6+PfYmoCUGOJ8GGOXk7JZliY9WhNZWmZXIu3dBseNeF8HLbJU4CANZFuD1jjW0cWXWypVwR79fcYXJLksc2dsRP0L1NS2cAHdpy2CHJL9tkW2zE+di76DRYSTY1ejRRc2zQO1XAi703lfic4Ior2paXOHDVKdv4fMof+MnLYa2JaqId7tfHYx3exdK5dZaa9IRhBPztRODnsjCuCJ9w4j6mKvd2cSgviq5RZeTsXFxNUPAzf8Q8uDXcm4lLRRPWdExc7VA6ShRP8bS+cchIdPAtdlwrWa+GwqE+dRpcz8MBMtfNZW17LPfor3dDoxJBRgnHTKwuRpCtk3twwQ1Fwp+FPBpJRico6Cz0YTr7lMZPiAId7GLdrtcBXY0mJwlOXqqIHuw7fk/ojzKID5ucpxNu7+3O4paexf1DxSvSEwVOWj9qS7wTbCjcxlYkD2WE1V3fxsaY7xT6Mu1Ll7itlVTlSYw6mD3shaIBC4W9tQ4YvbtD2lVQZxIJ+P21SBuCRfe0RV0ZQ2tapTMnEO0I50famiL5VMhmHeuZvYt2wUnWjUlBBRZeH8jifhiImSX38Nm4yMNM7BpMtys1oc/jKcL6eROuCfWuavHduGxUES4IexPey0OwkbNjv0+PpcJvaGkPhp0yoyOocbKzaBYHu3IsefDO+PpBlXu3ycULqen0SZbE3D3jmBVsuGLzkMKNDjXXpL8RG0mgp5HF01nMHKljOcTOc+Z4VQJb30feTSN2IGXtBJU1x5WnwLmiLrCU3ZJnYiAyWlW5+XE2fTcS5MGFtXqLhcqEP25lxZVWPYrB7aBoBdLM5lSkLJ3EppHedKtJMvy6hklZREuEjofNVqilRmNQx8EwqNjBXqzhO0qjmA7r6uGgrjdXhSSbyNT0lN0MqHkXZfyBmdk22raTUgsX12I3ZLwjDhN72qPwZgBVXN+OVIPgENUJ4gbXHyl6V8092laCYsnrDbqTOa+VDYkvBEN3+Tyr3EEsE6fyH2qC9fVRtEKE0ByTUw5Vo5HBowsl3YGDTdhbu8OV2FMmMWvI+RTkWaOpwflSrEUvkZly9BTnRo/k1tonpqV0UHZQhbw7o6dMaPwjU21UVRTku/cghuJ+8WLMn20xe2BBa6+n2saO7MbOk14w+Z2x36U76GIpzFREmTsKm93pVDOq36r3pDXvgSE95hubnkvPM+4yc3VwUkHveXI824TQ0ppt4qVxWAu4cdb2/dEJSF6VNpvksO5sXrFGMjGxferbDDuL4l0SJcdGRkOCj3UwG4eik+6pawwnReD0KTmV6zhBZ4kk9sbBbaOdOjca7SJpHLkzu/HX7XXO1bt0qIzboJsJG7ByaNW+K03DveRM2UnSy/EsFLIvnCSMasnO1A3FFypPvOx6MaiINM1gvI2uhC+kp9GfNgMjxwMlhprub+UZ8h6417l7R00pZdNuqMOxrvKjtmUT1Zl3Y2Wcy0iYtd0gnoq40aXRPJT3kqTp0IXMGw/lxMCVBnuUi0vTYjdfZlu2FFS217lrIx0klzrw64ew66vjTuy8/OrA3j7V9uiGQ7bw7giNB3HLw5kguyRVnAxm0qt9hQWsNMDjJctuNIiH1ak8z3O40juPm6mUtiBsI2f2Y2xzaBEFwFaDC5IZiL6NwNojRx74tmca4cj59Ry1XpaPVZ8gBEUeLTEH41PBYR5xUA5Yl3G6mo63loAzCxbPTHVzhLOVDoVbshbWVne4X0/UPkS2KGYn50QSvBt28wwime2HcYH69kAGw6jFWj8xUDBZpqFHm07IcwfOi4xXdNu7+maq2mgaJk1kHx2DvdyDnS5hAFViLL6wZuvTgj5Va82Fi/qkJJy757KNO9tWzBzXmUtzUZNd0MEXMt7hFMghYjgouHmQWKapiMZJ982AM5pH27stSfHKep/puGxsKSRhLiLmbMJrcbeRHGYefb5Wg/6WbzQjAQ25dQ19LyHyWedMAEGZMLmDhXl9u6ErNJTJa5zHcrTtijvoE7pudiHJoge7OR/Yc9VSJnUJWLs49p7s2n5A8LjJJrN4Ufhz2R5pvd3EkYJGjDJOepSiMAUmv2QbiOskEEB59Doj51JrMAVOovmg7RBxYknzfogIq2Q9NMB3G5evIce6mHds0gGqqzgL0z7Rhg++QTgvMrjZRDeOgwBrCuWcyLh2kc0NeTuQZ4YJvNra2E4x5BF7t6a74ib1IVhTY5Gnbc9i7ThamDi7bcFiBsvRkYQmD5LdH3M9YGcHk4uzwmVQrlzjSNJtNlEuOnFzcaS73F3e2ig9etWvvETKUnGEjKg4MsG8Pwk74PyqRMzLlcMMhW6Zh0IMwC2oeYNkjSbhe7ILwYbiGM4X+pFQtSQJYQwdvN3lGF9xz5TNcRriALmITYNSem1GOL5NQirJXKFETZITDjhDzl57HU4Oe7nCU2YYTWXrp1sd5G2wWx9OkEjLj617ous4YsIRmc1ATh49w5xoaudFLCcHF2ezF3CulKJWZonWP8GnfShd2B1ZJ222F/rLxHrebn+VpGgcsxmjy/vZxgeG0Su0tIOqvqA2x2/PkFE8LrhscxbHGCU643Gw5UUmujUlKQfy5iaSGbbnjvnknLvAJ8RjpPHsgbHNQsBJfQgmiLGxESmv0dWTjFPPu/60F4mmc8OiP97WEoJmYseNqWDBEbvF0+1Jsk6+dYrwtozhHY48GhNPuWKMYhBg2qZ2jDZVykWsM5w/xTUsQM0xgXTWt+5nwRSy0VEOtdeYh3BL3ziDZPw8BWOc4ybRWN+Vku/5e9M8eJ7t+Qa+QuaAq5rrVhavjY8zwQTM1aJ5qarj2thc+/t2tiTG2JPYBdRvYuiJbVNAbDBxXiG643XAajSvYbSzSS6wCjuwuOS6f5D1oJJM7+FQE/des1MNK053boLMdWgZKMDgNdGfJFQRw+60zoIHKzV7U+B2Vs3ZWDmlJSZsGee4u4tK87ChvfLIO+X6KKpkbx636xIktJKfd9eCUEsk7h/jFOduvcv5zelydM+3i+A6qoKohog2zIhUekBfTwIxqLF34wrL5ArbCXWwbZ03wY22DqcUnRpze7xsKqecsc3g7o6UJnebrRF2zppL9cYcfRdTNvM6RJnrxfEVmb2qp/lMXz3IV+cR6sQDx3C5Fs88fwo7D7v7YMYB+5ysnlwETX2RwYxwimjavsRH+ihSj6C2urALjzsFu3ca39pjyaDcNFEgKwwVGiF6wKvRjhSSwZwrDFK/tCOfOj66HNLM+UydhyiMyF2lhY4WSqPbWxiDxcKeaLmrJGNosR1utW6qD/TMov4Z8nTyttPca1+u1UaPz97YnZuLA+kNojSN5hZpx/TwhWJdaxNUbjjf92JldWebU9ohhi2pTpMMUW3yHEuSrnbq2qld5HaFL+dpgz/OTn0Q48POxSQk3sm0TD18VrrN8UlDVPeQXujEh0PR9BsNJiAGvhnQ3SpazalKGN7DBMGK5Qb3L2DXR5Z9aKnWQUKPg7nxhuzgrkNKpq+b2S8d+lCpygQJRO4g0YjqYEsfCwkWiaoApQVA4qIxaLw81dDsnigv9OKd+NjeoipM13x2utJoQfGPaT/dVD5FdsoYPdQ6QO/CVVWqUyBrYCfdHipCHnHV6VzfccHQL3I4EjMU7Fi4k2OHNUNfxXrHIhQd8nbBap7dTtxVDzaQtGbOOlMhJ7Q+sZNynruZ8JiJSz3xjnR86WkI0TFOPVwIOk1IMd0fwJ7xvtlCI5+iDIV0j/6Bl8KJsGHHSzTJvOauceyyWbz3voet1dK7iiAVbjLYgwfBfU9PtexNa74fCFLd1O7km2eijrNYVQ5r3T71hmhVerbH9qia75htiBOGfU734ibh5fHY4ejdCE/G3OCKdjKOxtpNpty7dz0rCwxbTTWr5gflpqwPDTEY97zZPhJ200/bUMCuc5Pi0ABylYYjhsEfAWwdycsdSS64xGsUrdzFdBclR6664pfrTXtEu9JlbGjHjLet7a4TaKS1/EGju72N02spcsjaZ/sQI8/7qkPUhgyFo5xrxlligra6MXHepoUQSMzYPeS4gWa19h3LDmqbRMkLGeyF8SDjUyBi8vq+FmnPQv042QV11mEHEYJ62M3OR2w+54HjZfcQAMigVPQJ53tEIOdrNkL2WYlQ1LOjIy9oKmnyPOLUO8QdHRYjQePlbUEzW1rZk/JpZolhB0uX6WSaSqGmeChk+e5aXw1jvPKd1clcGd82dIpBkKDzNYF08dCStOSSNW0FkLqGRkVBYllbw3fCq+F6VyOKAGsVEwoOqszUNV/TiPZg2mO9j9bcujtPOFnKaRD39RC7nWttGQXuECw3/AiWiPPVIxn5PBTqJIfbKeWdVEIPeqerMY2BgUQtPDm9EiRD7e9OKCvOvlbrPQSwZF3XkGEwenDZkXDh3VzzQFVeoSPF1dpeaCwOopQL5ulRuANGy00LayiZbM83qbU16qin23GI7TvA1RoM2Fy1W3Oer8tQBBubxCOLXLHqPQ5NG3drIWM1wNweoQqNHrZgAIcK/Hg6mS0vXzL8CGbTTesM9plT5hioeXdoJaINMW4OyO5RDncTPwiH607Y4DaTaIpJ7GTtQuzc0mAaeW/mEARbdzgyJy/MJVjKEuYsov60nuYcNhn2euzPlMYNzTANuxSl4/Zc5qozoLTH+CKFTmXnNbgZ2Im/q90HuV0DqCnrQu1nBKr128gneLvpZIRhbigjFt0UXbpLv7VjMMlPcRYc90hQHqBxuOEzfT9alI4XInpWxLhtOPHc0mYyhZfLBZKw7mgxxXakUO1Y9ftHdI73wZmcnci8S8x0oUr0xEBTy7oGqU/MJTt2pQk/zkcWYhgMWhORGltYiObQVZib2y1FktjVaSFVxE1wR28QXOB4CTdtw0OC4TL7OthKURRyxDm/0MORiaiTX5Ij8cDNLelLhLbd9ugDtkfQ1QKMQVJEhog95AuESTXnuca26X1d6Up0fPQ6hh5iOBsG8hwa5h3CxBPjN7XmwTQXxOF2t05O0SMVs1Quxzsy6cyGHtOHDlNCz18V3QkBDJnn+y0VsslWrwHHbHzSZfW8eYy83du546OUK5Ht4dEGWMzvThgTIp7jn3l62Og8s1WHGwBcNYf4VJ/O521MYdlU1sS9nsy45k92i493bMQxiXmQDuMfNZAwN7vBjsydUMmaJeRj3Z+U8cZV9enRoviljYNCyCnMR8f9dYahLlFRqBCKYAjWhotiI4F6D3vcDRcRtrvhPjmHSVNqTZbWNnySNW+db4/3HU1js+y541qZ1+LkRQVfWwOJaGdYyq3Yk09teV0r3l0QdA2X7nSpyBtLv9nKaaOVh7Co8A0ejFQ5rylmwx0a+qQHbS1jmVPwrRXuTni7mznQG9zI5gPJJhEAcIQcDtvx6MIK/biwbM8MZ3gU44i6X+T5NEe2OJthpwni4yFR0tmJNtH2rCBtk7XpuMlPJQLqwVHi4BjDUATxp0yWNv0jZ0T0ccluhNsi2yQPfHisNzOCB4JFM2ImekY6u+eWUmA2q7n7rix0nWXfPrwt57Hvp6r/6vtcyyHN/7OzotexzrdXNJ7HipEXfn7K+vwva/SXD29dkAF9XqdhfTkm74dHf3MW9vGfHMgvxPPrBalvJ8Wvk+fBS5Z3ht+yOhz7oZu/9k35fD0DUPhjv7xo2C/vogbg+/enon9jArjjha/XLKLu69B8fZ0FLnKzenkDIwqz3y6T92PCD2/h+2nwV5wiv0Zdu1j8ftgPDMU/IZ/wt7/+X3XmiA0FLgAA -->
