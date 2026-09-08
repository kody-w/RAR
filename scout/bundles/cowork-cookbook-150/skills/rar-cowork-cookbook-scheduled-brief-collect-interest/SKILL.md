---
name: "rar-cowork-cookbook-scheduled-brief-collect-interest"
description: "Builds a collect interest morning brief for a legal entity from Dynamics 365 ERP data \u2014 top 5 items by impact, anomalies vs the 7-day rolling average, and next actions \u2014 then saves a draft email to the owner plus a Teams"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_collect_interest", "rar_sha256": "0899b525cc84b055aef429e205eb4c8ad3499c439a72fc4b1051894b9926a558", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_collect_interest`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_collect_interest_agent.py` and in the RCI capsule.

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

Collect interest Scheduled Email Brief — Builds a collect interest morning brief for a legal entity from Dynamics 365 ERP data — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves a draft email to the owner plus a Teams

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-collect-interest
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
      "description": "Person the brief is addressed to; recipient of the saved email draft.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_collect_interest_agent.py` and embedded as the fenced Python below (sha256 0899b525cc84b055…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_collect_interest_agent.py` first:

```bash
python3 scheduled_brief_collect_interest_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_collect_interest_agent.py   # or on stdin
python3 scheduled_brief_collect_interest_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Collect interest Scheduled Email Brief — Builds a collect interest morning brief for a legal entity from Dynamics 365 ERP data — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves a draft email to the owner plus a Teams

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-collect-interest
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_collect_interest',
    "version": '3.0.3',
    "display_name": 'Collect interest Scheduled Email Brief',
    "description": 'Builds a collect interest morning brief for a legal entity from Dynamics 365 ERP data — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves a draft email to the owner plus a Teams',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-collect-interest',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-collect-interest',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3590e682d18df23f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/collect-interest'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/scheduled-brief-collect-interest', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'responsible_owner': 'Person the brief is addressed to; recipient of the saved email draft.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where collect interest stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on collect interest for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads collect interest, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a collect interest morning brief for a legal entity from Dynamics 365 ERP data — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves a draft email to the owner plus a Teams', 'example_request': 'Give me the collect interest morning brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Person the brief is addressed to; recipient of the saved email draft.', 'name': 'responsible_owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Use for a scheduled or ad-hoc collect interest brief for a D365 legal entity, when you want a drafted (unsent) owner email and a Teams-ready summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefCollectInterest(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefCollectInterest'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'responsible_owner': {'description': 'Person the brief is addressed to; recipient of the saved email draft.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefCollectInterest().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
