---
name: "rar-cowork-cookbook-scheduled-brief-define-service-terms"
description: "Builds a morning brief on define service terms from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_service_terms", "rar_sha256": "0f84b9c57cc88eafc20609ee85918e86654996a9095dc7c39d50779cb45dbb92", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_service_terms`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_service_terms_agent.py` and in the RCI capsule.

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

Define service terms Scheduled Email Brief — Builds a morning brief on define service terms from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to the

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-service-terms
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
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence/time for the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_service_terms_agent.py` and embedded as the fenced Python below (sha256 0f84b9c57cc88eaf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_service_terms_agent.py` first:

```bash
python3 scheduled_brief_define_service_terms_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_service_terms_agent.py   # or on stdin
python3 scheduled_brief_define_service_terms_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service terms Scheduled Email Brief — Builds a morning brief on define service terms from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to the

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-service-terms
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_service_terms',
    "version": '3.0.3',
    "display_name": 'Define service terms Scheduled Email Brief',
    "description": 'Builds a morning brief on define service terms from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to the',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-define-service-terms',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-service-terms',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'db3269076f986951',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/define-service-terms'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/scheduled-brief-define-service-terms', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence/time for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where define service terms stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on define service terms for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define service terms, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on define service terms from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, a saved email draft to the', 'example_request': 'Give me the 7am weekday define service terms brief for USMF and draft it to the owner.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence/time for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a recurring (daily or weekday-morning) define service terms brief for the responsible owner, drafted as an email and a Teams post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDefineServiceTerms(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineServiceTerms'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence/time for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefDefineServiceTerms().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
