---
name: "rar-cowork-cookbook-scheduled-brief-maintain-project-contracts"
description: "Builds a morning brief on maintain project contracts from Dynamics 365 ERP for a given legal entity and owner \u2014 top 5 items by impact, anomalies vs the 7-day rolling average, and next actions \u2014 then saves an email draft"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_maintain_project_contracts", "rar_sha256": "29c3cceb6d3b22a6ea718b29537c2d17618aa1bbad64a9cd55a42779c0619f8d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_maintain_project_contracts`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_maintain_project_contracts_agent.py` and in the RCI capsule.

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

Maintain project contracts Scheduled Email Brief — Builds a morning brief on maintain project contracts from Dynamics 365 ERP for a given legal entity and owner — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves an email draft

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-maintain-project-contracts
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
      "description": "Responsible owner the brief is written for and the draft email is addressed to.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence for running it, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_maintain_project_contracts_agent.py` and embedded as the fenced Python below (sha256 29c3cceb6d3b22a6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_maintain_project_contracts_agent.py` first:

```bash
python3 scheduled_brief_maintain_project_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_maintain_project_contracts_agent.py   # or on stdin
python3 scheduled_brief_maintain_project_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain project contracts Scheduled Email Brief — Builds a morning brief on maintain project contracts from Dynamics 365 ERP for a given legal entity and owner — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves an email draft

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-maintain-project-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_maintain_project_contracts',
    "version": '3.0.3',
    "display_name": 'Maintain project contracts Scheduled Email Brief',
    "description": 'Builds a morning brief on maintain project contracts from Dynamics 365 ERP for a given legal entity and owner — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves an email draft',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-maintain-project-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-maintain-project-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '90ba4e3e8edea340',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/maintain-project-contracts'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/scheduled-brief-maintain-project-contracts', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner the brief is written for and the draft email is addressed to.', 'schedule': 'Optional cadence for running it, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where maintain project contracts stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on maintain project contracts for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads maintain project contracts, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on maintain project contracts from Dynamics 365 ERP for a given legal entity and owner — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves an email draft', 'example_request': 'Give me the morning brief on project contracts for USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner the brief is written for and the draft email is addressed to.', 'name': 'owner'}, {'description': 'Optional cadence for running it, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly project-contracts brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefMaintainProjectContracts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMaintainProjectContracts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner the brief is written for and the draft email is addressed to.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for running it, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefMaintainProjectContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
