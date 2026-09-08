---
name: "rar-cowork-cookbook-scheduled-brief-plan-fixed-assets"
description: "Builds a morning brief on plan fixed assets from Dynamics 365 ERP for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_fixed_assets", "rar_sha256": "85f8414337b35af6f0c8a22fef03f79de8cdc8f0136506f686b264be991f4e0f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
