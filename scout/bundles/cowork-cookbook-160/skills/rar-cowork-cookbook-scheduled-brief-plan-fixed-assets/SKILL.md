---
name: "rar-cowork-cookbook-scheduled-brief-plan-fixed-assets"
description: "Builds a morning brief on plan fixed assets from Dynamics 365 ERP for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_fixed_assets", "rar_sha256": "85f8414337b35af6f0c8a22fef03f79de8cdc8f0136506f686b264be991f4e0f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_plan_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_plan_fixed_assets_agent.py` and in the RCI capsule.

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

Plan fixed assets Scheduled Email Brief — Builds a morning brief on plan fixed assets from Dynamics 365 ERP for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-fixed-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 85f8414337b35af6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_fixed_assets_agent.py` first:

```bash
python3 scheduled_brief_plan_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_plan_fixed_assets_agent.py   # or on stdin
python3 scheduled_brief_plan_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan fixed assets Scheduled Email Brief — Builds a morning brief on plan fixed assets from Dynamics 365 ERP for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_plan_fixed_assets',
    "version": '3.0.3',
    "display_name": 'Plan fixed assets Scheduled Email Brief',
    "description": 'Builds a morning brief on plan fixed assets from Dynamics 365 ERP for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-plan-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-plan-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7cf8ec9542a099f0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/plan-fixed-assets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-plan-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where plan fixed assets stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on plan fixed assets for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads plan fixed assets, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on plan fixed assets from Dynamics 365 ERP for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a', 'example_request': 'Give me the plan fixed assets morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly plan fixed assets brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefPlanFixedAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPlanFixedAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefPlanFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
