---
name: "rar-cowork-cookbook-scheduled-brief-monitor-service-assets"
description: "Builds a morning brief on monitor service assets from Dynamics 365 ERP (legal entity USMF) \u2014 top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions \u2014 then saves an email draft to the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_monitor_service_assets", "rar_sha256": "82b790d157ff0933ec122532287244d711b7b4a351ec7696dd454f90b15ad0b1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_monitor_service_assets`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_monitor_service_assets_agent.py` and in the RCI capsule.

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

Monitor service assets Scheduled Email Brief — Builds a morning brief on monitor service assets from Dynamics 365 ERP (legal entity USMF) — top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions — then saves an email draft to the

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-service-assets
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
      "description": "Dynamics 365 F&SCM legal entity to query; recipe default is USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_monitor_service_assets_agent.py` and embedded as the fenced Python below (sha256 82b790d157ff0933…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_monitor_service_assets_agent.py` first:

```bash
python3 scheduled_brief_monitor_service_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_monitor_service_assets_agent.py   # or on stdin
python3 scheduled_brief_monitor_service_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor service assets Scheduled Email Brief — Builds a morning brief on monitor service assets from Dynamics 365 ERP (legal entity USMF) — top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions — then saves an email draft to the

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-service-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_monitor_service_assets',
    "version": '3.0.3',
    "display_name": 'Monitor service assets Scheduled Email Brief',
    "description": 'Builds a morning brief on monitor service assets from Dynamics 365 ERP (legal entity USMF) — top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions — then saves an email draft to the',
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
        "upstream_slug": 'scheduled-brief-monitor-service-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-monitor-service-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'face2d6da5a5bb67',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/monitor-service-assets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/scheduled-brief-monitor-service-assets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query; recipe default is USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where monitor service assets stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on monitor service assets for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads monitor service assets, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on monitor service assets from Dynamics 365 ERP (legal entity USMF) — top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions — then saves an email draft to the', 'example_request': 'Give me the monitor service assets morning brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query; recipe default is USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Use for a daily or weekly scheduled monitor service asset brief for the responsible owner, drafted as email (not sent) plus a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefMonitorServiceAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMonitorServiceAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query; recipe default is USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefMonitorServiceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
