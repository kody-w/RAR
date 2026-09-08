---
name: "rar-cowork-cookbook-scheduled-brief-develop-service-catalogs"
description: "Builds a morning brief on develop service catalogs from Dynamics 365 ERP data for a legal entity, covering top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves an email draft to the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_service_catalogs", "rar_sha256": "cc2a4a450057119cb4be266633e20ae2279c867bb241dcbf241520783f545b33", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
