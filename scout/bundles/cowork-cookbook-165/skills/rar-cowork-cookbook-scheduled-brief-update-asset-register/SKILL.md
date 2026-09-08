---
name: "rar-cowork-cookbook-scheduled-brief-update-asset-register"
description: "Builds a morning brief on the asset register for a given legal entity via the Dynamics 365 ERP plugin \u2014 top 5 items by impact, anomalies vs the 7-day rolling average, and next actions \u2014 then saves an email draft to the o"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_update_asset_register", "rar_sha256": "2eb1899c261e90be21bf5cec10b05688b7348ff06b99c3615861d504d2adc5f0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_update_asset_register`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_update_asset_register_agent.py` and in the RCI capsule.

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

Update asset register Scheduled Email Brief — Builds a morning brief on the asset register for a given legal entity via the Dynamics 365 ERP plugin — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves an email draft to the o

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-update-asset-register
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
      "description": "D365 F&SCM legal entity to run against, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_update_asset_register_agent.py` and embedded as the fenced Python below (sha256 2eb1899c261e90be…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_update_asset_register_agent.py` first:

```bash
python3 scheduled_brief_update_asset_register_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_update_asset_register_agent.py   # or on stdin
python3 scheduled_brief_update_asset_register_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update asset register Scheduled Email Brief — Builds a morning brief on the asset register for a given legal entity via the Dynamics 365 ERP plugin — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves an email draft to the o

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-update-asset-register
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_update_asset_register',
    "version": '3.0.3',
    "display_name": 'Update asset register Scheduled Email Brief',
    "description": 'Builds a morning brief on the asset register for a given legal entity via the Dynamics 365 ERP plugin — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves an email draft to the o',
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
        "upstream_slug": 'scheduled-brief-update-asset-register',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-update-asset-register',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1b18fbe5a5a160c3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/update-asset-register'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/scheduled-brief-update-asset-register', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to run against, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where update asset register stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on update asset register for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads update asset register, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on the asset register for a given legal entity via the Dynamics 365 ERP plugin — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves an email draft to the o', 'example_request': 'Give me the USMF asset register morning brief and draft it to the owner, weekdays at 7am.', 'inputs': [{'description': 'D365 F&SCM legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly asset register brief for the responsible owner, drafted as an unsent email plus a Teams channel post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefUpdateAssetRegister(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefUpdateAssetRegister'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefUpdateAssetRegister().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
