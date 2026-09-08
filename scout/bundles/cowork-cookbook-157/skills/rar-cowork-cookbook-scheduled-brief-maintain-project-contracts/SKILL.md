---
name: "rar-cowork-cookbook-scheduled-brief-maintain-project-contracts"
description: "Builds a morning brief on maintain project contracts from Dynamics 365 ERP for a given legal entity and owner \u2014 top 5 items by impact, anomalies vs the 7-day rolling average, and next actions \u2014 then saves an email draft"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_maintain_project_contracts", "rar_sha256": "29c3cceb6d3b22a6ea718b29537c2d17618aa1bbad64a9cd55a42779c0619f8d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
