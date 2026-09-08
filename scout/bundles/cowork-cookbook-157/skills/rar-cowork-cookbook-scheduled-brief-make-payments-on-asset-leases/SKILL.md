---
name: "rar-cowork-cookbook-scheduled-brief-make-payments-on-asset-leases"
description: "Builds a morning brief on asset lease payments from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_make_payments_on_asset_leases", "rar_sha256": "89cc5bd78118b4a368553fef9f937077d4333560f4518c0fd3013e59d94b5213", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_make_payments_on_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_make_payments_on_asset_leases_agent.py` and in the RCI capsule.

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

Make payments on asset leases Scheduled Email Brief — Builds a morning brief on asset lease payments from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-make-payments-on-asset-leases
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
      "description": "Dynamics 365 legal entity to query, e.g. USMF.",
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
      "description": "Optional cadence for the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_make_payments_on_asset_leases_agent.py` and embedded as the fenced Python below (sha256 89cc5bd78118b4a3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_make_payments_on_asset_leases_agent.py` first:

```bash
python3 scheduled_brief_make_payments_on_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_make_payments_on_asset_leases_agent.py   # or on stdin
python3 scheduled_brief_make_payments_on_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Make payments on asset leases Scheduled Email Brief — Builds a morning brief on asset lease payments from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-make-payments-on-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_make_payments_on_asset_leases',
    "version": '3.0.3',
    "display_name": 'Make payments on asset leases Scheduled Email Brief',
    "description": 'Builds a morning brief on asset lease payments from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a',
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
        "upstream_slug": 'scheduled-brief-make-payments-on-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-make-payments-on-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '82721e850e1ae81d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/make-payments-on-asset-leases'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-make-payments-on-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where make payments on asset leases stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on make payments on asset leases for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads make payments on asset leases, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on asset lease payments from Dynamics 365 ERP for a legal entity, with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a', 'example_request': 'Draft my 7am asset lease payment brief for USMF and email it to the lease owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly asset-lease-payment brief for the responsible owner, drafted as email and a Teams channel post, not sent.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefMakePaymentsOnAssetLeases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMakePaymentsOnAssetLeases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefMakePaymentsOnAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
