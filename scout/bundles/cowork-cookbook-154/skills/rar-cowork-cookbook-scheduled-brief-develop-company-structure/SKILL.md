---
name: "rar-cowork-cookbook-scheduled-brief-develop-company-structure"
description: "Builds a morning brief on company structure from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended actions, a saved email draft to the owner, a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_company_structure", "rar_sha256": "6fa0933056770b4b7a5cdcc8a4f008115a6cb8669ac71f63079834d003480b27", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
