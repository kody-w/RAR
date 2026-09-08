---
name: "rar-cowork-cookbook-scheduled-brief-record-fixed-asset-acquisitions"
description: "Builds a morning brief on record fixed asset acquisitions from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (unse"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_record_fixed_asset_acquisitions", "rar_sha256": "1bfd32416d05954625bfef2db52c6f7f85e47c2ff4da594728862467f3eec4d0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
