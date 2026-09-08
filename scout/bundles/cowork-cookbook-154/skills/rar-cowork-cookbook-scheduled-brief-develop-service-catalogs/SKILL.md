---
name: "rar-cowork-cookbook-scheduled-brief-develop-service-catalogs"
description: "Builds a morning brief on develop service catalogs from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_service_catalogs", "rar_sha256": "cc2a4a450057119cb4be266633e20ae2279c867bb241dcbf241520783f545b33", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_develop_service_catalogs`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_develop_service_catalogs_agent.py` and in the RCI capsule.

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

Develop service catalogs Scheduled Email Brief — Builds a morning brief on develop service catalogs from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-service-catalogs
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
      "description": "When the brief should run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_service_catalogs_agent.py` and embedded as the fenced Python below (sha256 cc2a4a450057119c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_service_catalogs_agent.py` first:

```bash
python3 scheduled_brief_develop_service_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_service_catalogs_agent.py   # or on stdin
python3 scheduled_brief_develop_service_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop service catalogs Scheduled Email Brief — Builds a morning brief on develop service catalogs from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-service-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_develop_service_catalogs',
    "version": '3.0.3',
    "display_name": 'Develop service catalogs Scheduled Email Brief',
    "description": 'Builds a morning brief on develop service catalogs from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the',
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
        "upstream_slug": 'scheduled-brief-develop-service-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-develop-service-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '83937ecb93a1ea10',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-service-catalogs'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/scheduled-brief-develop-service-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where develop service catalogs stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on develop service catalogs for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop service catalogs, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on develop service catalogs from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the', 'example_request': 'Draft my 7am weekday service catalog brief for USMF and send it to the owner as a draft.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a recurring (daily/weekly, e.g. weekday 7am) service catalog brief emailed as a draft to the responsible owner with a Teams-post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDevelopServiceCatalogs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopServiceCatalogs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefDevelopServiceCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
