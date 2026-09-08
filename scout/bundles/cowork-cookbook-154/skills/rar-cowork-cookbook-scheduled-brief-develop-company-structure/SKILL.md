---
name: "rar-cowork-cookbook-scheduled-brief-develop-company-structure"
description: "Builds a morning brief on company structure from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended actions, a saved email draft to the owner, a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_company_structure", "rar_sha256": "6fa0933056770b4b7a5cdcc8a4f008115a6cb8669ac71f63079834d003480b27", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_develop_company_structure`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_develop_company_structure_agent.py` and in the RCI capsule.

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

Develop company structure Scheduled Email Brief — Builds a morning brief on company structure from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended actions, a saved email draft to the owner, a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-company-structure
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
      "description": "D365 legal entity to run against, e.g. USMF.",
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
      "description": "When to run, e.g. weekday mornings at 7am, daily or weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_company_structure_agent.py` and embedded as the fenced Python below (sha256 6fa0933056770b4b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_company_structure_agent.py` first:

```bash
python3 scheduled_brief_develop_company_structure_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_company_structure_agent.py   # or on stdin
python3 scheduled_brief_develop_company_structure_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop company structure Scheduled Email Brief — Builds a morning brief on company structure from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended actions, a saved email draft to the owner, a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-company-structure
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_develop_company_structure',
    "version": '3.0.3',
    "display_name": 'Develop company structure Scheduled Email Brief',
    "description": 'Builds a morning brief on company structure from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended actions, a saved email draft to the owner, a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-develop-company-structure',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-develop-company-structure',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6eab6cef561a249e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-company-structure'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-develop-company-structure', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run, e.g. weekday mornings at 7am, daily or weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where develop company structure stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on develop company structure for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads develop company structure, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on company structure from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended actions, a saved email draft to the owner, a', 'example_request': 'Run the company structure morning brief for USMF and draft it to the owner, weekdays at 7am.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run, e.g. weekday mornings at 7am, daily or weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly scheduled company-structure brief from D365 F&SCM, drafted as an email to the owner plus a Teams channel post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDevelopCompanyStructure(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopCompanyStructure'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run, e.g. weekday mornings at 7am, daily or weekly.', 'type': 'string'}},
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
    print(ScheduledBriefDevelopCompanyStructure().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
