---
name: "rar-cowork-cookbook-scheduled-brief-develop-new-services"
description: "Builds a morning brief on develop new services from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the own"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_new_services", "rar_sha256": "8a879b592db6e4ef5a17426d9bcb873301fb3b20f8911e9e811b2422b3fe0746", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
