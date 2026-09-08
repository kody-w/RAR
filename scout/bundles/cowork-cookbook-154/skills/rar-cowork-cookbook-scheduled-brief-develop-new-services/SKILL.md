---
name: "rar-cowork-cookbook-scheduled-brief-develop-new-services"
description: "Builds a morning brief on develop new services from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the own"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_new_services", "rar_sha256": "8a879b592db6e4ef5a17426d9bcb873301fb3b20f8911e9e811b2422b3fe0746", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_develop_new_services`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_develop_new_services_agent.py` and in the RCI capsule.

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

Develop new services Scheduled Email Brief — Builds a morning brief on develop new services from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the own

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-new-services
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
      "description": "D365 F&SCM legal entity to query, e.g. USMF.",
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
      "description": "Responsible owner who receives the drafted brief email.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence for the scheduled run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_new_services_agent.py` and embedded as the fenced Python below (sha256 8a879b592db6e4ef…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_new_services_agent.py` first:

```bash
python3 scheduled_brief_develop_new_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_new_services_agent.py   # or on stdin
python3 scheduled_brief_develop_new_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop new services Scheduled Email Brief — Builds a morning brief on develop new services from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the own

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-new-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_develop_new_services',
    "version": '3.0.3',
    "display_name": 'Develop new services Scheduled Email Brief',
    "description": 'Builds a morning brief on develop new services from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the own',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-develop-new-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-develop-new-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '13039ca1aa516f45',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings/develop-new-services'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/scheduled-brief-develop-new-services', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted brief email.', 'schedule': 'Optional cadence for the scheduled run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where develop new services stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on develop new services for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop new services, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on develop new services from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the own', 'example_request': 'Run the develop new services morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted brief email.', 'name': 'owner'}, {'description': 'Optional cadence for the scheduled run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a daily or weekly develop-new-services brief is needed for the responsible owner, with an unsent email draft and a Teams channel summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDevelopNewServices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopNewServices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted brief email.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefDevelopNewServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
