---
name: "rar-cowork-cookbook-scheduled-brief-record-fixed-asset-acquisitions"
description: "Builds a morning brief on record fixed asset acquisitions from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (unse"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_record_fixed_asset_acquisitions", "rar_sha256": "1bfd32416d05954625bfef2db52c6f7f85e47c2ff4da594728862467f3eec4d0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_record_fixed_asset_acquisitions`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_record_fixed_asset_acquisitions_agent.py` and in the RCI capsule.

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

Record fixed asset acquisitions Scheduled Email Brief — Builds a morning brief on record fixed asset acquisitions from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (unse

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-record-fixed-asset-acquisitions
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
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Person the brief is addressed to and whose draft email is created.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_record_fixed_asset_acquisitions_agent.py` and embedded as the fenced Python below (sha256 1bfd32416d059546…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_record_fixed_asset_acquisitions_agent.py` first:

```bash
python3 scheduled_brief_record_fixed_asset_acquisitions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_record_fixed_asset_acquisitions_agent.py   # or on stdin
python3 scheduled_brief_record_fixed_asset_acquisitions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record fixed asset acquisitions Scheduled Email Brief — Builds a morning brief on record fixed asset acquisitions from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (unse

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-record-fixed-asset-acquisitions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_record_fixed_asset_acquisitions',
    "version": '3.0.3',
    "display_name": 'Record fixed asset acquisitions Scheduled Email Brief',
    "description": 'Builds a morning brief on record fixed asset acquisitions from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (unse',
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
        "upstream_slug": 'scheduled-brief-record-fixed-asset-acquisitions',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-record-fixed-asset-acquisitions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '29d0f58c81470dcb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/record-fixed-asset-acquisitions'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-record-fixed-asset-acquisitions', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'responsible_owner': 'Person the brief is addressed to and whose draft email is created.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where record fixed asset acquisitions stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on record fixed asset acquisitions for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads record fixed asset acquisitions, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on record fixed asset acquisitions from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (unse', 'example_request': 'Send me the fixed asset acquisition morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Person the brief is addressed to and whose draft email is created.', 'name': 'responsible_owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly fixed asset acquisition brief for the responsible owner, as an email draft and Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefRecordFixedAssetAcquisitions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRecordFixedAssetAcquisitions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'responsible_owner': {'description': 'Person the brief is addressed to and whose draft email is created.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefRecordFixedAssetAcquisitions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
