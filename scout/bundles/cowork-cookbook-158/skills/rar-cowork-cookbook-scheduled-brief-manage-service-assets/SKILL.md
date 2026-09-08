---
name: "rar-cowork-cookbook-scheduled-brief-manage-service-assets"
description: "Builds a morning brief on service asset management from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_service_assets", "rar_sha256": "c727244deb41bdb377a7ed5d692c56fb83f8f8715904df9ee3954810a5877dcc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_service_assets`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_service_assets_agent.py` and in the RCI capsule.

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

Manage service assets Scheduled Email Brief — Builds a morning brief on service asset management from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-service-assets
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
      "description": "Responsible owner who receives the drafted email brief.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_service_assets_agent.py` and embedded as the fenced Python below (sha256 c727244deb41bdb3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_service_assets_agent.py` first:

```bash
python3 scheduled_brief_manage_service_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_service_assets_agent.py   # or on stdin
python3 scheduled_brief_manage_service_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service assets Scheduled Email Brief — Builds a morning brief on service asset management from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-service-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_service_assets',
    "version": '3.0.3',
    "display_name": 'Manage service assets Scheduled Email Brief',
    "description": 'Builds a morning brief on service asset management from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-manage-service-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-service-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b156c8113fc15f4a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/manage-service-assets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/scheduled-brief-manage-service-assets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where manage service assets stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on manage service assets for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage service assets, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on service asset management from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a', 'example_request': 'Draft my daily service assets morning brief from D365 USMF and save it to drafts for the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly service-assets brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefManageServiceAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageServiceAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefManageServiceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOjRrbmX9G894PtS9ULCIGgbnTECAkhhEAIxCaXo8y+77s8/u+TSKoqu9t9p3tiPo0qKiQg82x5zvOcfJPf3qyuDYv67dOb4ln5grXSNAq9emHl7mJbDEWdgK8iscH/hVPkbR3ZXVvUzduHN9drnDoq26jIwXS6i1K3WViLrKjzKA8Wdh15/qLIF41X95HjLaym8dpFZuVW4GVe3i78usgWuym3sshpFhiBLxhZWvyYeoGVLsCAqJ0WqiLsf/q0aItygS+i1suahT0toqy0nPYDsLLIrDTymkXfLNrQW6w/uta0qAvgBTDB6r0aKPvw8Cb3xnYBZgFzmw/zYGAZGDCb7NaW3y68zIpSoOkhqBhyEIUy7cBz4Ks3WlmZes3bp59/+fAG1Kdvn357c1Lg0xw6J/TcLvVcevZZeHioPL3ezE7P0UqtPABDywmEOwfXpVf7RZ2BWy4I0+vqx8ZL/Q+L//zPZLDqoPnp0+d88fp8fpv/yV3+MK8trKb13IVjlZYdpSBS74tNOlhTs6i9tqvz2a0GrFYevD9nfpcEQvm3+dmPTyXvgdf++PmtACZYc3A+v/20KGqgr+7m3++zlPLHn97TYvDqH3/6Lqfp7Nhz2lkYsPr9y+v6JRYM/D408hdfFInZvnTVnhOVHhD+B//mz9P0l7hXSL48B/9YlB8Wfy159udvwN5nPtpA7l+LBTEAM9/e4yLKf3zpqIvey63c8X786Z+JBWvrJGnUtP+S3J+fgkPPckG0XiH56cNj+X5ZQC/fvsn852pLkDD/jidg+Fd13wL1z2Q/VvbvRIOCAbXwdS3/UtxfTYD+tvj5n/r23034sPA/v+28NJpr1E69T4vfHiny8w/u95s//PI7EP1/FKMUXe08JHwB8BL5XtN++fLzD83j9g+//PxDV4Is9qzsS1enfyXzr+L60POnCL5G/fjnuUC/mic5AIzFtxpa/FaU/6P+/X2hAXRyv99vPi3+WInzB1rMTnxV+gzBH6qxAbb+IY4/vf0O4CcH3nRPJAP48R//sRAipy6aAoCY4hRduwAL3EaZNxt/DaNmET3RsfZAXJsIBPY1DuT/vMKzxYW/+PV/Og/E/+i8EB9uvgLblweaf3mC95cXon95IHrz6/viOiNmHQVRDpBb3kjS53kcgHiguKy9eTwAK3tqvY+gpj/OPxZRvvj1X5L/5SHqvZx+feB49ERAecvN6NeA2e+zn/oM6E+vHEBk3ug5HdCSFg4wyY8Adn8A/jdF2gP0nGPSJFGaLtwI4AsgtOkhG8Tt0yzs119/ta0m/Jw/4RpbPJmugcGAb+YsPn4EvvlpFITt59xzwmLxw2+//7D4X4v/btZD+KxDAt69VgVYeFTO4gJUWTczI1gwsMQAQh6r8tvvrwgDMTMpgTWM/Jnz5skgSxPP/Rpu5bD5uMSJhe2BMHszTRZ1OzNh1L4vOH/xzV6gdH40s0RYNO3C9Uovd73cmYBUC7jzLZJ50QKebKPGnz4susZ7aP3Vrq2HiRkod6v9dSFsJcBJxYM+6xdHgclFHoHwf0uG530gpP6hWdBfRbwvxDkvF6VVW2VYWy8dvvVcF8BFX6cD4Rbg8eFzPjPwo4l4FMkzPGAQiIzzWtKP85qDliUDOeU2X3U/xlgzc14fDFp/zptXAVj1vBQOIASgNOgid6aF/3qlVBMWXeo+4gcsnSW9VsF9rcojB5/M/+eGp1l86w4WzKPDeDQJi8/dEkFXi/+P26Y5IhuWlRl2c2V2C0a8yuZzpeZGcvbk2XvO9oJ0fVbl94bmK2h9xe7PeRqBtKun/3qOfKzva8wTD7saxFjeyA/5ILmAJbPcR+7PuVzXs8vArq8kATxcPBARhBsABSik2Y+vCuenXy0NARrM198bhkeu1O4cI5Dfi7KzU5B7vue5tuUkwKp6rt/XKoNC8OZaHsLICf/k1bxgIN+A/HnNI5AuIITv34D7+fSr6X+a+OyL5imPnrED5Vs/BAA7vNnAefWGqAUoZrXPvh34+ekhBLiRle3suw0KKPvwuunVXtVFDciX51KDuHolQOuP8/fT0/muN5agZkCwQGWUHYjuo5bmzMlA1wNsAHACSiuLctAFgKC8gvAQaGUzMADgfbWpT4mP2y+HvEcBzvT1deLsyDxn7gie2W/l0x/x4/pXaQLkZfOIh96/z7Rv2mbZM4Y2AAeBxq9Pn63D+5P9n+3F4qvcT/+wMfrx39s7Pfhc/XMCfFqEbVs2n2D4ycFfKfgdIBj8tLX5TscfHyjx8QkKH19I8fGJN38S/vT70+LfM/BPIl4F8mmBviPvyPzo9Eqw1wfEY/uRNj+u5qefc9n7DrJAPUCadiaBdJoR6Csjfh0CaDGoAXCBwU+GbGZiHQDKPCgBLMXn/I8ZP1ccYJw8mDO0Kf6ABI/WAGT/c+W+MRd4lLdAtzu3lIH3Pu/EZvMb7+1T3qXphzeAo96/uIebGSqbU7uZd3+giECX1kbe4+qBFGM7//zzxvj8+GGl74udB1Apbf6Yfi9emXn1D1XydBQ46AANHxYuCE8z8yBwdFY+V5jVgJQF2To71E7l7MFzuzc3iA8q+PKkgn806E/U8SfWAOBXdd6MsGBPanUpCCe4NXPJX6r51qT+ow4ddAXzXLf4NBPkhxfigG+wsfiw+LZHAM69dm2zBi/vwIb453l/Mkf7MWX+AeaAr2+Tvv3twfbefvkru2YS+kebZK8pAYk92t8nTw2gZQOx9qL+Ba4PRgN5++S0R5H9pedfC/GvHAcE+Ycm6CHjw8J7D94Xg+clM8++qB5QUbtYW9lfaAAqHlAMCG2Ox/dAf3e3eOzNZmNAeNrnnxJ+ewPZaYF0sV75+WruwXCAXB+buZWBQRkDheD6WXDg2f9d2/8S0oQW6DiBFGe9XC9XK9ezV6jt2th6ba09F3cJaunghG+TmE/65BrFKWTl+pTnYRS+IlHEwsn12nUcIO9Zu1/mpi2aDZutAvH4CMrf+/4Y3HJfHj09mMP1bZcxe/5y7Lc3m1iBkYdVw22eny1MoeDmyh5xA7oTXrG+0CehO+yjSkwuFqKniaVwynaizaUzHINLrR+xRBkljLprkiJGArPxuAQyj1Te53wFNXFyTzrMHQWOu2A3I7+W6KmFcI3Dcs8SMKFk1kfzzteYEoQ7md2rlkNjjZaWDD86rUkkAXlfG4CoYAiW4QjgXIxsgnIVy5J74q4sRmjHFFG4zCIateAbB7vqp2F13J30QN77cM+OnpR39S1krMiJgwtLnLm4v7cQmVU4k+h21LjbfVRg5oFTzsKYqMLEXsWjJWvJzWG1Q5P68VU6Xg6J5cry9s7xuBYLcmFEiUydNnJGXC+jMBbCPd5u9A1+75QlswoRjZdFvh7PWjQNFWmsEK+3URSiPL/HGthpjFWnYmuKovpx1wvKjUtWpyUHEjKHbGZ9tUVBa2zGCQU7l5n7+prWwigkSnOLJ56adA3yWO5g53pSRYypbm77TD0Ta5ygTPioMGPLaKFzIu1is7pOOaBNmeYzbCo3Ki3dymZLyqXDpLdMkFDjhLTd8X4il16fubhXqUqmbvLuUivS9orH0pbEmAvB7Lt0KBDh1DBXnlMaTJFF7nhuO3FdmyJ8201JJY10i9Q6G6s0ElGHQvKwc1+1q3Vy301xeRWZ/X6JJ0WC7lKJRhqe5UX3AIoXRrl9onfipJZ2oyLDAXL29rWMlRGRDoKkWTh0Oul0osXUpVxV2ZI8O3At6oRyILJzFgTHrdI0ET8dVIpIEFpLTydGiuSVUqmHrGFW2GHjQV7kJCZbujItEGFBKgJRuR0/FMLhcjHVeDpCvD86gSA2RH7CN9tDoNa0yo5ixZJaQRvXzZ6YbNRHFVANdI6X4269t1rNTvAbXmzpNees8YKIQJMg37wSy1I40oxsPRjI/ZyqdwaFaGk97VdFG/iXzN4FCXUXBkNcrwvLWKWUqstZqw2stNsP5Hij2Yhsi+Wt5OvJFMa7UPu+dFCuwsmqEMttqJpU8sb1stVhDI/yqu3TkAyuLuwGdgonjH6DpRwjYTg4erG7rPIVyyq7zfG0QZaBQ4wEd7yMF4u4D9FUc/baWRv8hhnsmCPkYN8m9Kk4GPpRVgW2ssV7qjdH/xh3d7nconAJLS+V1u0HtVKO2yUzWF0yiHxI14m7Pyd0iHiQgWXEetXlq+zGZDDNNacDojWn0+1mi9kNSd3uLq4P3aZqTjapufrZF/nzCmV90eLsuxGdV9hKi8RYJo1jEoTUVk8h/YpIrZMA5N3W2nUV6uIlSWm952Cy3oWwFldoiSxN+G5HNWQaDutMEHtukhO7z2gKShhHirytzWYUF2hhHG9GZAfzt3wfxaWKwDUshGXPxJTKaInTy+pxkCG+VQayq9e7xu61IHO7w5Jboi4upqs1HvACRhh4YNtGlgp3eCmUvFwToWY2m4JmjO1tpQZoQAqERmraJNutg2KWwjsKe+S2FnHKsb2ck050FnfVYHjZurDJq32uN+24cQzKHy/DwJ528Ib0WN7DvV13pq+0hkPDkRS5w4kx2318rZXIFbEtvfdud2Wnr2g2LbD25CR0dkVNC8dC84QTfYNnOw+qVmgYljwpjZRRlTeSJM4UBlLcNUYMPoydUBy9uwmK/SRwY7milwR2RI2JVFF1ncVeQNJkIpyoLUYpAx06xUrTYuneXm7jld126bYfDlgoiL2r7c7JXrkwRXY0iRq50K14Mbf9WpQ7tbqbWze/QSecGvhTxOW3iRqiPhjSJrzxlnqpy1tuyVtGXDo7rz8QcCNk/oRnqnzC0/AqLE/9+UbdBFfJNwICpamI6Wf3pDQREvABZyAhwfnd7cQpuLu+8Iqsw86x3hVHbqkZG7ao1wfCV/uhCo6WtglNj+QZZSdfILDHJkPKOO2U3tpI7XLXV/ptRHc6S0Tu6ZzArI/jlJuf1iTuI9klIZpmvBL06UYdUj1QyUzg6x0UCeyWK5R70oQVDAFypJa47bb0fn/li7slHfzhDhEUG5/WPl2Qvi2h8rCebrioxfc7R+71kd7sbC5dDw5WL+Vkz7I1luGoytibUVRHhnEv6nLpS3VoRTp0Sc+iaNCmaWL3qGfU86CD7bgWiMv8vKHKcbNcmWwUHqE84WVzVVSp2WiEPfE01OsXroCOpNkmlyZpzU6Rj/7OrtvMvR1FSNNJlobjqQ5umjxMZE3rHN+70k3a55HjN7C42W2YcbNmb8qI7tuTbjsXWix91ixWpHm5czYW7/PT/QrdN1Y7cPrS1Xp+f3fjbFwOI8/wh4HJKRbxzNidWvTY3SDuzJTFCr6yREyalibYuhJNhpRPCL9ZSoAcUqGzfUdK6FHWi0PG3TWR05gkKZz0Piqdl2Ubb7hsGlrCzcLloyazmK4WTmlZKE3imhm9P7K1fg9GAUaN0IzURN/z91ZcB/QWD+tjTHp9cmFP6MQrN/nUHK6Y6a9KM+0SrvL3uGqaxN5pqitaRO1w3W6MfXPxCp44t2BV98igd2PAS8zEWDcvFS82fmn4g2QzO+u+sQNKnRItOJD3GpF3OMdTEaSg/S6QPEIsLa52YvwkRal/4iKNbQkJlIJsSKKrB6dbZW3VPuW6zFNYDyFEEDslkQKTD7yjqMQAQbSKVAIWPsGCc5P316Yoi2M1Vu6mkgW/gfjUU7ehaGuoOAk06GBC54aeLjcFpoqJO7LAi8Agnb5aJaZ6wJiyuo/akY0JwxDkvShyDgYRMSfuYKk+XnqzJcV7By333vbm1BtAA1UVrJeIgUp70DGPB/dy5OE+t9OlY+QhBnoy6iJ7jJkTzjGq+o4NItSEcBPhQ4qtS4uNrGN3REAnqGQ0rOAXRq8yXjcp5bQVN3Stbe1Lyhf9EFkwu2MMjZ/E22U1VNlOGA12xW+98z6B/TY74VXaS71US+RawPhdwQUswuDr24YOqN0haEaVyLfUqWTyo0dWbBFFY2ye47RVzme49RJ6StHBTG0UT8e69FYFd2wCnmbOepZDIzOFkhEKxbLl4wFzxOUBhuFNtFOrCuGm08h0drwdYERsewZWI5pA9sMEWvqqKbvJxzl2GQti0IjezSJ8yBOGE3zdq9pumxw9jcUKnr9oUzOBZRtd54KuVfs2bek7a3crMxFg23PtOg/Tlt70NmPf1l0TVFMpS9GmQXUk1/Em0Id+g6gTA3h5f+O24nBLBArwdXe9JHvIsiuUNFw9ouIYRZVM2vCDhDMrTozs6w7ZCiDuyKbiuHTbQeqkbNirjjQ6ZW5vRdKXFuSkGKBnW263zki7FNudi1wwiGw1BPyl5JeqJcpCJWgdZxFaV123S8qALufbFt4kt6NjMFOWcnFtbduwLlFx05CnYtuXR7lS7rW6FwMLkwe32nUbr7ywGxIVG9Tj/QAPNwejNbaKyCABuqI3aTPZYQ8fCfHIHk3A3Qf9ltCsfDbj0/GEZByzo6LDRtnBt63H4WGlXfAug8Q1DMsT3w5ydAf9wt2k9k1KL/tAIA7VIactcbli63p1P+6DyHWvheNLSRx21aqKWwGT9t1WwS7FhbIi0AERZdn6tuBHe++I7NWw2RnRbTi3+HXYH0ySwSUxPXXUbokMV5MrPaxwVAKKl8thq+Y0vHVMHGEB/dFn/lAzUhGagkoeRJmmo8uKoS/4GCrXRsUu8tJuMCM97IWrfrwSDbesJmbLu6t4TZeduTUrporpau9B+GRxa3e66hPDlG3AkbV7Ye4W3qnrg6vwZ0M8OlGeU4NgCyqKS2CYdtL6Wzumw0Cx9/TKRXTLT91y2iLNHmmJ877QXYvAt/pZl6OKkTbb9ZTe+Gvs4Irv27S/zw+rwa6IcFt1mdF5lIq7ll+dLRNbd9rJTvsALjhlMDfL3ZBd9q5bXjSUzqtkFzorI0mWI2hH/QpjqEwgCE9F7YZbIScVM5enzUSytW2y6kUJBpY96321S7tWcRXWhDuAKdNyW2hyhO7WCS/warpZDfEd4KIISzzuM1Al2AZqi5h/6GE7OwWAY04iB5mKNHX1pctG0jmweXjfu4IbtUh4Ky9r+wiIvo1Iq7fQaFLZy7pBt0Rz0/IrRfgHXym32802V6btlpK8bUyGvBXrzSZnGekgKaFmpecOWeE2ueszIgosMe0rCpVwtk+M/g6FQ4z1myTlBptJMvkmrM+CXLXnxNreVP1K6qKuIMelH0Wy2YQxq/UCVh0OIpvmwYRVYGfi8muukLh6ZNKrneMbv5MPTichtxrsAyK2uJCkqE/nyZmqpa1rzuHej95NoLK4wvi8Z9myQVpbqKMdJm0G1M4buBpa010WVaZRVJ0o9xUI1UBmuLbskMrDht6BJLm6nMgyPXva5JKir90ozOgjHqeiPJZ9O+/u0OTcJTVr2zWKYwf6svTzMpdU1YZyvgzOp72k13dnfUgOx6IpTh51up7K7sydeeNUnauoXerQebr2Tl3hgwS2N0ZF5GJR2JTirbjosgaYfRzQcuCKzW0jarRatl1eqVq7PLIG2dlGw3BdJ/UDfiGljVAhCpl5JwZGUztwBURGD2F+T3S+i2343Ga2J2K4aUpl0p3zMDDsa41QZ5lAdxA5UvC4gs1qCmJzLfvwhEJ6F+eO2KMHBepv9up+ki8JdcJVmijpI76yCRIr/O01lis8X5IYuXW0fCVpRKrd1c2ghy2XpH2zAwAQnqcbQ9nrIvB162rpnoW11a2aBG25bEiqWxbUerMjsD7B0m2B3fy4F1RnnNLofsJDTTpAZyTfxx66p4KTBZWmcGTEiO0JCUUpjED16/mktPbygErn5fJ+2+1G7ayMVeMIvl52+0BSXApVWBRUc9dDHR+ZKuRHaXkYcT6mDE2pUkqXMNPe4rkM+SSTBEyZBI7Uw3rmg3aeVJCRsUa0vZpBzYWWHF1qqhktFFmfiOU5XOastg0nsNdt1m4mYxJmadiSucXDnbwLuOfp/XjG2JEyldVg4qZilirYPTby5GU9ocadvRP2l0CI2T0B5WZoR8HaPSiopGgZEQSAw49ivk0HJkgLZkVZLHk7dxwVHI19dSb9zVneGS2F21PTOJXlwvwaXq16DzamQacCIYQYM+a9a+dpdns1aJ24IJdq3UblODaIJ4bY1dHwGm7VvREQhNvZ/bSnpikQxgwSstSmJsw1zAjtNpmTc2fAqsDJvHbFpiaippSzMjgIPNV1ndbF1STdDUNNnVS8UcQqd0l5lUydF0jO7ZKRGWwxqOYHA3yGsUZpXermBJ1xTfd623g3FbRteK9nVzzdBnm7IY5QNGFclJ2dvlHKfVgdtGnEaAS5HhCo0zeZ5mzkjbo1jL3bGqawnWjYkKYLkckKg6dnGXZWU80WRuSFUBfyu7rf7ryBLlvUmQExJm5ovVQ6Isvb6O5i96rr9FXl+W6cj6i0zg8toiHqnYTsAo/PYPcf3IcWLfp+X1ypzHNOtY6C6Ceq7/ijoWNXTkd3bMxT5+XVreJxUMe7pdtNcuzUtsnDqxFYeu3k7l3v3ZSu7iUb70oXpJdlxeWOBduc/KR2vO91+xssFERxYkrSw/lGKDeloqnmkuEvrGkjvmO1tLCt15WMoge8lOFzn9LqetP2K/zoQo7Ky+s0H4Shz/Y3IrmMJcztD3UFM8nxgiO4WkLXO7fs+Koj48S4ezDPMdBBatyAuEpQszwoxsQHjC8W24maoibuL9V9e/MxzXBubhbD9mW32i13Lc5jtMBVMrlZusvNASrIXbZrnGs0FdTY0pcC3mIe5edqv8zNqCeLUtqF5XndnhoEQnp5SrB9Uw+VfbcrbeUAUKiv19gQ8Zvl+myV1rm9Sq8KMCw3mhXeRJAE9hv3aruc1Cm/DE1Mwx57PfZ39HCGWiTOvAK2kOTq4LQveorKF/hNuFYWXLsTlsFxdsRP3sVmVkhJ5sGuQqWtul+vk228KoiaunMIo8KtNSoes/ZY42gd1/sWPzD1mYKrw1XCCCih00NK+5C82/kbrW+N0wVaU8yyN6EtWTZEjbrMMUnToE6uBNgibY78StRDGIZgHaKqaq8i/RJl0S1OHAf5wC7XvXbtmXPc4bbtgR6sVMOE7KvJIEYyxewskS57ImCPPrI2Yp7n9CPV3PbZ6sZaPNuHwVpD+zHFrBhsgHDm1vgZf9clPcUxszF3o0QGykUe7vIF3DeJQ22cZbxwEGlJnxwiVhlpS8dJ2jiczJ3Qa5EFvoGv22EXIEeMBjg32XaLWwgVHsPMn+DdTVlBPeGUE5p764u6gVNDQfRhRGPodL1Iurc3cEs2EIy0MKyokwFBFXd9a1MKinoHDeF8guFRxiKUymDR23WBDwegGx3Jid0Qyk2Cas299J5snvYagtZOKaYwLu5cY6kkA2TiMD/ZxFqpdcUfbvUWs1O7E4l1mzuFQA71aFPnwe0zUyFlCKK6WBQGdxtaOw3FSqtZotIxrmrk0JaXyl1LodBsj/RGVHp/X+Vb29xyeVRFBL1P9+sr4bC7aF0ssdxQLsnKKVdCma+6ADMVJDWr8yEk1OukyGsvIJUzrhq5zNjrYFwi+qrMSawXw80+r3gbWt2odb0P7rJE4+qaPwISvNiYUBf1bbdiVu4NU6volLErpj0bF++AOuh9aOAer1fimcM4Nj5LmHaS5H1GKcf1vUtJl6SvHQHzMe1qu1A+wYbqdSNCnaCRPjLlEWE2m83f/vb24W0+On0dgP5772LNxzH/z05+ngc4X9+seJwAepb76aHr079p1y8f3monAlY9z7matAteh0V/d8r18V86TZ9FTM8Xnb4e8D6PjVsrmN8Gfotyt2vaevrSFOnjDQsww+6a+eXBZn6/1AHffzzM/Dt35jsvT9riy+vVx7f5Hb/5DQrPjazWe10GrzPAD2/u6wT3C0bgX7y6nJ1+HdMDX7F35B17+/1/AxIOdBLbLQAA -->
