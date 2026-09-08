---
name: "rar-cowork-cookbook-scheduled-brief-collect-interest"
description: "Builds a collect interest morning brief for a legal entity from Dynamics 365 ERP data \u2014 top 5 items by impact, anomalies vs the 7-day rolling average, and next actions \u2014 then saves a draft email to the owner plus a Teams"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_collect_interest", "rar_sha256": "0899b525cc84b055aef429e205eb4c8ad3499c439a72fc4b1051894b9926a558", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
