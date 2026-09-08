---
name: "rar-cowork-cookbook-scheduled-brief-finalize-work-orders"
description: "Builds a finalize-work-orders morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, plus an email saved to drafts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_finalize_work_orders", "rar_sha256": "2addd3d2fc2939e36a87aaf2e9bf46c3faa091d132655bd69068842bc35d3dad", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_finalize_work_orders`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_finalize_work_orders_agent.py` and in the RCI capsule.

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

Finalize work orders Scheduled Email Brief — Builds a finalize-work-orders morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, plus an email saved to drafts.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-finalize-work-orders
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
      "description": "D365 legal entity to query; defaults to USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_finalize_work_orders_agent.py` and embedded as the fenced Python below (sha256 2addd3d2fc2939e3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_finalize_work_orders_agent.py` first:

```bash
python3 scheduled_brief_finalize_work_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_finalize_work_orders_agent.py   # or on stdin
python3 scheduled_brief_finalize_work_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Finalize work orders Scheduled Email Brief — Builds a finalize-work-orders morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, plus an email saved to drafts.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-finalize-work-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_finalize_work_orders',
    "version": '3.0.3',
    "display_name": 'Finalize work orders Scheduled Email Brief',
    "description": 'Builds a finalize-work-orders morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, plus an email saved to drafts.',
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
        "upstream_slug": 'scheduled-brief-finalize-work-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-finalize-work-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9838790fb0c7d6df',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/finalize-work-orders'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/scheduled-brief-finalize-work-orders', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where finalize work orders stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on finalize work orders for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads finalize work orders, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a finalize-work-orders morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, plus an email saved to drafts.', 'example_request': 'Give me the finalize work orders morning brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when the responsible owner wants a daily or weekly finalize-work-orders brief with a draft email and a Teams-ready summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefFinalizeWorkOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefFinalizeWorkOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefFinalizeWorkOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
