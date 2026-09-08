---
name: "rar-cowork-cookbook-scheduled-brief-manage-service-assets"
description: "Builds a morning brief on service asset management from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_service_assets", "rar_sha256": "c727244deb41bdb377a7ed5d692c56fb83f8f8715904df9ee3954810a5877dcc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1: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 -->
